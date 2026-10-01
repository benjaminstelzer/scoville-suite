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
        import importlib.util
        suite = ROOT.parents[2]
        spec = importlib.util.spec_from_file_location('routing_build', suite / 'development/build_suite.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        for profile in ('general', 'codex'):
            config = builder.load(suite, profile)
            member = next(m for m in config['members'] if m['name'] == 'scoville-plan')
            package = builder.payload(suite, member, config)
            core = package['scoville-plan/SKILL.md'].decode()
            self.assertEqual('select_context-fallback.md' in core, profile == 'general')
            self.assertIn('Only when Python is unavailable' if profile == 'general' else 'Do not substitute manual execution', core)
            repair_path = 'scoville-plan/references/repair.md'
            self.assertIn(repair_path, package)
            repair_rows = [line for line in core.splitlines() if '](' + 'references/repair.md)' in line]
            self.assertEqual(len(repair_rows), 1)
            self.assertTrue(repair_rows[0].startswith('| Explicit request to inspect/repair'))
            for path, content in package.items():
                if path.endswith('.md') and path not in (repair_path, 'scoville-plan/SKILL.md'):
                    self.assertNotRegex(content.decode(), r'\]\([^)]*repair\.md\)')
            reader = package['scoville-plan/references/read-only.md'].decode()
            self.assertIn('--plan PLAN-0001 --position', reader)
            fallback_files = [path for path in package if '/fallbacks/' in path]
            self.assertEqual(bool(fallback_files), profile == 'general')
            if profile == 'general':
                fallback = package['scoville-plan/references/fallbacks/select_context-fallback.md'].decode()
                self.assertIn('actual task results', fallback)
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
