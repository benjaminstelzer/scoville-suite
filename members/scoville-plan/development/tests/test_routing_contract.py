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
        for profile, layout in (('general', 'standalone'), ('general', 'suite'), ('codex', 'suite')):
            config = builder.load(suite, profile, layout)
            member = next(m for m in config['members'] if m['name'] == 'scoville-plan')
            package = builder.payload(suite, member, config)
            core = package['scoville-plan/SKILL.md'].decode()
            self.assertEqual('select_context-fallback.md' in core, profile == 'general')
            self.assertIn('Only when Python is unavailable' if profile == 'general' else 'Do not substitute manual execution', core)
            repair_path = 'scoville-plan/references/repair.md'
            self.assertIn(repair_path, package)
            repair_rows = [line for line in core.splitlines() if '](' + 'references/repair.md)' in line]
            self.assertEqual(len(repair_rows), 1)
            self.assertRegex(repair_rows[0], r'(?i)explicit request.*inspect.*repair')
            for path, content in package.items():
                if path.endswith('.md') and path not in (repair_path, 'scoville-plan/SKILL.md'):
                    self.assertNotRegex(content.decode(), r'\]\([^)]*repair\.md\)')
            reader = package['scoville-plan/references/read-only.md'].decode()
            self.assertIn('--plan PLAN-0001 --position', reader)
            self.assertIn('--proposals --format json', core)
            self.assertNotIn('--proposals --format json', reader)
            self.assertIn('../SKILL.md#proposal-inventory', reader)
            self.assertIn('scoville-plan/scripts/markdown_structure.py', package)
            edit = package['scoville-plan/references/edit.md'].decode()
            self.assertIn('../SKILL.md#runtime-helpers', edit)
            self.assertNotIn('#load-only-the-current-route', edit)
            self.assertNotIn('sole no-Python fallback', edit)
            if profile == 'codex':
                for path, content in package.items():
                    if path.startswith('scoville-plan/') and path.endswith('.md'):
                        self.assertNotRegex(content.decode(), r'(?i)without Python,\s*(?:General uses|use|follow)')
                self.assertIn('Scoville Workflow can group', reader)
            else:
                self.assertNotIn('Scoville Workflow can group', reader)
            decision = package['scoville-plan/references/native-decision-format.md'].decode()
            self.assertEqual('validator manual route' in decision, profile == 'general')
            fallback_files = [path for path in package if '/fallbacks/' in path]
            self.assertEqual(bool(fallback_files), profile == 'general')
            if profile == 'general':
                fallback = package['scoville-plan/references/fallbacks/select_context-fallback.md'].decode()
                self.assertIn('actual task results', fallback)
                self.assertIn('project-wide proposal inventory', fallback)
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
        # Generated references must resolve in the shipped package, not through
        # development-source files unavailable to its consumer.
        import importlib.util
        import posixpath
        suite = ROOT.parents[2]
        spec = importlib.util.spec_from_file_location('link_build', suite / 'development/build_suite.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        for profile, layout in (('general', 'standalone'), ('general', 'suite'), ('codex', 'suite')):
            config = builder.load(suite, profile, layout)
            member = next(m for m in config['members'] if m['name'] == 'scoville-plan')
            package = builder.payload(suite, member, config)
            for name, data in package.items():
                if not name.startswith('scoville-plan/') or not name.endswith('.md'):
                    continue
                for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", data.decode('utf-8')):
                    if '://' not in target:
                        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
                        self.assertIn(resolved, package, (profile, layout, name, target))


if __name__ == "__main__":
    unittest.main()
