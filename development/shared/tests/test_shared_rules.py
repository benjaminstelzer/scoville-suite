"""Verify shared-rule projection and receipt provenance, not fixed prose."""
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1]
ROOT = SHARED.parent / 'scoville-suite'
sys.path.insert(0, str(SHARED / 'build'))
import build_suite as builder


class SharedRulesTests(unittest.TestCase):
    def test_all_writing_consumers_bundle_the_same_standalone_file(self):
        source = (SHARED / 'prompting/common.md').read_text(encoding='utf-8')
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            expected = builder.expand_fragments(ROOT, source, config=config)
            for member in config['members']:
                files = builder.payload(ROOT, member, config)
                path = member['name'] + '/references/writing.md'
                self.assertEqual(expected, files[path].decode('utf-8'))
                self.assertTrue(any(b'writing.md' in data for name, data in files.items()
                                    if name != path and name.endswith(('.md', '.py'))))

    def test_projected_rules_come_from_the_canonical_files(self):
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            with self.subTest(profile=profile, layout=layout), tempfile.TemporaryDirectory() as temp:
                receipt = builder.build(ROOT, Path(temp) / 'build', True, [], profile, layout)
                for member in config['members']:
                    name = member['name']
                    rule = ('rules.optout' if name in ('scoville-code', 'scoville-ui') else
                            'rules.python' if name in ('scoville-ask-for-codex', 'scoville-setup') else None)
                    if rule:
                        source = SHARED / builder.RULE_FRAGMENTS[rule]
                        text = source.read_bytes()
                        payload = builder.payload(ROOT, member, config)
                        self.assertIn(text.strip(), payload[name + '/SKILL.md'])
                        self.assertEqual(hashlib.sha256(text).hexdigest(),
                                         receipt['shared_sources'][builder.RULE_FRAGMENTS[rule]])

    def test_unknown_rule_fails_and_corrected_include_expands(self):
        config = builder.load(ROOT, 'codex', 'suite')
        with self.assertRaisesRegex(ValueError, 'unknown build fragment'):
            builder.expand_fragments(ROOT, '{{ include: rules.typo }}', config=config)
        result = builder.expand_fragments(ROOT, '{{include: rules.python}}', config=config)
        self.assertEqual((SHARED / 'runtime/python_discovery.md').read_text(encoding='utf-8').strip(), result)


if __name__ == '__main__':
    unittest.main()
