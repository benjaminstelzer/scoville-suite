"""Instruction routing contracts; behavioral model runs are recorded separately."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "scoville-plan"
TESTS = Path(__file__).resolve().parent


class RoutingContractTest(unittest.TestCase):
    def test_common_edit_route_is_self_contained(self):
        core = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        row = next(line for line in core.splitlines() if line.startswith("| Insert,"))
        self.assertEqual(re.findall(r"\]\(([^)]+)\)", row), ["references/edit.md"])
        edit = (ROOT / "references/edit.md").read_text(encoding="utf-8")
        for command in ("scripts/validate_profile.py", "scripts/select_context.py"):
            self.assertIn(command, edit)
        for state in ("todo", "in_progress", "paused", "done", "cancelled"):
            self.assertIn(state, edit)
        for exit_result in ("0 / true", "1 / false", "2 / null", "3 / null"):
            self.assertIn(exit_result, edit)

    def test_runtime_profiles_keep_distinct_fallback_contracts(self):
        core = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        general = " ".join(re.findall(r"{{ profile: general }}(.*?){{ /profile }}", core, re.S))
        codex = " ".join(re.findall(r"{{ profile: codex }}(.*?){{ /profile }}", core, re.S))
        self.assertIn("profile-without-python.md", general)
        self.assertIn("Python 3.11+", codex)
        self.assertNotIn("profile-without-python.md", codex)
        self.assertIn("blocks", codex)
        edit = (ROOT / "references/edit.md").read_text(encoding="utf-8")
        general_edit = " ".join(re.findall(r"{{ profile: general }}(.*?){{ /profile }}", edit, re.S))
        codex_edit = " ".join(re.findall(r"{{ profile: codex }}(.*?){{ /profile }}", edit, re.S))
        self.assertIn("Only when Python is available", general_edit)
        self.assertIn("Without Python, use the manual routes", general_edit)
        self.assertIn("required Python 3.11+", codex_edit)
        self.assertNotIn("manual routes", codex_edit)

    def test_granularity_keeps_mechanism_and_annotations_without_class_definitions(self):
        text = (ROOT / "references/planning-granularity.md").read_text(encoding="utf-8")
        for meaning in ("accepted, blocked, resumed", "repository-relative paths",
                        "interacting owners", "necessary discovery", "verification",
                        "materially different consequence", "[route: ...]", "[execute: ...]"):
            self.assertIn(meaning, text)
        self.assertNotRegex(text, r"`(?:ultra_low|low|medium|high|ultra_high)`")

    def test_activation_preserves_transition_authority(self):
        lifecycle = (ROOT / "references/native-project-lifecycle.md").read_text(encoding="utf-8")
        self.assertIn("target draft Plan", lifecycle)
        self.assertIn("do not reactivate them", lifecycle)
        self.assertIn("never a lifecycle transition", lifecycle)

    def test_contract_sources_resolve(self):
        contract = json.loads((TESTS / "native-feature-contract.json").read_text(encoding="utf-8"))
        for feature in contract["features"]:
            for source in feature["sources"]:
                self.assertTrue((ROOT / source).is_file(), (feature["id"], source))
        for file in [ROOT / "SKILL.md", * (ROOT / "references").glob("*.md")]:
            for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", file.read_text(encoding="utf-8")):
                if "://" not in target:
                    self.assertTrue((file.parent / target).is_file(), (file.name, target))


if __name__ == "__main__":
    unittest.main()
