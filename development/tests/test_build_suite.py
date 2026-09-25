import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

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
        config = builder.load(ROOT)
        member = config['members'][0]
        member['visibility'] = 'private'
        member['public_distribution'] = False
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(builder._module, 'load', return_value=config):
                with self.assertRaises(ValueError):
                    builder.build(ROOT, Path(temp) / member['name'], True, [member['name']])

    def test_readmes_match_sources(self):
        self.assertEqual([], builder.render_readmes(ROOT, False))

    def test_single_ui_package_in_each_distribution(self):
        name = 'scoville-ui'
        retired = {'scoville-ui-anti-ai-slop', 'scoville-wordpress-ui-backend-anti-ai-slop'}
        for profile, layout in [('general', 'standalone'), ('general', 'suite'), ('codex', 'suite')]:
            with self.subTest(profile=profile, layout=layout), tempfile.TemporaryDirectory() as temp:
                output = Path(temp) / 'build'
                receipt = builder.build(ROOT, output, True, [], profile, layout)
                names = {m['name'] for m in receipt['members']}
                self.assertIn(name, names)
                self.assertFalse(retired & names)
                member = next(m for m in receipt['members'] if m['name'] == name)
                package = output / member['package_path'] / name
                self.assertEqual([package / 'SKILL.md'], list(package.rglob('SKILL.md')))
                for relative in ('references/wordpress/adapter.md', 'references/wordpress/routing.md',
                                 'references/validation.md', 'references/wordpress/validation.md'):
                    self.assertTrue((package / relative).is_file(), relative)
                self.assertIn('$' + name, (package / 'agents/openai.yaml').read_text(encoding='utf-8'))
                for path in package.rglob('*.md'):
                    text = path.read_text(encoding='utf-8')
                    self.assertNotIn('{{', text)
                    self.assertFalse(any(old in text for old in retired), path)
                for exported in receipt['members']:
                    readme = (output / exported['package_path'] / 'README.md').read_text(encoding='utf-8')
                    self.assertNotIn('{{ include:', readme)
                    self.assertFalse(any(old in readme for old in retired), exported['name'])


if __name__ == '__main__':
    unittest.main()
