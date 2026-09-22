"""Regression: exact-ID successor works even when the normal list omits it."""
import importlib.util
import copy
from pathlib import Path
import unittest

SHARED = Path(__file__).resolve().parents[5] / 'shared'
spec = importlib.util.spec_from_file_location('lifecycle', SHARED / 'runtime/task_lifecycle.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)


class RolloverReadinessTests(unittest.TestCase):
    def request(self):
        def handle(identifier):
            return dict(state='ready', threadId=identifier, hostId='local', family='workflow', role='coordinator')
        return dict(operation='rollover_readiness', successor=handle('new'), predecessor=handle('old'),
                    workflow_id='workflow', generation=2, guard_capability_verified=True,
                    guard=dict(workflow_id='workflow', generation=2, coordinator_id='new',
                               state='coordinator_active', writer=None, rollover=None),
                    exact_successor=dict(threadId='new', hostId='local', reachable=True),
                    activation_turn_id='activation',
                    predecessor_turn=dict(threadId='old', hostId='local', turnId='activation', status='completed'),
                    listing=dict(threads=[], pinnedThreads=[], sections=[]), status_retained=True)

    def test_missing_list_entry_allows_only_guarded_continuation(self):
        result = lc.run(self.request())
        self.assertTrue(result['may_continue'])
        self.assertTrue(result['retain_predecessor'])
        self.assertFalse(result['may_archive_predecessor'])
        self.assertIsNone(result['archive_arguments'])
        self.assertNotIn('create_arguments', result)

    def test_visibility_by_id_not_title(self):
        request = self.request()
        request['listing']['threads'] = [dict(id='new', hostId='local', kind='codex', title='any renamed title')]
        result = lc.run(request)
        self.assertEqual(dict(threadId='old', hostId='local', archived=True), result['archive_arguments'])
        request['listing']['threads'][0]['id'] = 'wrong'
        self.assertFalse(lc.run(request)['may_archive_predecessor'])

    def test_active_exact_successor_can_replace_missing_list_entry(self):
        request = self.request()
        request['exact_successor']['status'] = 'active'
        result = lc.run(request)
        self.assertEqual([], result['archive_blockers'])
        self.assertFalse(result['retain_predecessor'])
        self.assertEqual(dict(threadId='old', hostId='local', archived=True), result['archive_arguments'])
        for status in ('idle', 'notLoaded', 'failed', 'needsAttention', None):
            request['exact_successor']['status'] = status
            with self.subTest(status=status):
                self.assertFalse(lc.run(request)['may_archive_predecessor'])

    def test_active_successor_does_not_bypass_other_archive_proofs(self):
        base = self.request()
        base['exact_successor']['status'] = 'active'
        for change in ({'status_retained': False},
                       {'listing': dict(threads=[], pinnedThreads=[], sections=[], unavailableHosts=['local'])},
                       {'listing': dict(threads=[], pinnedThreads=[], sections=[], unavailableSources=['codex'])},
                       {'listing': dict(threads=[], pinnedThreads=[], sections=[{}])},
                       {'listing': dict(threads=[])}):
            with self.subTest(change=change):
                self.assertFalse(lc.run(base | change)['may_archive_predecessor'])
        for section, key, value in (('exact_successor', 'hostId', 'other'),
                                    ('exact_successor', 'threadId', 'other'),
                                    ('exact_successor', 'reachable', False),
                                    ('guard', 'coordinator_id', 'old'),
                                    ('predecessor_turn', 'status', 'active')):
            request = copy.deepcopy(base)
            request[section][key] = value
            with self.subTest(section=section, key=key), self.assertRaises(ValueError):
                lc.run(request)

    def test_deferred_archive_rechecks_fresh_proof_and_verifies_target(self):
        initial = self.request()
        deferred = lc.run(initial)
        self.assertEqual(['successor_not_listed'], deferred['archive_blockers'])
        record = deferred['archive_record']
        for field in ('guard', 'guard_capability_verified', 'listing', 'exact_successor', 'status_retained'):
            self.assertNotIn(field, record)
        with self.assertRaises((KeyError, ValueError)):
            lc.run(record | {'operation': 'rollover_readiness'})
        retry = initial | record
        retry['listing'] = dict(threads=[dict(id='new', hostId='local', kind='codex')],
                               pinnedThreads=[], sections=[])
        approved = lc.run(retry)
        self.assertEqual([], approved['archive_blockers'])
        self.assertEqual(record, approved['archive_record'])
        self.assertEqual(dict(threadId='old', hostId='local', archived=True), approved['archive_arguments'])
        verification = dict(operation='verify_archive', handle=record['predecessor'])
        for reply in ({'threadId': 'old', 'archived': False}, {'threadId': 'new', 'archived': True}):
            with self.assertRaises(ValueError):
                lc.run(verification | {'reply': reply})
        self.assertTrue(lc.run(verification | {'reply': {'threadId': 'old', 'archived': True}})['verified'])

    def test_deferred_archive_does_not_reuse_stale_generation(self):
        request = self.request()
        record = lc.run(request)['archive_record']
        request['guard'] = request['guard'] | {'generation': 3, 'coordinator_id': 'newer'}
        with self.assertRaises(ValueError):
            lc.run(request | record)

    def test_each_missing_handoff_proof_blocks(self):
        changes = [('guard', 'coordinator_id', 'old'), ('guard', 'generation', 1),
                   ('guard', 'workflow_id', 'other'), ('guard', 'state', 'coordinator_pending_activation'),
                   ('guard', 'writer', {'task_id': 'writer'}),
                   ('exact_successor', 'threadId', 'other'), ('exact_successor', 'reachable', False),
                   ('predecessor_turn', 'threadId', 'other'), ('predecessor_turn', 'turnId', 'older'),
                   ('predecessor_turn', 'status', 'active'), ('predecessor_turn', 'status', 'idle'),
                   ('predecessor_turn', 'status', 'failed')]
        for section, key, value in changes:
            request = self.request()
            request[section][key] = value
            with self.subTest(section=section, key=key, value=value), self.assertRaises(ValueError):
                lc.run(request)
        with self.assertRaises(ValueError):
            lc.run(self.request() | {'guard_capability_verified': False})

    def test_pinned_sectioned_or_incomplete_list_does_not_archive(self):
        entry = dict(id='new', hostId='local', kind='codex')
        for listing in (dict(threads=[entry]),
                        dict(threads=[entry], pinnedThreads=[entry], sections=[]),
                        dict(threads=[entry], pinnedThreads=[], sections=[dict(itemKeys=['codex:thread:local:new'])])):
            request = self.request() | {'listing': listing}
            request['exact_successor']['status'] = 'active'
            result = lc.run(request)
            self.assertTrue(result['may_continue'])
            self.assertFalse(result['may_archive_predecessor'])

    def recovery_request(self):
        first = lc.run(self.request())['archive_record']
        request = self.request()
        request['generation'] = 3
        request['predecessor'] = dict(first['successor'])
        request['successor'] = dict(first['successor'], threadId='newest')
        request['guard'] = dict(request['guard'], generation=3, coordinator_id='newest')
        request['exact_successor'] = dict(threadId='newest', hostId='local', reachable=True)
        request['activation_turn_id'] = 'next-activation'
        request['predecessor_turn'] = dict(threadId='new', hostId='local', turnId='next-activation', status='completed')
        request['listing']['threads'] = [dict(id='newest', hostId='local', kind='codex')]
        request['archive_chain'] = [first, lc.run(request)['archive_record']]
        request['operation'] = 'recover_rollover_archives'
        return request

    def test_recovery_across_generations_preserves_unverified_targets(self):
        request = self.recovery_request()
        result = lc.run(request)
        self.assertEqual(['old', 'new'], [a['threadId'] for a in result['archive_arguments']])
        request['archive_receipts'] = [dict(threadId='old', hostId='local',
                                            reply=dict(threadId='old', archived=True))]
        result = lc.run(request)
        self.assertEqual(['new'], [a['threadId'] for a in result['archive_arguments']])
        request['listing']['threads'] = []
        result = lc.run(request)
        self.assertEqual([], result['archive_arguments'])
        self.assertEqual(['new'], [h['threadId'] for h in result['pending_predecessors']])
        self.assertTrue(result['may_continue'])

    def test_recovery_archives_chain_when_active_successor_is_omitted(self):
        request = self.recovery_request()
        request['listing']['threads'] = []
        request['exact_successor']['status'] = 'active'
        result = lc.run(request)
        self.assertEqual(['old', 'new'], [a['threadId'] for a in result['archive_arguments']])
        request['archive_receipts'] = [dict(threadId='old', hostId='local', reply=dict(threadId='old', archived=True))]
        self.assertEqual(['new'], [a['threadId'] for a in lc.run(request)['archive_arguments']])

    def test_recovery_rejects_broken_chain_and_wrong_receipts(self):
        base = self.recovery_request()
        for field, value in [('workflow_id', 'other'), ('generation', 1),
                             ('predecessor_turn', dict(threadId='old', hostId='local',
                                                       turnId='activation', status='active')),
                             ('successor', dict(state='ready', threadId='wrong', hostId='local',
                                                family='workflow', role='coordinator'))]:
            request = copy.deepcopy(base)
            request['archive_chain'][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                lc.run(request)
        for receipt in (dict(threadId='newest', hostId='local', reply=dict(threadId='newest', archived=True)),
                        dict(threadId='old', hostId='local', reply=dict(threadId='old', archived=False)),
                        dict(threadId='old', hostId='local', reply=dict(threadId='wrong', archived=True))):
            with self.subTest(receipt=receipt), self.assertRaises(ValueError):
                lc.run(base | {'archive_receipts': [receipt]})


if __name__ == '__main__':
    unittest.main()
