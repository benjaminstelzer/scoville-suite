"""Project overrides reach the actual model and context consumers."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

from test_contract import PACKAGE
sys.path.insert(0, str(PACKAGE / "scripts"))
from resolve_model_pair import load_config, resolve
from check_context_checkpoint import read_thresholds


class ProjectConfigTests(unittest.TestCase):
    def test_partial_file_overrides_and_ephemeral_model_choice(self):
        defaults = PACKAGE / "assets/workflow.toml"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            original = load_config(defaults, root)
            self.assertFalse((root / ".scoville").exists())
            (root / ".scoville").mkdir()
            path = root / ".scoville/config.json"
            saved = {"workflow": {"execute": {"low": {"model": "custom-model"}},
                                  "context": {"worker_percent": 80}}}
            path.write_text(json.dumps(saved), encoding="utf-8")
            config = load_config(defaults, root)
            self.assertEqual(config["execute"]["low"]["model"], "custom-model")
            self.assertEqual(config["execute"]["low"]["reasoning"], original["execute"]["low"]["reasoning"])
            self.assertEqual(config["review"], original["review"])
            self.assertEqual(read_thresholds(defaults, root)["worker_percent"], 80)
            self.assertEqual(resolve(config, "executor", "low", "one-call")["model"], "one-call")
            self.assertEqual(json.loads(path.read_text()), saved)
            child = root / "child"
            child.mkdir()
            self.assertEqual(load_config(defaults, child), original)
            saved["workflow"]["execute"]["low"]["model"] = "next-run"
            path.write_text(json.dumps(saved), encoding="utf-8")
            self.assertEqual(load_config(defaults, root)["execute"]["low"]["model"], "next-run")

    def test_invalid_values_fail_in_the_consuming_operation(self):
        defaults = PACKAGE / "assets/workflow.toml"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".scoville").mkdir()
            path = root / ".scoville/config.json"
            for value in (None, [], {"execute": {"low": {"reasoning": False}}}):
                path.write_text(json.dumps({"workflow": value}), encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_config(defaults, root)
            for value in (False, 0, 100, 33.5, "75"):
                path.write_text(json.dumps({"workflow": {"context": {"worker_percent": value}}}), encoding="utf-8")
                with self.assertRaises(ValueError):
                    read_thresholds(defaults, root)


if __name__ == "__main__":
    unittest.main()
