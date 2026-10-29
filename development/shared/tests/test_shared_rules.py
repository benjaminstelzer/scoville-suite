"""Verify shared-rule projection and receipt provenance, not fixed prose."""
import hashlib
import re
import sys
import tempfile
import unittest
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1]
ROOT = SHARED.parent / 'scoville-suite'
sys.path.insert(0, str(SHARED / 'build'))
import build_suite as builder


class SharedRulesTests(unittest.TestCase):
    def test_machine_data_and_python_have_separate_packaged_routes(self):
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            for member in config['members']:
                files = builder.payload(ROOT, member, config)
                prefix = member['name'] + '/'
                if not any(f['source'] == 'shared:prompting/common.md' for f in member['files']):
                    continue
                with self.subTest(profile=profile, layout=layout, member=member['name']):
                    self.assertEqual((SHARED / 'prompting/machine-data.md').read_bytes(),
                                     files[prefix + 'references/machine-data.md'])
                    self.assertIn(b'](machine-data.md)', files[prefix + 'references/writing.md'])
                    discovery = (SHARED / 'runtime/python_discovery.md').read_bytes()
                    self.assertEqual(discovery, files[prefix + 'references/python-discovery.md'])
                    self.assertNotIn(discovery.strip(), files[prefix + 'SKILL.md'])
                    self.assertIn(b'](python-discovery.md)', files[prefix + 'references/shell-commands.md'])
                    builder.validate_package_links(files)

    def test_all_writing_consumers_bundle_the_same_standalone_file(self):
        source = (SHARED / 'prompting/common.md').read_text(encoding='utf-8')
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            expected = builder.expand_fragments(ROOT, source, config=config)
            for member in config['members']:
                if not any(f['source'] == 'shared:prompting/common.md'
                           for f in member['files']):
                    continue
                files = builder.payload(ROOT, member, config)
                path = member['name'] + '/references/writing.md'
                self.assertEqual(expected, files[path].decode('utf-8'))
                for name, data in files.items():
                    if name.endswith(('.md', '.py')):
                        for obsolete in (b'--part', b'rules.reader', b'document_reader', b'bundled reader'):
                            self.assertNotIn(obsolete, data, name)
                self.assertTrue(any(b'writing.md' in data for name, data in files.items()
                                    if name != path and name.endswith(('.md', '.py'))))

    def test_instruction_design_is_self_contained_in_all_authoring_consumers(self):
        source = (SHARED / 'prompting/instruction-design.md').read_bytes()
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            for member in config['members']:
                with self.subTest(profile=profile, layout=layout, member=member['name']):
                    files = builder.payload(ROOT, member, config)
                    path = member['name'] + '/references/instruction-design.md'
                    self.assertEqual(source, files[path])
                    self.assertTrue(any(b'instruction-design.md' in data
                                        for name, data in files.items()
                                        if name != path and name.endswith(('.md', '.py'))))

    def test_code_review_policy_is_self_contained_only_in_its_consumers(self):
        source = (SHARED / 'prompting/code-review.md').read_text(encoding='utf-8')
        consumers = {'scoville-code', 'scoville-ui', 'scoville-workflow-for-codex', 'scoville-ask-for-codex'}
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            for member in config['members']:
                with self.subTest(profile=profile, layout=layout, member=member['name']):
                    files = builder.payload(ROOT, member, config)
                    path = member['name'] + '/references/code-review.md'
                    self.assertEqual(member['name'] in consumers, path in files)
                    if member['name'] in consumers:
                        self.assertEqual(source, files[path].decode('utf-8'))
                    routes = {
                        'scoville-code': [('SKILL.md', 'references/code-review.md'),
                                          ('references/implementation-review.md', 'code-review.md')],
                        'scoville-ui': [('SKILL.md', 'references/code-review.md')],
                    }
                    for file, target in routes.get(member['name'], []):
                        text = files[member['name'] + '/' + file].decode('utf-8')
                        links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', text)
                        self.assertIn(target, links)

    def test_projected_rules_come_from_the_canonical_files(self):
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            with self.subTest(profile=profile, layout=layout), tempfile.TemporaryDirectory() as temp:
                receipt = builder.build(ROOT, Path(temp) / 'build', True, [], profile, layout)
                native_consumers = 0
                for member in config['members']:
                    name = member['name']
                    entrypoint = (ROOT / 'members' / name / name / 'SKILL.md').read_text(encoding='utf-8')
                    routes = [('rules.optout', name + '/SKILL.md')] if '{{ include: rules.optout }}' in entrypoint else []
                    if profile == 'codex' and any(item['source'] == 'shared:prompting/output-delivery.md'
                                                  for item in member['files']):
                        routes.append(('rules.native_output', name + '/references/output-delivery.md'))
                        native_consumers += 1
                    for rule, target in routes:
                        source = SHARED / builder.RULE_FRAGMENTS[rule]
                        text = builder.package_bytes(source)
                        payload = builder.payload(ROOT, member, config)
                        self.assertIn(text.strip(), payload[target])
                        self.assertEqual(hashlib.sha256(text).hexdigest(),
                                         receipt['shared_sources'][builder.RULE_FRAGMENTS[rule]])
                if profile == 'codex':
                    self.assertGreater(native_consumers, 0, 'The native capture projection must be exercised.')

    def test_unknown_rule_fails_and_corrected_include_expands(self):
        config = builder.load(ROOT, 'codex', 'suite')
        with self.assertRaisesRegex(ValueError, 'unknown build fragment'):
            builder.expand_fragments(ROOT, '{{ include: rules.typo }}', config=config)
        result = builder.expand_fragments(ROOT, '{{include: rules.optout}}', config=config)
        self.assertEqual((SHARED / 'runtime/skill_optout.md').read_text(encoding='utf-8').strip(), result)


if __name__ == '__main__':
    unittest.main()
