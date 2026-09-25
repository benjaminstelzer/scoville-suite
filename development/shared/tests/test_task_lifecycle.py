import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('lifecycle', Path(__file__).resolve().parents[1] / 'runtime/task_lifecycle.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)


class LifecycleTests(unittest.TestCase):
    def creation(self, **overrides):
        return dict(operation='create', family='workflow', role='executor', projectId='project',
                    caller_title='Suite fixes', unit='W-001/step-1', run_number=1, attempt=1, reference='dispatch1', prompt='scoville_role=executor\nPark.',
                    model='gpt-5.6-sol', thinking='xhigh', creation_authorized=True,
                    prior_state='not_started', **overrides)

    def handle(self, **changes):
        return dict(state='ready', threadId='child', hostId='local', family='workflow',
                    role='executor', reference='dispatch1') | changes

    def test_nested_project_and_exact_prompt(self):
        request = self.creation()
        output = lc.run(request)
        self.assertEqual({'type': 'project', 'projectId': 'project', 'environment': {'type': 'local'}}, output['arguments']['target'])
        self.assertNotIn('projectId', output['arguments'])
        self.assertEqual('scoville_role=executor\nworkflow_reference=dispatch1\nPark.', output['arguments']['prompt'])
        self.assertEqual('creation_unknown', output['handle']['state'])

    def test_role_and_double_creation_rejected(self):
        for patch in ({'prompt': ' scoville_role=executor\nPark.'}, {'role': 'reviewer'},
                      {'prior_state': 'pending'}, {'prior_state': 'creation_unknown'}, {'creation_authorized': False}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                lc.run(self.creation() | patch)

    def test_ask_marker_and_destination(self):
        output = lc.run(self.creation() | {'family': 'ask', 'role': 'adviser', 'subject': 'Review', 'adviser': 'ASTRA', 'return_to_thread_id': 'caller', 'prompt': 'Read-only role and question.'})
        self.assertTrue(output['arguments']['prompt'].startswith('ask_role=adviser\nconsultation_reference=dispatch1\nreturn_to_thread_id=caller\n'))

    def test_ready_pending_unknown(self):
        initial = lc.run(self.creation())['handle']
        for reply, expected in (({'threadId': 'child', 'hostId': 'local'}, 'ready'), ({'clientThreadId': 'provisional'}, 'pending'), ({}, 'creation_unknown')):
            output = lc.run({'operation': 'creation_result', 'handle': initial, 'reply': reply})
            self.assertEqual(expected, output['handle']['state'])
            self.assertFalse(output['may_create_again'])
        with self.assertRaises(ValueError):
            lc.run({'operation': 'creation_result', 'handle': initial, 'reply': {'threadId': 'same', 'clientThreadId': 'same', 'hostId': 'local'}})

    def test_reconciliation_exact_unique_project_and_title(self):
        initial = lc.run(self.creation())['handle'] | {'state': 'pending', 'clientThreadId': 'pending'}
        entry = {'id': 'child', 'kind': 'codex', 'hostId': 'local', 'title': initial['title'], 'projectId': 'project', 'workflow_reference': 'dispatch1'}
        def reconcile(entries):
            return lc.run({'operation': 'reconcile', 'handle': initial, 'entries': entries})['handle']
        self.assertEqual('pending', reconcile([entry | {'title': 'prefix ' + entry['title']}])['state'])
        self.assertEqual('pending', reconcile([entry | {'projectId': 'different'}])['state'])
        self.assertEqual('pending', reconcile([entry | {'kind': 'chatgpt'}])['state'])
        self.assertEqual('pending', reconcile([entry | {'workflow_reference': 'other'}])['state'])
        self.assertEqual('pending', reconcile([entry | {'workflow_reference': None}])['state'])
        self.assertEqual('child', reconcile([entry])['threadId'])
        with self.assertRaises(ValueError):
            reconcile([entry, entry | {'id': 'other'}])

    def test_message_no_pending_or_duplicate_send(self):
        request = {'operation': 'message', 'handle': self.handle(), 'prompt': 'Question', 'delivery_state': 'not_sent'}
        self.assertNotIn('model', lc.run(request)['arguments'])
        for change in ({'handle': self.handle(state='pending')}, {'delivery_state': 'unknown'}, {'delivery_state': 'sent'}):
            with self.assertRaises(ValueError):
                lc.run(request | change)

    def test_delivery_identity_scope_and_complete(self):
        delivery = dict(threadId='child', reference='dispatch1', scope='W1', complete=True, body='Answer')
        request = dict(operation='match_delivery', handle=self.handle(), expected_scope='W1', delivery=delivery)
        self.assertTrue(lc.run(request)['matched'])
        for patch in ({'threadId': 'other'}, {'reference': 'old'}, {'scope': 'W2'}, {'complete': False}):
            with self.assertRaises(ValueError):
                lc.run(request | {'delivery': delivery | patch})

    def test_distinct_archive_policies(self):
        request = dict(operation='archive', handle=self.handle(), status='completed', result_retained=True)
        self.assertTrue(lc.run(request)['arguments']['archived'])
        ask = request | {'handle': self.handle(family='ask', role='adviser')}
        with self.assertRaises(ValueError):
            lc.run(ask)
        self.assertTrue(lc.run(ask | {'explicit_yes_in_adviser': True})['arguments']['archived'])
        self.assertTrue(lc.run(ask | {'status': 'failed', 'failure_rule_applies': True})['arguments']['archived'])
        for change in ({'result_retained': False}, {'status': 'needs_user_decision'}, {'handle': self.handle(role='coordinator')}):
            with self.assertRaises(ValueError):
                lc.run(request | change)

    def test_workflow_archive_retains_exact_identity_for_each_role(self):
        for role in ('executor', 'reviewer', 'repair'):
            for status in ('completed', 'pass', 'changes_requested', 'blocked', 'failed', 'replaced'):
                with self.subTest(role=role, status=status):
                    request = dict(operation='archive', handle=self.handle(role=role),
                                   status=status, result_retained=True)
                    self.assertEqual(dict(threadId='child', hostId='local', archived=True),
                                     lc.run(request)['arguments'])

    def test_rollover_archive_waits_for_ended_predecessor_and_started_successor(self):
        for role in ('coordinator', 'executor', 'reviewer', 'repair'):
            request = dict(operation='archive', handle=self.handle(role=role),
                           status='context_handoff', result_retained=True,
                           predecessor_ended=True, successor_started=True)
            with self.subTest(role=role):
                self.assertTrue(lc.run(request)['arguments']['archived'])
                for key in ('predecessor_ended', 'successor_started', 'result_retained'):
                    for value in (None, False, 'true'):
                        with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                            lc.run(request | {key: value})

    def test_unfinished_or_unretained_tasks_stay_open(self):
        for family, roles in [('workflow', ('coordinator', 'executor', 'reviewer', 'repair')),
                              ('ask', ('adviser',))]:
            for role in roles:
                request = dict(operation='archive', handle=self.handle(family=family, role=role),
                               status='completed', result_retained=True,
                               predecessor_ended=True, successor_started=True,
                               explicit_cleanup_authorized=True)
                for status in ('active', 'pending', 'needs_user_decision', 'unknown'):
                    with self.subTest(family=family, role=role, status=status), self.assertRaises(ValueError):
                        lc.run(request | {'status': status})
                for state in ('pending', 'creation_unknown'):
                    with self.assertRaises(ValueError):
                        lc.run(request | {'handle': request['handle'] | {'state': state}})
                with self.assertRaises(ValueError):
                    lc.run(request | {'result_retained': False})

    def test_archive_requires_exact_boolean_state(self):
        for reply in ({'threadId': 'child'}, {'threadId': 'child', 'archived': 'true'}, {'threadId': 'wrong', 'archived': True}, {'status': 'completed'}, {'threadId': 'child', 'archived': False}, {'threadId': 'child', 'archived': True, 'isError': True}):
            with self.assertRaises(ValueError):
                lc.run(dict(operation='verify_archive', handle=self.handle(), reply=reply))
        self.assertTrue(lc.run(dict(operation='verify_archive', handle=self.handle(), reply={'threadId': 'child', 'archived': True}))['verified'])


if __name__ == '__main__':
    unittest.main()
