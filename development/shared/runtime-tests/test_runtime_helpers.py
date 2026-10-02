"""Exercise built Skills as isolated consumers, without network or real advisers."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
INPUT = json.loads((ROOT / 'runtime-input.json').read_text(encoding='utf-8'))
KNOWN = {
    'scoville-plan': {'select_context.py', 'validate_profile.py', 'markdown_structure.py'},
    'scoville-workflow-for-codex': {'build_dispatch_prompt.py', 'build_manager_handoff.py',
        'check_context_checkpoint.py', 'inspect_native_context.py', 'resolve_model_pair.py',
        'workflow_settings.py', 'run_feedback.py', 'scoville_config.py',
        'native_task_arguments.py', 'select_context.py', 'markdown_structure.py'},
    'scoville-ask-for-codex': {'ask.py', 'ask_settings.py', 'ask_claude.py',
        'build_adviser_prompt.py', 'scoville_config.py'},
    'scoville-setup': {'setup.py', 'ask_settings.py', 'workflow_settings.py', 'scoville_config.py'},
}
QUESTION = 'Prüfe Grüße 中文\n"quoted" code: a < b\n'


def packages(member):
    for variant, meta in INPUT['variants'].items():
        if any(name.startswith(member + '/') for name in meta['helper_contracts']):
            yield ROOT / 'packages' / variant / member / member


class RuntimeHelpers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='runtime-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / 'Projekt ä 中文 with spaces'
        self.project.mkdir()

    def run_cli(self, package, script, *args, request=None, env=None, ok=True):
        result = subprocess.run([sys.executable, '-B', str(package / 'scripts' / script), *map(str, args)],
            input=json.dumps(request, ensure_ascii=False) if request is not None else None,
            cwd=self.project, env=env, text=True, encoding='utf-8', capture_output=True, timeout=25)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertTrue(result.stdout or result.stderr, 'invalid invocation needs a diagnostic')
        return json.loads(result.stdout) if result.stdout.strip() else result.stderr

    def profile(self):
        (self.project / 'docs/plans').mkdir(parents=True)
        (self.project / 'docs/decisions').mkdir()
        (self.project / 'PROJECT_INDEX.md').write_text(
            '---\nformat_version: 1\nactive_plan: PLAN-0001\n---\n', encoding='utf-8', newline='\n')
        (self.project / 'docs/plans/0001-runtime.md').write_text('''---
format_version: 1
id: PLAN-0001
status: active
created: 2026-10-02
updated: 2026-10-02
current_item: W-001
---

# Runtime test

## Goal

Preserve Grüße 中文 across helper consumers.

## Non-goals

No external work.

## Work items

### W-001 Verify runtime

Status: in_progress
Depends on: []
Blocked by: []
Decisions: []
Outcome: Unicode output reaches its consumer.
Acceptance: The selected assignment retains Grüße 中文.
Instructions: []
Steps:
1. [status: in_progress] Check Grüße 中文.
Evidence: []
''', encoding='utf-8', newline='\n')

    def launcher(self, name, source):
        folder = self.base / ('CLI with spaces ' + name)
        folder.mkdir()
        server = folder / 'server.py'
        server.write_text(source, encoding='utf-8', newline='\n')
        executable = folder / (name + '.cmd' if os.name == 'nt' else name)
        if os.name == 'nt':
            executable.write_text(f'@echo off\n"{sys.executable}" "%~dp0server.py" %*\n', encoding='utf-8')
        else:
            executable.write_text(f'#!{sys.executable}\n' + source, encoding='utf-8', newline='\n')
            executable.chmod(0o755)
        # Remove other installed CLIs while keeping Python and OS utilities.
        env = dict(os.environ, PATH=str(folder) + os.pathsep + str(Path(sys.executable).parent))
        if os.name == 'nt':
            env['PATH'] += os.pathsep + str(Path(os.environ['SystemRoot']) / 'System32')
        return env

    def test_exact_inventory_and_every_registered_helper_has_coverage(self):
        self.assertEqual(INPUT['schema_version'], 1)
        self.assertTrue(INPUT['variants'])
        for variant, meta in INPUT['variants'].items():
            folder = ROOT / 'packages' / variant
            observed = {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in folder.rglob('*') if p.is_file()}
            self.assertEqual(observed, meta['files'], variant)
            registered = set(meta['helper_contracts'])
            self.assertEqual({p for p in observed if p.endswith('.py')}, registered)
            for member in {p.split('/')[0] for p in registered}:
                self.assertIn(member, KNOWN, 'add actual consumer tests for the new package')
                self.assertEqual({Path(p).name for p in registered if p.startswith(member + '/')}, KNOWN[member])
        for name, expected in INPUT['test_assets'].items():
            self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), expected)

    def test_plan_valid_invalid_and_selected_context(self):
        self.profile()
        for package in packages('scoville-plan'):
            with self.subTest(package=str(package)):
                verdict = self.run_cli(package, 'validate_profile.py', '--root', self.project)
                self.assertTrue(verdict['valid'], verdict)
                selected = self.run_cli(package, 'select_context.py', '--root', self.project, '--unit', 'W-001/step-1')
                self.assertIn('Grüße 中文', selected['work_item']['source_text'])
                position = self.run_cli(package, 'select_context.py', '--root', self.project, '--position')
                self.assertEqual(position['current_units'], ['W-001/step-1'])
                proposals = self.run_cli(package, 'select_context.py', '--root', self.project, '--proposals')
                self.assertEqual(proposals, {'proposals': []})
                bad = self.run_cli(package, 'select_context.py', '--root', self.project, '--unit', 'wrong', ok=False)
                self.assertTrue(bad['diagnostics'])
                bad = self.run_cli(package, 'validate_profile.py', '--root', self.project / 'missing', ok=False)
                self.assertTrue(bad['diagnostics'])

    def test_workflow_report_settings_dispatch_and_manager_consumers(self):
        self.profile()
        request = self.project / 'request.txt'
        request.write_text(QUESTION, encoding='utf-8')
        for package in packages('scoville-workflow-for-codex'):
            report = self.run_cli(package, 'run_feedback.py', 'create', '--project-root', self.project)['report_file']
            issue = self.run_cli(package, 'run_feedback.py', 'add', '--report-file', report,
                '--kind', 'problem', '--location', 'PLAN-0001 / W-001', '--text-file', request)
            self.run_cli(package, 'run_feedback.py', 'resolve', '--report-file', report,
                '--issue-id', issue['issue_id'], '--text-file', request)
            complete = self.run_cli(package, 'run_feedback.py', 'finish', '--report-file', report, '--completed')
            self.assertIn('Grüße 中文', complete['display_text'])
            read = self.run_cli(package, 'run_feedback.py', 'read', '--report-file', report)
            self.assertEqual(read['text'], Path(report).read_text(encoding='utf-8'))
            self.run_cli(package, 'run_feedback.py', 'read', '--report-file', self.project / 'wrong', ok=False)
            progress = self.run_cli(package, 'run_feedback.py', 'progress', '--project', 'Grüße 中文', '--project-root', self.project)
            self.assertIn('W-001/step-1', progress['message'])
            status = self.run_cli(package, 'run_feedback.py', 'status', '--kind', 'blocked', '--project', 'Grüße 中文', '--text', QUESTION)
            self.assertIn(QUESTION.strip(), status['text'])
            pair = self.run_cli(package, 'resolve_model_pair.py', '--role', 'executor', '--route', 'medium', '--project-root', self.project)
            self.run_cli(package, 'resolve_model_pair.py', '--project-root', self.project, ok=False)
            assignment = self.run_cli(package, 'build_dispatch_prompt.py', '--role', 'executor',
                '--workspace-root', self.project, '--unit', 'W-001/step-1', '--manager-agent-id', 'manager',
                '--format', 'create', '--project-name', 'Grüße 中文', '--worker-number', '1',
                '--model', pair['model'], '--thinking', pair['thinking'])
            self.assertEqual(assignment['model'], pair['model'])
            self.assertIn('Grüße 中文', assignment['message'])
            common = ['--runner-id', 'runner', '--project-name', 'Grüße 中文', '--manager-number', '1', '--report-file', report]
            start = self.run_cli(package, 'build_manager_handoff.py', '--mode', 'start', *common,
                '--project-root', self.project, '--request-file', request)
            successor = self.run_cli(package, 'build_manager_handoff.py', '--mode', 'successor', *common,
                '--predecessor-id', 'old-manager', '--model', start['model'], '--thinking', start['reasoning_effort'])
            self.assertEqual(successor['model'], start['model'])
            self.run_cli(package, 'build_manager_handoff.py', '--mode', 'start', ok=False)
            for payload in (assignment, start, successor):
                self.assertEqual(set(payload), {'task_name', 'message', 'fork_turns', 'model', 'reasoning_effort'})
                self.assertEqual(payload['fork_turns'], 'none')

    def test_checkpoint_consumes_native_events(self):
        usage = {'input_tokens': 10}
        events = [
            {'ordinal': 1, 'type': 'session_meta', 'payload': {'id': 'test-thread'}},
            {'ordinal': 2, 'type': 'turn_context', 'payload': {'turn_id': 'turn'}},
            {'ordinal': 3, 'type': 'token_usage_record', 'payload': {'thread_id': 'test-thread', 'turn_id': 'turn', 'usage': usage}},
            {'ordinal': 4, 'type': 'event_msg', 'payload': {'type': 'token_count', 'info': {'last_token_usage': usage, 'model_context_window': 100}}},
        ]
        home = self.base / 'codex-home'
        (home / 'sessions').mkdir(parents=True)
        (home / 'sessions/rollout-test-thread.jsonl').write_text(''.join(json.dumps(e) + '\n' for e in events), encoding='utf-8')
        env = dict(os.environ, CODEX_HOME=str(home), CODEX_THREAD_ID='test-thread')
        for package in packages('scoville-workflow-for-codex'):
            result = self.run_cli(package, 'check_context_checkpoint.py', '--role', 'executor', '--project-root', self.project, env=env)
            self.assertEqual(result['telemetry'], 'fresh')
            self.assertEqual(result['action'], 'continue')
            self.run_cli(package, 'check_context_checkpoint.py', '--role', 'coordinator', '--project-root', self.project, ok=False)

    def test_redirected_report_directory_is_rejected_without_external_write(self):
        outside = self.base / 'outside'
        outside.mkdir()
        link = self.project / '.scoville'
        if os.name == 'nt':
            # Fixed fixture paths; no shell receives source or user-controlled text.
            subprocess.run(['cmd.exe', '/d', '/c', 'mklink', '/J', str(link), str(outside)],
                           check=True, capture_output=True)
        else:
            link.symlink_to(outside, target_is_directory=True)
        try:
            for package in packages('scoville-workflow-for-codex'):
                error = self.run_cli(package, 'run_feedback.py', 'create', '--project-root', self.project, ok=False)
                self.assertIn('redirected path', error)
            self.assertEqual(list(outside.iterdir()), [])
        finally:
            if os.name == 'nt':
                os.rmdir(link)
            else:
                link.unlink()
        for package in packages('scoville-workflow-for-codex'):
            report = self.run_cli(package, 'run_feedback.py', 'create', '--project-root', self.project)
            self.assertTrue(Path(report['report_file']).is_file())

    def test_setup_saved_settings_reach_workflow_consumer(self):
        for package in packages('scoville-setup'):
            self.run_cli(package, 'setup.py', 'set', '--project-root', self.project,
                         request={'workflow': {'manager': {'reasoning': 'invalid'}}}, ok=False)
            saved = self.run_cli(package, 'setup.py', 'set', '--project-root', self.project,
                         request={'workflow': {'manager': {'model': 'test-model', 'reasoning': 'high'}}})
            self.assertTrue(saved['saved'])
            shown = self.run_cli(package, 'setup.py', 'show', '--project-root', self.project)
            workflow = package.parent.parent / 'scoville-workflow-for-codex/scoville-workflow-for-codex'
            consumed = self.run_cli(workflow, 'resolve_model_pair.py', '--show-config', '--project-root', self.project)
            self.assertEqual(consumed['config']['manager'], shown['effective']['workflow']['manager'])
            self.assertEqual(consumed['config']['manager'], {'model': 'test-model', 'reasoning': 'high'})

    def test_ask_prompt_and_claude_request_reach_actual_cli(self):
        env = self.launcher('claude', "import json,sys\nsys.stdin.reconfigure(encoding='utf-8'); sys.stdout.reconfigure(encoding='utf-8')\nprompt=sys.stdin.read()\nprint(json.dumps({'result':prompt,'session_id':'test-session'},ensure_ascii=False))\n")
        question = self.project / 'question.txt'
        question.write_text(QUESTION, encoding='utf-8')
        for package in packages('scoville-ask-for-codex'):
            native = self.run_cli(package, 'build_adviser_prompt.py', '--adviser-id', 'sol',
                '--workspace-root', self.project, '--question-file', question, '--mode', 'review',
                '--scope', 'runtime', '--reference', 'test', '--format', 'spawn',
                '--task-name', 'runtime_test', '--model', 'test-model', '--effort', 'high')
            self.assertIn(QUESTION, native['message'])
            self.run_cli(package, 'build_adviser_prompt.py', '--adviser-id', 'sol', ok=False)
            config = self.run_cli(package, 'ask.py', '--project-root', self.project, '--adviser', 'sol')
            self.assertEqual(config['config']['advisers'][0]['id'], 'sol')
            prepared = self.run_cli(package, 'ask.py', request={'operation': 'prepare', 'mode': 'review',
                'question': QUESTION, 'scope': 'runtime', 'reference': 'test', 'cwd': str(self.project),
                'overrides': {'advisers': [{'id': 'test', 'route': 'claude-cli', 'model': 'test-model', 'effort': 'high'}]}})
            request = prepared['entries'][0]['request']
            input_file = self.project / 'request.json'
            input_file.write_text(json.dumps(request, ensure_ascii=False), encoding='utf-8')
            answer = self.run_cli(package, 'ask.py', '--input-file', input_file, env=env)
            self.assertEqual(answer['answer'], request['prompt'])
            self.assertEqual(answer['session_id'], 'test-session')
            followed = self.run_cli(package, 'ask.py', request={**request, 'session_id': answer['session_id'], 'prompt': QUESTION}, env=env)
            self.assertEqual(followed['answer'], QUESTION)
            self.assertEqual(followed['context_mode'], 'continued')
            self.run_cli(package, 'ask.py', request={'operation': 'unknown'}, ok=False)


    def test_claude_file_preparation_and_explicit_followup_overrides(self):
        env = self.launcher('claude', "import json,sys\nsys.stdin.reconfigure(encoding='utf-8'); sys.stdout.reconfigure(encoding='utf-8')\nprompt=sys.stdin.read()\nprint(json.dumps({'result':prompt,'session_id':'retained-session'},ensure_ascii=False))\n")
        question = self.base / 'question.txt'
        question.write_text(QUESTION, encoding='utf-8')
        for package in packages('scoville-ask-for-codex'):
            self.assertFalse((package / 'scripts/list_models.py').exists())
            first = self.base / 'first.json'
            arguments = ['--project-root', self.project, '--adviser', 'claude',
                         '--question-file', question, '--mode', 'review', '--scope', 'runtime',
                         '--reference', 'first', '--output-file', first]
            bad = self.run_cli(package, 'ask.py', *arguments, '--effort', 'ultra', ok=False)
            self.assertIn('effort', bad['error'])
            self.assertFalse(first.exists())
            self.run_cli(package, 'ask.py', *arguments, '--effort', 'max', '--web-tools', 'true')
            saved = json.loads(first.read_text(encoding='utf-8'))
            answer = self.run_cli(package, 'ask.py', '--input-file', first, env=env)
            self.assertEqual(answer['answer'], saved['prompt'])
            self.assertTrue(answer['answer'].endswith(QUESTION))
            following = self.base / 'next.json'
            followup = ['--resume-request', first, '--session-id', answer['session_id'],
                        '--question-file', question, '--mode', 'consultation', '--scope', 'runtime',
                        '--reference', 'next', '--output-file', following]
            self.run_cli(package, 'ask.py', *followup)
            retained = json.loads(following.read_text(encoding='utf-8'))
            for key in ('adviser', 'claude', 'cwd'):
                self.assertEqual(retained[key], saved[key])
            self.run_cli(package, 'ask.py', *followup, '--model', 'test-model', '--effort', 'high', '--web-tools', 'false')
            changed = json.loads(following.read_text(encoding='utf-8'))
            self.assertFalse(changed['claude']['web_tools'])
            answer = self.run_cli(package, 'ask.py', '--input-file', following, env=env)
            self.assertEqual(answer['requested_model'], 'test-model')
            self.assertEqual(answer['requested_effort'], 'high')
            self.assertEqual(answer['context_mode'], 'continued')
            self.assertEqual(answer['answer'], changed['prompt'])
            first.unlink()
            following.unlink()

    def test_claude_timeout_terminates_its_actual_process_family(self):
        # Exercise packaged adapter code, without starting Claude or using credentials.
        wrapper = self.base / 'wrapper.py'
        wrapper.write_text("import subprocess,sys,time,json,os\nfrom pathlib import Path\np=subprocess.Popen([sys.executable,'-c','import time; time.sleep(60)'])\nPath('pids.json').write_text(json.dumps([os.getpid(),p.pid]))\ntime.sleep(60)\n", encoding='utf-8')
        for package in packages('scoville-ask-for-codex'):
            code = "import sys; from pathlib import Path; sys.path.insert(0,sys.argv[1]); import ask_claude\ntry: ask_claude.run_command([sys.executable,sys.argv[2]],Path(sys.argv[3]),'',2)\nexcept ask_claude.ClaudeTimeout as e: print(str(e))\nelse: raise RuntimeError('timeout not reported')"
            result = subprocess.run([sys.executable, '-B', '-c', code, str(package / 'scripts'), str(wrapper), str(self.base)], capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('no retry', result.stdout)
            self.assertNotIn('could not be confirmed', result.stdout)
            for pid in json.loads((self.base / 'pids.json').read_text(encoding='utf-8')):
                if os.name == 'nt':
                    import ctypes
                    from ctypes import wintypes
                    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
                    kernel.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
                    kernel.OpenProcess.restype = wintypes.HANDLE
                    kernel.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
                    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
                    handle = kernel.OpenProcess(0x100000, False, pid)
                    if handle:
                        try: self.assertNotEqual(kernel.WaitForSingleObject(handle, 1000), 258)
                        finally: kernel.CloseHandle(handle)
                else:
                    state = subprocess.run(['ps', '-o', 'stat=', '-p', str(pid)], capture_output=True, text=True).stdout.strip()
                    self.assertTrue(not state or state.startswith('Z'), f'owned process {pid} survived: {state}')


if __name__ == '__main__':
    unittest.main()
