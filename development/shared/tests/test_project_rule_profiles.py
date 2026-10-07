"""Profile selection and rule-file coverage, not proof of model compliance."""
import sys
import unittest
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1]
ROOT = SHARED.parent / 'scoville-suite'
sys.path.insert(0, str(SHARED / 'build'))
import build_suite as builder


class ProjectRuleProfilesTests(unittest.TestCase):
    def test_profile_inside_package_selects_without_leaking(self):
        source = '{{ package: suite }}Rules: {{ profile: general }}AGENTS.md and CLAUDE.md{{ /profile }}{{ profile: codex }}AGENTS.md{{ /profile }}{{ /package }}'
        for profile in ('general', 'codex'):
            for layout in ('standalone', 'suite'):
                result = builder.variant_text(source, {'profile': profile, 'layout': layout})
                expected = '' if layout == 'standalone' else ('Rules: AGENTS.md and CLAUDE.md' if profile == 'general' else 'Rules: AGENTS.md')
                self.assertEqual(expected, result)
        for source in ('{{ profile: general }}{{ profile: codex }}x{{ /profile }}{{ /profile }}',
                       '{{ package: suite }}{{ package: standalone }}x{{ /package }}{{ /package }}'):
            with self.assertRaises(ValueError):
                builder.variant_text(source, {'profile': 'general', 'layout': 'suite'})

    def test_every_rule_file_reference_uses_selected_profile(self):
        expected = {'scoville-code': ['SKILL.md', 'references/project-conventions.md'],
                    'scoville-project-context-cleanup': ['SKILL.md']}
        for profile, layout in [('general', 'standalone'), ('general', 'suite'),
                                ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            for member in config['members']:
                if member['name'] not in expected: continue
                files = builder.payload(ROOT, member, config)
                for relative in expected[member['name']]:
                    text = files[member['name'] + '/' + relative].decode('utf-8')
                    with self.subTest(profile=profile, layout=layout, path=relative, member=member['name']):
                        self.assertIn('AGENTS.md', text)
                        self.assertEqual(profile == 'general', 'CLAUDE.md' in text)
                        self.assertNotIn('{{ profile:', text)
                        self.assertNotIn('{{ package:', text)


if __name__ == '__main__':
    unittest.main()
