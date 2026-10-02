"""Fenced examples remain literal across validation and selector consumers."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

import test_validate_profile as base


class FencedRecordTests(unittest.TestCase):
    setUp = base.ValidatorTest.setUp
    tearDown = base.ValidatorTest.tearDown
    path = base.ValidatorTest.path
    replace = base.ValidatorTest.replace
    run_json = base.ValidatorTest.run_json
    decision = "docs/decisions/0001-use-read-only-validation.md"
    plan = "docs/plans/0001-validate-profile.md"

    def select(self, *args):
        run = subprocess.run(
            [sys.executable, "-B", str(base.SCRIPT.with_name("select_context.py")),
             "--root", str(self.root), *args, "--format", "json"],
            capture_output=True, text=True, encoding="utf-8")
        return run, json.loads(run.stdout)

    def test_code_headings_do_not_change_decision_identity_or_content(self):
        path = self.path(self.decision)
        original = path.read_text(encoding="utf-8")
        examples = (
            "```sh\n# Comment\n## Confirmation\necho café\n```",
            "~~~sh\n# Comment\n## Revisit when\necho café\n~~~",
            "````sh\n```\n# Still code\n## Still code\n~~~\n````",
            "   ```sh\n# Comment\n## Revisit when\n   ````` \t",
        )
        for example in examples:
            for newline in ("\n", "\r\n"):
                with self.subTest(example=example, newline=repr(newline)):
                    text = original.replace("status: accepted", "status: proposed").replace("accepted: 2026-08-08\n", "")
                    text = text.replace("## Confirmation\n", "## Confirmation\n\n" + example + "\n")
                    path.write_bytes(text.replace("\n", newline).encode("utf-8"))
                    run, validation = self.run_json()
                    self.assertEqual(0, run.returncode, validation)
                    run, inventory = self.select("--proposals")
                    self.assertEqual(0, run.returncode, inventory)
                    item = inventory["proposals"][0]
                    self.assertEqual("Use read-only validation", item["title"])
                    # The next consumer reads the returned path, including the exact code.
                    self.assertEqual(path.read_bytes(), (self.root / item["path"]).read_bytes())
                    run, context = self.select()
                    self.assertEqual(0, run.returncode, context)
                    self.assertEqual(text.replace("\n", newline), context["decisions"][0])

    def test_accepted_decision_example_does_not_block_empty_inventory(self):
        self.replace(self.decision, "## Confirmation\n", "## Confirmation\n\n```sh\n# Comment\n```\n")
        run, result = self.select("--proposals")
        self.assertEqual(0, run.returncode, result)
        self.assertEqual({"proposals": []}, result)

    def test_plan_section_names_in_code_preserve_exact_selection(self):
        example = "```markdown\n# Example\n\n## Non-goals\n\n## Work items\n\n### W-999 Example\n```"
        self.replace(self.plan, "Observe one valid profile.", "Observe one valid profile.\n\n" + example)
        run, validation = self.run_json()
        self.assertEqual(0, run.returncode, validation)
        for args in ((), ("--unit", "W-001"), ("--position",)):
            run, context = self.select(*args)
            self.assertEqual(0, run.returncode, context)
            if "--position" not in args:
                self.assertIn(example, context["plan"]["goal"])
                self.assertEqual("## Non-goals\n\n- Do not mutate project state.", context["plan"]["non_goals"].rstrip())
        run, context = self.select("--unit", "W-001/step-1")
        self.assertEqual(0, run.returncode, context)
        self.assertEqual("1. Read the canonical files.\n", context["work_item"]["source_text"])

    def test_real_extra_headings_still_fail_and_correction_passes(self):
        for heading, validator_code, selector_code in (
            ("# Extra", "SECTION_H1_INVALID", "DECISION_TITLE_INVALID"),
            ("## Extra", "SECTION_H2_ORDER", None),
        ):
            with self.subTest(heading=heading):
                self.replace(self.decision, "## Confirmation\n", "## Confirmation\n\n" + heading + "\n")
                run, validation = self.run_json()
                self.assertEqual(1, run.returncode)
                self.assertIn(validator_code, [d["code"] for d in validation["diagnostics"]])
                if selector_code:
                    run, result = self.select("--proposals")
                    self.assertEqual(1, run.returncode)
                    self.assertEqual(selector_code, result["diagnostics"][0]["code"])
                self.replace(self.decision, "\n" + heading + "\n", "\n")
                run, validation = self.run_json()
                self.assertEqual(0, run.returncode, validation)

    def test_unclosed_fence_cannot_hide_required_sections(self):
        self.replace(self.decision, "## Confirmation\n", "## Confirmation\n\n```sh\n# Comment\n")
        run, validation = self.run_json()
        self.assertEqual(1, run.returncode)
        self.assertIn("SECTION_H2_ORDER", [d["code"] for d in validation["diagnostics"]])
