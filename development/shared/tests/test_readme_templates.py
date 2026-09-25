import importlib.util
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

SHARED = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('readme_builder', SHARED / 'build/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class ReadmeTemplateTests(unittest.TestCase):
    def test_workflow_beta_notice_can_be_removed_without_runtime_changes(self):
        root = SHARED.parent / 'scoville-suite'
        config = builder.load(root, 'codex')
        member = next(m for m in config['members'] if m['name'] == 'scoville-workflow-for-codex')
        beta = builder.payload(root, member, config)
        stable = dict(member, variables=dict(member['variables'], release_notice=''))
        candidate = builder.payload(root, stable, config)
        self.assertIn(b'**Beta.**', beta['README.md'])
        self.assertNotIn(b'**Beta.**', candidate['README.md'])
        self.assertEqual({p: b for p, b in beta.items() if p != 'README.md'},
                         {p: b for p, b in candidate.items() if p != 'README.md'})

    def test_development_blocks_are_suite_only_for_every_member(self):
        for profile in ('general', 'codex'):
            name = 'scoville-suite'
            root = SHARED.parent / name
            config = builder.load(root, profile)
            index = builder.expand_fragments(root, '{{ include: suite.development }}', config=config)
            for member in config['members']:
                with self.subTest(suite=name, member=member['name']):
                    release = builder.readme(root, member, config=config).decode()
                    preview = builder.readme(root, member, 'suite', config=config).decode()
                    self.assertNotIn('## Development\n', release)
                    self.assertIn('## How it was developed\n', preview)
                    self.assertIn(member['name'], index)
                    for path in member['development'].values():
                        self.assertTrue((root / path).exists())
                        self.assertIn('/main/' + path, preview)
                        self.assertIn('/main/' + path, index)
                    self.assertNotIn('{{', preview)
                    builder.payload(root, member, config)

    def test_audience_typos_and_unscoped_development_fail(self):
        with self.assertRaisesRegex(ValueError, 'invalid README fragment'):
            builder.readme_references([{'source': 'notes.md', 'audience': 'sutie'}], 'release')
        with self.assertRaisesRegex(ValueError, 'unknown README audience'):
            builder.readme_references([], 'sutie')
        root = SHARED.parent / 'scoville-suite'
        member = dict(builder.load(root)['members'][0])
        member.pop('description_fragments', None)
        member['readme'] = ['shared:member-development.md']
        with self.assertRaisesRegex(ValueError, 'requires suite audience'):
            builder.readme(root, member)
        member['development'] = dict(member['development'], notes='development/missing.md')
        with self.assertRaisesRegex(ValueError, 'missing development target'):
            builder.readme(root, member, 'suite')

    def test_new_member_joins_developer_index_from_manifest(self):
        root = SHARED.parent / 'scoville-suite'
        config = builder.load(root)
        added = dict(config['members'][0], name='new-ask-variant', family=dict(config['members'][0]['family'], order=99))
        config['members'].append(added)
        with patch.object(builder, 'load', return_value=config):
            index = builder.expand_fragments(root, '{{ include: suite.development }}', config=config)
        self.assertEqual(1, index.count('**new-ask-variant**'))
        self.assertIn(added['development']['source'], index.split('**new-ask-variant**')[1])

    def test_package_links_use_output_inventory_not_source_tree(self):
        files = {'README.md': b'[Skill](skill/SKILL.md)\n[Notes][n]\n[n]: <skill/references/with%20space.md>\n',
                 'skill/SKILL.md': b'[Rule](references/with%20space.md#rule)\n[Root](../README.md)\n',
                 'skill/references/with space.md': b'# Rule\n'}
        builder.validate_package_links(files)
        for link in ('[Missing](development/test.py)', '[Escape](../README.md)',
                     '[File](file:///C:/source/README.md)', '[Drive](C:/source/README.md)',
                     '[Encoded](%2e%2e/README.md)', '[Root](/README.md)',
                     '[Missing][test]\n[test]: development/test.py',
                     '<a href="development/test.py">Test</a>',
                     '![Preview](development/screenshot.png)'):
            with self.subTest(link=link), self.assertRaises(ValueError):
                builder.validate_package_links(dict(files, **{'README.md': link.encode()}))
        files['README.md'] += b'\n[Web](https://example.org/no-local-file)\n[Section](#title)\n`[Example](missing.md)`\n```md\n[Example](missing.md)\n```\n'
        files['CHANGELOG.md'] = b'[Historical](development/old-test.py)'
        builder.validate_package_links(files)

    def test_release_gate_rejects_excluded_files_and_missing_links(self):
        root = SHARED.parent / 'scoville-suite'
        member = dict(builder.load(root)['members'][0])
        member['files'] = member['files'] + [{'source': 'suite.json', 'target': member['name'] + '/development/test.json'}]
        with self.assertRaisesRegex(ValueError, 'development or local file'):
            builder.payload(root, member)
        member = builder.load(root)['members'][0]
        with patch.object(builder, 'readme', return_value=b'[Absent](development/test.py)'):
            with self.assertRaisesRegex(ValueError, 'missing package link target'):
                builder.payload(root, member)

    def test_suite_descriptions_reuse_member_sources_and_feature_workflow(self):
        root = SHARED.parent / 'scoville-suite'
        result = builder.expand_fragments(root, '{{ include: suite.descriptions }}', config=builder.load(root, 'codex'))
        self.assertTrue(result.startswith('## Scoville Workflow for Codex\n'))
        for member in builder.load(root)['members']:
            source = builder.readme_source(root, member['readme'][0]).read_text(encoding='utf-8').strip()
            self.assertIn(builder.expand_variables(source.partition('\n')[2], member), result)
        self.assertIn('Workflow is suite-only', result)
        self.assertIn('requires Codex desktop', result)
        expected = sorted(builder.load(root)['members'], key=lambda m: m['family']['order'])
        expected = [m for m in expected if m['name'] != 'scoville-workflow-for-codex']
        headings = [builder.readme_source(root, m['readme'][0]).read_text(encoding='utf-8').splitlines()[0][2:] for m in expected]
        positions = [result.index('## ' + heading + '\n') for heading in headings]
        self.assertEqual(sorted(positions), positions)
        with self.assertRaisesRegex(ValueError, 'only valid in the suite README'):
            builder.expand_fragments(root, '{{ include: suite.descriptions }}', builder.load(root)['members'][0])

    def test_description_addition_edit_and_missing_source(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            member = {'name': 'new-skill', 'repository': 'benjaminstelzer/new-skill',
                      'visibility': 'public', 'public_distribution': True, 'readme': ['intro.md']}
            config = {'schema_version': 1, 'name': 'test-suite', 'members': [member]}
            (root / 'suite.json').write_text(json.dumps(config), encoding='utf-8')
            source = root / 'intro.md'
            source.write_text('# New Skill\n\nOriginal description.\n', encoding='utf-8')
            for body in ('Original description.', 'Updated description.'):
                source.write_text('# New Skill\n\n' + body + '\n', encoding='utf-8')
                self.assertIn(body, builder.readme(root, member).decode())
                self.assertIn(body, builder.expand_fragments(root, '{{ include: suite.descriptions }}'))
            source.unlink()
            with self.assertRaises(FileNotFoundError):
                builder.expand_fragments(root, '{{ include: suite.descriptions }}')
            source.write_text('# New Skill\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'expected title and description'):
                builder.expand_fragments(root, '{{ include: suite.descriptions }}')
            source.write_text('# New Skill\n\n[Local](relative.md)\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'absolute links'):
                builder.expand_fragments(root, '{{ include: suite.descriptions }}')

    def test_complete_suite_has_one_final_monorepo_link(self):
        root = SHARED.parent / 'scoville-suite'
        for member in builder.load(root)['members']:
            result = builder.readme(root, member).decode()
            section = result.split('### Install the complete Scoville suite\n', 1)[1].split('\n## ', 1)[0]
            self.assertEqual(1, section.count('https://github.com/'))
            self.assertIn('https://github.com/benjaminstelzer/scoville-suite', section)
            self.assertIn('Install its released Skill packages, not development templates.', section)
            self.assertNotIn('has not been created yet', section)
            self.assertNotIn('Private repository access', section)
            self.assertNotIn('/tree/main/', section)

    def test_shared_sources_are_confined_and_missing_templates_fail(self):
        root = SHARED.parent / 'scoville-suite'
        self.assertEqual(SHARED / 'readme/license.md', builder.readme_source(root, 'shared:license.md'))
        with self.assertRaises(ValueError):
            builder.readme_source(root, 'shared:../runtime/task_lifecycle.py')
        with self.assertRaises(FileNotFoundError):
            builder.readme(root, {'readme': ['shared:missing-template.md']})

    def test_both_profiles_render_shared_license_without_placeholders(self):
        for profile in ('general', 'codex'):
            root = SHARED.parent / 'scoville-suite'
            config = builder.load(root, profile)
            members = [m for m in config['members'] if 'shared:license.md' in m['readme']]
            self.assertTrue(members)
            for member in members:
                result = builder.readme(root, member).decode()
                self.assertIn('MIT. See [LICENSE](LICENSE).', result)
                self.assertNotIn('{{', result)

    def test_shared_install_requires_member_variables(self):
        root = SHARED.parent / 'scoville-suite'
        member = dict(builder.load(root)['members'][0])
        member['readme'] = ['shared:ask-native-install.md']
        member['variables'] = {}
        with self.assertRaisesRegex(ValueError, 'missing or invalid variant variable: skill_name'):
            builder.readme(root, member)

    def test_native_install_keeps_python_check_and_personal_config(self):
        root = SHARED.parent / 'scoville-suite'
        config = builder.load(root, 'codex', 'standalone')
        member = config['members'][0]
        result = builder.readme(root, member, config=config).decode()
        self.assertIn('verify the interpreter', result)
        self.assertIn('ask before', result)
        self.assertIn('overwriting conflicting files', result)
        self.assertIn('`config.json` settings during updates', result)

    def test_receipt_tracks_shared_template_and_source_drift_is_detected(self):
        root = SHARED.parent / 'scoville-suite'
        member = 'scoville-ask-for-codex'
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'packages'
            builder.build(root, output, True, [member], 'codex', 'standalone')
            receipt = json.loads((output / 'build-receipt.json').read_text())
            self.assertIn('readme/license.md', receipt['shared_sources'])
            changed = Path(temporary) / 'license.md'
            changed.write_text('## License\n\nChanged source for drift test.\n', encoding='utf-8')
            original = builder.readme_source
            def source(suite, reference):
                return changed if reference == 'shared:license.md' else original(suite, reference)
            with patch.object(builder, 'readme_source', side_effect=source):
                self.assertEqual([member + ': package differs from current sources'],
                                 builder.verify_packages(root, output))


if __name__ == '__main__':
    unittest.main()
