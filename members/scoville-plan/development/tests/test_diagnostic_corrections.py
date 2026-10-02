"""Exercise faulty profiles and apply the diagnostic's actual correction."""
import unittest
import test_validate_profile as base


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
        self.replace(self.plan, 'Evidence: ' + bad, 'Evidence: ' + corrected)
        completed, valid = self.run_json()
        self.assertEqual(completed.returncode, 0, valid)
        self.assertTrue(valid['valid'])

    def test_length_reports_actual_limit_and_correction(self):
        self.check_evidence('x' * 212, 'Checks passed; details in tests/results.md.',
                            ['212', '200', 'Shorten', 'Do not invent evidence'])

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
