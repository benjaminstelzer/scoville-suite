import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

SHARED = Path(__file__).resolve().parents[1]
ROOT = SHARED.parent / 'scoville-suite'
spec = importlib.util.spec_from_file_location('family_builder', SHARED / 'build/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class FamilyFragmentsTests(unittest.TestCase):
    def test_suite_only_install_projection_uses_suite_package(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = builder.load(ROOT)
            workflow = next(m for m in config['members'] if m.get('distribution') == 'suite')
            workflow['visibility'] = 'public'
            workflow['public_distribution'] = True
            (root / 'suite.json').write_text(json.dumps(config), encoding='utf-8')
            result = builder.expand_fragments(root, '{{ include: family.install }}')
            self.assertIn('https://github.com/benjaminstelzer/scoville-suite/tree/main/packages/scoville-workflow-for-codex/scoville-workflow-for-codex', result)
            self.assertNotIn('https://github.com/benjaminstelzer/scoville-workflow-for-codex', result)

    def test_new_member_updates_every_full_projection_but_not_subsets(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'suite'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            shutil.copytree(SHARED / 'readme', root.parent / 'shared/readme')
            config = builder.load(root)
            name = 'scoville-test-member'
            config['members'].append({'name': name, 'repository': 'benjaminstelzer/' + name,
                                      'visibility': 'public', 'public_distribution': True,
                                      'family': {'order': 100, 'label': 'Test member', 'owner': 'test ownership.',
                                                 'summary': 'provides a test capability.'}})
            (root / 'suite.json').write_text(json.dumps(config), encoding='utf-8')
            for member in config['members'][:-1]:
                readme = builder.readme(root, member).decode()
                self.assertIn(f'https://github.com/benjaminstelzer/{name}', readme)
                self.assertIn('[Test member]', readme)
                self.assertIn('[Workflow Codex](https://github.com/benjaminstelzer/scoville-suite)', readme)
                source = root / f'members/{member["name"]}/{member["name"]}/SKILL.md'
                raw = source.read_text(encoding='utf-8')
                rendered = builder.expand_fragments(root, raw, member)
                self.assertNotIn('{{ include:', rendered)
                if 'family.owners' in raw:
                    self.assertLess(rendered.index('`scoville-handoff`:'), rendered.index(f'`{name}`:'))
                elif 'family.neighbors' in raw:
                    self.assertNotIn(name, rendered)
            index = builder.expand_fragments(root, '{{ include: suite.members }}')
            self.assertIn(f'members/{name}/README.md', index)

    def test_unknown_fragment_and_bad_order_fail(self):
        with self.assertRaisesRegex(ValueError, 'unknown build fragment'):
            builder.expand_fragments(ROOT, '{{ include: family.typo }}')
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = builder.load(ROOT)
            config['members'][0]['family']['order'] = config['members'][1]['family']['order']
            (root / 'suite.json').write_text(json.dumps(config), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'unique nonnegative integer'):
                builder.expand_fragments(root, '{{ include: family.owners }}')

    def test_ask_index_grows_without_scoville_metadata(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = builder.load(SHARED.parent / 'ask-suite-for-codex')
            config['members'].append({'name': 'ask-test', 'repository': 'benjaminstelzer/ask-test',
                                      'visibility': 'public', 'public_distribution': True})
            (root / 'suite.json').write_text(json.dumps(config), encoding='utf-8')
            result = builder.expand_fragments(root, '{{ include: suite.members }}')
            self.assertTrue(result.endswith('- [ask-test](https://github.com/benjaminstelzer/ask-test).'))
            self.assertNotIn('scoville', result)

    def test_standalone_build_and_modified_copy_detection(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'built'
            receipt = builder.build(ROOT, output, True, [])
            self.assertEqual([], builder.verify_packages(ROOT, output))
            self.assertIn('manifest_sha256', receipt)
            for member in receipt['members']:
                for relative in member['files']:
                    if relative.endswith('.md'):
                        self.assertNotIn(b'{{ include:', (output / member['package_path'] / relative).read_bytes())
            altered = output / 'scoville-code-anti-ai-slop/scoville-code-anti-ai-slop/SKILL.md'
            altered.write_text(altered.read_text(encoding='utf-8').replace('source-backed research', 'DRIFT'), encoding='utf-8')
            self.assertEqual(['scoville-code-anti-ai-slop: package differs from current sources'],
                             builder.verify_packages(ROOT, output))


if __name__ == '__main__':
    unittest.main()
