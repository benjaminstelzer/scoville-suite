"""Functional ASK contract checks with simulated host and CLI boundaries."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


PACKAGE = Path(__file__).resolve().parents[2] / "scoville-ask-for-codex"
SCRIPTS = PACKAGE / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location("ask_under_test", SCRIPTS / "ask.py")
assert SPEC and SPEC.loader
ask = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ask)

CATALOG = {"source": "model/list", "models": [
    {"model": "gpt-6-astra", "efforts": ["medium", "high"]},
    {"model": "gpt-6-sol", "efforts": ["low", "medium", "high"]},
]}
ADVISERS = [
    {"id": "astra", "route": "native", "model": "gpt-6-astra", "effort": "high"},
    {"id": "claude", "name": "Second reader", "route": "claude-cli", "model": "claude-fable-5-1", "effort": "high"},
    {"id": "sol", "route": "native", "model": "gpt-6-sol", "effort": "medium"},
]


def prepare_request(advisers=ADVISERS, **extra):
    return {"mode": "review", "question": "Could this patch lose data?", "scope": "patch A",
            "reference": "round-1", "caller_id": "caller-17", "caller_title": "Review patch",
            "projectId": "project-1", "creation_authorized": True,
            "prior_state": "not_started", "prior_task_ids": ["older-task"],
            "cwd": str(PACKAGE), "catalog": CATALOG,
            "overrides": {"advisers": advisers}, **extra}


class AskBehaviorTests(unittest.TestCase):
    def test_config_layers_preserve_precedence_between_inline_and_preset_fields(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "config.default.json").write_bytes((PACKAGE / "config.default.json").read_bytes())
            (root / "config.json").write_text(json.dumps({
                "advisers": [{"id": "sol", "effort": "medium"}]}), encoding="utf-8")
            with mock.patch.object(ask, "ROOT", root):
                personal_then_project = ask.resolve({"catalog": CATALOG,
                    "project_config": {"presets": {"sol": {"effort": "high"}}}})
            self.assertEqual(personal_then_project["config"]["advisers"][0]["effort"], "high")
            (root / "config.json").unlink()
            with mock.patch.object(ask, "ROOT", root):
                project_then_request = ask.resolve({"catalog": CATALOG,
                    "project_config": {"advisers": [{"id": "sol", "effort": "medium"}]},
                    "overrides": {"presets": {"sol": {"effort": "high"}}}})
                same_layer = ask.resolve({"catalog": CATALOG,
                    "project_config": {"advisers": [{"id": "sol", "effort": "medium"}],
                                       "presets": {"sol": {"effort": "high"}}}})
            self.assertEqual(project_then_request["config"]["advisers"][0]["effort"], "high")
            self.assertEqual(same_layer["config"]["advisers"][0]["effort"], "medium")

    def test_claude_defaults_and_explicit_adviser_override_are_distinct(self):
        selected = ask.resolve({"catalog": CATALOG,
            "overrides": {"advisers": ["sol", "claude", "fable"]}})["config"]["advisers"]
        self.assertEqual([(a["id"], a["model"], a["effort"]) for a in selected], [
            ("sol", "gpt-6-sol", "high"),
            ("claude", "claude-opus-5-5", "high"),
            ("fable", "claude-fable-5-1", "medium"),
        ])
        explicit = ask.resolve({"overrides": {"advisers": [
            {"id": "fable", "effort": "high"}]}})["config"]["advisers"]
        self.assertEqual([(a["id"], a["model"], a["effort"]) for a in explicit],
                         [("fable", "claude-fable-5-1", "high")])

    def test_model_list_protocol_pages_and_preserves_model_efforts(self):
        fake_server = '''import json, sys
for line in sys.stdin:
    request = json.loads(line)
    if "id" not in request:
        continue
    if request["method"] == "initialize":
        result = {}
    elif request["params"]["cursor"] is None:
        result = {"data": [{"model": "gpt-6-astra", "supportedReasoningEfforts":
            [{"reasoningEffort": "medium"}, {"reasoningEffort": "high"}],
            "defaultReasoningEffort": "high"}], "nextCursor": "page-2"}
    else:
        result = {"data": [{"model": "third-party-model", "supportedReasoningEfforts":
            [{"reasoningEffort": "low"}], "defaultReasoningEffort": "low"}],
            "nextCursor": None}
    print(json.dumps({"id": request["id"], "result": result}), flush=True)
'''
        with tempfile.TemporaryDirectory() as temporary:
            script = Path(temporary) / "fake_app_server.py"
            script.write_text(fake_server, encoding="utf-8")
            catalog = ask.list_models([sys.executable, str(script)], timeout=5)
        self.assertEqual(catalog, {"source": "model/list", "models": [
            {"model": "gpt-6-astra", "efforts": ["medium", "high"], "default_effort": "high"},
            {"model": "third-party-model", "efforts": ["low"], "default_effort": "low"},
        ]})

    def test_json_cli_uses_utf8_for_unicode_question_without_environment_override(self):
        request = prepare_request([ADVISERS[0]], question="Prüfe Änderung äöü 😀")
        request["operation"] = "prepare"
        completed = subprocess.run([sys.executable, str(SCRIPTS / "ask.py")],
            input=json.dumps(request), text=True, encoding="utf-8",
            capture_output=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        output = json.loads(completed.stdout)
        self.assertTrue(output["ok"])
        self.assertIn("Prüfe Änderung äöü 😀", output["entries"][0]["arguments"]["prompt"])

    def test_resolution_selects_one_two_and_three_without_extra_dispatch(self):
        for count in (1, 2, 3):
            with self.subTest(count=count):
                selected = ADVISERS[:count]
                result = ask.resolve({"catalog": CATALOG, "project_config": {
                    "advisers": [ADVISERS[-1]]}, "overrides": {"advisers": selected}})
                self.assertEqual(result["config"]["advisers"], selected)
                prepared = ask.prepare(prepare_request(selected))
                self.assertEqual([e["adviser"]["id"] for e in prepared["entries"]],
                                 [a["id"] for a in selected])
                self.assertEqual([e["adviser"]["route"] for e in prepared["entries"]],
                                 [a["route"] for a in selected])

    def test_native_payload_keeps_exact_title_identity_and_review_independence(self):
        result = ask.prepare(prepare_request())
        native = [e for e in result["entries"] if e["adviser"]["route"] == "native"]
        self.assertEqual([e["arguments"]["title"] for e in native],
                         ["Review patch ASK-TASK"] * 2)
        self.assertEqual([e["arguments"]["model"] for e in native],
                         ["gpt-6-astra", "gpt-6-sol"])
        self.assertEqual([e["arguments"]["thinking"] for e in native],
                         ["high", "medium"])
        self.assertEqual([e["reference"] for e in native], ["round-1:astra", "round-1:sol"])
        for entry in native:
            prompt = entry["arguments"]["prompt"]
            self.assertIn("Could this patch lose data?", prompt)
            self.assertIn('"mode": "review"', prompt)
            self.assertIn("return_to_thread_id=caller-17", prompt)
            self.assertEqual(entry["handle"]["state"], "creation_unknown")
            self.assertEqual(entry["handle"]["return_to_thread_id"], "caller-17")
        self.assertEqual(result["entries"][1]["request"]["operation"], "claude")

    def test_ambiguous_mode_and_unauthorized_creation_cannot_prepare(self):
        with self.assertRaisesRegex(ValueError, "clarify ambiguous intent"):
            ask.prepare(prepare_request(mode=None))
        with self.assertRaisesRegex(ValueError, "existing authority"):
            ask.prepare(prepare_request(creation_authorized=False))

    def test_missing_catalog_model_effort_and_task_start_do_not_fallback(self):
        with mock.patch.object(ask, "list_models", side_effect=OSError("catalog offline")):
            with self.assertRaisesRegex(OSError, "catalog offline"):
                ask.resolve({"overrides": {"advisers": [ADVISERS[0]]}})
        for adviser, message in [
            ({**ADVISERS[0], "model": "missing"}, "model unavailable"),
            ({**ADVISERS[0], "effort": "ultra"}, "effort unavailable"),
        ]:
            with self.subTest(adviser=adviser), self.assertRaisesRegex(ValueError, message):
                ask.prepare(prepare_request([adviser]))
        entry = ask.prepare(prepare_request([ADVISERS[0]]))["entries"][0]
        with self.assertRaisesRegex(ValueError, "creation failed"):
            ask.task_lifecycle.creation_result({"handle": entry["handle"],
                                               "reply": {"isError": True, "message": "start refused"}})

    def test_same_title_tasks_are_disambiguated_by_ids_and_reference(self):
        entries = ask.prepare(prepare_request([ADVISERS[0], ADVISERS[2]]))["entries"]
        handles = []
        for index, entry in enumerate(entries):
            result = ask.task_lifecycle.creation_result({"handle": entry["handle"],
                "reply": {"threadId": f"task-{index}", "hostId": "local"}})
            handles.append(result["handle"])
        self.assertEqual([h["threadId"] for h in handles], ["task-0", "task-1"])
        delivery = {"threadId": "task-1", "reference": "round-1:sol",
                    "scope": "patch A", "complete": True, "body": "Finding at a.py:7"}
        self.assertTrue(ask.task_lifecycle.match_delivery({"handle": handles[1],
            "delivery": delivery, "expected_scope": "patch A"})["matched"])
        with self.assertRaisesRegex(ValueError, "wrong delivery sender"):
            ask.task_lifecycle.match_delivery({"handle": handles[0],
                "delivery": delivery, "expected_scope": "patch A"})
        with self.assertRaisesRegex(ValueError, "complete result"):
            ask.task_lifecycle.match_delivery({"handle": handles[1],
                "delivery": {**delivery, "complete": False}, "expected_scope": "patch A"})

    def test_followup_targets_retained_handle_and_rejects_archived_or_duplicate_send(self):
        entry = ask.prepare(prepare_request([ADVISERS[0]]))["entries"][0]
        handle = ask.task_lifecycle.creation_result({"handle": entry["handle"],
            "reply": {"threadId": "task-astra", "hostId": "local"}})["handle"]
        request = {"handle": handle, "archived": False, "delivery_state": "not_sent",
                   "reference": "round-2:astra", "scope": "patch B", "question": "Check revised patch",
                   "catalog": CATALOG}
        result = ask.followup(request)
        self.assertEqual(result["arguments"]["threadId"], "task-astra")
        self.assertEqual(result["arguments"]["hostId"], "local")
        self.assertEqual(result["handle"]["reference"], "round-2:astra")
        self.assertEqual(result["context_mode"], "continued")
        with self.assertRaisesRegex(ValueError, "unarchived"):
            ask.followup({**request, "archived": True})
        with self.assertRaisesRegex(ValueError, "reconcile prior delivery"):
            ask.followup({**request, "delivery_state": "unknown"})
        with self.assertRaises(ValueError):
            ask.followup({**request, "overrides": {"id": "different-adviser"}})

    def test_sidebar_preserves_other_order_and_reports_unsupported_host(self):
        result = ask.sidebar({"section_id": "custom-1", "manual_sort": True,
            "thread_ids": ["other-a", "caller", "other-b", "ask-2", "ask-1"],
            "caller_id": "caller", "adviser_ids": ["ask-1", "ask-2"]})
        self.assertEqual(result["arguments"]["threadIds"],
                         ["other-a", "ask-1", "ask-2", "caller", "other-b"])
        unsupported = ask.sidebar({"section_id": "threads", "manual_sort": True})
        self.assertFalse(unsupported["supported"])
        self.assertIn("no targeted order", unsupported["reason"])

    def test_claude_executes_only_adapter_command_and_preserves_session(self):
        cli_request = ask.prepare(prepare_request([ADVISERS[1]]))["entries"][0]["request"]
        completed = subprocess.CompletedProcess(["claude"], 0,
            json.dumps({"result": "  Independent answer\n", "session_id": "sid-1",
                        "model": "claude-fable-5-1", "permission_denials": ["Read secret"]}), "")
        with mock.patch.object(ask.ask_claude, "resolve_claude_command", return_value=["claude"]), \
             mock.patch.object(ask.subprocess, "run", return_value=completed) as run:
            result = ask.claude(cli_request)
        command = run.call_args.args[0]
        self.assertEqual(command[command.index("--tools") + 1],
                         "Read,Grep,Glob,WebSearch,WebFetch")
        self.assertIn("--safe-mode", command)
        self.assertNotIn("--resume", command)
        self.assertEqual(result["answer"], "  Independent answer\n")
        self.assertEqual(result["session_id"], "sid-1")
        self.assertTrue(result["continuation_available"])
        self.assertEqual(result["permission_denials"], ["Read secret"])
        with mock.patch.object(ask.ask_claude, "resolve_claude_command", return_value=["claude"]), \
             mock.patch.object(ask.subprocess, "run", return_value=completed) as resumed:
            next_result = ask.claude({**cli_request, "session_id": "sid-1"})
        self.assertEqual(resumed.call_args.args[0][resumed.call_args.args[0].index("--resume") + 1], "sid-1")
        self.assertEqual(next_result["context_mode"], "continued")

    def test_claude_failures_never_return_answer(self):
        request = ask.prepare(prepare_request([ADVISERS[1]]))["entries"][0]["request"]
        for completed, error in [
            (subprocess.CompletedProcess(["claude"], 1, "", "authentication failed"), "authentication failed"),
            (subprocess.CompletedProcess(["claude"], 0, "not-json", ""), "invalid JSON"),
            (subprocess.CompletedProcess(["claude"], 0, json.dumps({"result": " "}), ""), "Claude answer"),
            (subprocess.CompletedProcess(["claude"], 0, json.dumps({"is_error": True,
                "errors": ["budget exhausted"]}), ""), "budget exhausted"),
        ]:
            with self.subTest(error=error), \
                 mock.patch.object(ask.ask_claude, "resolve_claude_command", return_value=["claude"]), \
                 mock.patch.object(ask.subprocess, "run", return_value=completed), \
                 self.assertRaisesRegex(ValueError, error):
                ask.claude(request)

    def test_claude_exit_error_uses_oauth_detail_from_stdout_json(self):
        request = ask.prepare(prepare_request([ADVISERS[1]]))["entries"][0]["request"]
        oauth_error = "Failed to authenticate: OAuth session expired and could not be refreshed"
        completed = subprocess.CompletedProcess(["claude"], 1,
            json.dumps({"is_error": True, "errors": [oauth_error]}), "")
        with mock.patch.object(ask.ask_claude, "resolve_claude_command", return_value=["claude"]), \
             mock.patch.object(ask.subprocess, "run", return_value=completed) as launch, \
             self.assertRaisesRegex(ValueError, oauth_error):
            ask.claude(request)
        launch.assert_called_once()


if __name__ == "__main__":
    unittest.main()
