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
            if not path.exists():  # A tracked file may be deleted or renamed in this change.
                continue
            try:
                text = path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                continue
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIsNone(private_root.search(text))

    def test_public_packages_have_no_machine_specific_paths(self):
        private_root = re.compile(
            r'(?i)(?:[a-z]:[/\\](?:users|dropbox|projekts)(?:[/\\]|$)|/(?:users|home)/[^/\s]+/)'
        )
        # Rendered public packages complement the complete tracked-source check,
        # which conservatively covers every profile-filtered suite export source.
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            for member in config['members']:
                if not member['public_distribution']:
                    continue
                for relative, data in builder.payload(ROOT, member, config).items():
                    try:
                        text = data.decode('utf-8')
                    except UnicodeDecodeError:
                        continue
                    with self.subTest(profile=profile, layout=layout,
                                      member=member['name'], path=relative):
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


    def test_suite_overview_links_each_member_how_to_use(self):
        for profile, expected_count in (('general', 5), ('codex', 8)):
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

            # Setup activation is checked by the native effect cases, not prose spelling.

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

    def test_project_context_package_is_suite_owned_and_self_contained(self):
        name = 'scoville-project-context-cleanup'
        shared_rule = ROOT.parent / 'shared/prompting/common.md'
        for profile, layout in [('general', 'standalone'), ('general', 'suite'), ('codex', 'suite')]:
            with self.subTest(profile=profile, layout=layout), tempfile.TemporaryDirectory() as temp:
                output = Path(temp) / 'build'
                receipt = builder.build(ROOT, output, True, [], profile, layout)
                member = next(m for m in receipt['members'] if m['name'] == name)
                self.assertEqual('suite', member['distribution'])
                self.assertEqual('benjaminstelzer/' + receipt['suite'], member['repository'])
                self.assertEqual(receipt['suite'] + '/packages/' + name, member['package_path'])
                package = output / member['package_path'] / name
                self.assertTrue((package / 'agents/openai.yaml').is_file())
                config = builder.load(ROOT, profile, layout)
                source_member = next(m for m in config['members'] if m['name'] == name)
                self.assertEqual(builder._module.expand_fragments(ROOT, shared_rule.read_text(encoding='utf-8'), config=config),
                                 (package / 'references/writing.md').read_text(encoding='utf-8'))
                actual_scripts = {path.relative_to(package).as_posix()
                                  for path in (package / 'scripts').rglob('*') if path.is_file()}
                self.assertEqual(set(source_member['helper_contracts']), actual_scripts)
                for path in package.rglob('*.md'):
                    text = path.read_text(encoding='utf-8')
                    self.assertNotIn('{{', text)
                    self.assertNotIn('shared/prompting/', text)

    def test_missing_project_context_writing_contract_blocks_packaging(self):
        config = builder.load(ROOT, 'codex', 'suite')
        member = next(m for m in config['members'] if m['name'] == 'scoville-project-context-cleanup')
        self.assertIn('scoville-project-context-cleanup/references/writing.md',
                      builder.payload(ROOT, member, config))
        member['files'] = [entry for entry in member['files']
                           if not entry['target'].endswith('/references/writing.md')]
        with self.assertRaisesRegex(ValueError, 'writing.md'):
            builder.payload(ROOT, member, config)


if __name__ == '__main__':
    unittest.main()
