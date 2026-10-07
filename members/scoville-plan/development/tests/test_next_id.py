import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_select_context import DECISION, SCRIPT, plan


class NextIdTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / 'docs/plans').mkdir(parents=True)
        (self.root / 'docs/decisions').mkdir(parents=True)
        self.write('PROJECT_INDEX.md', '---\nformat_version: 1\nactive_plan: null\n---\n')
        self.write('docs/plans/0001-fixture.md', plan())
        self.write('docs/decisions/0001-fixture.md', DECISION)

    def write(self, path, text):
        (self.root / path).write_text(text, encoding='utf-8', newline='\n')

    def invoke(self, *arguments):
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.root), *arguments], capture_output=True)
        self.assertEqual(before, {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        return result, json.loads(result.stdout)

    def test_all_kinds_gaps_conflicts_and_direct_manual_filename_consumption(self):
        self.write('docs/plans/0007-fixture.md', plan().replace('id: PLAN-0001', 'id: PLAN-0009'))
        self.write('docs/decisions/0008-fixture.md', DECISION.replace('id: ADR-0001', 'id: ADR-0006'))
        for kind, expected in [('plan', 'PLAN-0010'), ('decision', 'ADR-0009'), ('work-item', 'W-005')]:
            with self.subTest(kind=kind):
                args = ['--next-id', kind] + (['--plan', 'PLAN-0001'] if kind == 'work-item' else [])
                result, payload = self.invoke(*args)
                self.assertEqual(result.returncode, 0, payload)
                self.assertEqual(payload['next_id'], expected)
                self.assertFalse(payload['reserved'])
                if kind != 'work-item':
                    self.assertEqual(len(payload['conflicts']), 1)
                    # Actual next operation uses helper values unchanged; only
                    # the human-authored subject/template is supplied here.
                    path = self.root / payload['filename_pattern'].replace('<lowercase-hyphenated-subject>', 'manual-fixture')
                    template = plan() if kind == 'plan' else DECISION
                    old_id = 'PLAN-0001' if kind == 'plan' else 'ADR-0001'
                    path.write_text(template.replace('id: ' + old_id, 'id: ' + payload['next_id']), encoding='utf-8', newline='\n')
                    again, next_payload = self.invoke(*args)
                    self.assertEqual(again.returncode, 0, next_payload)
                    self.assertNotEqual(next_payload['next_id'], expected)

    def test_explicit_plan_and_incompatible_modes_have_corrected_calls(self):
        for args in [('--next-id', 'work-item'), ('--next-id', 'plan', '--plan', 'PLAN-0001'),
                     ('--next-id', 'plan', '--position'), ('--next-id', 'plan', '--proposals'),
                     ('--next-id', 'plan', '--unit', 'W-001')]:
            failed, payload = self.invoke(*args)
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn('diagnostics', payload)
        corrected, payload = self.invoke('--next-id', 'work-item', '--plan', 'PLAN-0001')
        self.assertEqual(corrected.returncode, 0, payload)
        self.assertEqual(payload['next_id'], 'W-005')

    def test_empty_directories_and_exhausted_formats(self):
        (self.root / 'docs/decisions/0001-fixture.md').unlink()
        result, payload = self.invoke('--next-id', 'decision')
        self.assertEqual(result.returncode, 0, payload)
        self.assertEqual(payload['next_id'], 'ADR-0001')
        self.write('docs/decisions/9999-fixture.md', DECISION)
        self.write('docs/plans/9999-fixture.md', plan())
        self.write('docs/plans/0001-fixture.md', plan().replace('W-004', 'W-999'))
        for kind in ('decision', 'plan', 'work-item'):
            args = ['--next-id', kind] + (['--plan', 'PLAN-0001'] if kind == 'work-item' else [])
            result, payload = self.invoke(*args)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(payload['diagnostics'][0]['code'], 'ID_SPACE_EXHAUSTED')

    def test_malformed_metadata_prevents_incomplete_success(self):
        self.write('docs/decisions/0007-fixture.md', DECISION.replace('id: ADR-0001', 'id: invalid'))
        failed, payload = self.invoke('--next-id', 'decision')
        self.assertNotEqual(failed.returncode, 0)
        self.assertEqual(payload['diagnostics'][0]['code'], 'RECORD_ID_INVALID')
        self.assertNotIn('next_id', payload)


if __name__ == '__main__':
    unittest.main()
