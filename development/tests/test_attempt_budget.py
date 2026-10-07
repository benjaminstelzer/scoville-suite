"""Authorized register transitions retain attempts and enforce their own limits."""
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'instruction_tests'))
import attempts


class BudgetTests(unittest.TestCase):
    def register(self, root, authority, limit, suite, workflow):
        path = root / 'attempts.jsonl'
        rows = [{'authority': authority, 'limit': limit, 'model': 'gpt-6-luna', 'effort': 'high'}]
        for index, pool in enumerate(['suite'] * suite + ['workflow'] * workflow):
            rows.append({'attempt_id': str(index), 'output': str(root / str(index)), 'pool': pool})
        path.write_text(''.join(json.dumps(row) + '\n' for row in rows), encoding='utf-8')
        return path

    def test_new_allowance_is_shared_and_stops_after_200_followups(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.register(root, 'ADR-0168', 591, 294, 97)
            original = path.read_bytes()
            for index in range(200):
                pool = 'suite' if index % 2 else 'workflow'
                attempts.reserve(path, 'workflow-budget' if pool == 'workflow' else 'budget',
                                 root / f'followup-{index}', pool=pool)
            self.assertTrue(path.read_bytes().startswith(original))
            self.assertEqual(len(attempts.read(path)), 591)
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, '591-attempt budget exhausted'):
                attempts.reserve(path, 'budget', root / 'extra')
            self.assertEqual(path.read_bytes(), before)
            self.assertFalse(path.with_suffix('.jsonl.lock').exists())

    def test_old_register_keeps_its_pool_limit_until_explicit_migration(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.register(root, 'ADR-0167', 400, 300, 97)
            with self.assertRaisesRegex(ValueError, '300-attempt budget exhausted for suite'):
                attempts.reserve(path, 'budget', root / 'extra')
            attempts.reserve(path, 'workflow-budget', root / 'workflow-extra', pool='workflow')
            self.assertEqual(len(attempts.read(path)), 398)

    def test_mismatched_authority_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = self.register(Path(temporary), 'ADR-0167', 591, 0, 0)
            with self.assertRaisesRegex(ValueError, 'approved'):
                attempts.read(path)

    def plan0035(self, root, count=1):
        path = root / 'attempts.json'
        record = {'schema_version': 1, 'plan_id': 'PLAN-0035', 'limit': 80,
                  'model': 'gpt-6-luna', 'effort': 'high', 'attempts': []}
        for index in range(count):
            record['attempts'].append({'attempt_id': str(index), 'case_id': 'early',
                'output': str(root / str(index)), 'model': 'gpt-6-luna', 'effort': 'high',
                'status': 'completed', 'result': 'retained native evidence'})
        path.write_text(json.dumps(record), encoding='utf-8')
        return path

    def test_plan0035_preserves_native_attempt_and_shares_the_80_limit(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root)
            original = attempts.read(path)[0]
            for index in range(79):
                pool = 'suite' if index % 2 else 'workflow'
                row = attempts.reserve(path, 'workflow-probe' if pool == 'workflow' else 'probe',
                    root / f'new-{index}', variant='codex-suite-luna-high', run_set='0035', pool=pool)
                self.assertTrue(row['reserved_before_start'])
                self.assertEqual((row['model'], row['effort']), ('gpt-6-luna', 'high'))
            rows, limit = attempts.read(path, with_limit=True)
            self.assertEqual((len(rows), limit), (80, 80))
            self.assertEqual(rows[0], original)
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, '80-attempt budget exhausted'):
                attempts.reserve(path, 'extra', root / 'extra')
            self.assertEqual(path.read_bytes(), before)
            self.assertFalse(path.with_suffix('.json.lock').exists())

    def test_plan0035_duplicate_output_and_rejected_replace_preserve_register(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root)
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'fresh output'):
                attempts.reserve(path, 'probe', root / '0')
            with patch.object(attempts.os, 'replace', side_effect=OSError('denied')):
                with self.assertRaisesRegex(OSError, 'denied'):
                    attempts.reserve(path, 'probe', root / 'new')
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(list(root.iterdir()), [path])
            attempts.reserve(path, 'probe', root / 'new')
            self.assertEqual(len(attempts.read(path)), 2)

    def test_plan0035_authorized_100_limit_is_shared_and_preserves_prior_attempts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=8)
            record = json.loads(path.read_text(encoding='utf-8'))
            original = record['attempts'].copy()
            record.update(limit=100, authority='ADR-0185')
            path.write_text(json.dumps(record), encoding='utf-8')
            for index in range(92):
                pool = 'suite' if index % 2 else 'workflow'
                attempts.reserve(path, 'workflow-probe' if pool == 'workflow' else 'probe',
                                 root / f'new-{index}', pool=pool)
            rows, limit = attempts.read(path, with_limit=True)
            self.assertEqual((len(rows), limit), (100, 100))
            self.assertEqual(rows[:8], original)
            before = path.read_bytes()
            for pool in ('suite', 'workflow'):
                with self.assertRaisesRegex(ValueError, '100-attempt budget exhausted'):
                    attempts.reserve(path, 'workflow-extra' if pool == 'workflow' else 'extra',
                                     root / pool, pool=pool)
            self.assertEqual(path.read_bytes(), before)
            self.assertFalse(path.with_suffix('.json.lock').exists())

    def test_plan0035_100_requires_its_authority_and_rejects_overflow(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=101)
            record = json.loads(path.read_text(encoding='utf-8'))
            for authority in (None, 'ADR-0175'):
                record.update(limit=100, authority=authority)
                path.write_text(json.dumps(record), encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'ADR-0185'):
                    attempts.read(path)
            record['authority'] = 'ADR-0185'
            path.write_text(json.dumps(record), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'attempt count'):
                attempts.read(path)

    def test_plan0035_120_preserves_all_81_attempts_and_stops_both_consumers(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=81)
            record = json.loads(path.read_text(encoding='utf-8'))
            original = record['attempts'].copy()
            record.update(limit=120, authority='ADR-0187')
            path.write_text(json.dumps(record), encoding='utf-8')
            for index in range(39):
                pool = 'suite' if index % 2 else 'workflow'
                attempts.reserve(path, 'workflow-probe' if pool == 'workflow' else 'probe',
                                 root / f'new-{index}', pool=pool)
            rows, limit = attempts.read(path, with_limit=True)
            self.assertEqual((len(rows), limit), (120, 120))
            self.assertEqual(rows[:81], original)
            before = path.read_bytes()
            for pool in ('suite', 'workflow'):
                with self.assertRaisesRegex(ValueError, '120-attempt budget exhausted'):
                    attempts.reserve(path, 'workflow-extra' if pool == 'workflow' else 'extra',
                                     root / pool, pool=pool)
                self.assertEqual(path.read_bytes(), before)
            self.assertFalse(path.with_suffix('.json.lock').exists())

    def test_plan0035_120_rejects_wrong_authority_and_overflow_before_reservation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=120)
            record = json.loads(path.read_text(encoding='utf-8'))
            record.update(limit=120, authority='ADR-0185')
            path.write_text(json.dumps(record), encoding='utf-8')
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'ADR-0187'):
                attempts.reserve(path, 'extra', root / 'extra')
            self.assertEqual(path.read_bytes(), before)
            record['authority'] = 'ADR-0187'
            record['attempts'].append({**record['attempts'][0], 'attempt_id': 'overflow',
                                       'output': str(root / 'overflow')})
            path.write_text(json.dumps(record), encoding='utf-8')
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'attempt count'):
                attempts.reserve(path, 'extra', root / 'extra')
            self.assertEqual(path.read_bytes(), before)
            self.assertFalse(path.with_suffix('.json.lock').exists())

    def test_plan0035_300_preserves_history_and_stops_both_pools(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=120)
            record = json.loads(path.read_text(encoding='utf-8'))
            original = record['attempts'].copy()
            record.update(limit=300, authority='ADR-0192')
            path.write_text(json.dumps(record), encoding='utf-8')
            for index in range(180):
                pool = 'workflow' if index % 2 else 'suite'
                attempts.reserve(path, 'workflow-probe' if pool == 'workflow' else 'probe',
                                 root / f'new-{index}', pool=pool)
            rows, limit = attempts.read(path, with_limit=True)
            self.assertEqual((len(rows), limit), (300, 300))
            self.assertEqual(rows[:120], original)
            before = path.read_bytes()
            for pool in ('suite', 'workflow'):
                with self.assertRaisesRegex(ValueError, '300-attempt budget exhausted'):
                    attempts.reserve(path, 'workflow-extra' if pool == 'workflow' else 'extra', root / pool, pool=pool)
                self.assertEqual(path.read_bytes(), before)
            self.assertFalse(path.with_suffix('.json.lock').exists())

    def test_plan0035_300_rejects_wrong_authority_and_preserves_historical_pool_rule(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=120)
            record = json.loads(path.read_text(encoding='utf-8'))
            record.update(limit=300, authority='ADR-0187')
            path.write_text(json.dumps(record), encoding='utf-8')
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'ADR-0192'):
                attempts.reserve(path, 'extra', root / 'extra')
            self.assertEqual(path.read_bytes(), before)
            old = self.register(root, 'ADR-0166', 300, 0, 0)
            old_before = old.read_bytes()
            with self.assertRaisesRegex(ValueError, 'workflow pool requires'):
                attempts.reserve(old, 'workflow-extra', root / 'historical-extra', pool='workflow')
            self.assertEqual(old.read_bytes(), old_before)

    def test_explicit_medium_reservation_keeps_the_same_300_limit_and_history(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=299)
            record = json.loads(path.read_text(encoding='utf-8'))
            original = record['attempts'].copy()
            record.update(limit=300, authority='ADR-0192')
            path.write_text(json.dumps(record), encoding='utf-8')
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'allowed_efforts'):
                attempts.reserve(path, 'final-medium', root / 'medium', effort='medium')
            self.assertEqual(path.read_bytes(), before)
            record['allowed_efforts'] = ['high', 'medium']
            path.write_text(json.dumps(record), encoding='utf-8')
            row = attempts.reserve(path, 'final-medium', root / 'medium', effort='medium')
            self.assertEqual(row['effort'], 'medium')
            rows, limit = attempts.read(path, with_limit=True)
            self.assertEqual(rows[:299], original)
            self.assertEqual((len(rows), limit), (300, 300))
            before = path.read_bytes()
            for effort in ('high', 'medium'):
                with self.assertRaisesRegex(ValueError, '300-attempt budget exhausted'):
                    attempts.reserve(path, 'extra', root / effort, effort=effort)
                self.assertEqual(path.read_bytes(), before)

    def test_plan0035_rejects_changed_limits_models_and_malformed_records(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root)
            original = json.loads(path.read_text(encoding='utf-8'))
            invalid = [[], {**original, 'limit': 591}, {**original, 'effort': 'low'},
                       {**original, 'attempts': original['attempts'] * 2},
                       {**original, 'attempts': [original['attempts'][0],
                           {**original['attempts'][0], 'attempt_id': 'other'}]},
                       {**original, 'attempts': [{**original['attempts'][0], 'model': 'gpt-6.1-sol'}]},
                       {**original, 'attempts': [{**original['attempts'][0], 'attempt_id': []}]}]
            for record in invalid:
                with self.subTest(record=record):
                    path.write_text(json.dumps(record), encoding='utf-8')
                    before = path.read_bytes()
                    with self.assertRaises(ValueError):
                        attempts.reserve(path, 'probe', root / 'new')
                    self.assertEqual(path.read_bytes(), before)
                    self.assertFalse(path.with_suffix('.json.lock').exists())

    @unittest.skipUnless(os.name == 'nt', 'Windows case-insensitive path contract')
    def test_plan0035_windows_case_aliases_are_rejected_without_rewriting_evidence(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.plan0035(root, count=0)
            attempts.reserve(path, 'probe', root / 'CaseOutput')
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'fresh output'):
                attempts.reserve(path, 'probe', root / 'caseoutput')
            self.assertEqual(path.read_bytes(), before)
            record = json.loads(path.read_text(encoding='utf-8'))
            record['attempts'].append({**record['attempts'][0], 'attempt_id': 'different',
                                      'output': str(root / 'CASEOUTPUT')})
            path.write_text(json.dumps(record), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'duplicate PLAN-0035 output'):
                attempts.read(path)
