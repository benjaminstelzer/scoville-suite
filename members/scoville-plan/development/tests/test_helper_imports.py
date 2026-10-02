"""Bundled imports work in isolation and report broken packages without a verdict."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[2] / "scoville-plan" / "scripts"
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "valid-profile"
HELPERS = ("select_context.py", "validate_profile.py")


class HelperImportTests(unittest.TestCase):
    def run_helper(self, script, mode="normal", output_format="json"):
        env = os.environ.copy()
        env.pop("PYTHONSAFEPATH", None)
        if mode == "safepath":
            env["PYTHONSAFEPATH"] = "1"
        return subprocess.run(
            [sys.executable, "-B", *(["-I"] if mode == "isolated" else []),
             str(script), "--root", str(FIXTURE), "--format", output_format],
            capture_output=True, text=True, encoding="utf-8", env=env,
        )

    def assert_success(self, run, helper):
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        self.assertEqual("", run.stderr)
        result = json.loads(run.stdout)
        if helper == "validate_profile.py":
            self.assertIs(result["valid"], True)
            self.assertEqual([], result["diagnostics"])
        else:
            # The context consumer receives the original canonical Work Item.
            plan = next((FIXTURE / "docs" / "plans").glob("*.md")).read_text(encoding="utf-8")
            self.assertIn(result["work_item"].rstrip(), plan)
            self.assertIn("### W-001", result["work_item"])

    def test_isolated_and_safe_path_match_normal_context(self):
        for helper in HELPERS:
            normal = self.run_helper(SCRIPTS / helper)
            self.assert_success(normal, helper)
            for mode in ("isolated", "safepath"):
                with self.subTest(helper=helper, mode=mode):
                    run = self.run_helper(SCRIPTS / helper, mode)
                    self.assert_success(run, helper)
                    self.assertEqual(json.loads(normal.stdout), json.loads(run.stdout))

    def test_missing_or_broken_module_reports_failure_and_restoration_works(self):
        for helper in HELPERS:
            for defect in ("missing", "syntax", "export"):
                with self.subTest(helper=helper, defect=defect), tempfile.TemporaryDirectory() as directory:
                    script = Path(directory) / helper
                    module = script.with_name("markdown_structure.py")
                    shutil.copyfile(SCRIPTS / helper, script)
                    if defect == "syntax":
                        module.write_text("def broken(\n", encoding="utf-8")
                    elif defect == "export":
                        module.write_text("# missing export\n", encoding="utf-8")
                    run = self.run_helper(script, "isolated")
                    self.assertEqual(3, run.returncode, run.stdout + run.stderr)
                    self.assertEqual("", run.stderr)
                    result = json.loads(run.stdout)
                    self.assertIsNone(result["valid"])
                    diagnostic = result["diagnostics"][0]
                    self.assertEqual(str(module), diagnostic.get("file", diagnostic.get("path")))
                    self.assertIn("mask_fenced_code", diagnostic["expected"])
                    self.assertIn("same package version", diagnostic.get("suggestion", diagnostic["message"]))
                    self.assertTrue(diagnostic["observed"])
                    self.assertNotIn("work_item", result)
                    if helper == "validate_profile.py":
                        self.assertEqual(0, result["summary"]["files_checked"])
                        text_run = self.run_helper(script, "isolated", "text")
                        self.assertEqual(3, text_run.returncode)
                        self.assertIn("markdown_structure.py", text_run.stdout)
                        self.assertIn("same package version", text_run.stdout)
                    # Apply the actual diagnostic's correction and consume its result.
                    shutil.copyfile(SCRIPTS / "markdown_structure.py", module)
                    self.assert_success(self.run_helper(script, "isolated"), helper)
