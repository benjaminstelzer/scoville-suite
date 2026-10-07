import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_select_context import DECISION, SCRIPT, plan


class CheckStartTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / 'docs/plans').mkdir(parents=True)
        (self.root / 'docs/decisions').mkdir(parents=True)
        self.write('PROJECT_INDEX.md', '---\nformat_version: 1\nactive_plan: PLAN-0001\n---\n')
        self.write('docs/plans/0001-fixture.md', plan())
        self.write('docs/decisions/0001-fixture.md', DECISION.replace('status: accepted', 'status: proposed'))

    def write(self, path, text):
        (self.root / path).write_text(text, encoding='utf-8', newline='\n')

    def invoke(self, *arguments):
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.root), *arguments], capture_output=True)
        self.assertEqual(before, {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        return result, json.loads(result.stdout)

    def test_dependency_blockers_other_writer_and_open_proposal_facts(self):
        text = plan().replace('Status: paused', 'Status: in_progress', 1)
        text = text.replace(
            'Depends on: [W-001, W-002]\nBlocked by: []', 'Depends on: [W-001, W-002]\nBlocked by: [EXT-ACCESS]')
        self.write('docs/plans/0001-fixture.md', text)
        result, payload = self.invoke('--check-start', 'W-003')
        self.assertEqual(result.returncode, 0, payload)
        self.assertEqual(payload['work_status'], 'todo')
        self.assertEqual(payload['dependencies'], [{'id': 'W-001', 'status': 'done'}, {'id': 'W-002', 'status': 'in_progress'}])
        self.assertEqual(payload['blocked_by'], ['EXT-ACCESS'])
        self.assertEqual(payload['other_in_progress'], ['W-002'])
        self.assertEqual(payload['violated_conditions'], ['dependencies_not_done', 'external_blockers', 'other_item_in_progress'])
        self.assertEqual(payload['open_decisions'], [{'id': 'ADR-0001', 'status': 'proposed',
                                                    'title': 'Preserve exact Unicode', 'path': 'docs/decisions/0001-fixture.md'}])
        self.assertNotIn('authorized', payload)

    def test_todo_resume_started_terminal_draft_inactive_and_no_current(self):
        for status, state in [('todo', 'not_started'), ('paused', 'resume'), ('in_progress', 'already_started'),
                              ('done', 'terminal'), ('cancelled', 'terminal')]:
            text = plan().replace('Status: paused', 'Status: done', 1).replace(
                '### W-003 Selected café item\n\nStatus: todo', '### W-003 Selected café item\n\nStatus: ' + status)
            self.write('docs/plans/0001-fixture.md', text)
            result, payload = self.invoke('--check-start', 'W-003')
            self.assertEqual(result.returncode, 0, payload)
            self.assertEqual(payload['start_state'], state)
            self.assertEqual(payload['violated_conditions'], [] if status in ('todo', 'paused') else
                             ['item_already_started'] if status == 'in_progress' else ['item_terminal'])
        self.write('docs/plans/0001-fixture.md', plan().replace('status: active', 'status: draft').replace('current_item: W-003\n', ''))
        self.write('PROJECT_INDEX.md', '---\nformat_version: 1\nactive_plan: null\n---\n')
        failed, diagnostic = self.invoke('--check-start', 'W-003')
        self.assertNotEqual(failed.returncode, 0)
        corrected, payload = self.invoke('--check-start', 'W-003', '--plan', 'PLAN-0001')
        self.assertEqual(corrected.returncode, 0, payload)
        self.assertEqual(payload['plan_status'], 'draft')
        self.assertIsNone(payload['current_item'])
        self.assertEqual(payload['violated_conditions'], ['plan_not_active', 'plan_not_selected', 'item_not_current', 'dependencies_not_done'])
        for status in ('completed', 'cancelled'):
            self.write('docs/plans/0001-fixture.md', plan().replace('status: active', 'status: ' + status))
            result, payload = self.invoke('--check-start', 'W-003', '--plan', 'PLAN-0001')
            self.assertEqual(result.returncode, 0, payload)
            self.assertEqual(payload['plan_status'], status)
            self.assertIn('plan_not_active', payload['violated_conditions'])

    def test_unknown_lifecycle_or_linked_decision_status_stops_incomplete_facts(self):
        self.write('docs/plans/0001-fixture.md', plan().replace('status: active', 'status: unknown'))
        result, payload = self.invoke('--check-start', 'W-003')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(payload['diagnostics'][0]['code'], 'PLAN_STATUS_INVALID')
        self.write('docs/plans/0001-fixture.md', plan())
        self.write('docs/decisions/0001-fixture.md', DECISION.replace('status: accepted', 'status: unknown'))
        result, payload = self.invoke('--check-start', 'W-003')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(payload['diagnostics'][0]['code'], 'DECISION_STATUS_INVALID')

    def test_invalid_modes_missing_item_and_corrected_read(self):
        for args in [('--check-start', 'W-3'), ('--check-start', 'W-999'),
                     ('--check-start', 'W-003', '--position'), ('--check-start', 'W-003', '--proposals'),
                     ('--check-start', 'W-003', '--unit', 'W-003'), ('--check-start', 'W-003', '--next-id', 'plan')]:
            result, payload = self.invoke(*args)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('diagnostics', payload)
            corrected, facts = self.invoke('--check-start', 'W-003')
            self.assertEqual(corrected.returncode, 0, facts)
            self.assertTrue(facts['matches_current_item'])

    def test_missing_empty_duplicate_proposal_titles_fail_then_corrected_facts(self):
        original = DECISION.replace('status: accepted', 'status: proposed')
        for title in ('', '# ', '# First\n\n# Second', '# Preserve exact Unicode\n\n# '):
            with self.subTest(title=title):
                self.write('docs/decisions/0001-fixture.md', original.replace('# Preserve exact Unicode', title))
                failed, payload = self.invoke('--check-start', 'W-003')
                self.assertNotEqual(failed.returncode, 0)
                self.assertEqual(payload['diagnostics'][0]['code'], 'DECISION_TITLE_INVALID')
                self.assertNotIn('open_decisions', payload)
                self.write('docs/decisions/0001-fixture.md', original)
                corrected, facts = self.invoke('--check-start', 'W-003')
                self.assertEqual(corrected.returncode, 0, facts)
                self.assertEqual(facts['open_decisions'], [{'id': 'ADR-0001', 'status': 'proposed',
                    'title': 'Preserve exact Unicode', 'path': 'docs/decisions/0001-fixture.md'}])


if __name__ == '__main__':
    unittest.main()
