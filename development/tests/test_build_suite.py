import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('builder', ROOT / 'development/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BuildTests(unittest.TestCase):
    def test_reproducible_public_packages_and_exact_inventory(self):
        with tempfile.TemporaryDirectory() as temp:
            a = builder.build(ROOT, Path(temp) / 'a', True, [])
            b = builder.build(ROOT, Path(temp) / 'b', True, [])
            self.assertEqual(a, b)
            expected = {m['name'] for m in builder.load(ROOT)['members'] if m['public_distribution']}
            self.assertEqual(expected, {m['name'] for m in a['members']})
            self.assertNotIn('scoville-workflow-for-codex', expected)
            for member in a['members']:
                self.assertIn(member['name'] + '/SKILL.md', member['files'])
                self.assertIn('README.md', member['files'])
                self.assertTrue(all('development' not in Path(p).parts for p in member['files']))

    def test_rejects_overwrite_traversal_and_unknown_member(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                builder.build(ROOT, Path(temp), True, [])
            with self.assertRaises(ValueError):
                builder.build(ROOT, Path(temp) / 'unknown', True, ['unknown'])
            for path in ('../escape', '/absolute', 'C:/absolute', 'a\\b', ''):
                with self.subTest(path=path), self.assertRaises(ValueError):
                    builder.within(ROOT, path)

    def test_private_member_is_not_silently_published(self):
        private = [m['name'] for m in builder.load(ROOT)['members'] if not m['public_distribution']]
        with tempfile.TemporaryDirectory() as temp:
            for name in private:
                with self.assertRaises(ValueError):
                    builder.build(ROOT, Path(temp) / name, True, [name])

    def test_readmes_match_sources(self):
        self.assertEqual([], builder.render_readmes(ROOT, False))

    def test_wordpress_member_routing_and_family_projection(self):
        name = 'scoville-wordpress-ui-backend-anti-ai-slop'
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'build'
            receipt = builder.build(ROOT, output, True, [])
            self.assertIn(name, {m['name'] for m in receipt['members']})
            for member in receipt['members']:
                readme = (output / member['name'] / 'README.md').read_text(encoding='utf-8')
                family = readme.split('## Scoville family', 1)[1]
                self.assertEqual(family.count('https://github.com/benjaminstelzer/' + name), 1)
                self.assertNotIn('{{ include:', readme)
            package = output / name / name
            core = (package / 'SKILL.md').read_text(encoding='utf-8')
            self.assertIn('name: ' + name, core)
            self.assertTrue((package / 'references/routing.md').is_file())
            self.assertIn('$' + name, (package / 'agents/openai.yaml').read_text(encoding='utf-8'))
            for neighbor in ('scoville-ui-anti-ai-slop', 'scoville-design-anti-ai-slop'):
                metadata = (output / neighbor / neighbor / 'SKILL.md').read_text(encoding='utf-8').split('---', 2)[1]
                self.assertIn(name, metadata)
                self.assertNotIn(' wordpress-backend-ui', metadata)


if __name__ == '__main__':
    unittest.main()
