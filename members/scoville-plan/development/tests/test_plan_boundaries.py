"""Validator and selector agree on semantic Plan boundaries."""
import json
import subprocess
import sys
import unittest

import test_validate_profile as base


class PlanBoundaryTests(unittest.TestCase):
    setUp = base.ValidatorTest.setUp
    tearDown = base.ValidatorTest.tearDown
    path = base.ValidatorTest.path
    run_json = base.ValidatorTest.run_json

    def test_layout_variants_preserve_context_or_explain_unowned_text(self):
        path = self.path('docs/plans/0001-validate-profile.md')
        original = path.read_text(encoding='utf-8')
        for old, new, valid in (
            ('\n# Validate a native profile', '\n   \n# Validate a native profile', True),
            ('\n\n## Goal', '\n## Goal', True),
            ('\n\n## Non-goals', '\n\n\n## Non-goals', True),
            ('Observe one valid profile.', '### Scope\n\nObserve one valid profile.', True),
            ('# Validate a native profile', '# Validate a native profile\n\nUnowned introduction.', False),
            ('## Work items\n', '## Work items\n\nUnowned work introduction.\n', False),
        ):
            with self.subTest(new=new):
                changed = original.replace(old, new)
                path.write_bytes(changed.encode('utf-8'))
                _, validation = self.run_json()
                selected = subprocess.run([sys.executable, '-X', 'utf8', str(base.SCRIPT.with_name('select_context.py')),
                    '--root', str(self.root), '--format', 'json'], capture_output=True, text=True, encoding='utf-8')
                self.assertEqual(valid, validation['valid'], validation)
                self.assertEqual(valid, selected.returncode == 0, selected.stdout)
                if valid and '### Scope' in changed:
                    self.assertIn('### Scope', json.loads(selected.stdout)['plan']['goal'])
                if not valid:
                    errors = [d for d in validation['diagnostics'] if d['file'].endswith(path.name)]
                    self.assertTrue(any(isinstance(d.get('line'), int) and d.get('suggestion') for d in errors))
                    self.assertRegex(json.loads(selected.stdout)['diagnostics'][0]['message'], r'line \d+')
                self.assertEqual(changed.encode('utf-8'), path.read_bytes())

    def test_unparsed_index_does_not_claim_that_the_index_is_idle(self):
        self.path('PROJECT_INDEX.md').write_bytes(b'---\nformat_version: 1\nactive_plan: PLAN-0001\n')
        _, result = self.run_json()
        self.assertFalse(result['valid'])
        self.assertFalse(any(d['code'] == 'PROFILE_ACTIVE_PLAN_COUNT' for d in result['diagnostics']))
