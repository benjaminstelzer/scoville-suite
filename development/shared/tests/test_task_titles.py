import importlib.util
from pathlib import Path
import unittest
import json
import os
import subprocess
import sys

spec = importlib.util.spec_from_file_location('titles', Path(__file__).resolve().parents[1] / 'runtime/task_lifecycle.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)


class TitleTests(unittest.TestCase):
    def test_workflow_titles_use_role_number_and_plan_context(self):
        for role, label in [('coordinator', 'MNGR'), ('executor', 'WORK'),
                            ('reviewer', 'REVW'), ('repair', 'FIXR')]:
            for number in (1, 2, 12):
                request = dict(operation='task_title', family='workflow', role=role,
                               plan_id='PLAN-0011', unit='W-010/step-2', run_number=number,
                               caller_title='Ignored caller', unit_title='Ignored point title')
                suffix = 'PLAN-0011' if role == 'coordinator' else 'W-010/STEP-2'
                self.assertEqual(f'S-{label}-#{number}-{suffix}', lc.run(request)['title'])
        self.assertEqual('S-WORK-#1-W-010', lc.task_title(
            dict(family='workflow', role='executor', unit='W-010', run_number=1))['title'])

    def test_workflow_rejects_invalid_canonical_ids(self):
        for role, key, values in (
            ('coordinator', 'plan_id', ('PLAN-11', 'plan-0011', 'PLAN-0011 extra', 'PLAN-0011/step-1')),
            ('executor', 'unit', ('W-01', 'W-001/STEP-1', 'W-001/step-0', 'W-001/step-01', '../W-001')),
        ):
            for value in values:
                with self.subTest(role=role, value=value), self.assertRaises(ValueError):
                    lc.task_title(dict(family='workflow', role=role, run_number=1, **{key: value}))

    def test_ask_provider_labels(self):
        for adviser in ['ASTRA', 'SOL', 'CLAUDE']:
            self.assertEqual(f'ASK API review {adviser} RUN [#1]', lc.task_title(
                dict(family='ask', role='adviser', subject='API review', adviser=adviser, attempt=1))['title'])

    def test_ask_caller_title_with_selected_model(self):
        for title in ('Short', 'Long ' * 100, 'Änderung 中文 [plan]'):
            result = lc.task_title(dict(family='ask', role='adviser',
                                        caller_title=title, model='gpt-6-astra'))
            self.assertEqual('Ask gpt-6-astra · ' + title, result['title'])

    def test_cli_uses_utf8_under_legacy_windows_encoding(self):
        script = Path(__file__).resolve().parents[1] / 'runtime/task_lifecycle.py'
        request = dict(operation='task_title', family='ask', role='adviser',
                       caller_title='Änderung 中文', model='gpt-6-astra')
        result = subprocess.run([sys.executable, '-B', str(script)],
                                input=json.dumps(request, ensure_ascii=False).encode('utf-8'),
                                capture_output=True, env={**os.environ, 'PYTHONIOENCODING': 'cp1252'})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['title'], 'Ask gpt-6-astra · Änderung 中文')
        invalid = subprocess.run([sys.executable, '-B', str(script)], input=b'\xff', capture_output=True)
        self.assertEqual(invalid.returncode, 1)
        self.assertFalse(json.loads(invalid.stdout)['ok'])

    def test_invalid_values_fail_without_silent_truncation(self):
        request = dict(family='workflow', role='executor', unit='W-001/step-1', run_number=1)
        for patch in [{'run_number': 0}, {'run_number': True}, {'run_number': '1'},
                      {'unit': ''}, {'unit': 'W-001\nnew'}, {'role': 'unknown'}]:
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                lc.task_title(request | patch)

    def test_create_and_retained_handle_use_same_label(self):
        request = dict(family='workflow', role='executor', unit='W-001/step-1', run_number=1,
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
