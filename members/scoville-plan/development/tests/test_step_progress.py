"""Legacy inputs, explicit progress and deterministic recovery through real CLIs."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "scoville-plan"
FIXTURE = Path(__file__).parent / "fixtures/valid-profile"


class StepProgressTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "project"
        shutil.copytree(FIXTURE, self.root)
        self.plan = self.root / "docs/plans/0001-validate-profile.md"
        self.original = self.plan.read_text(encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def steps(self, lines, ending="\n"):
        text = self.original.replace("1. Read the canonical files.\n2. Check the local record shapes.", "\n".join(f"{i}. {text}" for i, text in enumerate(lines, 1)))
        self.plan.write_bytes(text.replace("\n", ending).encode("utf-8"))

    def call(self, script, *args):
        before = self.plan.read_bytes()
        run = subprocess.run([sys.executable, str(ROOT / "scripts" / script), "--root", str(self.root), *args], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(before, self.plan.read_bytes(), "read-only helper wrote the Plan")
        return run, json.loads(run.stdout)

    def test_legacy_dispatch_is_unchanged_and_position_is_explicitly_unknown(self):
        run, context = self.call("select_context.py", "--unit", "W-001")
        self.assertEqual(run.returncode, 0, run.stdout)
        self.assertNotIn("step_statuses", context["work_item"])
        run, position = self.call("select_context.py", "--plan", "PLAN-0001", "--position")
        self.assertEqual(run.returncode, 0, run.stdout)
        self.assertEqual(position["work_item"], "W-001")
        self.assertEqual(position["current_steps"], [])
        self.assertIsNone(position["next_step"])
        self.assertEqual(position["untracked_steps"], [1, 2])
        self.assertIn("actual task results", position["guidance"])

    def test_mixed_statuses_preserve_source_and_disjoint_active_ranges(self):
        lines = ["[status: done] Verify the source.", "[status: in_progress] [route: high] [execute: reasoning=medium] Write the result.", "[status: in_progress] Check it.", "Keep legacy work unknown.", "[status: in_progress] Inspect another result.", "[status: cancelled] Retired task."]
        for ending in ("\n", "\r\n"):
            self.steps(lines, ending)
            run, result = self.call("validate_profile.py", "--format", "json")
            self.assertEqual(run.returncode, 0, run.stdout)
            self.assertTrue(result["valid"])
            run, context = self.call("select_context.py", "--unit", "W-001/steps-1-6")
            self.assertEqual(run.returncode, 0, run.stdout)
            self.assertEqual(context["work_item"]["source_text"], "\n".join(f"{i}. {text}" for i, text in enumerate(lines, 1)) + "\n")
            self.assertIsNone(context["work_item"]["step_statuses"][3]["status"])
            run, position = self.call("select_context.py", "--position")
            self.assertEqual(position["current_steps"], [2, 3, 5])
            self.assertEqual(position["current_units"], ["W-001/steps-2-3", "W-001/step-5"])
            self.assertEqual(position["untracked_steps"], [4])

    def test_invalid_status_diagnostic_and_corrected_call(self):
        for invalid in ("[status: paused] Read the result.", "[status:done] Read the result.", "[status: done] [status: todo] Read the result.", "[route: low] [status: done] Read the result.", "[status: done]"):
            self.steps([invalid, "Keep the second Step."])
            for script, args in (("validate_profile.py", ("--format", "json")), ("select_context.py", ("--position",))):
                run, result = self.call(script, *args)
                self.assertNotEqual(run.returncode, 0, run.stdout)
                diagnostic = next(d for d in result["diagnostics"] if d["code"] == "WORK_STEP_STATUS_INVALID")
                self.assertIn("status", diagnostic["message"].lower())
                self.assertIn("todo", str(diagnostic))
            self.steps(["[status: done] Read the result.", "[status: todo] Verify the remaining result."])
            run, result = self.call("validate_profile.py", "--format", "json")
            self.assertEqual(run.returncode, 0, run.stdout)
            run, position = self.call("select_context.py", "--position")
            self.assertEqual(position["next_step"], 2)

    def test_status_example_within_action_is_legacy_prose(self):
        self.steps(["Document the example [status: done] without changing it.", "Check the text."])
        run, result = self.call("validate_profile.py", "--format", "json")
        self.assertEqual(run.returncode, 0, run.stdout)
        run, context = self.call("select_context.py", "--unit", "W-001")
        self.assertNotIn("step_statuses", context["work_item"])

    def test_named_idle_and_invalid_position_arguments(self):
        self.plan.write_text(self.original.replace("status: active\n", "status: draft\n", 1).replace("current_item: W-001\n", "", 1).replace("Status: in_progress", "Status: todo", 1), encoding="utf-8")
        (self.root / "PROJECT_INDEX.md").write_text("---\nformat_version: 1\nactive_plan: null\n---\n", encoding="utf-8")
        run, position = self.call("select_context.py", "--plan", "PLAN-0001", "--position")
        self.assertEqual(run.returncode, 0, run.stdout)
        self.assertIsNone(position["work_item"])
        self.assertEqual(position["reason"], "no_current_item")
        for args in (("--plan", "PLAN-x", "--position"), ("--plan", "PLAN-0001", "--position", "--unit", "W-001")):
            run, result = self.call("select_context.py", *args)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("--", result["diagnostics"][0]["message"])

    def test_completed_steps_do_not_complete_whole_item(self):
        self.steps(["[status: done] Write the result.", "[status: cancelled] Retired optional task."])
        run, position = self.call("select_context.py", "--position")
        self.assertEqual(position["work_status"], "in_progress")
        self.assertEqual(position["reason"], "steps_terminal_work_item_acceptance_pending")
        self.assertIsNone(position["next_step"])

    def test_written_steps_need_no_legacy_next_action_and_keep_acceptance_context(self):
        self.steps(["[status: todo] Perform the single action."])
        self.plan.write_text(self.plan.read_text(encoding="utf-8").replace("Next action: Run the structural validator.\n", ""), encoding="utf-8")
        run, result = self.call("validate_profile.py", "--format", "json")
        self.assertEqual(run.returncode, 0, run.stdout)
        run, position = self.call("select_context.py", "--position")
        self.assertEqual(run.returncode, 0, run.stdout)
        self.assertEqual(position["next_step"], 1)
        self.assertNotIn("legacy_next_action", position)
        self.assertIn("Acceptance", self.original)
        self.assertEqual(position["acceptance"], "The validator reports a valid profile.")
        run, context = self.call("select_context.py", "--unit", "W-001/step-1")
        self.assertEqual(context["work_item"]["source_text"], "1. [status: todo] Perform the single action.\n")

    def test_instructions_paused_returns_and_open_decisions_are_explicit_context(self):
        self.steps(["[status: in_progress] Validate current records."])
        text = self.plan.read_text(encoding="utf-8").replace("Steps:\n", "Instructions: Before completion, obtain independent review.\nSteps:\n", 1)
        text = text.replace("Status: todo", "Status: paused", 1).replace("### W-002 Validate relationships", "### W-002 Deferred after W-001: Validate relationships")
        text = text.replace("Next action: Wait for W-001 acceptance evidence.", "Next action: After W-001 completes resume here; preserve original review requirement.")
        self.plan.write_text(text, encoding="utf-8")
        decision = self.root / "docs/decisions/0001-use-native-records.md"
        decision = next((self.root / "docs/decisions").glob("0001-*.md"))
        decision.write_text(decision.read_text(encoding="utf-8").replace("status: accepted", "status: proposed").replace("accepted: 2026-08-08\n", ""), encoding="utf-8")
        run, position = self.call("select_context.py", "--position")
        self.assertEqual(run.returncode, 0, run.stdout)
        self.assertEqual(position["instructions"], "Before completion, obtain independent review.")
        self.assertEqual(position["open_decisions"][0]["id"], "ADR-0001")
        paused = position["paused_context"][0]
        self.assertEqual(paused["work_item"], "W-002")
        self.assertIsNone(paused["instructions"])
        self.assertIn("resume here", paused["legacy_next_action"])
        self.assertEqual(paused["dependencies"], [{"id": "W-001", "status": "in_progress"}])
        self.assertEqual(position["historical_priorities"], [paused])
        self.assertNotIn("return_target", position)
        self.plan.write_text(text.replace("Next action: After W-001 completes resume here; preserve original review requirement.", "Instructions: After W-001 completes resume here; preserve original review requirement.\nNext action: Wait."), encoding="utf-8")
        run, position = self.call("select_context.py", "--position")
        self.assertIn("resume here", position["paused_context"][0]["instructions"])
        self.assertNotIn("legacy_next_action", position["paused_context"][0])

    def test_missing_explicit_empty_and_invalid_instructions_remain_distinct(self):
        self.steps(["[status: todo] Perform the action."])
        original = self.plan.read_text(encoding="utf-8")
        run, position = self.call("select_context.py", "--position")
        self.assertIsNone(position["instructions"])
        for value in ("[]", "Before closure, independently review the result."):
            self.plan.write_text(original.replace("Steps:\n", f"Instructions: {value}\nSteps:\n", 1), encoding="utf-8")
            run, validation = self.call("validate_profile.py", "--format", "json")
            self.assertEqual(run.returncode, 0, run.stdout)
            run, position = self.call("select_context.py", "--position")
            self.assertEqual(position["instructions"], value)
            run, context = self.call("select_context.py", "--unit", "W-001/step-1")
            self.assertEqual(context["work_item"]["instructions"], value)
        self.plan.write_text(original.replace("Steps:\n", "Instructions:\nSteps:\n", 1), encoding="utf-8")
        for script, args in (("validate_profile.py", ("--format", "json")), ("select_context.py", ("--position",))):
            run, result = self.call(script, *args)
            self.assertNotEqual(run.returncode, 0, run.stdout)
            self.assertIn("Instructions", str(result["diagnostics"]))

    def test_repaired_code_and_text_records_reach_real_consumers(self):
        # Author-established results exercise repaired records, not model inference.
        products = self.root / "products"
        products.mkdir()
        code = products / "conversion.py"
        code.write_text("def convert(value):\n    return int(value)\n", encoding="utf-8")
        check = subprocess.run([sys.executable, "-c", "from conversion import convert; assert convert('12') == 12; assert convert('bad') is None"], cwd=products, capture_output=True, text=True)
        self.assertNotEqual(check.returncode, 0)
        self.assertIn("ValueError", check.stderr)
        draft = products / "draft.txt"
        draft.write_text("Purpose\nExplain conversion.\nExample\n12 becomes 12.\n", encoding="utf-8")
        self.assertNotIn("Limitations", draft.read_text(encoding="utf-8"))
        for completed, unfinished, evidence in (
            ("Implement decimal conversion.", "Check invalid input.", "Numeric case passed; invalid input raised ValueError. Stale completion report disproved; repair changes records only."),
            ("Write the initial text.", "Check the text against the brief.", "Draft contains Purpose and Example; required Limitations section is missing. Brief review started, not accepted."),
        ):
            self.steps([f"[status: done] {completed}", f"[status: in_progress] {unfinished}", "Resolve an unreported external outcome."])
            text = self.plan.read_text(encoding="utf-8").replace("Evidence: []", "Evidence: " + evidence, 1)
            self.plan.write_text(text, encoding="utf-8")
            before = {path: path.read_bytes() for path in products.iterdir() if path.is_file()}
            run, result = self.call("validate_profile.py", "--format", "json")
            self.assertEqual(run.returncode, 0, run.stdout)
            run, position = self.call("select_context.py", "--position")
            self.assertEqual(position["current_steps"], [2])
            self.assertEqual(position["untracked_steps"], [3])
            self.assertEqual(position["work_status"], "in_progress")
            run, context = self.call("select_context.py", "--unit", "W-001/step-2")
            self.assertEqual(context["work_item"]["step_statuses"], [{"number": 2, "status": "in_progress"}])
            self.assertEqual(context["work_item"]["source_text"], f"2. [status: in_progress] {unfinished}\n")
            self.assertEqual(before, {path: path.read_bytes() for path in products.iterdir() if path.is_file()})
