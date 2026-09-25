"""Exercise the shipped Setup helper and the actual configuration consumers."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location("setup_builder", ROOT / "development/build_suite.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class SetupTests(unittest.TestCase):
    def test_built_setup_saves_only_valid_explicit_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            config = builder.load(ROOT, "codex", "suite")
            for name in ("scoville-setup", "scoville-ask-for-codex", "scoville-workflow-for-codex"):
                member = next(m for m in config["members"] if m["name"] == name)
                for relative, data in builder.payload(ROOT, member, config).items():
                    target = base / name / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
            project = base / "Projekt ä 中文"
            project.mkdir()
            helper = base / "scoville-setup/scoville-setup/scripts/setup.py"

            def run(operation, patch=None):
                result = subprocess.run([sys.executable, "-B", str(helper), operation,
                                         "--project-root", str(project)],
                                        input=json.dumps(patch), capture_output=True,
                                        text=True, encoding="utf-8")
                return result, json.loads(result.stdout)

            result, shown = run("show")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(shown["effective"]["ask"]["claude"]["timeout_seconds"], 3600)
            self.assertEqual(shown["effective"]["workflow"]["context"],
                             {"coordinator_percent": 25, "worker_percent": 75})
            self.assertFalse((project / ".scoville").exists())
            result, saved = run("set", {"ask": {"claude": {"timeout_seconds": 2400}},
                                        "workflow": {"context": {"worker_percent": 82}}})
            self.assertEqual(result.returncode, 0, result.stderr)
            path = project / ".scoville/config.json"
            values = json.loads(path.read_text(encoding="utf-8"))
            values["other_tool"] = {"keep": [1, 2]}
            path.write_text(json.dumps(values), encoding="utf-8")
            result, saved = run("set", {"ask": {"presets": {"sol": {"effort": "medium"}}}})
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(path.read_text())["other_tool"], {"keep": [1, 2]})
            self.assertEqual(saved["effective"]["ask"]["claude"]["timeout_seconds"], 2400)
            for level in ("none", "minimal", "max", "ultra"):
                result, failed = run("set", {"workflow": {"execute": {"low": {"reasoning": level}}}})
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("manually", failed["diagnostic"])
                result, failed = run("set", {"ask": {"presets": {"astra": {"effort": level}}}})
                self.assertNotEqual(result.returncode, 0)
            for level in ("low", "medium", "high", "xhigh"):
                result, saved = run("set", {"workflow": {"execute": {"low": {"reasoning": level}}}})
                self.assertEqual(result.returncode, 0, result.stdout)
            manual = json.loads(path.read_text(encoding="utf-8"))
            manual["workflow"]["execute"]["low"]["reasoning"] = "ultra"
            manual["ask"]["presets"]["astra"] = {"effort": "ultra"}
            path.write_text(json.dumps(manual), encoding="utf-8")
            result, saved = run("set", {"workflow": {"context": {"worker_percent": 82}}})
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertEqual(saved["effective"]["workflow"]["execute"]["low"]["reasoning"], "ultra")
            self.assertEqual(saved["effective"]["ask"]["presets"]["astra"]["effort"], "ultra")
            before = path.read_bytes()
            for patch in ({"ask": {"claude": {"timeout_seconds": 0}}},
                          {"ask": {"presets": {"sol": {"model": False}}}},
                          {"workflow": {"context": {"worker_percent": True}}},
                          {"workflow": {"execute": {"low": {"reasoning": "bad"}}}},
                          {"workflow": {"coordinator": {"title": "unwanted"}}}):
                result, failed = run("set", patch)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(failed["ok"])
                self.assertEqual(path.read_bytes(), before)
            ask = base / "scoville-ask-for-codex/scoville-ask-for-codex/scripts/ask.py"
            request = {"operation": "resolve", "project_root": str(project),
                       "overrides": {"advisers": ["fable"]}}
            result = subprocess.run([sys.executable, "-B", str(ask)], input=json.dumps(request),
                                    text=True, encoding="utf-8", capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["config"]["claude"]["timeout_seconds"], 2400)
            checkpoint = base / "scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/check_context_checkpoint.py"
            result = subprocess.run([sys.executable, "-B", str(checkpoint), "--role", "executor",
                                     "--project-root", str(project)], capture_output=True,
                                    text=True, encoding="utf-8")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["threshold_percent"], 82)

    def test_setup_is_codex_suite_only(self):
        for profile, layout, expected in [("codex", "suite", True), ("codex", "standalone", False),
                                          ("general", "suite", False)]:
            config = builder.load(ROOT, profile, layout)
            self.assertEqual(any(m["name"] == "scoville-setup" for m in config["members"]), expected)


if __name__ == "__main__":
    unittest.main()
