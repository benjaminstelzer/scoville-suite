import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('titles', Path(__file__).resolve().parents[1] / 'runtime/task_lifecycle.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)


class TitleTests(unittest.TestCase):
    def test_workflow_roles_and_generation(self):
        for role, label in [('executor', 'WORK'), ('reviewer', 'REVIEW'), ('repair', 'REPAIR')]:
            request = dict(operation='task_title', family='workflow', role=role,
                           unit='PLAN-0001 W-013/step-3', attempt=2)
            self.assertEqual(f'SCW PLAN-0001 W-013/step-3 {label} RUN [#2]', lc.run(request)['title'])
        title = lc.task_title(dict(family='workflow', role='coordinator', coordinator_title='SCW COORD',
                                   workflow_id='workflow-id', generation=3))['title']
        self.assertEqual('SCW COORD [workflow-id] G3', title)

    def test_ask_provider_labels(self):
        for adviser in ['ASTRA', 'SOL', 'CLAUDE']:
            self.assertEqual(f'ASK API review {adviser} RUN [#1]', lc.task_title(
                dict(family='ask', role='adviser', subject='API review', adviser=adviser, attempt=1))['title'])

    def test_invalid_values_fail_without_silent_truncation(self):
        request = dict(family='workflow', role='executor', unit='W-001', attempt=1)
        for patch in [{'attempt': 0}, {'attempt': True}, {'attempt': '1'}, {'unit': 'x' * 81},
                      {'unit': 'W-001\nnew'}, {'unit': '[W-001]'}, {'unit': ' W-001'}, {'role': 'unknown'}]:
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                lc.task_title(request | patch)

    def test_create_and_retained_handle_use_same_label(self):
        request = dict(family='workflow', role='executor', unit='W-001', attempt=1,
                       projectId='p', reference='d', prompt='scoville_role=executor\nPark.',
                       model='m', thinking='medium', creation_authorized=True, prior_state='not_started')
        generated = lc.task_title(request)['title']
        result = lc.create(request)
        self.assertEqual(generated, result['arguments']['title'])
        self.assertEqual(generated, result['handle']['title'])
        with self.assertRaisesRegex(ValueError, 'differs'):
            lc.create(request | {'title': 'old invented title'})
        ready = result['handle'] | dict(state='ready', threadId='exact', hostId='local', title='Legacy title')
        message = lc.message(dict(handle=ready, prompt='Continue', delivery_state='not_sent'))
        self.assertEqual('exact', message['arguments']['threadId'])
        self.assertNotIn('title', message['arguments'])

    def test_same_attempt_replacement_does_not_reuse_predecessor(self):
        handle = dict(state='creation_unknown', projectId='p', title='SCW W-001 WORK RUN [#1]',
                      prior_task_ids=['old'])
        old = dict(id='old', hostId='local', kind='codex', projectId='p', title=handle['title'])
        request = dict(handle=handle, entries=[old])
        self.assertEqual('creation_unknown', lc.reconcile(request)['handle']['state'])
        request['entries'].append(old | {'id': 'new'})
        self.assertEqual('new', lc.reconcile(request)['handle']['threadId'])


if __name__ == '__main__':
    unittest.main()
