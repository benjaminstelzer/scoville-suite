import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_contract import PACKAGE, GUARD_HELPER
from native_startup_fixture import contract_module, write_native


CONTRACT = contract_module(PACKAGE)
LIFECYCLE = PACKAGE / "scripts" / "task_lifecycle.py"
MODEL_RESOLVER = PACKAGE / "scripts" / "resolve_model_pair.py"


class SimulatedHost:
    """Minimal native-host double. Workflow policy remains outside this class."""

    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def create(self, arguments, *, reply="ready"):
        task_id = f"task-{self.next_id}"
        self.next_id += 1
        self.tasks[task_id] = {
            "id": task_id,
            "hostId": "local",
            "kind": "codex",
            "projectId": arguments["target"]["projectId"],
            "title": arguments["title"],
            "status": "active",
            "prompt": arguments["prompt"],
            "result": None,
            "archived": False,
        }
        if reply == "ready":
            return {"threadId": task_id, "hostId": "local"}
        if reply == "pending":
            return {"clientThreadId": "pending-" + task_id}
        if reply == "unknown":
            return {}
        raise ValueError("unknown simulated creation reply")

    def list_threads(self):
        return [dict(task) for task in self.tasks.values() if not task["archived"]]

    def complete(self, task_id, body):
        task = self.tasks[task_id]
        task["status"] = "completed"
        task["result"] = body
        return {"threadId": task_id, "hostId": task["hostId"],
                "status": "completed", "body": body}

    def archive(self, arguments):
        task = self.tasks[arguments["threadId"]]
        if task["hostId"] != arguments["hostId"] or arguments.get("archived") is not True:
            raise ValueError("wrong simulated archive target")
        task["archived"] = True
        return {"threadId": task["id"], "hostId": task["hostId"], "archived": True}


class WorkflowSimulationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="workflow-simulation-")
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.home = self.workspace / "host"
        self.host = SimulatedHost()

    def guard(self, actor, action, revision=None, generation=0, *extra):
        command = [sys.executable, "-B", str(GUARD_HELPER), action,
                   "--workspace", str(self.workspace), "--workflow-id", "launcher"]
        if revision is not None:
            command += ["--expected-revision", str(revision), "--expected-generation", str(generation)]
        completed = subprocess.run(command + list(extra), capture_output=True, text=True, encoding="utf-8",
                                   env=dict(os.environ, CODEX_HOME=str(self.home), CODEX_THREAD_ID=actor))
        return completed.returncode, json.loads(completed.stdout)

    def coordinator_rollout(self, identity, start, parent):
        prompt = ("scoville_role=coordinator\ncoordinator_start=" + start
                  + "\nworkspace_root=" + str(self.workspace) + "\nworkflow_id=launcher\n")
        write_native(self.home, identity, CONTRACT.build_prompt(prompt, PACKAGE), parent)

    def lifecycle(self, request):
        completed = subprocess.run([sys.executable, "-B", str(LIFECYCLE)], input=json.dumps(request),
                                   capture_output=True, text=True, encoding="utf-8")
        return completed.returncode, json.loads(completed.stdout)

    def create_child(self, role, reference, prompt=None, reply="ready"):
        prompt = prompt or ("scoville_role=" + role + "\nunit=W-001/step-1\n")
        request = {
            "operation": "create", "creation_authorized": True, "prior_state": "not_started",
            "family": "workflow", "role": role, "projectId": "project", "prompt": prompt,
            "reference": reference, "prior_task_ids": [], "thinking": "medium", "model": "gpt-6-sol",
            "unit": "W-001/step-1", "attempt": 1,
        }
        code, creation = self.lifecycle(request)
        self.assertEqual(0, code)
        native_reply = self.host.create(creation["arguments"], reply=reply)
        code, result = self.lifecycle({"operation": "creation_result", "handle": creation["handle"],
                                       "reply": native_reply})
        self.assertEqual(0, code)
        return creation, result["handle"]

    def match_result(self, handle, reference, body, complete=True):
        return self.lifecycle({"operation": "match_delivery", "handle": handle,
                               "expected_scope": "W-001/step-1",
                               "delivery": {"threadId": handle["threadId"], "reference": reference,
                                            "scope": "W-001/step-1", "complete": complete, "body": body}})

    def test_guard_and_lifecycle_helpers_accept_one_compatible_trace(self):
        self.assertEqual(0, self.guard("launcher", "acquire")[0])
        self.assertEqual(0, self.guard("launcher", "reconcile-coordinator", 0, 0,
                                      "--task-id", "coordinator-1")[0])
        self.coordinator_rollout("coordinator-1", "initial_parking", "launcher")
        self.assertEqual(0, self.guard("coordinator-1", "claim", 1)[0])

        self.assertEqual(0, self.guard("coordinator-1", "authorize-writer", 2, 0,
                                      "--role", "executor", "--unit", "W-001/step-1",
                                      "--dispatch-key", "dispatch-1", "--title", "Executor")[0])
        writer_prompt = ("scoville_role=executor\nunit=W-001/step-1\nworkspace_root="
                         + str(self.workspace) + "\nworkflow_id=launcher\ndispatch_key=dispatch-1\n")
        write_native(self.home, "executor-1", writer_prompt, "coordinator-1")
        self.assertEqual(0, self.guard("coordinator-1", "reconcile-writer", 3, 0,
                                      "--dispatch-key", "dispatch-1", "--task-id", "executor-1")[0])
        self.assertEqual(0, self.guard("coordinator-1", "activate-writer", 4, 0,
                                      "--dispatch-key", "dispatch-1", "--task-id", "executor-1")[0])
        code, verified = self.guard("executor-1", "verify", 5, 0, "--role", "executor",
                                    "--capability", "source", "--unit", "W-001/step-1",
                                    "--dispatch-key", "dispatch-1")
        self.assertEqual(0, code)
        self.assertTrue(verified["authorized"])
        self.assertEqual(0, self.guard("coordinator-1", "clear-writer", 5, 0,
                                      "--dispatch-key", "dispatch-1")[0])

        code, reviewer = self.guard("reviewer-1", "verify", 6, 0, "--role", "reviewer",
                                    "--capability", "read_only")
        self.assertEqual(0, code)
        self.assertFalse(reviewer["authorized"])

        handle = {"state": "ready", "family": "workflow", "role": "reviewer",
                  "projectId": "project", "title": "Review", "reference": "review-1",
                  "threadId": "reviewer-1", "hostId": "local", "prior_task_ids": []}
        code, archive = self.lifecycle({"operation": "archive", "handle": handle,
                                       "status": "pass", "result_retained": True})
        self.assertEqual(0, code)
        self.assertEqual({"threadId": "reviewer-1", "hostId": "local", "archived": True},
                         archive["arguments"])
        code, proof = self.lifecycle({"operation": "verify_archive", "handle": handle,
                                     "reply": {"threadId": "reviewer-1", "archived": True}})
        self.assertEqual(0, code)
        self.assertTrue(proof["verified"])

        self.assertEqual(0, self.guard("coordinator-1", "begin-rollover", 6, 0,
                                      "--transition-key", "rollover-1", "--accepted-unit", "W-001/step-1",
                                      "--title", "Successor")[0])
        self.coordinator_rollout("coordinator-2", "rollover_parking", "coordinator-1")
        self.assertEqual(0, self.guard("coordinator-1", "reconcile-successor", 7, 0,
                                      "--transition-key", "rollover-1", "--task-id", "coordinator-2")[0])
        self.assertEqual(0, self.guard("coordinator-2", "validate-successor", 8, 0,
                                      "--transition-key", "rollover-1")[0])
        self.assertEqual(0, self.guard("coordinator-1", "transfer-coordinator", 9, 0,
                                      "--transition-key", "rollover-1")[0])
        self.assertEqual(0, self.guard("coordinator-2", "activate-coordinator", 10, 1,
                                      "--transition-key", "rollover-1")[0])
        code, owner = self.guard("coordinator-2", "verify", 11, 1, "--role", "coordinator",
                                 "--capability", "plan")
        self.assertEqual(0, code)
        self.assertTrue(owner["authorized"])
        self.assertEqual(0, self.guard("coordinator-2", "release", 11, 1)[0])
        self.assertFalse((self.workspace / ".scoville-workflow" / "guard.json").exists())

    def test_unknown_creation_reconciles_without_duplicate_creation(self):
        creation, handle = self.create_child("reviewer", "review-unknown", reply="unknown")
        self.assertEqual("creation_unknown", handle["state"])
        self.assertFalse(self.lifecycle({
            "operation": "creation_result", "handle": creation["handle"], "reply": {}
        })[1]["may_create_again"])

        code, reconciled = self.lifecycle({"operation": "reconcile", "handle": handle,
                                           "entries": self.host.list_threads()})
        self.assertEqual(0, code)
        self.assertEqual("ready", reconciled["handle"]["state"])
        self.assertEqual(1, len(self.host.tasks))

        duplicate = {
            "operation": "create", "creation_authorized": True, "prior_state": "creation_unknown",
            "family": "workflow", "role": "reviewer", "projectId": "project",
            "prompt": "scoville_role=reviewer\nunit=W-001/step-1\n", "reference": "review-unknown",
            "prior_task_ids": [], "thinking": "medium", "model": "gpt-6-sol",
            "unit": "W-001/step-1", "attempt": 1,
        }
        code, rejected = self.lifecycle(duplicate)
        self.assertEqual(1, code)
        self.assertIn("reconcile prior creation", rejected["error"])

    def test_executor_result_recovery_and_archive_use_exact_identity(self):
        creation, handle = self.create_child("executor", "executor-result")
        body = ("SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\n"
                "code_changed=yes\ncritical_docs_changed=no\nsummary=done")
        completed = self.host.complete(handle["threadId"], body)
        self.assertEqual(handle["threadId"], completed["threadId"])
        code, matched = self.match_result(handle, "executor-result", completed["body"])
        self.assertEqual(0, code)
        self.assertTrue(matched["matched"])

        for change in ({"complete": False}, {"reference": "other"}, {"threadId": "other"}):
            delivery = {"threadId": handle["threadId"], "reference": "executor-result",
                        "scope": "W-001/step-1", "complete": True, "body": body} | change
            code, rejected = self.lifecycle({"operation": "match_delivery", "handle": handle,
                                             "expected_scope": "W-001/step-1", "delivery": delivery})
            with self.subTest(change=change):
                self.assertEqual(1, code)
                self.assertFalse(rejected["ok"])

        code, archive = self.lifecycle({"operation": "archive", "handle": handle,
                                        "status": "completed", "result_retained": True})
        self.assertEqual(0, code)
        receipt = self.host.archive(archive["arguments"])
        code, proof = self.lifecycle({"operation": "verify_archive", "handle": handle, "reply": receipt})
        self.assertEqual(0, code)
        self.assertTrue(proof["verified"])

    def test_reviewer_change_request_keeps_three_repair_limit(self):
        _, handle = self.create_child("reviewer", "review-findings")
        body = ("SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\n"
                "summary=fix one issue\nfinding=correct the binding")
        self.host.complete(handle["threadId"], body)
        self.assertEqual(0, self.match_result(handle, "review-findings", body)[0])

        for repair_number in (1, 2, 3):
            completed = subprocess.run([
                sys.executable, "-B", str(MODEL_RESOLVER), "--role", "repair",
                "--original-model", "gpt-6-sol", "--original-reasoning", "medium",
                "--repair-number", str(repair_number),
            ], capture_output=True, text=True, encoding="utf-8")
            with self.subTest(repair_number=repair_number):
                self.assertEqual(0, completed.returncode)
                self.assertTrue(json.loads(completed.stdout)["valid"])
        exhausted = subprocess.run([
            sys.executable, "-B", str(MODEL_RESOLVER), "--role", "repair",
            "--original-model", "gpt-6-sol", "--original-reasoning", "medium",
            "--repair-number", "4",
        ], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(1, exhausted.returncode)
        self.assertFalse(json.loads(exhausted.stdout)["valid"])

    def test_stop_releases_guard_only_after_active_writer_reconciliation(self):
        self.assertEqual(0, self.guard("launcher", "acquire")[0])
        self.assertEqual(0, self.guard("launcher", "reconcile-coordinator", 0, 0,
                                      "--task-id", "coordinator-1")[0])
        self.coordinator_rollout("coordinator-1", "initial_parking", "launcher")
        self.assertEqual(0, self.guard("coordinator-1", "claim", 1)[0])
        self.assertEqual(0, self.guard("coordinator-1", "authorize-writer", 2, 0,
                                      "--role", "executor", "--unit", "W-001/step-1",
                                      "--dispatch-key", "stop-dispatch", "--title", "Executor")[0])
        writer_prompt = ("scoville_role=executor\nunit=W-001/step-1\nworkspace_root="
                         + str(self.workspace) + "\nworkflow_id=launcher\ndispatch_key=stop-dispatch\n")
        write_native(self.home, "executor-stop", writer_prompt, "coordinator-1")
        self.assertEqual(0, self.guard("coordinator-1", "reconcile-writer", 3, 0,
                                      "--dispatch-key", "stop-dispatch", "--task-id", "executor-stop")[0])
        self.assertEqual(0, self.guard("coordinator-1", "activate-writer", 4, 0,
                                      "--dispatch-key", "stop-dispatch", "--task-id", "executor-stop")[0])
        code, blocked = self.guard("coordinator-1", "release", 5, 0)
        self.assertEqual(1, code)
        self.assertEqual("state_mismatch", blocked["reason"])
        self.assertEqual(0, self.guard("coordinator-1", "clear-writer", 5, 0,
                                      "--dispatch-key", "stop-dispatch")[0])
        self.assertEqual(0, self.guard("coordinator-1", "release", 6, 0)[0])

    def test_compaction_requires_complete_contract_reload(self):
        self.coordinator_rollout("coordinator-1", "initial_parking", "launcher")
        rollout = self.home / "sessions" / "rollout-coordinator-1.jsonl"
        with rollout.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps({"ordinal": 2, "type": "compacted", "payload": {}}) + "\n")
        with self.assertRaisesRegex(CONTRACT.ContractError, "shown completely again"):
            CONTRACT.verify_coordinator("coordinator-1", "launcher", self.workspace,
                                        PACKAGE, self.home / "sessions")
        with rollout.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps({"ordinal": 3, "type": "response_item", "payload": {
                "type": "function_call_output", "output": CONTRACT.runtime_contract(PACKAGE)
            }}) + "\n")
        CONTRACT.verify_coordinator("coordinator-1", "launcher", self.workspace,
                                    PACKAGE, self.home / "sessions")


if __name__ == "__main__":
    unittest.main()
