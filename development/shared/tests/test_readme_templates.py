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
    def test_setup_sections_reject_misplaced_configuration_and_accept_correction(self):
        root = SHARED.parent / 'scoville-suite'
        config = builder.load(root, 'codex', 'suite')
        member = next(m for m in config['members'] if m['name'] == 'scoville-workflow-for-codex')
        expected = builder.readme(root, member, 'suite', config=config)
        changed = dict(member, readme=list(member['readme']))
        configuration = next(p for p in changed['readme'] if isinstance(p, str) and p.endswith('/configuration.md'))
        changed['readme'].remove(configuration)
        changed['readme'].insert(1, configuration)
        with self.assertRaisesRegex(ValueError, 'Order the member readme entries'):
            builder.readme(root, changed, 'suite', config=config)
        changed['readme'] = member['readme']
        self.assertEqual(expected, builder.readme(root, changed, 'suite', config=config))


    def test_optional_sections_may_be_absent_and_edition_gaps_close(self):
        root = SHARED.parent / 'scoville-suite'
        for profile in ('general', 'codex'):
            config = builder.load(root, profile, 'suite')
            for member in config['members']:
                with self.subTest(profile=profile, member=member['name']):
                    text = builder.readme(root, member, 'suite', config=config).decode()
                    headings = [line[3:] for line in text.splitlines() if line.startswith('## ')]
                    self.assertEqual([h for h in builder.README_SECTIONS if h in headings], headings)
                    self.assertLessEqual({'How it works', 'How to use', 'Install', 'License'}, set(headings))
                    # A fragment that is empty in this edition leaves no run of blank lines.
                    self.assertNotIn('\n\n\n\n', text)

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
                    self.assertIn('## Developer links\n', preview)
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
        member.pop('family')
        member['readme'] = ['shared:member-development-inline.md']
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

    def test_shared_sources_are_confined_and_missing_templates_fail(self):
        root = SHARED.parent / 'scoville-suite'
        self.assertEqual(SHARED / 'readme/license.md', builder.readme_source(root, 'shared:license.md'))
        with self.assertRaises(ValueError):
            builder.readme_source(root, 'shared:../runtime/scoville_config.py')
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
                self.assertIn('](LICENSE)', result)
                self.assertNotIn('{{', result)

    def test_shared_install_requires_member_variables(self):
        root = SHARED.parent / 'scoville-suite'
        member = dict(builder.load(root)['members'][0])
        member['readme'] = ['shared:scoville-install.md']
        member['variables'] = {}
        with self.assertRaisesRegex(ValueError, 'missing or invalid variant variable: skill_name'):
            builder.readme(root, member)

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
