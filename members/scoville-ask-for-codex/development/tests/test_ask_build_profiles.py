"""Build three actual distributions and check ASK's distinct membership contracts."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[4]
SPEC = importlib.util.spec_from_file_location("suite_builder", ROOT / "development/build_suite.py")
assert SPEC and SPEC.loader
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)
NAME = "scoville-ask-for-codex"


class AskBuildProfileTests(unittest.TestCase):
    def test_actual_standalone_codex_contains_only_isolated_ask_package(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "output"
            receipt = builder.build(ROOT, output, True, [], "codex", "standalone")
            self.assertEqual([member["name"] for member in receipt["members"]], [NAME])
            member = receipt["members"][0]
            package = output / member["package_path"] / NAME
            self.assertTrue((package / "SKILL.md").is_file())
            for script in ("ask.py", "list_models.py", "ask_claude.py", "task_lifecycle.py"):
                self.assertTrue((package / "scripts" / script).is_file(), script)
            self.assertEqual([package / "SKILL.md"], list(output.rglob("SKILL.md")))
            request = {"operation": "prepare", "mode": "consultation",
                "question": "Wie lösen wir das?", "scope": "isolated package",
                "reference": "standalone-proof", "caller_id": "caller-1",
                "caller_title": "Isolated task", "projectId": "project-1",
                "creation_authorized": True, "prior_state": "not_started",
                "catalog": {"source": "model/list", "models": [
                    {"model": "gpt-6-astra", "efforts": ["high"]}]}}
            result = subprocess.run([sys.executable, str(package / "scripts" / "ask.py")],
                input=json.dumps(request), text=True, encoding="utf-8",
                capture_output=True, check=False, cwd=temporary)
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertTrue(payload["ok"])
            self.assertEqual(payload["entries"][0]["arguments"]["title"], "Ask gpt-6-astra · Isolated task")

    def test_actual_codex_suite_contains_ask_as_member(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "output"
            receipt = builder.build(ROOT, output, True, [], "codex", "suite")
            members = {member["name"]: member for member in receipt["members"]}
            self.assertIn(NAME, members)
            package = output / members[NAME]["package_path"] / NAME
            self.assertTrue((package / "scripts" / "ask.py").is_file())
            self.assertTrue((package / "scripts" / "task_lifecycle.py").is_file())
            self.assertEqual(1, len(list(output.rglob("scoville-ask-for-codex/SKILL.md"))))

    def test_actual_general_suite_catalogs_ask_without_runtime_payload(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "output"
            receipt = builder.build(ROOT, output, True, [], "general", "suite")
            self.assertNotIn(NAME, {member["name"] for member in receipt["members"]})
            self.assertFalse(list(output.rglob("scoville-ask-for-codex/SKILL.md")))
            self.assertFalse(list(output.rglob("scoville-ask-for-codex/scripts/ask.py")))
            preview = Path(temporary) / "preview"
            builder.render_readmes(ROOT, True, builder.load(ROOT, "general", "suite"), preview)
            readme = (preview / "README.md").read_text(encoding="utf-8")
            self.assertIn(NAME, readme)
            self.assertIn("Codex online", readme)
            self.assertIn("Install this Skill for all my projects from this exact package directory:", readme)
            self.assertIn(
                "https://github.com/benjaminstelzer/scoville-ask-for-codex/tree/main/scoville-ask-for-codex",
                readme,
            )


if __name__ == "__main__":
    unittest.main()
