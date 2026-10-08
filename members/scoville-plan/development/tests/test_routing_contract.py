"""Package resource contracts; wording is assessed by practical model reviews."""
import importlib.util
import json
import posixpath
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "scoville-plan"
TESTS = Path(__file__).resolve().parent


def builder():
    suite = ROOT.parents[2]
    spec = importlib.util.spec_from_file_location('routing_build', suite / 'development/build_suite.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return suite, module


class RoutingContractTest(unittest.TestCase):
    def test_runtime_profiles_keep_distinct_fallback_resources(self):
        suite, build = builder()
        for profile, layout in (('general', 'standalone'), ('general', 'suite'), ('codex', 'suite')):
            config = build.load(suite, profile, layout)
            member = next(m for m in config['members'] if m['name'] == 'scoville-plan')
            package = build.payload(suite, member, config)
            expected = {'scoville-plan/' + rule['fallback']
                        for rule in member['helper_contracts'].values() if rule.get('fallback')}
            actual = {path for path in package if '/references/fallbacks/' in path}
            self.assertEqual(actual, expected if profile == 'general' else set())
            for script in member['helper_contracts']:
                self.assertIn('scoville-plan/' + script, package)

    def test_contract_sources_and_shipped_links_resolve(self):
        contract = json.loads((TESTS / 'native-feature-contract.json').read_text(encoding='utf-8'))
        for feature in contract['features']:
            for source in feature['sources']:
                self.assertTrue((ROOT / source).is_file(), (feature['id'], source))
        suite, build = builder()
        for profile, layout in (('general', 'standalone'), ('general', 'suite'), ('codex', 'suite')):
            config = build.load(suite, profile, layout)
            member = next(m for m in config['members'] if m['name'] == 'scoville-plan')
            package = build.payload(suite, member, config)
            for name, data in package.items():
                if not name.startswith('scoville-plan/') or not name.endswith('.md'):
                    continue
                for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", data.decode('utf-8')):
                    if '://' not in target:
                        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
                        self.assertIn(resolved, package, (profile, layout, name, target))


if __name__ == '__main__':
    unittest.main()
