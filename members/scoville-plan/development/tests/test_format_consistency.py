"""Regression boundaries for the shared native grammar and diagnostics."""
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

import test_validate_profile as base


class FormatConsistency(unittest.TestCase):
    setUp = base.ValidatorTest.setUp
    tearDown = base.ValidatorTest.tearDown
    path = base.ValidatorTest.path
    replace = base.ValidatorTest.replace
    run_json = base.ValidatorTest.run_json
    plan = 'docs/plans/0001-validate-profile.md'
    decision = 'docs/decisions/0001-use-read-only-validation.md'

    def select(self, *args, root=None):
        result = subprocess.run([sys.executable, '-B', str(base.SCRIPT.with_name('select_context.py')),
                                 '--root', str(root or self.root), *args],
                                capture_output=True, text=True, encoding='utf-8', timeout=15)
        return result, json.loads(result.stdout)

    def test_leading_zero_step_is_rejected_by_both_helpers(self):
        self.replace(self.plan, '1. Read', '01. Read')
        status, value = self.run_json()
        self.assertEqual(status.returncode, 1)
        self.assertIn('WORK_STEPS_INVALID', {d['code'] for d in value['diagnostics']})
        result, selected = self.select('--unit', 'W-001/step-1')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(selected['diagnostics'][0]['code'], 'WORK_STEPS_INVALID')
        line = self.path(self.plan).read_text(encoding='utf-8').splitlines().index('01. Read the canonical files.') + 1
        self.assertIn(f'line {line}', selected['diagnostics'][0]['message'])

    def test_empty_supersession_is_rejected_by_both_helpers(self):
        self.replace(self.decision, 'scope: skill/profile-validation', 'scope: skill/profile-validation\nsupersedes: ')
        result, value = self.run_json()
        self.assertEqual(result.returncode, 1)
        self.assertIn('FRONTMATTER_ENTRY_INVALID', {d['code'] for d in value['diagnostics']})
        result, value = self.select()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(value['diagnostics'][0]['code'], 'FRONTMATTER_ENTRY_INVALID')

    def test_inactive_index_position_rejected_but_named_inspection_retained(self):
        self.replace(self.plan, 'status: active', 'status: draft')
        result, value = self.select('--position')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(value['diagnostics'][0]['code'], 'ACTIVE_PLAN_INVALID')
        self.replace(self.plan, 'current_item: W-001\n', '')
        self.replace(self.plan, 'Status: in_progress', 'Status: todo')
        result, value = self.select('--position', '--plan', 'PLAN-0001')
        self.assertEqual(result.returncode, 0, value)

    def test_raw_parent_component_rejected_without_normalization(self):
        raw = str(self.root / '..' / self.root.name)
        result, value = self.select(root=raw)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(value['diagnostics'][0]['code'], 'ROOT_TRAVERSAL')
        result, value = self.run_json(root=Path(raw))
        self.assertEqual(result.returncode, 2)
        self.assertIn('ROOT_TRAVERSAL', {d['code'] for d in value['diagnostics']})

    def test_large_valid_context_can_be_retried_with_reported_complete_size(self):
        self.replace(self.plan, 'Observe one valid profile.', 'Observe one valid profile.\n' + 'z' * 70000)
        status, value = self.run_json()
        self.assertEqual(status.returncode, 0, value)
        result, value = self.select()
        self.assertNotEqual(result.returncode, 0)
        required = value['diagnostics'][0]['observed']['required_bytes']
        result, value = self.select('--max-output-bytes', str(required))
        self.assertEqual(result.returncode, 0, value)
        self.assertIn('z' * 70000, json.dumps(value))

    def test_selection_diagnostic_uses_header_or_argument_origin(self):
        self.replace(self.plan, 'current_item: W-001', 'current_item: W-099')
        result, value = self.select()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('line 7', value['diagnostics'][0]['message'])
        self.replace(self.plan, 'updated: 2026-08-08\ncurrent_item: W-099',
                     'current_item: W-099\nupdated: 2026-08-08')
        result, value = self.select()
        self.assertIn('line 6', value['diagnostics'][0]['message'])
        result, value = self.select('--work-item', 'W-098')
        self.assertIn('--work-item argument', value['diagnostics'][0]['message'])
        self.assertNotIn('line 1:', value['diagnostics'][0]['message'])

    def test_list_error_identifies_actual_item_and_field_line(self):
        self.replace(self.plan, 'Depends on: []', 'Depends on: W-002')
        result, value = self.select()
        self.assertNotEqual(result.returncode, 0)
        line = self.path(self.plan).read_text(encoding='utf-8').splitlines().index('Depends on: W-002') + 1
        self.assertIn(f'W-001, line {line}: Depends on', value['diagnostics'][0]['message'])

    def test_heading_space_is_visible_and_whitespace_content_is_empty(self):
        self.replace(self.plan, '## Goal\n', '## Goal \n')
        result, value = self.run_json()
        diagnostic = next(d for d in value['diagnostics'] if d['code'] == 'SECTION_H2_ORDER')
        self.assertIn('"Goal "', diagnostic['observed'])
        self.replace(self.plan, '## Goal \n', '## Goal\n')
        self.replace(self.plan, 'Observe one valid profile.', '   ')
        result, value = self.run_json()
        self.assertIn('SECTION_EMPTY', {d['code'] for d in value['diagnostics']})

    def test_failed_inventory_has_no_invented_missing_plan_and_keeps_independent_error(self):
        self.replace('PROJECT_INDEX.md', 'format_version: 1', 'format_version: 99')
        original = os.scandir
        def scan(path):
            if str(path) == str(self.root / 'docs/plans'):
                raise PermissionError('fixture denied')
            return original(path)
        with mock.patch.object(base.VALIDATOR.os, 'scandir', side_effect=scan):
            value, code = base.VALIDATOR.Validator(str(self.root)).run()
        codes = {d['code'] for d in value['diagnostics']}
        self.assertEqual(code, 2)
        self.assertIn('DIRECTORY_UNREADABLE', codes)
        self.assertIn('FORMAT_VERSION_UNSUPPORTED', codes)
        self.assertNotIn('INDEX_ACTIVE_PLAN_MISSING', codes)
        self.assertNotIn('PROFILE_ACTIVE_PLAN_COUNT', codes)

    def test_unreadable_decision_is_not_reported_as_missing(self):
        self.path(self.decision).write_bytes(b'\xff')
        result, value = self.run_json()
        codes = {d['code'] for d in value['diagnostics']}
        self.assertIn('FILE_UTF8_INVALID', codes)
        self.assertNotIn('WORK_DECISION_MISSING', codes)

    def test_nested_records_warn_without_reading_or_recursing(self):
        child = self.root / 'docs/plans/archive'
        child.mkdir()
        (child / '0002-private.md').write_bytes(b'\xff')
        (child / 'deeper').mkdir()
        (child / 'deeper/0003-ignored.md').write_bytes(b'\xff')
        result, value = self.run_json()
        self.assertEqual(result.returncode, 0, value)
        self.assertTrue(value['valid'])
        self.assertEqual(value['summary']['files_checked'], 3)
        warnings = [d for d in value['diagnostics'] if d['code'] == 'RECORD_NESTED_UNSUPPORTED']
        self.assertEqual([d['file'] for d in warnings], ['docs/plans/archive/0002-private.md'])
        result, value = self.select('--next-id', 'plan')
        self.assertEqual(result.returncode, 0, value)
        self.assertEqual(value['next_id'], 'PLAN-0002')

    def test_batch_requires_actual_calendar_date(self):
        self.replace(self.decision, 'scope: skill/profile-validation',
                     'scope: skill/profile-validation\ntransition_batch: batch-20260230-1\ntransition_batch_members: [ADR-0001]')
        result, value = self.run_json()
        issue = next(d for d in value['diagnostics'] if d['code'] == 'DECISION_BATCH_HASH_INVALID')
        self.assertIn('date', issue['message'].lower())
        self.assertIn('date', issue['suggestion'].lower())
        self.assertIn('20260230', issue['observed'])
        self.replace(self.decision, 'batch-20260230-1', 'batch-20260228-1')
        result, value = self.run_json()
        self.assertEqual(result.returncode, 0, value)

    def test_malformed_written_steps_do_not_request_legacy_next_action(self):
        self.replace(self.plan, '1. Read the canonical files.\n2. Check the local record shapes.',
                     '01. [status: done] One.\n02. [status: in_progress] Two.')
        self.replace(self.plan, 'Next action: Run the structural validator.\n', '')
        result, value = self.run_json()
        codes = {d['code'] for d in value['diagnostics'] if d.get('record') == 'PLAN-0001/W-001'}
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('WORK_STEPS_INVALID', codes)
        self.assertNotIn('WORK_NEXT_ACTION_REQUIRED', codes)
        self.replace(self.plan, 'Steps:\n01. [status: done] One.\n02. [status: in_progress] Two.\n', '')
        result, value = self.run_json()
        self.assertIn('WORK_NEXT_ACTION_REQUIRED', {d['code'] for d in value['diagnostics']})

    def test_step_trailing_space_diagnostic_names_repair(self):
        self.replace(self.plan, '1. Read the canonical files.', '1. [status: in_progress] Do it. ')
        result, value = self.run_json()
        issue = next(d for d in value['diagnostics'] if d['code'] == 'WORK_STEP_STATUS_INVALID')
        self.assertIn('trailing', issue['message'].lower())
        self.assertIn('trailing', issue['suggestion'].lower())
        self.replace(self.plan, '1. [status: in_progress] Do it. ', '1. [status: in_progress] Do it.')
        result, value = self.run_json()
        self.assertEqual(result.returncode, 0, value)

    def test_check_start_idle_index_returns_json_null(self):
        self.replace('PROJECT_INDEX.md', 'active_plan: PLAN-0001', 'active_plan: null')
        result, value = self.select('--check-start', 'W-002', '--plan', 'PLAN-0001')
        self.assertEqual(result.returncode, 0, value)
        self.assertIsNone(value['index_active_plan'])


if __name__ == '__main__':
    unittest.main()
