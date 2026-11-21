"""Exercise faulty profiles and apply the diagnostic's actual correction."""
import subprocess
import sys
import unittest
from datetime import date

import test_validate_profile as base

W2_HEAD = 'Status: todo\nDepends on: [W-001]\nBlocked by: []'
W2_TAIL = 'Acceptance: The graph validator reports no error.\nEvidence: []\nNext action: Wait for W-001 acceptance evidence.'
W2_CANCELLED = "Acceptance: The graph validator reports no error.\nEvidence: Cancelled at the user's direction on 2026-11-20."


class DiagnosticCorrections(unittest.TestCase):
    setUp = base.ValidatorTest.setUp
    tearDown = base.ValidatorTest.tearDown
    path = base.ValidatorTest.path
    replace = base.ValidatorTest.replace
    run_json = base.ValidatorTest.run_json
    plan = 'docs/plans/0001-validate-profile.md'

    def check_evidence(self, bad, corrected, messages):
        self.replace(self.plan, 'Evidence: []', 'Evidence: ' + bad)
        result, payload = self.run_json()
        self.assertEqual(result.returncode, 1)
        issue = next(d for d in payload['diagnostics'] if d['code'] == 'WORK_EVIDENCE_INVALID')
        self.assertEqual(issue['field'], 'Evidence')
        self.assertEqual(issue['record'], 'PLAN-0001/W-001')
        self.assertEqual(issue['file'], self.plan)
        self.assertIsInstance(issue['line'], int)
        for text in messages:
            self.assertIn(text, issue['message'] + ' ' + issue['suggestion'])
        self.assertTrue(issue['expected'])
        self.assertNotIn('references/', issue['suggestion'])
        self.replace(self.plan, 'Evidence: ' + bad, 'Evidence: ' + corrected)
        completed, valid = self.run_json()
        self.assertEqual(completed.returncode, 0, valid)
        self.assertTrue(valid['valid'])

    def test_length_reports_actual_limit_and_correction(self):
        # The suggestion states the Evidence format itself instead of pointing at Skill prose.
        self.check_evidence('x' * 212, 'Checks passed; details in tests/results.md.',
                            ['212', '200', 'Shorten', 'Do not invent evidence',
                             'observed results only', 'Evidence: []', 'must not start with `[`'])

    def test_control_character_reports_exact_code_and_correction(self):
        self.check_evidence('Result\x01 retained', 'Result retained',
                            ['U+0001', 'Replace control characters'])

    def test_list_punctuation_can_be_preserved_in_plain_text(self):
        self.check_evidence('[Result [x] retained]', 'Result [x] retained',
                            ['U+005B', 'U+005D', 'plain-text Evidence'])

    def test_exact_limit_is_valid(self):
        self.replace(self.plan, 'Evidence: []', 'Evidence: ' + 'x' * 200)
        completed, payload = self.run_json()
        self.assertEqual(completed.returncode, 0, payload)

    def test_blocker_and_execution_diagnostics_support_real_corrections(self):
        cases = (
            ("Blocked by: []", "Blocked by: [waiting for API key]", "Blocked by: [EXT-API-KEY]",
             "WORK_BLOCKER_INVALID", ["[A-Z]", "ADR", "PLAN", "W"], "Blocked by"),
            ("Blocked by: []", "Blocked by: [ADR-0001]", "Blocked by: [EXT-API-KEY]",
             "WORK_BLOCKER_INVALID", ["reserved"], "Blocked by"),
            ("1. Read the canonical files.", "1. [execute: reasoning=very-high] Read the canonical files.",
             "1. [execute: reasoning=high] Read the canonical files.",
             "WORK_STEP_EXECUTION_INVALID", ["none", "minimal", "low", "medium", "high", "xhigh", "max", "ultra"], "Steps"),
            ("1. Read the canonical files.", "1. [execute: model=GPT_6] Read the canonical files.",
             "1. [execute: model=gpt-6] Read the canonical files.",
             "WORK_STEP_EXECUTION_INVALID", ["lowercase", "alphanumeric", "dots", "hyphens"], "Steps"),
            ("1. Read the canonical files.", "1. [route: very_high] Read the canonical files.",
             "1. [route: high] Read the canonical files.",
             "WORK_STEP_EXECUTION_INVALID", ["ultra_low", "low", "medium", "high", "ultra_high"], "Steps"),
            ("1. Read the canonical files.", "1. [execute: reasoning=high; model=gpt-6] Read the canonical files.",
             "1. [execute: model=gpt-6; reasoning=high] Read the canonical files.",
             "WORK_STEP_EXECUTION_INVALID", ["model first", "separator"], "Steps"),
        )
        for old, bad, good, code, expected, field in cases:
            with self.subTest(bad=bad):
                self.replace(self.plan, old, bad)
                result, payload = self.run_json()
                self.assertEqual(1, result.returncode)
                issue = next(d for d in payload["diagnostics"] if d["code"] == code)
                self.assertEqual(field, issue["field"])
                self.assertEqual(self.plan, issue["file"])
                self.assertIsInstance(issue["line"], int)
                for text in expected:
                    self.assertIn(text, issue["expected"])
                self.replace(self.plan, bad, good)
                corrected, payload = self.run_json()
                self.assertEqual(0, corrected.returncode, payload)
                self.assertTrue(payload["valid"])
                self.replace(self.plan, good, old)


    def test_scope_instruction_repairs_actual_record(self):
        path = 'docs/decisions/0001-use-read-only-validation.md'
        self.replace(path, 'scope: skill/profile-validation', 'scope: Skill/Profile-validation')
        completed, payload = self.run_json()
        self.assertEqual(completed.returncode, 1)
        issue = next(d for d in payload['diagnostics'] if d['code'] == 'DECISION_SCOPE_INVALID')
        self.assertIn('lowercase', issue['suggestion'])
        self.assertIn('single slashes', issue['suggestion'])
        self.assertEqual(issue['observed'], 'Skill/Profile-validation')
        self.replace(path, 'scope: Skill/Profile-validation', 'scope: skill/profile-validation')
        completed, payload = self.run_json()
        self.assertEqual(completed.returncode, 0, payload)

    def test_field_order_instruction_preserves_values(self):
        original = 'Outcome: The local record shapes are valid.\nAcceptance: The validator reports a valid profile.'
        reversed_fields = '\n'.join(reversed(original.splitlines()))
        self.replace(self.plan, original, reversed_fields)
        completed, payload = self.run_json()
        self.assertEqual(completed.returncode, 1)
        issue = next(d for d in payload['diagnostics'] if d['code'] == 'WORK_FIELD_ORDER')
        self.assertIn('Outcome, Acceptance', issue['expected'])
        self.assertIn('without changing their values', issue['suggestion'])
        self.replace(self.plan, reversed_fields, original)
        completed, payload = self.run_json()
        self.assertEqual(completed.returncode, 0, payload)

    # A writer finishing their own edit must be able to act on these diagnostics alone.
    decision = 'docs/decisions/0001-use-read-only-validation.md'
    index = 'PROJECT_INDEX.md'

    def diagnostic(self, code):
        result, payload = self.run_json()
        self.assertEqual(1, result.returncode, payload)
        return next(d for d in payload['diagnostics'] if d['code'] == code)

    def assert_valid(self):
        result, payload = self.run_json()
        self.assertEqual(0, result.returncode, payload)
        self.assertTrue(payload['valid'])

    def test_cancelling_an_item_states_terminal_evidence_and_blocker_targets(self):
        self.replace(self.plan, W2_HEAD, 'Status: cancelled\nDepends on: [W-001]\nBlocked by: [EXT-API-KEY]')
        self.replace(self.plan, W2_TAIL, 'Acceptance: The graph validator reports no error.\nEvidence: []')
        evidence = self.diagnostic('WORK_TERMINAL_EVIDENCE_REQUIRED')
        self.assertIn("the user's direction and its date", evidence['suggestion'])
        self.assertIn('Never invent Evidence', evidence['suggestion'])
        self.assertIn('nonempty', evidence['expected'])
        blocked = self.diagnostic('WORK_TERMINAL_BLOCKED')
        self.assertEqual('Blocked by: []', blocked['expected'])
        self.assertIn('same edit', blocked['suggestion'])
        self.replace(self.plan, 'Blocked by: [EXT-API-KEY]', 'Blocked by: []')
        self.replace(self.plan, 'Acceptance: The graph validator reports no error.\nEvidence: []',
                     W2_CANCELLED[:-1] + '; EXT-API-KEY unresolved.')
        self.assert_valid()

    def test_completing_the_plan_states_every_terminal_target(self):
        self.replace(self.plan, 'status: active', 'status: completed')
        forbidden = self.diagnostic('PLAN_CURRENT_ITEM_FORBIDDEN')
        self.assertIn('no current_item', forbidden['expected'])
        self.assertIn('active_plan: null', forbidden['suggestion'])
        nonterminal = self.diagnostic('PLAN_COMPLETED_NONTERMINAL')
        self.assertIn('Status done or cancelled', nonterminal['expected'])
        self.assertIn('Evidence', nonterminal['suggestion'])
        index_status = self.diagnostic('INDEX_ACTIVE_PLAN_STATUS')
        self.assertIn('active_plan: null', index_status['expected'])
        self.assertIn('active_plan: null', index_status['suggestion'])
        count = self.diagnostic('PROFILE_ACTIVE_PLAN_COUNT')
        self.assertIn('active_plan: null', count['expected'])
        self.replace(self.plan, 'current_item: W-001\n', '')
        self.replace(self.plan, 'Status: in_progress', 'Status: done')
        self.replace(self.plan, 'Evidence: []\nNext action: Run the structural validator.',
                     'Evidence: Validator reported a valid profile.')
        self.replace(self.plan, W2_HEAD, 'Status: cancelled\nDepends on: [W-001]\nBlocked by: []')
        self.replace(self.plan, W2_TAIL, W2_CANCELLED)
        self.replace(self.index, 'active_plan: PLAN-0001', 'active_plan: null')
        self.assert_valid()

    def test_idle_index_with_active_plan_names_the_index_value(self):
        self.replace(self.index, 'active_plan: PLAN-0001', 'active_plan: null')
        issue = self.diagnostic('PROFILE_ACTIVE_PLAN_COUNT')
        self.assertIn('active_plan: PLAN-0001', issue['suggestion'])
        self.replace(self.index, 'active_plan: null', 'active_plan: PLAN-0001')
        self.assert_valid()

    def test_active_plan_without_current_item_states_the_field(self):
        self.replace(self.plan, 'current_item: W-001\n', '')
        issue = self.diagnostic('PLAN_CURRENT_ITEM_REQUIRED')
        self.assertIn('current_item: W-NNN', issue['expected'])
        self.assertIn('todo, in_progress or paused', issue['expected'])
        self.replace(self.plan, 'updated: 2026-08-08\n', 'updated: 2026-08-08\ncurrent_item: W-001\n')
        self.assert_valid()

    def test_empty_decision_section_names_the_empty_marker(self):
        self.replace(self.decision, 'Validation remains independent from correction.\n', '')
        issue = self.diagnostic('SECTION_EMPTY')
        self.assertEqual('Consequences', issue['field'])
        self.assertIn('write `[]`', issue['suggestion'])
        self.replace(self.decision, '## Consequences\n', '## Consequences\n\n[]\n')
        self.assert_valid()

    def test_missing_acceptance_date_uses_today_for_a_new_acceptance(self):
        self.replace(self.decision, 'accepted: 2026-08-08\n', '')
        issue = self.diagnostic('DECISION_ACCEPTED_REQUIRED')
        self.assertIn("today's date", issue['suggestion'])
        self.assertIn('accepted: YYYY-MM-DD', issue['expected'])
        self.replace(self.decision, 'created: 2026-08-08\n',
                     f'created: 2026-08-08\naccepted: {date.today().isoformat()}\n')
        self.assert_valid()

    def test_help_states_exit_codes_and_read_only_scope(self):
        run = subprocess.run([sys.executable, str(base.SCRIPT), '--help'],
                             capture_output=True, text=True, encoding='utf-8', timeout=15)
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertTrue(run.stdout.isascii())
        for text in ('0  VALID', '1  INVALID', '2  INCOMPLETE', '3  INTERNAL ERROR',
                     'valid stays true', 'structure only', 'writes nothing'):
            self.assertIn(text, run.stdout)
