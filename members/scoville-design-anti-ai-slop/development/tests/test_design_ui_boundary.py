"""Regression tests for boundary guards at their actual Design and UI owners."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


DEVELOPMENT = Path(__file__).resolve().parents[1]
ROOT = DEVELOPMENT.parent / "scoville-design-anti-ai-slop"
UI_ROOT = ROOT.parent.parent / "scoville-ui-anti-ai-slop" / "scoville-ui-anti-ai-slop"


class DesignUIBoundaryTests(unittest.TestCase):
    def check_boundary(self, owner: str | None = None, clause: str = ""):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            for name, source in (("design", ROOT), ("ui", UI_ROOT)):
                content = " ".join((source / "SKILL.md").read_text(encoding="utf-8").split())
                if name == owner:
                    self.assertIn(clause, content)
                    content = content.replace(clause, "", 1)
                target = temporary / name
                target.mkdir()
                (target / "SKILL.md").write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(DEVELOPMENT / "scripts/validate_design_ui_boundary.py"),
                 "--design-root", str(temporary / "design"),
                 "--ui-root", str(temporary / "ui")],
                capture_output=True, text=True, encoding="utf-8", check=False,
            )

    def test_current_owners_pass(self):
        result = self.check_boundary()
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_ui_fallback_must_remain_in_ui(self):
        result = self.check_boundary("ui", "retain this Skill's bounded standalone direction")
        self.assertEqual(1, result.returncode)
        self.assertIn("UI missing UI standalone fallback", result.stdout)

    def test_design_still_works_without_partner(self):
        result = self.check_boundary("design", "without a partner, handle authorised work directly")
        self.assertEqual(1, result.returncode)
        self.assertIn("Design missing Design standalone operation", result.stdout)

    def test_active_partner_does_not_take_design_ownership(self):
        result = self.check_boundary("design", "Design defines and judges; that partner implements")
        self.assertEqual(1, result.returncode)
        self.assertIn("Design missing design owns visual definition", result.stdout)


if __name__ == "__main__":
    unittest.main()
