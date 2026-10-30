"""Exercise built Skills as isolated consumers, without network or real advisers."""
import hashlib
import importlib.util
import json
import os
import re
from pathlib import Path
import shutil
import shlex
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
INPUT = json.loads((ROOT / 'runtime-input.json').read_text(encoding='utf-8'))
KNOWN = {
    'scoville-plan': {'select_context.py', 'validate_profile.py', 'markdown_structure.py'},
    'scoville-workflow-for-codex': {'build_dispatch_prompt.py', 'resolve_model_pair.py',
        'workflow_settings.py', 'scoville_config.py',
        'native_task_arguments.py', 'select_context.py', 'validate_profile.py', 'markdown_structure.py'},
    'scoville-ask-for-codex': {'ask.py', 'ask_settings.py', 'ask_claude.py',
        'build_adviser_prompt.py', 'scoville_config.py'},
    'scoville-setup': {'setup.py', 'ask_settings.py', 'workflow_settings.py', 'scoville_config.py'},
}
for member in ['scoville-code', 'scoville-handoff', 'scoville-plan', 'scoville-ui',
               'scoville-workflow-for-codex', 'scoville-ask-for-codex', 'scoville-setup',
               'scoville-project-context-cleanup']:
    KNOWN.setdefault(member, set()).add('check_text_size.py')

QUESTION = 'Prüfe Grüße 中文\n"quoted" code: a < b\n'


def packages(member):
    for variant, meta in INPUT['variants'].items():
        if any(name.startswith(member + '/') for name in meta['helper_contracts']):
            yield ROOT / 'packages' / variant / member / member


class RuntimeHelpers(unittest.TestCase):
    def test_capture_without_token_limit_always_saves_complete_streams(self):
        checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
        cases = ((0, False, False), (7, False, False), (125, False, False), (9, True, False), (0, False, True))
        for exit_code, invalid, timeout in cases:
            with self.subTest(exit_code=exit_code, invalid=invalid, timeout=timeout):
                marker = self.base / f'once-{exit_code}-{invalid}-{timeout}'
                stdout = b'BEGIN' + b'x' * 431000 + (b'\xff' if invalid else b'END')
                stderr = b'needed diagnostic'
                code = 'import sys,time;from pathlib import Path;p=Path(sys.argv[1]);p.write_text(p.read_text()+"x" if p.exists() else "x");sys.stdout.buffer.write(b"BEGIN"+b"x"*431000+' + repr(b'\xff' if invalid else b'END') + ');sys.stdout.buffer.flush();sys.stderr.buffer.write(b"needed diagnostic");sys.stderr.buffer.flush();' + ('time.sleep(60)' if timeout else f'sys.exit({exit_code})')
                result = subprocess.run([sys.executable, '-X', 'utf8', str(checker),
                    '--publish-full', '--project-root', str(self.project),
                    '--timeout-seconds', '2', '--run', '--', sys.executable, '-c', code, str(marker)],
                    capture_output=True, timeout=20)
                self.assertEqual(result.returncode, 125 if invalid or timeout else exit_code)
                metadata = json.loads(result.stderr if invalid or timeout else result.stdout)
                self.assertEqual(metadata['capture_complete'], not timeout)
                self.assertFalse(metadata['output_complete'])
                self.assertLess(len(result.stdout) + len(result.stderr), 1600)
                if not timeout:
                    self.assertEqual(metadata['exit_code'], exit_code)
                else:
                    self.assertEqual(metadata['error'], 'timeout')
                self.assertNotIn('recommended_max_utf8_bytes', metadata)
                self.assertNotIn('tool_output_limit_tokens', metadata)
                expected = f'exit={metadata["exit_code"]} stdout_bytes={len(stdout)} stderr_bytes={len(stderr)}\n'.encode() + b'stdout:\n' + stdout + b'\nstderr:\n' + stderr
                self.assertEqual(Path(metadata['full_file']).read_bytes(), expected)
                self.assertEqual(marker.read_text(), 'x')

    def test_publication_failure_keeps_original_capture_error_and_process(self):
        checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
        wrapper = self.base / 'double-failure.py'
        wrapper.write_text('''import errno,sys
from unittest.mock import patch
sys.path.insert(0,sys.argv.pop(1))
import check_text_size
original=check_text_size.collect_output
def unconfirmed(process, timeout):
    out,err,failure=original(process,timeout)
    assert failure == 'timeout'
    return out,err,'timeout_cleanup_incomplete'
storage_failure = (patch.object(check_text_size.os,'link',side_effect=OSError(errno.EOPNOTSUPP,'no hardlinks')) if sys.argv.pop(1) == 'link' else patch.object(check_text_size,'publish_full',side_effect=PermissionError(errno.EACCES,'write denied')))
with patch.object(check_text_size,'collect_output',side_effect=unconfirmed), storage_failure:
    raise SystemExit(check_text_size.main())
''', encoding='utf-8')
        pid_file = self.base / 'producer.pid'
        producer = 'import os,sys,time;from pathlib import Path;Path(sys.argv[1]).write_text(str(os.getpid()));print("before-timeout",flush=True);time.sleep(60)'
        for failure_mode in ('link', 'write'):
            with self.subTest(failure_mode=failure_mode):
                result = subprocess.run([sys.executable, str(wrapper), str(checker.parent), failure_mode, '--max-output-tokens', '2500',
                    '--publish-full', '--project-root', str(self.project), '--timeout-seconds', '2', '--run', '--',
                    sys.executable, '-c', producer, str(pid_file)], capture_output=True, timeout=20)
                self.assertEqual(result.returncode, 125)
                metadata = json.loads(result.stderr)
                self.assertEqual(metadata['error'], 'publication_failed')
                self.assertEqual(metadata['capture_error'], 'timeout_cleanup_incomplete')
                self.assertEqual(metadata['process_id'], int(pid_file.read_text()))
                self.assertFalse(metadata['capture_complete'])
                if failure_mode == 'link':
                    self.assertIn(b'before-timeout', Path(metadata['full_file']).read_bytes())
                else:
                    self.assertIsNone(metadata['full_file'])
                    self.assertIn('No saved copy', metadata['instruction'])

    def test_publication_failure_retains_full_capture_without_repeating_effect(self):
        checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
        marker = self.base / 'once.txt'
        # Unsupported hardlinks are a real filesystem limit. Inject that boundary
        # after actual creation/close of the complete capture, not a fake result.
        wrapper = self.base / 'unsupported-link.py'
        wrapper.write_text('''import errno,sys
from unittest.mock import patch
sys.path.insert(0,sys.argv.pop(1))
import check_text_size
with patch.object(check_text_size.os,'link',side_effect=OSError(errno.EOPNOTSUPP,'no hardlinks')):
    raise SystemExit(check_text_size.main())
''', encoding='utf-8')
        producer = 'import sys;from pathlib import Path;p=Path(sys.argv[1]);p.write_text(p.read_text()+"x" if p.exists() else "x");sys.stdout.buffer.write(b"BEGIN"+b"x"*431000+b"END");sys.stderr.buffer.write(b"required error");sys.exit(7)'
        result = subprocess.run([sys.executable, '-X', 'utf8', str(wrapper), str(checker.parent),
            '--max-output-tokens', '2000', '--publish-full', '--project-root', str(self.project),
            '--run', '--', sys.executable, '-c', producer, str(marker)], capture_output=True, timeout=25)
        self.assertEqual(result.returncode, 125)
        self.assertEqual(result.stdout, b'')
        meta = json.loads(result.stderr)
        self.assertEqual(meta['error'], 'publication_failed')
        self.assertTrue(meta['capture_complete'])
        self.assertEqual(meta['exit_code'], 7)
        self.assertLessEqual(len(result.stderr), 1600)
        output = b'BEGIN' + b'x' * 431000 + b'END'
        error = b'required error'
        expected = f'exit=7 stdout_bytes={len(output)} stderr_bytes={len(error)}\n'.encode() + b'stdout:\n' + output + b'\nstderr:\n' + error
        self.assertEqual(Path(meta['full_file']).read_bytes(), expected)
        self.assertEqual(marker.read_text(), 'x')
        self.assertIn('OSError', meta['reason'])

    def test_existing_wrong_target_is_preserved_and_recovery_contains_original(self):
        package = next(packages('scoville-code'))
        source = self.base / 'original.txt'
        data = b'whole original content'
        source.write_bytes(data)
        directory = self.project / '.scoville/temp'
        directory.mkdir(parents=True)
        target = directory / (hashlib.sha256(data).hexdigest() + '.txt')
        target.write_bytes(b'existing content')
        result = self.run_cli(package, 'check_text_size.py', '--file', source,
                              '--publish-full', '--project-root', self.project, ok=False, raw=True)
        self.assertEqual(result.returncode, 2)
        meta = json.loads(result.stderr)
        self.assertEqual(meta['status'], 'publication_failed')
        self.assertEqual(Path(meta['full_file']).read_bytes(), data)
        self.assertEqual(target.read_bytes(), b'existing content')
        self.assertEqual(source.read_bytes(), data)

    def test_child_exit_125_is_complete_output_not_capture_failure(self):
        checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
        result = subprocess.run([sys.executable, str(checker), '--max-output-tokens', '1000',
                                '--run', '--', sys.executable, '-c', 'print("actual child output");raise SystemExit(125)'],
                               capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 125)
        self.assertIn(b'exit=125 ', result.stdout)
        self.assertIn(b'actual child output', result.stdout)
        self.assertEqual(result.stderr, b'')

    @unittest.skipIf(os.name == 'nt', 'Windows TerminateProcess is not a catchable POSIX signal')
    def test_checker_posix_signals_stop_actual_family_and_preserve_available_bytes(self):
        import signal
        for signum in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
            with self.subTest(signal=signum):
                checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
                pids = self.base / f'signal-pids-{int(signum)}.json'
                producer = 'import os,sys,subprocess,time,json;from pathlib import Path;p=subprocess.Popen([sys.executable,"-c","import time;time.sleep(60)"]);print("before-interruption",flush=True);Path(sys.argv[1]).write_text(json.dumps([os.getpid(),p.pid]));time.sleep(60)'
                process = subprocess.Popen([sys.executable, str(checker), '--max-output-tokens', '1500',
                    '--publish-full', '--project-root', str(self.project), '--run', '--',
                    sys.executable, '-c', producer, str(pids)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    deadline = time.monotonic() + 5
                    while not pids.exists() and time.monotonic() < deadline:
                        time.sleep(0.02)
                    self.assertTrue(pids.exists(), 'producer must start before interruption')
                    process.send_signal(signum)
                    out, err = process.communicate(timeout=15)
                    self.assertEqual(process.returncode, 125, err)
                    self.assertEqual(out, b'')
                    meta = json.loads(err)
                    self.assertEqual(meta['error'], 'interrupted')
                    self.assertFalse(meta['capture_complete'])
                    self.assertIn(b'before-interruption', Path(meta['full_file']).read_bytes())
                    for pid in json.loads(pids.read_text()):
                        state = subprocess.run(['ps', '-o', 'stat=', '-p', str(pid)], capture_output=True, text=True, timeout=5).stdout.strip()
                        self.assertTrue(not state or state.startswith('Z'), f'owned process {pid} survived: {state}')
                finally:
                    if process.poll() is None:
                        process.kill()
                        process.communicate(timeout=5)
                    if pids.exists():
                        for pid in json.loads(pids.read_text()):
                            try: os.kill(pid, signal.SIGKILL)
                            except ProcessLookupError: pass

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='runtime-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / 'Projekt ä 中文 with spaces'
        self.project.mkdir()

    def run_cli(self, package, script, *args, request=None, env=None, ok=True, raw=False):
        result = subprocess.run([sys.executable, '-B', str(package / 'scripts' / script), *map(str, args)],
            input=json.dumps(request, ensure_ascii=False) if request is not None else None,
            cwd=self.project, env=env, text=True, encoding='utf-8', capture_output=True, timeout=25)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertTrue(result.stdout or result.stderr, 'invalid invocation needs a diagnostic')
        if raw:
            return result
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
        self.assertEqual(INPUT['schema_version'], 2)
        self.assertTrue(INPUT['variants'])
        for variant, meta in INPUT['variants'].items():
            folder = ROOT / 'packages' / variant
            observed = {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in folder.rglob('*') if p.is_file()}
            self.assertEqual(observed, meta['files'], variant)
            instructions = meta['instruction_files']
            self.assertEqual(instructions, sorted(set(instructions)))
            self.assertTrue(set(instructions) <= observed.keys())
            self.assertEqual(meta['runtime_inputs'],
                             {p: h for p, h in observed.items() if p not in instructions})
            registered = set(meta['helper_contracts'])
            self.assertEqual({p for p in observed if p.endswith('.py')}, registered)
            for member in {p.split('/')[0] for p in registered}:
                self.assertIn(member, KNOWN, 'add actual consumer tests for the new package')
                self.assertEqual({Path(p).name for p in registered if p.startswith(member + '/')}, KNOWN[member])
        for name, expected in INPUT['test_assets'].items():
            self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), expected)

    def test_plan_valid_invalid_and_selected_context(self):
        self.profile()
        for package in (*packages('scoville-plan'), *packages('scoville-workflow-for-codex')):
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

    def test_next_ids_reach_manual_creation_without_helper_writes(self):
        self.profile()
        plan = self.project / 'docs/plans/0001-runtime.md'
        draft = plan.read_text(encoding='utf-8').replace('id: PLAN-0001', 'id: PLAN-0009', 1)
        draft = draft.replace('status: active', 'status: draft', 1)
        (plan.parent / '0007-conflict.md').write_text(draft, encoding='utf-8', newline='\n')
        (self.project / 'docs/decisions/0008-conflict.md').write_text(
            '---\nformat_version: 1\nid: ADR-0006\nstatus: proposed\ncreated: 2026-10-02\nscope: runtime\n---\n\n# Runtime choice\n',
            encoding='utf-8', newline='\n')
        snapshot = lambda: {p.relative_to(self.project).as_posix(): p.read_bytes()
                            for p in self.project.rglob('*') if p.is_file()}
        original = snapshot()
        for package in packages('scoville-plan'):
            invalid = self.run_cli(package, 'select_context.py', '--root', self.project,
                                   '--next-id', 'work-item', ok=False)
            self.assertEqual(invalid['diagnostics'][0]['code'], 'USAGE_ERROR')
            self.assertNotIn('next_id', invalid)
            for kind, expected, highest in (('work-item', 'W-002', 1),
                                            ('plan', 'PLAN-0010', 9), ('decision', 'ADR-0009', 8)):
                extra = ['--plan', 'PLAN-0001'] if kind == 'work-item' else []
                result = self.run_cli(package, 'select_context.py', '--root', self.project,
                                      '--next-id', kind, *extra)
                self.assertEqual(result['next_id'], expected)
                self.assertEqual(result['highest_number'], highest)
                self.assertFalse(result['reserved'])
                if kind != 'work-item':
                    prefix = 'plans' if kind == 'plan' else 'decisions'
                    filename = '0007' if kind == 'plan' else '0008'
                    metadata = 'PLAN-0009' if kind == 'plan' else 'ADR-0006'
                    self.assertEqual(result['conflicts'], [{'path': f'docs/{prefix}/{filename}-conflict.md',
                        'id': metadata, 'filename_id': ('PLAN-' if kind == 'plan' else 'ADR-') + filename}])
                    destination = self.project / result['filename_pattern'].replace('<lowercase-hyphenated-subject>', 'consumer')
                    self.assertFalse(destination.exists())
                    destination.write_text(result['next_id'] + '\n', encoding='utf-8')
                    self.assertEqual(destination.read_text(encoding='utf-8').strip(), expected)
                    destination.unlink()
                self.assertEqual(snapshot(), original)

    def test_start_facts_remain_read_only(self):
        self.profile()
        for package in packages('scoville-plan'):
            before = {p.relative_to(self.project).as_posix(): p.read_bytes()
                      for p in self.project.rglob('*') if p.is_file()}
            invalid = self.run_cli(package, 'select_context.py', '--root', self.project,
                                   '--check-start', 'W-1', ok=False)
            self.assertEqual(invalid['diagnostics'][0]['code'], 'WORK_ITEM_ID_INVALID')
            facts = self.run_cli(package, 'select_context.py', '--root', self.project, '--check-start', 'W-001')
            self.assertEqual(facts['work_status'], 'in_progress')
            self.assertTrue(facts['matches_current_item'])
            self.assertEqual(facts['dependencies'], [])
            self.assertEqual(facts['blocked_by'], [])
            self.assertEqual(before, {p.relative_to(self.project).as_posix(): p.read_bytes()
                                     for p in self.project.rglob('*') if p.is_file()})

    def test_encoding_warnings_do_not_hide_syntax_errors(self):
        self.profile()
        plan = self.project / 'docs/plans/0001-runtime.md'
        original = plan.read_text(encoding='utf-8')
        damaged = original.replace('Preserve Grüße', 'Preserve GrÃ¼ße', 1)
        for package in packages('scoville-plan'):
            plan.write_text(damaged, encoding='utf-8', newline='\n')
            valid = self.run_cli(package, 'validate_profile.py', '--root', self.project, raw=True)
            self.assertEqual(valid.returncode, 0)
            result = json.loads(valid.stdout)
            self.assertTrue(result['valid'])
            warning = next(d for d in result['diagnostics'] if d['code'] == 'FILE_MOJIBAKE_SUSPECTED')
            self.assertEqual(warning['severity'], 'warning')
            self.assertIn('line', warning)
            plan.write_text(damaged.replace('[status: in_progress]', '[status: nonsense]', 1),
                            encoding='utf-8', newline='\n')
            invalid = self.run_cli(package, 'validate_profile.py', '--root', self.project, ok=False)
            self.assertFalse(invalid['valid'])
            self.assertIn('WORK_STEP_STATUS_INVALID', [d['code'] for d in invalid['diagnostics']])
            plan.write_text(original, encoding='utf-8', newline='\n')
            self.assertTrue(self.run_cli(package, 'validate_profile.py', '--root', self.project)['valid'])


    def test_budget_corrections_execute_unchanged_in_host_shell(self):
        self.profile()
        plan = self.project / 'docs/plans/0001-runtime.md'
        plan.write_text(plan.read_text(encoding='utf-8').replace('Instructions: []',
            'Instructions: ' + 'Retain the authorized scope. ' * 40, 1), encoding='utf-8', newline='\n')
        shell = ((shutil.which('powershell') or shutil.which('pwsh')) if os.name == 'nt'
                 else shutil.which('sh'))
        self.assertIsNotNone(shell)
        project_name = 'Fixture "quoted" ü \' $() \\"tail'
        for number, package in enumerate(packages('scoville-workflow-for-codex')):
            assignment = self.base / f"assignment {number} ü ' $().txt"
            calls = [('build_dispatch_prompt.py', ['--communication-language', 'German', '--project-root', self.project, '--unit', 'W-001/step-1',
                '--role', 'reviewer', '--format', 'create', '--project-name', project_name, '--agent-number', '1', '--model', 'gpt-6.1-sol',
                '--thinking', 'xhigh',
                '--assignment-file', assignment, '--max-output-bytes=512'])]
            for script, arguments in calls:
                failed = self.run_cli(package, script, *arguments, ok=False, raw=True)
                self.assertEqual(failed.stdout, '')
                self.assertIn('OUTPUT_BUDGET_EXCEEDED', failed.stderr)
                if script == 'build_dispatch_prompt.py':
                    self.assertFalse(assignment.exists())
                prefix = '& {' if os.name == 'nt' else shlex.quote(sys.executable) + ' '
                commands = [line for line in failed.stderr.splitlines() if line.startswith(prefix)]
                self.assertEqual(len(commands), 1)
                correction = commands[0]
                command = ([shell, '-NoProfile', '-NonInteractive', '-Command', correction]
                           if os.name == 'nt' else [shell, '-c', correction])
                corrected = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', timeout=25)
                self.assertEqual(corrected.returncode, 0, corrected.stderr)
                payload = json.loads(corrected.stdout)
                if script == 'build_dispatch_prompt.py':
                    self.assertEqual(set(payload), {'task_name', 'message', 'fork_turns', 'model', 'reasoning_effort'})
                    self.assertIn(str(assignment), payload['message'])
                    self.assertIn(project_name, assignment.read_text(encoding='utf-8'))

    def test_workflow_fixed_pairs_and_dispatch_consumers(self):
        self.profile()
        for number, package in enumerate(packages('scoville-workflow-for-codex')):
            pair = self.run_cli(package, 'resolve_model_pair.py', '--role', 'reviewer', '--project-root', self.project)
            self.assertEqual(('gpt-6.1-sol','xhigh'), (pair['model'],pair['thinking']))
            self.run_cli(package, 'resolve_model_pair.py', '--project-root', self.project, ok=False)
            path=self.base/f'review-{number}.txt'
            assignment=self.run_cli(package,'build_dispatch_prompt.py','--communication-language','German',
                '--role','reviewer','--project-root',self.project,'--unit','W-001/step-1',
                '--format','create','--project-name','Grüße 中文','--agent-number','1','--assignment-file',path)
            self.assertEqual(pair['model'],assignment['model'])
            self.assertEqual(pair['thinking'],assignment['reasoning_effort'])
            self.assertEqual({'task_name','message','fork_turns','model','reasoning_effort'},set(assignment))
            self.assertEqual('none',assignment['fork_turns'])
            self.assertIn('Grüße 中文',path.read_text(encoding='utf-8'))
            selected=self.run_cli(package,'select_context.py','--root',self.project,'--unit','W-001/step-1')
            self.assertEqual('W-001/step-1',selected['work_item']['unit'])
            self.run_cli(package,'resolve_model_pair.py','--role','executor',ok=False)
            self.run_cli(package,'build_dispatch_prompt.py','--role','main','--communication-language','German',
                '--project-root',self.project,'--unit','W-001/step-1','--route','medium',ok=False)

    def test_review_accepts_needed_proof_without_synthetic_execution_final(self):
        self.profile()
        evidence=self.project/'check.txt'
        for number,package in enumerate(packages('scoville-workflow-for-codex')):
            assignment=self.base/f'fresh-review-{number}.txt'
            args=['--communication-language','German','--role','reviewer','--project-root',self.project,
                '--unit','W-001/step-1','--format','create','--project-name','Review','--agent-number','1',
                '--assignment-file',assignment]
            for text in ('',' \n\t'):
                evidence.write_text(text,encoding='utf-8')
                failed=self.run_cli(package,'build_dispatch_prompt.py',*args,'--supplemental-context',evidence,ok=False,raw=True)
                self.assertFalse(assignment.exists())
                self.assertEqual('',failed.stdout)
            self.run_cli(package,'build_dispatch_prompt.py',*args,'--executor-result',evidence,ok=False)
            self.assertFalse(assignment.exists())
            evidence.write_text(QUESTION,encoding='utf-8')
            payload=self.run_cli(package,'build_dispatch_prompt.py',*args,'--supplemental-context',evidence)
            self.assertIn(str(assignment),payload['message'])
            self.assertIn(QUESTION,assignment.read_text(encoding='utf-8'))
            self.run_cli(package,'build_dispatch_prompt.py',*args,'--agent-id','/root/review1',ok=False)
            assignment.unlink()
            # Required proof is evaluated by the fresh reviewer; no formal Executor final is required.
            self.run_cli(package,'build_dispatch_prompt.py',*args)
            self.assertTrue(assignment.exists())

    def test_automatic_assignments_are_complete_unique_external_files(self):
        self.profile()
        temporary=self.base/"Research and Development ü ' $()"
        temporary.mkdir()
        env=dict(os.environ,TMPDIR=str(temporary),TEMP=str(temporary),TMP=str(temporary))
        request=self.project/'request.txt';request.write_text(QUESTION,encoding='utf-8')
        paths=[]
        for package in packages('scoville-workflow-for-codex'):
            for role in ('explorer','reviewer'):
                payload=self.run_cli(package,'build_dispatch_prompt.py','--communication-language','German',
                    '--role',role,'--project-root',self.project,'--unit','W-001/step-1','--format','create',
                    '--project-name','Grüße "quoted" 中文','--agent-number','1',
                    '--supplemental-context',request,env=env)
                candidates=[p for p in temporary.iterdir() if p.is_file() and str(p) in payload['message']]
                self.assertEqual(1,len(candidates))
                path=candidates[0]
                self.assertTrue(path.is_absolute())
                self.assertEqual(temporary.resolve(), path.parent.resolve())
                self.assertNotIn(path,paths);paths.append(path)
                self.assertFalse(path.resolve().is_relative_to(self.project))
                content=path.read_bytes().decode('utf-8')
                self.assertTrue(content.endswith('\n'))
                self.assertIn(QUESTION,content)
                self.assertEqual(1,content.count('## Non-goals'))
                self.assertIn(str(self.project),content)
                for obsolete in ('check_agent_context.py','TAKEOVER_COMPLETE','rollover_pending'):
                    self.assertNotIn(obsolete,content)
            original=paths[-1].read_bytes()
            self.run_cli(package,'build_dispatch_prompt.py','--communication-language','German','--role','reviewer',
                '--project-root',self.project,'--unit','W-001/step-1','--format','create','--project-name','Collision',
                '--agent-number','2','--assignment-file',paths[-1],ok=False)
            self.assertEqual(original,paths[-1].read_bytes())

    def test_setup_saved_settings_reach_workflow_consumer(self):
        for package in packages('scoville-setup'):
            self.run_cli(package,'setup.py','set','--project-root',self.project,
                request={'workflow':{'manager':{'reasoning':'invalid'}}},ok=False)
            saved=self.run_cli(package,'setup.py','set','--project-root',self.project,
                request={'workflow':{'review':{'model':'test-model','reasoning':'high'}},
                         'ask':{'presets':{'sol':{'name':'Prüfung 東京 🌶'}}}})
            self.assertTrue(saved['saved'])
            shown=self.run_cli(package,'setup.py','show','--project-root',self.project)
            workflow=package.parent.parent/'scoville-workflow-for-codex/scoville-workflow-for-codex'
            consumed=self.run_cli(workflow,'resolve_model_pair.py','--show-config','--project-root',self.project)
            self.assertEqual(consumed['config']['review'],shown['effective']['workflow']['review'])
            self.assertEqual({'model':'test-model','reasoning':'high'},consumed['config']['review'])
            ask=package.parent.parent/'scoville-ask-for-codex/scoville-ask-for-codex'
            advice=self.run_cli(ask,'ask.py','--project-root',self.project,'--adviser','sol')
            self.assertEqual('Prüfung 東京 🌶',advice['config']['advisers'][0]['name'])
            path=self.project/'.scoville/config.json'
            before=path.read_bytes()
            for patch in ({'workflow':{'main':{'reasoning':'max'}}},
                          {'ask':{'presets':{'sol':{'effort':'ultra'}}}}):
                self.run_cli(package,'setup.py','set','--project-root',self.project,
                             request=patch,ok=False)
                self.assertEqual(before,path.read_bytes())
            manual=json.loads(before.decode('utf-8'))
            manual['workflow']['main']={'reasoning':'ultra'}
            manual['ask']['presets']['sol']['effort']='max'
            path.write_text(json.dumps(manual),encoding='utf-8')
            self.run_cli(package,'setup.py','set','--project-root',self.project,
                         request={'ask':{'claude':{'timeout_seconds':2400}}})
            self.assertEqual('ultra',json.loads(path.read_text(encoding='utf-8'))['workflow']['main']['reasoning'])
            advice=self.run_cli(ask,'ask.py','--project-root',self.project,'--adviser','sol')
            self.assertEqual('max',advice['config']['advisers'][0]['effort'])

    def test_setup_preserves_actual_modes_and_rejects_redirected_config_write(self):
        import stat
        for package in packages('scoville-setup'):
            path = self.project / '.scoville/config.json'
            path.parent.mkdir(exist_ok=True)
            path.write_text('{"other":7}', encoding='utf-8')
            path.chmod(0o640)
            mode = stat.S_IMODE(path.stat().st_mode)
            self.run_cli(package, 'setup.py', 'set', '--project-root', self.project,
                         request={'workflow': {'main': {'reasoning': 'medium'}}})
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), mode)
            self.assertEqual(json.loads(path.read_text())['other'], 7)
            outside = self.base / 'unchanged.json'
            outside.write_bytes(path.read_bytes())
            path.unlink()
            try:
                path.symlink_to(outside)
            except OSError as error:
                self.skipTest(f'symlink unavailable: {error}')
            original = outside.read_bytes()
            self.run_cli(package, 'setup.py', 'set', '--project-root', self.project,
                         request={'workflow': {'main': {'reasoning': 'high'}}}, ok=False)
            self.assertTrue(path.is_symlink())
            self.assertEqual(outside.read_bytes(), original)

    def test_workflow_section_read_and_setup_error_summary_remain_distinct(self):
        for package in packages('scoville-setup'):
            path = self.project / '.scoville/config.json'
            path.parent.mkdir(exist_ok=True)
            path.write_text('{"ask":null,"workflow":{"schema_version":2}}', encoding='utf-8')
            workflow = package.parent.parent / 'scoville-workflow-for-codex/scoville-workflow-for-codex'
            resolved = self.run_cli(workflow, 'resolve_model_pair.py', '--show-config', '--project-root', self.project)
            self.assertTrue(resolved['valid'])
            path.write_text('{"ask":null,"workflow":false}', encoding='utf-8')
            shown = self.run_cli(package, 'setup.py', 'show', '--project-root', self.project, ok=False)
            self.assertFalse(shown['ok'])
            self.assertEqual(set(shown['diagnostics']), {'ask', 'workflow'})
            self.assertNotIn('effective', shown)

    def test_own_active_main_pair_and_identity_in_every_package(self):
        host=self.base/'host';sessions=host/'sessions';sessions.mkdir(parents=True)
        thread='runtime-main';rollout=sessions/('rollout-'+thread+'.jsonl')
        env=dict(os.environ,CODEX_THREAD_ID=thread,CODEX_HOME=str(host))
        def record(model='gpt-6.1-sol',source='vscode',active=True):
            records=[('session_meta',{'id':thread,'source':source}),
                ('event_msg',{'type':'task_started','turn_id':'turn-1'}),
                ('turn_context',{'turn_id':'turn-1','model':model,'effort':'high'})]
            if not active:records.append(('event_msg',{'type':'task_complete','turn_id':'turn-1'}))
            rollout.write_text('\n'.join(json.dumps({'ordinal':i,'type':kind,'payload':payload})
                for i,(kind,payload) in enumerate(records))+'\n',encoding='utf-8')
        for package in packages('scoville-workflow-for-codex'):
            self.assertFalse((package/'scripts/check_agent_context.py').exists())
            record()
            result=self.run_cli(package,'resolve_model_pair.py','--role','main','--project-root',self.project,env=env)
            self.assertTrue(result['valid']);self.assertEqual(thread,result['thread_id'])
            self.assertEqual(('gpt-6.1-sol','high'),(result['model'],result['thinking']))
            for kwargs in ({'model':'wrong-model'},{'source':{'subagent':{}}},{'active':False}):
                record(**kwargs)
                invalid=self.run_cli(package,'resolve_model_pair.py','--role','main','--project-root',self.project,env=env,ok=False)
                self.assertFalse(invalid['valid'])
            spec=importlib.util.spec_from_file_location('runtime_title',package/'scripts/native_task_arguments.py')
            module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
            with self.assertRaises(ValueError):module.workflow_title('test','reviewer',1,'PLAN-0001/W-001/step-1..step-2')

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

    def test_prepared_claude_request_uses_selected_project_not_process_cwd(self):
        env = self.launcher('claude', "import json,os,sys\nsys.stdin.reconfigure(encoding='utf-8'); sys.stdout.reconfigure(encoding='utf-8')\nprompt=sys.stdin.read()\nprint(json.dumps({'result':json.dumps({'prompt':prompt,'cwd':os.getcwd()},ensure_ascii=False),'session_id':'selected-project-session'},ensure_ascii=False))\n")
        selected = self.base / 'Selected Grüße 中文 workspace'
        selected.mkdir()
        unrelated = self.project / '.scoville/config.json'
        unrelated.parent.mkdir()
        invalid_bytes = b'{ deliberately malformed unrelated config'
        unrelated.write_bytes(invalid_bytes)
        question = self.base / 'selected-question.txt'
        question.write_text(QUESTION, encoding='utf-8')
        for package in packages('scoville-ask-for-codex'):
            request_file = self.base / 'selected-request.json'
            self.run_cli(package, 'ask.py', '--project-root', selected, '--adviser', 'claude',
                         '--question-file', question, '--mode', 'review', '--scope', 'runtime',
                         '--reference', 'selected-project', '--model', 'test-model', '--effort', 'high',
                         '--output-file', request_file)
            original = request_file.read_bytes()
            request = json.loads(original)
            invalid = self.run_cli(package, 'ask.py',
                                   request={**request, 'cwd': str(selected / 'missing')}, env=env, ok=False)
            self.assertFalse(invalid['ok'])
            self.assertIn('cwd', invalid['error'])
            self.assertIn(repr(str(selected / 'missing')), invalid['error'])
            self.assertNotIn('answer', invalid)
            answer = self.run_cli(package, 'ask.py', '--input-file', request_file, env=env)
            received = json.loads(answer['answer'])
            self.assertEqual(received['prompt'], request['prompt'])
            self.assertTrue(received['prompt'].endswith(QUESTION))
            self.assertEqual(Path(received['cwd']).resolve(), selected.resolve())
            self.assertEqual(answer['session_id'], 'selected-project-session')
            self.assertEqual(answer['requested_model'], 'test-model')
            self.assertEqual(answer['requested_effort'], 'high')
            continued = self.run_cli(package, 'ask.py',
                                     request={**request, 'session_id': answer['session_id'], 'prompt': QUESTION}, env=env)
            self.assertEqual(json.loads(continued['answer'])['prompt'], QUESTION)
            self.assertEqual(continued['context_mode'], 'continued')
            self.assertEqual(request_file.read_bytes(), original)
            self.assertEqual(unrelated.read_bytes(), invalid_bytes)
            request_file.unlink()

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


    def test_generated_process_preserves_argv_exit_and_successful_shell(self):
        package = next(packages('scoville-workflow-for-codex'))
        spec = importlib.util.spec_from_file_location('process_arguments', package / 'scripts/native_task_arguments.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        probe = self.base / 'argv probe.py'
        probe.write_text('import json, sys\nprint(json.dumps(sys.argv[1:]))\n', encoding='utf-8')
        values = ['', 'with spaces', "apostrophe's", 'literal"quote', 'trailing\\', '$() ` ${value}']
        shells = ([value for name in ('powershell', 'pwsh') if (value := shutil.which(name))]
                  if os.name == 'nt' else [shutil.which('sh')])
        self.assertTrue(shells and all(shells))
        for shell in shells:
            flags = ['-NoProfile', '-NonInteractive', '-Command'] if os.name == 'nt' else ['-c']
            command = module.shell_command([sys.executable, '-X', 'utf8', str(probe), *values])
            continuation = '; Write-Output SHELL_CONTINUES' if os.name == 'nt' else '; printf "SHELL_CONTINUES\\n"'
            good = subprocess.run([shell, *flags, command + continuation], capture_output=True, timeout=25)
            self.assertEqual(good.returncode, 0, good.stderr)
            lines = good.stdout.decode('utf-8').splitlines()
            self.assertEqual(json.loads(lines[0]), values)
            self.assertEqual(lines[1], 'SHELL_CONTINUES')
            for code, stderr in [(0, 'child stderr'), (3, '')]:
                invocation = module.shell_command([sys.executable, '-X', 'utf8', '-c',
                    f'import sys; sys.stderr.write({stderr!r}); sys.exit({code})'])
                result = subprocess.run([shell, *flags, invocation], capture_output=True, timeout=25)
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertEqual(result.stderr.decode('utf-8'), stderr)
            missing = self.base / 'missing interpreter Grüße 中文'
            # The catch must produce UTF-8 even in a legacy console encoding.
            prefix = "[Console]::OutputEncoding = [Text.Encoding]::GetEncoding(437); " if os.name == 'nt' else ''
            failed = subprocess.run([shell, *flags, prefix + module.shell_command([str(missing)])], capture_output=True, timeout=25)
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn(str(missing), failed.stderr.decode('utf-8', errors='strict'))
            if os.name == 'nt':
                self.assertEqual(failed.returncode, 125)


    def test_text_preflight_and_complete_unicode_file_consumer(self):
        text_file = self.base / 'Complete Grüße 中文.txt'
        # One actual packaged consumer per build variant; all copies are covered by inventory hashes.
        for package in packages('scoville-code'):
            with self.subTest(package=str(package)):
                small = (QUESTION + 'Required final fact: preserve the public interface.\n').encode('utf-8')
                text_file.write_bytes(small)
                result = self.run_cli(package, 'check_text_size.py', '--file', text_file, '--max-output-tokens', 10000)
                self.assertEqual(result['status'], 'fits_conservative_budget')
                self.assertEqual(result['utf8_bytes'], len(small))
                self.assertEqual(result['tool_output_limit_tokens'], 10000)
                self.assertEqual(text_file.read_bytes(), small)
                # Individually fitting pieces can exceed the combined budget; labels are included.
                combined = ('first result: ' + 'a' * 6000 + '\nsecond result: ' + 'b' * 6000 + '\nEND REQUIRED Grüße 中文\n').encode('utf-8')
                text_file.write_bytes(combined)
                measured = self.run_cli(package, 'check_text_size.py', '--file', text_file, '--max-output-tokens', 10000, raw=True)
                result = json.loads(measured.stdout)
                self.assertEqual(result['status'], 'compact_required')
                self.assertEqual(result['utf8_bytes'], len(combined))
                self.assertNotIn('END REQUIRED', measured.stdout)
                self.assertEqual(text_file.read_bytes(), combined)
                published = self.run_cli(package, 'check_text_size.py', '--file', text_file, '--max-output-tokens', 10000, '--publish-full', '--project-root', self.project)
                retained = Path(published['full_file'])
                self.assertEqual(published['status'], 'complete_file')
                self.assertTrue(retained.is_absolute())
                self.assertEqual(retained.parent, self.project / '.scoville/temp')
                self.assertEqual(retained.name, hashlib.sha256(combined).hexdigest() + '.txt')
                self.assertEqual((retained.parent / '.gitignore').read_text(encoding='utf-8').splitlines(), ['*'])
                # Intended next consumer uses metadata unchanged and reads the ENTIRE bytes.
                received = retained.read_bytes()
                self.assertEqual(received, combined)
                self.assertIn('END REQUIRED Grüße 中文', received.decode('utf-8'))
                again = self.run_cli(package, 'check_text_size.py', '--file', text_file, '--max-output-tokens', 10000, '--publish-full', '--project-root', self.project)
                self.assertEqual(again['full_file'], str(retained))
                # An authenticated transfer may require a file independently of size.
                unmeasured = self.run_cli(package, 'check_text_size.py', '--file', text_file, '--publish-full', '--project-root', self.project)
                self.assertEqual(set(unmeasured), {'status', 'utf8_bytes', 'full_file', 'instruction'})
                self.assertEqual(unmeasured['status'], 'complete_file')
                self.assertEqual(unmeasured['utf8_bytes'], len(combined))
                received = Path(unmeasured['full_file']).read_bytes()
                self.assertEqual(received, combined)
                self.assertFalse(list(retained.parent.glob('tmp*')))

    def test_retired_reader_flag_cannot_return_source_content(self):
        source = self.base / 'Required source Grüße.txt'
        data = b'REQUIRED CONTENT MUST NOT BE EMITTED BY AN OUTPUT CHECK'
        source.write_bytes(data)
        for package in packages('scoville-code'):
            rejected = subprocess.run([sys.executable, str(package / 'scripts/check_text_size.py'),
                '--file', str(source), '--max-output-tokens', '1000', '--part', '1'], capture_output=True)
            self.assertEqual(rejected.returncode, 2)
            self.assertEqual(rejected.stdout, b'')
            self.assertIn(b'unrecognized arguments: --part 1', rejected.stderr)
            self.assertEqual(source.read_bytes(), data)

    def test_generated_memory_capture_reaches_host_shell(self):
        shells = ([value for name in ('powershell', 'pwsh') if (value := shutil.which(name))]
                  if os.name == 'nt' else [shutil.which('sh')])
        self.assertTrue(shells and all(shells))
        package = next(packages('scoville-workflow-for-codex'))
        spec = importlib.util.spec_from_file_location('case_native_arguments', package / 'scripts/native_task_arguments.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        producer = self.base / 'producer.py'
        producer.write_text("import sys\nsys.stdout.buffer.write('Grüße → 😀\\n\\n'.encode('utf-8'))\nsys.stderr.buffer.write('Fehler ä\\n\\n'.encode('utf-8'))\nsys.exit(7)\n", encoding='utf-8')
        out, err = 'Grüße → 😀\n\n'.encode('utf-8'), 'Fehler ä\n\n'.encode('utf-8')
        expected = f'exit=7 stdout_bytes={len(out)} stderr_bytes={len(err)}\n'.encode('ascii') + b'stdout:\n' + out + b'\nstderr:\n' + err
        for shell in shells:
            flags = ['-NoProfile', '-NonInteractive', '-Command'] if os.name == 'nt' else ['-c']
            captured = subprocess.run([shell, *flags, module.shell_command([sys.executable, '-X', 'utf8', str(package / 'scripts/check_text_size.py'),
                '--max-output-tokens', '1000', '--run', '--', sys.executable, '-X', 'utf8', str(producer)])], capture_output=True, timeout=25)
            self.assertEqual(captured.returncode, 7, captured.stderr)
            self.assertEqual(captured.stdout, expected)
            self.assertEqual(captured.stderr, b'')
            self.assertLessEqual(len(captured.stdout), 800)
            argv = [sys.executable, '-X', 'utf8', str(package / 'scripts/check_text_size.py'),
                    '--max-output-tokens', '1000', '--run', '--', sys.executable, '-X', 'utf8', str(producer)]
            if os.name == 'nt':
                quote = lambda value: "'" + value.replace("'", "''") + "'"
                typed = '& ' + ' '.join(quote(value) for value in argv) + '\nexit $LASTEXITCODE'
            else:
                typed = shlex.join(argv)
            documented = subprocess.run([shell, *flags, typed], capture_output=True, timeout=25)
            self.assertEqual(documented.returncode, 7, documented.stderr)
            self.assertEqual(documented.stdout, expected)
            self.assertEqual(documented.stderr, b'')

    def test_small_publish_enabled_capture_stays_inline_without_artifact(self):
        package = next(packages('scoville-code'))
        producer = self.base / 'small-once.py'
        marker = self.base / 'small-count.txt'
        producer.write_text("from pathlib import Path; import sys\nPath(sys.argv[1]).write_text('executed')\nsys.stdout.buffer.write('Grüße\\n'.encode('utf-8'))\nsys.stderr.buffer.write(b'notice\\n')\nsys.exit(7)\n", encoding='utf-8')
        result = subprocess.run([sys.executable, '-X', 'utf8', str(package/'scripts/check_text_size.py'),
            '--max-output-tokens', '1000', '--publish-full', '--project-root', str(self.project),
            '--run', '--', sys.executable, '-X', 'utf8', str(producer), str(marker)], capture_output=True)
        out, err = 'Grüße\n'.encode('utf-8'), b'notice\n'
        expected = f'exit=7 stdout_bytes={len(out)} stderr_bytes={len(err)}\n'.encode('ascii') + b'stdout:\n' + out + b'\nstderr:\n' + err
        self.assertEqual(result.returncode, 7, result.stderr)
        self.assertEqual(result.stdout, expected)
        self.assertEqual(result.stderr, b'')
        self.assertEqual(marker.read_text(), 'executed')
        self.assertFalse(list((self.project/'.scoville/temp').glob('*.txt')))
        self.assertFalse((self.project/'.scoville/temp/.gitignore').exists())

    def test_command_capture_withheld_publication_and_prestart_errors(self):
        package = next(packages('scoville-code'))
        checker = package / 'scripts/check_text_size.py'
        producer = self.base / 'one-execution.py'
        counter = self.base / 'execution-count.txt'
        producer.write_text("import sys\nfrom pathlib import Path\np=Path(sys.argv[1]); p.write_text(p.read_text()+'x' if p.exists() else 'x')\nsys.stdout.buffer.write(('ü→😀'*100).encode('utf-8'))\nsys.stderr.buffer.write(b'failure\\n\\n')\nsys.exit(7)\n", encoding='utf-8')
        child = [sys.executable, '-X', 'utf8', str(producer), str(counter)]
        def invoke(limit, extra=(), command=None):
            return subprocess.run([sys.executable, '-X', 'utf8', str(checker), '--max-output-tokens', str(limit),
                *map(str, extra), '--run', '--', *(child if command is None else command)], capture_output=True, timeout=25)
        guarded_root = self.base / 'Guarded capture ü 中文'
        guarded_root.mkdir()
        uppercase = self.base / 'one-execution.PY'
        uppercase.write_bytes(producer.read_bytes())
        diagnostic = (b'output_complete=false error=PYTHON_INTERPRETER_REQUIRED child_started=false: '
            b'insert the verified Python executable and -X utf8 before the script; '
            b'keep all existing arguments exit=None\n')
        for script, extra in [(producer, []), (uppercase, ['--publish-full', '--project-root', guarded_root])]:
            guarded = invoke(1000, extra, command=[str(script), str(counter)])
            self.assertEqual(guarded.returncode, 125)
            self.assertEqual(guarded.stdout, b'')
            self.assertEqual(guarded.stderr, diagnostic)
            self.assertFalse(counter.exists(), 'direct script must not start the marker child')
            self.assertEqual(list(guarded_root.iterdir()), [], 'guard must precede publication preparation')
        short = invoke(100, command=[str(producer), str(counter)])
        self.assertEqual(short.returncode, 125)
        self.assertEqual(short.stdout, b'')
        self.assertEqual(short.stderr, b'output_complete=false error=capture exit=None\n')
        self.assertFalse(counter.exists())
        withheld = invoke(100)
        self.assertEqual(withheld.returncode, 7)
        self.assertIn(b'output_complete=false', withheld.stdout)
        self.assertNotIn('ü→😀'.encode('utf-8'), withheld.stdout)
        self.assertLessEqual(len(withheld.stdout) + len(withheld.stderr), 80)
        self.assertEqual(counter.read_text(), 'x')
        counter.unlink()
        published = invoke(1000, ['--publish-full', '--project-root', self.project])
        self.assertEqual(published.returncode, 7, published.stderr)
        meta = json.loads(published.stdout)
        self.assertFalse(meta['output_complete'])
        self.assertEqual(meta['exit_code'], 7)
        received = Path(meta['full_file']).read_bytes()
        self.assertNotIn('sha256', meta)
        out, err = ('ü→😀'*100).encode('utf-8'), b'failure\n\n'
        self.assertEqual(received, f'exit=7 stdout_bytes={len(out)} stderr_bytes={len(err)}\n'.encode('ascii') + b'stdout:\n' + out + b'\nstderr:\n' + err)
        self.assertEqual(counter.read_text(), 'x')
        counter.unlink()
        child_two = invoke(1000, command=[sys.executable, '-c', 'import sys;sys.exit(2)'])
        self.assertEqual(child_two.returncode, 2)
        self.assertIn(b'exit=2 ', child_two.stdout)
        abbreviated = subprocess.run([sys.executable, str(checker), '--max-output-tokens', '1000',
            '--ru', '--', *child], capture_output=True, timeout=25)
        self.assertNotEqual(abbreviated.returncode, 0)
        self.assertNotIn(b'Traceback', abbreviated.stdout + abbreviated.stderr)
        self.assertFalse(counter.exists())
        for limit, extra in [(1, []), (100, ['--part', '1']), (100, ['--file', str(producer)]),
                             (100, ['--publish-full', '--project-root', self.project])]:
            invalid = invoke(limit, extra)
            self.assertEqual(invalid.returncode, 125)
            self.assertFalse(counter.exists(), 'invalid options must fail before child effects')
            self.assertLessEqual(len(invalid.stdout) + len(invalid.stderr), limit * 4 // 5)
        binary = invoke(1000, command=[sys.executable, '-c', 'import sys;sys.stdout.buffer.write(bytes([255]));sys.exit(7)'])
        self.assertEqual(binary.returncode, 125)
        self.assertEqual(binary.stdout, b'')
        self.assertNotIn(b'\xff', binary.stderr)
        self.assertIn(b'exit=7', binary.stderr)
        missing = invoke(1000, command=[str(self.base / 'absent-executable')])
        self.assertEqual(missing.returncode, 125)
        self.assertIn(b'output_complete=false', missing.stderr)
        for blocked in ('.scoville', '.scoville/temp'):
            root = self.base / ('blocked-' + blocked.replace('/', '-'))
            root.mkdir()
            target = root / blocked
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b'existing regular file')
            invalid = invoke(1000, ['--publish-full', '--project-root', root])
            self.assertEqual(invalid.returncode, 125)
            self.assertFalse(counter.exists(), 'known publication failure must precede child effects')
            self.assertEqual(target.read_bytes(), b'existing regular file')
        if os.name != 'nt':
            signal = invoke(1000, command=[sys.executable, '-c', 'import os,signal;os.kill(os.getpid(),signal.SIGTERM)'])
            self.assertEqual(signal.returncode, 143)
            self.assertIn(b'exit=-15', signal.stdout)

    def test_capture_uses_eof_and_preserves_failed_original_bytes(self):
        checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
        prefix = [sys.executable, '-X', 'utf8', str(checker), '--max-output-tokens', '1500']
        eof = subprocess.run([*prefix, '--run', '--', sys.executable, '-c',
            'import sys;print(len(sys.stdin.buffer.read()))'], input=b'inherited input',
            capture_output=True, timeout=20)
        self.assertEqual(eof.returncode, 0, eof.stderr)
        self.assertIn(b'stdout:\n0\n', eof.stdout.replace(b'\r\n', b'\n'))
        marker = self.base / 'once.txt'
        code = 'import sys;from pathlib import Path;p=Path(sys.argv[1]);p.write_text(p.read_text()+"x" if p.exists() else "x");sys.stdout.buffer.write(b"\\xff");sys.stderr.buffer.write(b"\\x80");sys.exit(7)'
        bad = subprocess.run([*prefix, '--publish-full', '--project-root', str(self.project),
            '--run', '--', sys.executable, '-c', code, str(marker)], capture_output=True, timeout=20)
        self.assertEqual(bad.returncode, 125)
        self.assertEqual(bad.stdout, b'')
        meta = json.loads(bad.stderr)
        self.assertEqual(meta['error'], 'invalid_utf8')
        self.assertIn('instruction', meta)
        self.assertIn('text-dependent', meta['instruction'])
        self.assertIn('producer-established encoding', meta['instruction'])
        self.assertTrue(meta['capture_complete'])
        self.assertEqual(meta['exit_code'], 7)
        self.assertEqual(Path(meta['full_file']).read_bytes(), b'exit=7 stdout_bytes=1 stderr_bytes=1\nstdout:\n\xff\nstderr:\n\x80')
        self.assertEqual(marker.read_text(), 'x', 'capture failure must not rerun the effect')

    def test_capture_timeout_preserves_partial_output_and_stops_family(self):
        checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
        pids = self.base / 'pids.json'
        code = 'import subprocess,sys,time,json,os;from pathlib import Path;p=subprocess.Popen([sys.executable,"-c","import time;time.sleep(60)"]);Path(sys.argv[1]).write_text(json.dumps([os.getpid(),p.pid]));print("started",flush=True);time.sleep(60)'
        result = subprocess.run([sys.executable, '-X', 'utf8', str(checker),
            '--max-output-tokens', '1500', '--publish-full', '--project-root', str(self.project),
            '--timeout-seconds', '2', '--run', '--', sys.executable, '-c', code, str(pids)],
            capture_output=True, timeout=25)
        self.assertEqual(result.returncode, 125)
        meta = json.loads(result.stderr)
        self.assertEqual(meta['error'], 'timeout')
        self.assertFalse(meta['capture_complete'])
        self.assertIsInstance(meta['exit_code'], int)
        self.assertIn(b'started', Path(meta['full_file']).read_bytes())
        for pid in json.loads(pids.read_text()):
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

    def test_capture_deadline_survives_an_exited_parent_with_open_child_pipes(self):
        checker = next(packages('scoville-code')) / 'scripts/check_text_size.py'
        child_pid = self.base / 'orphan-pid.txt'
        code = 'import subprocess,sys;from pathlib import Path;p=subprocess.Popen([sys.executable,"-c","import time;time.sleep(60)"]);Path(sys.argv[1]).write_text(str(p.pid));print("before-parent-exit",flush=True)'
        try:
            result = subprocess.run([sys.executable, '-X', 'utf8', str(checker),
                '--max-output-tokens', '1500', '--publish-full', '--project-root', str(self.project),
                '--timeout-seconds', '0.5', '--run', '--', sys.executable, '-c', code, str(child_pid)],
                capture_output=True, timeout=20)
            self.assertEqual(result.returncode, 125)
            meta = json.loads(result.stderr)
            self.assertFalse(meta['capture_complete'])
            self.assertEqual(meta['error'], 'timeout_cleanup_incomplete' if os.name == 'nt' else 'timeout')
            self.assertIn(b'before-parent-exit', Path(meta['full_file']).read_bytes())
        finally:
            if child_pid.exists():
                pid = int(child_pid.read_text())
                if os.name == 'nt':
                    subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'], capture_output=True, timeout=10)
                else:
                    import signal
                    try: os.kill(pid, signal.SIGKILL)
                    except ProcessLookupError: pass


    def test_text_preflight_invalid_and_corrected_cli_without_overwrite(self):
        package = next(packages('scoville-code'))
        missing = self.base / 'missing.txt'
        bad = self.run_cli(package, 'check_text_size.py', '--file', missing, '--max-output-tokens', 10000, ok=False, raw=True)
        self.assertEqual(bad.stdout, '')
        self.assertIn('--file', bad.stderr)
        self.assertIn(str(missing), bad.stderr)
        self.assertIn('UTF-8', bad.stderr)
        missing.write_bytes(b'\xff')
        invalid_utf8 = self.run_cli(package, 'check_text_size.py', '--file', missing,
                                    '--max-output-tokens', 10000, ok=False, raw=True)
        self.assertEqual(invalid_utf8.stdout, '')
        self.assertIn(str(missing), invalid_utf8.stderr)
        self.assertIn('UTF-8', invalid_utf8.stderr)
        missing.write_text('complete corrected input', encoding='utf-8')
        fixed = self.run_cli(package, 'check_text_size.py', '--file', missing, '--max-output-tokens', 10000)
        self.assertEqual(fixed['status'], 'fits_conservative_budget')
        no_limit = self.run_cli(package, 'check_text_size.py', '--file', missing, ok=False, raw=True)
        self.assertEqual(no_limit.stdout, '')
        self.assertIn('--max-output-tokens', no_limit.stderr)
        self.assertIn('--publish-full', no_limit.stderr)
        corrected_check = self.run_cli(package, 'check_text_size.py', '--file', missing, '--max-output-tokens', 10000)
        self.assertEqual(corrected_check['status'], 'fits_conservative_budget')
        for invalid_limit in (0, -1):
            invalid = self.run_cli(package, 'check_text_size.py', '--file', missing, '--max-output-tokens', invalid_limit,
                                   '--publish-full', '--project-root', self.project, ok=False, raw=True)
            self.assertEqual(invalid.stdout, '')
            self.assertIn('--max-output-tokens', invalid.stderr)
            self.assertFalse((self.project / '.scoville/temp').exists())
        corrected_publication = self.run_cli(package, 'check_text_size.py', '--file', missing, '--publish-full', '--project-root', self.project)
        received = Path(corrected_publication['full_file']).read_bytes()
        self.assertEqual(received, missing.read_bytes())
        digest = hashlib.sha256(missing.read_bytes()).hexdigest()
        target = self.project / '.scoville/temp' / (digest + '.txt')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b'existing content must survive')
        rejected = self.run_cli(package, 'check_text_size.py', '--file', missing, '--max-output-tokens', 10000, '--publish-full', '--project-root', self.project, ok=False, raw=True)
        self.assertEqual(rejected.stdout, '')
        failure = json.loads(rejected.stderr)
        self.assertEqual(failure['status'], 'publication_failed')
        self.assertIn(str(target), failure['message'])
        self.assertEqual(target.read_bytes(), b'existing content must survive')
        recovery = Path(failure['full_file'])
        self.assertEqual(recovery.read_bytes(), missing.read_bytes())
        self.assertEqual(set(target.parent.glob('tmp*')), {recovery})
        safe = self.base / 'corrected project Ä 中文'
        safe.mkdir()
        corrected = self.run_cli(package, 'check_text_size.py', '--file', missing,
                                 '--publish-full', '--project-root', safe)
        received = Path(corrected['full_file']).read_bytes()
        self.assertEqual(received, missing.read_bytes())
        self.assertEqual(target.read_bytes(), b'existing content must survive')

    def test_text_preflight_rejects_path_escape_before_writing(self):
        package = next(packages('scoville-code'))
        source = self.base / 'whole.txt'
        source.write_text('complete payload', encoding='utf-8')
        outside = self.base / 'outside'
        outside.mkdir()
        try:
            (self.project / '.scoville').symlink_to(outside, target_is_directory=True)
        except OSError as error:
            self.skipTest('Host cannot create the test directory symlink: ' + str(error))
        result = self.run_cli(package, 'check_text_size.py', '--file', source, '--max-output-tokens', 10000, '--publish-full', '--project-root', self.project, ok=False, raw=True)
        self.assertEqual(result.stdout, '')
        self.assertIn('--project-root', result.stderr)
        self.assertIn(str((outside / 'temp').resolve()), result.stderr)
        self.assertIn(str(self.project.resolve()), result.stderr)
        self.assertEqual(list(outside.iterdir()), [])
        safe = self.base / 'contained project'
        safe.mkdir()
        corrected = self.run_cli(package, 'check_text_size.py', '--file', source,
                                 '--publish-full', '--project-root', safe)
        received = Path(corrected['full_file']).read_bytes()
        self.assertEqual(received, source.read_bytes())
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
