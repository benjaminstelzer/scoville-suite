import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('builder', ROOT / 'development/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BuildTests(unittest.TestCase):
    def test_public_source_text_has_no_machine_specific_paths(self):
        private_root = re.compile(
            r'(?i)(?:[a-z]:[/\\](?:users|dropbox|projekts)(?:[/\\]|$)|/(?:users|home)/[^/\s]+/)'
        )
        tracked = subprocess.run(
            ['git', 'ls-files', '-z'], cwd=ROOT, check=True, capture_output=True
        ).stdout.split(b'\0')
        for relative in tracked:
            if not relative:
                continue
            path = ROOT / relative.decode('utf-8')
            try:
                text = path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                continue
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIsNone(private_root.search(text))

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

    def test_sizes_count_utf8_bytes_and_trace_reads_without_claiming_stale_measurements(self):
        files = {'demo/SKILL.md': 'café'.encode(), 'demo/references/a.md': '日本語'.encode()}
        trace = {'case_id': 'read-twice', 'served_files': [
            {'path': 'references/a.md', 'sha256': hashlib.sha256(files['demo/references/a.md']).hexdigest()}
        ] * 2}
        report = builder.size_report('demo', files, [trace])
        self.assertEqual(14, report['package_bytes'])
        self.assertEqual(5, report['entrypoint_bytes'])
        self.assertEqual(18, report['observed_routes'][0]['observed_reference_bytes'])
        files['demo/references/a.md'] = b'changed'
        stale = builder.size_report('demo', files, [trace])['observed_routes'][0]
        self.assertIsNone(stale['observed_reference_bytes'])
        self.assertEqual(14, stale['current_equivalent_reference_bytes'])
        self.assertFalse(stale['matches_current_files'])

    def test_readmes_match_sources(self):
        self.assertEqual([], builder.render_readmes(ROOT, False))

    def test_suite_readmes_separate_new_install_and_complete_upgrade(self):
        legacy = {
            'scoville-brainstorm', 'scoville-code-anti-ai-slop',
            'scoville-design-anti-ai-slop', 'scoville-handoff', 'scoville-plan',
            'scoville-research', 'scoville-scribe-anti-ai-slop',
            'scoville-ui-anti-ai-slop',
            'scoville-wordpress-ui-backend-anti-ai-slop',
            'scoville-workflow-for-codex', 'scoville-workflow-codex',
            'ask-astra-for-review-for-codex', 'ask-sol-for-review-for-codex',
            'ask-claude-for-codex', 'ask-claude-and-astra-for-codex',
            'ask-claude-and-sol-for-codex',
        }
        repositories = {
            'general': 'https://github.com/benjaminstelzer/scoville-suite',
            'codex': 'https://github.com/benjaminstelzer/scoville-suite-for-codex',
        }
        for profile, repository in repositories.items():
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as temp:
                destination = Path(temp)
                config = builder.load(ROOT, profile, 'suite')
                builder.render_readmes(ROOT, True, config, destination)
                text = (destination / 'README.md').read_text(encoding='utf-8')
                new_marker = '### New installation'
                upgrade_marker = '### Upgrade from an earlier Scoville or Ask suite'
                self.assertLess(text.index(new_marker), text.index(upgrade_marker))
                new_install = text.split(new_marker, 1)[1].split(upgrade_marker, 1)[0]
                upgrade = text.split(upgrade_marker, 1)[1].split('\n## ', 1)[0]
                self.assertIn(repository, new_install)
                self.assertNotIn('Uninstall these Skills', new_install)
                self.assertIn(repository, upgrade)
                inventory = upgrade.split(
                    'Uninstall these Skills completely, including their settings, when present:\n', 1
                )[1].split('\nSkip absent entries', 1)[0]
                actual = {item.strip().rstrip('.') for item in inventory.replace('\n', ' ').split(',')}
                self.assertEqual(legacy, actual)
                self.assertIn('leave unrelated Skills untouched', upgrade)
                self.assertIn('keep no backup or settings migration', upgrade)
                for readme in destination.rglob('README.md'):
                    rendered = readme.read_text(encoding='utf-8')
                    self.assertNotRegex(rendered, r'(?<![A-Za-z])[A-Za-z]:[\\/]')
                    self.assertNotIn('/Users/', rendered)
                    self.assertNotIn('/home/', rendered)

    def test_suite_overview_links_each_member_how_to_use(self):
        for profile, expected_count in (('general', 4), ('codex', 7)):
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as temp:
                destination = Path(temp)
                config = builder.load(ROOT, profile, 'suite')
                builder.render_readmes(ROOT, True, config, destination)
                overview = (destination / 'README.md').read_text(encoding='utf-8')
                self.assertEqual(expected_count, overview.count('/README.md#how-to-use)'))
                for member in config['members']:
                    name = member['name']
                    self.assertIn(f'(members/{name}/README.md#how-to-use)', overview)
                    full_readme = destination / 'members' / name / 'README.md'
                    self.assertTrue(full_readme.is_file())
                    self.assertIn('\n## How to use\n', full_readme.read_text(encoding='utf-8'))
                workflow_link = '(members/scoville-workflow-for-codex/README.md#how-to-use)'
                self.assertEqual(profile == 'codex', workflow_link in overview)

    def test_family_contract_preserves_exclusions_and_explicit_activation(self):
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            cores = {}
            for member in config['members']:
                name = member['name']
                core = builder.payload(ROOT, member, config)[name + '/SKILL.md'].decode()
                cores[name] = core
                with self.subTest(profile=profile, layout=layout, member=name):
                    if layout == 'standalone':
                        self.assertIn('Honor explicit user exclusions.', core)
                        self.assertIn('simulate or require an absent sibling', core)
                        self.assertNotIn('installed and enabled', core)
                    else:
                        self.assertIn('Explicit invocation gates and user exclusions still apply.', core)
                        self.assertIn('without checking sibling availability', core)
                        self.assertNotIn('Other Scoville Skills are optional', core)
            if 'scoville-workflow-for-codex' in cores:
                self.assertIn('Ordinary implementation, planning or delegation requests do not activate it.',
                              cores['scoville-workflow-for-codex'])
            if 'scoville-ask-for-codex' in cores:
                self.assertIn('Ordinary questions to the current assistant do not trigger a consultation.',
                              cores['scoville-ask-for-codex'])
            if 'scoville-setup' in cores:
                self.assertIn('Do not start Ask,\nWorkflow', cores['scoville-setup'])

    def test_each_suite_rejects_partial_installation_build(self):
        for profile in ('general', 'codex'):
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as temp:
                output = Path(temp) / 'partial'
                with self.assertRaisesRegex(ValueError, 'complete member set'):
                    builder.build(ROOT, output, True, ['scoville-plan'], profile, 'suite')
                self.assertFalse(output.exists())

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
