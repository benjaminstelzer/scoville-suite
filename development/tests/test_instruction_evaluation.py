"""Model-free integration checks against a supplied frozen dataset and build."""
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'development/instruction_tests'))
import attempts
import evaluation
import prepare


def digest(data):
    return hashlib.sha256(data).hexdigest()


@unittest.skipUnless(os.environ.get('SCOVILLE_TEST_DATA') and os.environ.get('SCOVILLE_TEST_BUILD'),
                     'Set SCOVILLE_TEST_DATA and SCOVILLE_TEST_BUILD for frozen-data integration')
class EvaluationFramingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = Path(os.environ['SCOVILLE_TEST_DATA'])
        build = Path(os.environ['SCOVILLE_TEST_BUILD']) / 'codex-suite'
        self.case = 'code-comprehension-structured-plan-small-change'
        self.variant = 'codex-suite-luna-high'
        prepared = self.root / 'runs/prepared'
        vault = self.root / 'vault/prepared'
        prepare.prepare(self.data, self.case, self.variant,
                        build / 'scoville-suite-for-codex', build / 'build-receipt.json', prepared, vault)
        metadata = json.loads((vault / 'preparation.json').read_text(encoding='utf-8'))
        self.instructions = (ROOT / 'development/luna-tests/comprehension-instructions.md').read_bytes()
        prompt = (prepared / 'prompt.txt').read_bytes()
        self.register = self.root / 'synthetic-no-model-attempts.jsonl'
        attempts.initialize(self.register)
        self.runs = []
        for number in range(3):
            run = self.root / f'synthetic-{number}'
            row = attempts.reserve(self.register, self.case, run, self.variant, 'synthetic-no-model')
            run.mkdir()
            self.runs.append(run)
            manifest = {**row, 'case_binding': metadata['case_binding'],
                        'fixture_root': str(prepared / 'workspace'),
                        'hashes': {'prompt': digest(prompt), 'receipt': metadata['receipt_sha256']},
                        'runner_sha256': 'synthetic', 'instructions_sha256': digest(self.instructions),
                        'process_lifetime_sha256': 'synthetic', 'failure_policy_sha256': 'synthetic',
                        'binding_helper_sha256': 'synthetic', 'max_turns': 8, 'timeout_seconds': 180,
                        'model': 'synthetic-no-model', 'effort': 'synthetic-no-model'}
            summary = {'case_id': self.case, 'protocol_grade': 'PASS', 'protocol_failure': None,
                       'final_answer': 'Synthetic answer for packet assembly only.', 'turns': [{'turn': 1}]}
            for name, value in [('manifest.json', manifest), ('summary.json', summary)]:
                (run / name).write_text(json.dumps(value), encoding='utf-8')
            (run / 'model-instructions.md').write_bytes(self.instructions)
            (run / 'turn-01-prompt.md').write_bytes(prompt)

    def group(self, name):
        return evaluation.group(self.data, self.register, self.case, self.root / name, 'synthetic-no-model')

    def test_complete_packet_retains_actual_frame_without_model_identity(self):
        result = self.group('review')
        review = Path(result['prepared'])
        text = (review / 'review.txt').read_text(encoding='utf-8')
        packet = json.loads(text.split('\n\n', 1)[1])
        self.assertEqual(3, len(packet['runs']))
        for row in packet['runs']:
            self.assertEqual(self.instructions.decode('utf-8'), row['test_instructions'])
        self.assertNotIn('synthetic-no-model', text)
        assignment = json.loads((review / 'assignment.json').read_text())
        self.assertIn(str(review / 'review.txt'), assignment['message'])

    def test_attempt_preparation_hashes_differ_but_catalog_revisions_must_match(self):
        for number, run in enumerate(self.runs):
            path = run / 'manifest.json'
            manifest = json.loads(path.read_text(encoding='utf-8'))
            manifest['hashes'].update(preparation=f'per-attempt-{number}', catalog='same-catalog')
            path.write_text(json.dumps(manifest), encoding='utf-8')
        self.assertEqual(3, self.group('separate-preparations')['runs'])
        path = self.runs[0] / 'manifest.json'
        manifest = json.loads(path.read_text(encoding='utf-8'))
        manifest['hashes']['catalog'] = 'changed-catalog'
        path.write_text(json.dumps(manifest), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'mixed evaluation revisions'):
            self.group('mixed-catalog')
        self.assertFalse((self.root / 'mixed-catalog').exists())

    def test_fixed_failure_retains_diagnostics_without_regrading(self):
        p = self.runs[0] / 'summary.json'
        row = json.loads(p.read_text())
        row.update(protocol_grade='FAIL', protocol_failure='forbidden_model_action',
                   native={'native_action_evidence': [{'type': 'custom_tool_call',
                           'name': 'exec', 'input': 'READ SKILL.md'}]})
        p.write_text(json.dumps(row))
        review = Path(self.group('fixed-diagnostics')['prepared'])
        payload = json.loads((review / 'review.txt').read_text().split('\n\n', 1)[1])
        fixed = next(r for r in payload['runs'] if r.get('fixed_verdict'))
        self.assertEqual('FAIL', fixed['fixed_verdict'])
        self.assertEqual(row['final_answer'], fixed['non_gradeable_diagnostics']['answer'])
        self.assertEqual('READ SKILL.md', fixed['non_gradeable_diagnostics']['native_actions'][0]['input'])
        selection = json.loads((review / 'selection.json').read_text())
        judgment = {'runs': [{'id': label, 'verdict': 'PASS'} for label in selection['evaluable_ids']]}
        with self.assertRaisesRegex(ValueError, 'preserve observed behavior failures'):
            evaluation.score(review, judgment)

    def test_plan0035_group_and_score_retain_current_budget(self):
        rows = [{**row, 'model': 'gpt-6-luna', 'effort': 'high'}
                for row in attempts.read(self.register)]
        self.register = self.root / 'synthetic-plan0035.json'
        self.register.write_text(json.dumps({
            'schema_version': 1, 'plan_id': 'PLAN-0035', 'model': 'gpt-6-luna',
            'effort': 'high', 'authority': 'ADR-0185', 'limit': 100,
            'attempts': rows}), encoding='utf-8')
        review = Path(self.group('review-current-budget')['prepared'])
        selection = json.loads((review / 'selection.json').read_text(encoding='utf-8'))
        self.assertEqual(100, selection['budget_limit'])
        judgment = {'runs': [{'id': label, 'verdict': 'PASS'}
                             for label in selection['evaluable_ids']]}
        result = evaluation.score(review, judgment)
        self.assertEqual('PASS', result['variants'][self.variant]['verdict'])
        self.assertIn('100-attempt', result['budget_note'])
        self.assertNotIn('591', result['budget_note'])

    def test_missing_or_changed_frame_refuses_group_before_output_then_corrected_passes(self):
        frame = self.runs[0] / 'model-instructions.md'
        frame.unlink()
        with self.assertRaises(FileNotFoundError):
            self.group('missing')
        self.assertFalse((self.root / 'missing').exists())
        frame.write_bytes(b'Different test frame')
        with self.assertRaisesRegex(ValueError, 'model instructions do not match'):
            self.group('changed')
        self.assertFalse((self.root / 'changed').exists())
        frame.write_bytes(self.instructions)
        self.assertEqual(3, self.group('corrected')['runs'])


if __name__ == '__main__':
    unittest.main()
