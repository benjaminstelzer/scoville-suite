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


class CoordinatorBootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="coordinator-bootstrap-")
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.home = self.workspace / "host"

    def call(self, actor, action, revision=None, generation=0, *extra):
        command = [sys.executable, "-B", str(GUARD_HELPER), action,
                   "--workspace", str(self.workspace), "--workflow-id", "launcher"]
        if revision is not None:
            command += ["--expected-revision", str(revision), "--expected-generation", str(generation)]
        result = subprocess.run(command + list(extra), capture_output=True, text=True, encoding="utf-8",
                                env=dict(os.environ, CODEX_HOME=str(self.home), CODEX_THREAD_ID=actor))
        return result.returncode, json.loads(result.stdout)

    def coordinator(self, identity="coordinator", start="initial_parking", source="agent_created_thread"):
        base = ("scoville_role=coordinator\ncoordinator_start=" + start + "\nworkspace_root="
                + str(self.workspace) + "\nworkflow_id=launcher\n")
        return write_native(self.home, identity, CONTRACT.build_prompt(base, PACKAGE), "launcher", source)

    def ready(self):
        self.assertEqual(0, self.call("launcher", "acquire")[0])
        self.assertEqual(0, self.call("launcher", "reconcile-coordinator", 0, 0, "--task-id", "coordinator")[0])

    def active(self):
        self.ready()
        self.coordinator()
        self.assertEqual(0, self.call("coordinator", "claim", 1)[0])

    def test_missing_contract_rejects_claim_without_mutating_guard(self):
        self.ready()
        path = self.workspace / ".scoville-workflow/guard.json"
        before = path.read_bytes()
        code, result = self.call("coordinator", "claim", 1)
        self.assertEqual((1, "coordinator_contract_invalid"), (code, result["reason"]))
        self.assertEqual(before, path.read_bytes())

    def test_native_first_and_rollover_coordinators_receive_same_complete_contract(self):
        for start in ("initial_parking", "rollover_parking"):
            self.coordinator(start=start)
            CONTRACT.verify_coordinator("coordinator", "launcher", self.workspace, PACKAGE, self.home / "sessions")
        supplied = CONTRACT.runtime_contract(PACKAGE)
        for instruction in ("create_thread", "task_lifecycle.py", "changes_requested", "wait_threads",
                            "release", "stage_commit", "check_context_checkpoint.py"):
            self.assertIn(instruction, supplied)
        self.assertNotIn("### Writer activation scenarios", supplied)

    def test_truncated_stale_or_foreign_contract_is_not_a_read_receipt(self):
        path = self.coordinator()
        original = path.read_text()
        for old, new in (("stage_commit", "stage-commit"), ("workflow_id=launcher", "workflow_id=other"),
                         ("Coordinator runtime contract", "Coordinator runtime receipt")):
            path.write_text(original.replace(old, new), encoding="utf-8")
            with self.assertRaises(CONTRACT.ContractError):
                CONTRACT.verify_coordinator("coordinator", "launcher", self.workspace, PACKAGE, self.home / "sessions")
        path.write_text(original, encoding="utf-8")
        CONTRACT.verify_coordinator("coordinator", "launcher", self.workspace, PACKAGE, self.home / "sessions")

    def test_subagent_coordinator_is_rejected_even_with_complete_text(self):
        self.coordinator(source="subagent")
        with self.assertRaises(CONTRACT.ContractError):
            CONTRACT.verify_coordinator("coordinator", "launcher", self.workspace, PACKAGE, self.home / "sessions")

    def test_compaction_requires_complete_contract_delivery_not_a_hash_or_summary(self):
        self.active()
        path = self.home / "sessions/rollout-coordinator.jsonl"
        events = [json.loads(line) for line in path.read_text().splitlines()]
        events.append({"ordinal": 2, "type": "compacted", "payload": {"summary": "all rules loaded"}})
        events.append({"ordinal": 3, "type": "response_item", "payload": {
            "type": "custom_tool_call_output", "output": [{"type": "input_text", "text": "contract read: true"}]}})
        path.write_text("\n".join(map(json.dumps, events)) + "\n", encoding="utf-8")
        guard = self.workspace / ".scoville-workflow/guard.json"
        before = guard.read_bytes()
        self.assertEqual(1, self.call("coordinator", "verify", 2, 0, "--role", "coordinator", "--capability", "plan")[0])
        self.assertEqual(before, guard.read_bytes())
        # Same wrapper shape as a native functions.exec shell result.
        events.append({"ordinal": 4, "type": "response_item", "payload": {
            "type": "custom_tool_call_output", "output": [{"type": "input_text", "text": json.dumps({
                "output": CONTRACT.runtime_contract(PACKAGE).replace("\n", "\r\n"), "exit_code": 0})}]}})
        path.write_text("\n".join(map(json.dumps, events)) + "\n", encoding="utf-8")
        code, result = self.call("coordinator", "verify", 2, 0, "--role", "coordinator", "--capability", "plan")
        self.assertEqual(0, code)
        self.assertTrue(result["authorized"])

    def test_native_writer_binding_and_subagent_rejection(self):
        self.active()
        self.assertEqual(0, self.call("coordinator", "authorize-writer", 2, 0, "--role", "executor",
                                    "--unit", "W-001/step-1", "--dispatch-key", "dispatch", "--title", "Writer")[0])
        prompt = ("scoville_role=executor\nunit=W-001/step-1\nworkspace_root=" + str(self.workspace)
                  + "\nworkflow_id=launcher\ndispatch_key=dispatch\n")
        guard_path = self.workspace / ".scoville-workflow/guard.json"
        before = guard_path.read_bytes()
        for source, parent in (("subagent", "coordinator"), ("agent_created_thread", "foreign")):
            write_native(self.home, "writer", prompt, parent, source)
            code, result = self.call("coordinator", "reconcile-writer", 3, 0, "--dispatch-key", "dispatch", "--task-id", "writer")
            self.assertEqual((1, "writer_transport_invalid"), (code, result["reason"]))
            self.assertEqual(before, guard_path.read_bytes())
        write_native(self.home, "writer", prompt, "coordinator")
        self.assertEqual(0, self.call("coordinator", "reconcile-writer", 3, 0, "--dispatch-key", "dispatch", "--task-id", "writer")[0])
        self.assertEqual(0, self.call("coordinator", "activate-writer", 4, 0, "--dispatch-key", "dispatch", "--task-id", "writer")[0])
        code, result = self.call("writer", "verify", 5, 0, "--role", "executor", "--capability", "source",
                                 "--unit", "W-001/step-1", "--dispatch-key", "dispatch")
        self.assertEqual(0, code)
        self.assertTrue(result["authorized"])

    def test_stop_cleanup_remains_available_after_contract_loss(self):
        self.active()
        self.assertEqual(0, self.call("coordinator", "authorize-writer", 2, 0, "--role", "executor",
                                    "--unit", "W-001", "--dispatch-key", "dispatch", "--title", "Writer")[0])
        path = self.home / "sessions/rollout-coordinator.jsonl"
        path.write_text(path.read_text().replace("Coordinator runtime contract", "missing contract"), encoding="utf-8")
        self.assertEqual(1, self.call("coordinator", "verify", 3, 0, "--role", "coordinator", "--capability", "plan")[0])
        self.assertEqual(0, self.call("coordinator", "clear-writer", 3, 0, "--dispatch-key", "dispatch")[0])
        self.assertEqual(0, self.call("coordinator", "release", 4)[0])
        self.assertFalse((self.workspace / ".scoville-workflow/guard.json").exists())


if __name__ == "__main__":
    unittest.main()
