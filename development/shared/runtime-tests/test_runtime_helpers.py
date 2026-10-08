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

    def test_complete_output_is_consumed_and_repeat_preserves_report(self):
        for package in packages('scoville-workflow-for-codex'):
            report = Path(self.run_cli(package, 'run_feedback.py', 'create', '--project-root', self.project)['report_file'])
            arguments = ['complete', '--report-file', report, '--project', 'Grüße 中文',
                         '--plan', 'PLAN-0001', '--point', 'W-001', '--text', QUESTION]
            before = report.read_bytes()
            failed = self.run_cli(package, 'run_feedback.py', *arguments, ok=False, raw=True)
            self.assertEqual(failed.stdout, '')
            self.assertIn('--completed', failed.stderr)
            self.assertEqual(report.read_bytes(), before)
            completed = self.run_cli(package, 'run_feedback.py', *arguments, '--completed')
            self.assertTrue(completed['message'].startswith('COMPLETED\n'))
            read = self.run_cli(package, 'run_feedback.py', 'read', '--report-file', report)
            self.assertEqual(read['text'], report.read_text(encoding='utf-8'))
            before, mtime = report.read_bytes(), report.stat().st_mtime_ns
            self.assertEqual(self.run_cli(package, 'run_feedback.py', *arguments, '--completed'), completed)
            self.assertEqual(report.read_bytes(), before)
            self.assertEqual(report.stat().st_mtime_ns, mtime)

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
            calls = [('build_dispatch_prompt.py', ['--project-root', self.project, '--unit', 'W-001/step-1',
                '--role', 'executor', '--format', 'create', '--manager-agent-id', 'manager',
                '--project-name', project_name, '--worker-number', '1', '--model', 'gpt-6-luna',
                '--thinking', 'high', '--assignment-file', assignment, '--max-output-bytes=512']),
                ('run_feedback.py', ['progress', '--project', project_name, '--project-root', self.project,
                '--point', 'W-001/step-1', '--previous-key', 'a' * 64, '--max-output-bytes', '512'])]
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
                else:
                    direct = self.run_cli(package, script, *arguments[:-1], '65536')
                    self.assertEqual(payload, direct)

    def test_workflow_report_settings_dispatch_and_manager_consumers(self):
        self.profile()
        request = self.project / 'request.txt'
        request.write_text(QUESTION, encoding='utf-8')
        for package_number, package in enumerate(packages('scoville-workflow-for-codex')):
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
                '--model', pair['model'], '--thinking', pair['thinking'],
                '--assignment-file', self.project / f'worker-{package_number}.txt')
            self.assertEqual(assignment['model'], pair['model'])
            self.assertIn('Grüße 中文', assignment['message'])
            common = ['--runner-id', 'runner', '--project-name', 'Grüße 中文', '--manager-number', '1', '--report-file', report]
            start_file = self.project / f'manager-start-{package_number}.txt'
            start = self.run_cli(package, 'build_manager_handoff.py', '--mode', 'start', *common,
                '--project-root', self.project, '--request-file', request, '--assignment-file', start_file)
            successor_file = self.project / f'manager-successor-{package_number}.txt'
            successor = self.run_cli(package, 'build_manager_handoff.py', '--mode', 'successor', *common,
                '--predecessor-id', 'old-manager', '--model', start['model'],
                '--thinking', start['reasoning_effort'], '--assignment-file', successor_file)
            self.assertEqual(successor['model'], start['model'])
            self.run_cli(package, 'build_manager_handoff.py', '--mode', 'start', ok=False)
            for payload in (assignment, start, successor):
                self.assertEqual(set(payload), {'task_name', 'message', 'fork_turns', 'model', 'reasoning_effort'})
                self.assertEqual(payload['fork_turns'], 'none')
            for payload, assignment_file in ((start, start_file), (successor, successor_file)):
                self.assertIn(str(assignment_file), payload['message'])
                paths = [line.removeprefix('Plan Skill: ') for line in assignment_file.read_text(encoding='utf-8').splitlines()
                         if line.startswith('Plan Skill: ')]
                self.assertEqual(len(paths), 1)
                plan = Path(paths[0])
                self.assertTrue(plan.read_text(encoding='utf-8').strip())
                selected = self.run_cli(plan.parent, 'select_context.py', '--root', self.project, '--unit', 'W-001/step-1')
                self.assertEqual(selected['work_item']['unit'], 'W-001/step-1')
                self.assertTrue(self.run_cli(plan.parent, 'validate_profile.py', '--root', self.project)['valid'])

    def test_recovery_assignments_keep_selected_constraints_without_completed_procedure(self):
        self.profile()
        plan = self.project / 'docs/plans/0001-runtime.md'
        original = 'First write the approved text, then transfer its document check.'
        constraint = 'Preserve approved wording and unchanged tests.'
        plan.write_text(plan.read_text(encoding='utf-8').replace('Instructions: []',
            'Instructions: ' + original + ' ' + constraint), encoding='utf-8')
        handoff = self.project / 'handoff.txt'
        handoff.write_text('Approved text is saved and checked. Only its document check remains.', encoding='utf-8')
        facts = self.project / 'facts.txt'
        facts.write_text(constraint + ' Check the saved document only. No external work.', encoding='utf-8')
        assignments = self.base / "Recovery Aufträge ü 中文"
        assignments.mkdir()
        for package_number, package in enumerate(packages('scoville-workflow-for-codex')):
            for role in ('executor', 'reviewer'):
                assignment = assignments / f'{package_number}-{role}.txt'
                arguments = ['--role', role, '--project-root', self.project,
                    '--unit', 'W-001/step-1', '--manager-agent-id', 'manager',
                    '--context-handoff', handoff,
                    '--supplemental-context', facts, '--predecessor-agent-id', 'previous-worker']
                payload = self.run_cli(package, 'build_dispatch_prompt.py', '--role', role,
                    '--project-root', self.project, '--unit', 'W-001/step-1', '--manager-agent-id', 'manager',
                    '--format', 'create', '--project-name', 'Recovery', '--worker-number', '1',
                    '--model', 'gpt-6-luna', '--thinking', 'high', '--context-handoff', handoff,
                    '--supplemental-context', facts, '--predecessor-agent-id', 'previous-worker',
                    '--assignment-file', assignment)
                complete = assignment.read_text(encoding='utf-8')
                self.assertIn(str(assignment), payload['message'])
                self.assertIn(handoff.read_text(encoding='utf-8'), complete)
                self.assertIn(facts.read_text(encoding='utf-8'), complete)
                self.assertNotIn(original, complete)
                self.assertIn('HANDOFF_ACCEPTED previous-worker', complete)
                self.assertIn('TAKEOVER_COMPLETE', complete)
                self.assertEqual((payload['model'], payload['reasoning_effort']), ('gpt-6-luna', 'high'))
                self.assertEqual(set(payload), {'message', 'task_name', 'fork_turns', 'model', 'reasoning_effort'})
                self.assertIn(f'scoville_role={role}', complete.splitlines())
                self.assertTrue(payload['task_name'].startswith(f'scoville_{role}_1_'))
                direct = self.run_cli(package, 'build_dispatch_prompt.py', *arguments,
                    '--format', 'prompt', raw=True)
                label = next(line for line in payload['message'].splitlines() if line.startswith('Assignment: '))
                self.assertEqual(complete, direct.stdout + '\n' + label + '\n')

    def test_recovery_assignment_rejects_invalid_format_and_collision(self):
        self.profile()
        handoff = self.project / 'handoff.txt'
        handoff.write_text('Initial effects are checked. Only document review remains.', encoding='utf-8')
        facts = self.project / 'facts.txt'
        facts.write_text('Review the checked document only. No external work.', encoding='utf-8')
        for number, package in enumerate(packages('scoville-workflow-for-codex')):
            assignment = self.base / f'recovery-{number}.txt'
            arguments = ['--role', 'reviewer', '--project-root', self.project,
                '--unit', 'W-001/step-1', '--manager-agent-id', 'manager', '--project-name', 'Recovery',
                '--worker-number', '1', '--model', 'gpt-6-luna', '--thinking', 'high',
                '--context-handoff', handoff, '--supplemental-context', facts,
                '--predecessor-agent-id', 'previous-worker', '--assignment-file', assignment]
            failed = self.run_cli(package, 'build_dispatch_prompt.py', *arguments,
                '--format', 'prompt', ok=False, raw=True)
            self.assertEqual(failed.stdout, '')
            self.assertIn('--format create', failed.stderr)
            self.assertFalse(assignment.exists())
            payload = self.run_cli(package, 'build_dispatch_prompt.py', *arguments, '--format', 'create')
            self.assertIn(str(assignment), payload['message'])
            retained = assignment.read_bytes()
            collision = self.run_cli(package, 'build_dispatch_prompt.py', *arguments,
                '--format', 'create', ok=False, raw=True)
            self.assertEqual(collision.stdout, '')
            self.assertIn('--assignment-file', collision.stderr)
            self.assertEqual(assignment.read_bytes(), retained)

    def test_fresh_review_rejects_missing_and_blank_context_before_publication(self):
        self.profile()
        result = self.project / 'checked-result.txt'
        result.write_text('completed: initial fixture change checked.', encoding='utf-8')
        facts = self.project / 'review-facts.txt'
        assignment = self.base / 'fresh-review.txt'
        for package in packages('scoville-workflow-for-codex'):
            args = ['--role', 'reviewer', '--project-root', self.project,
                '--unit', 'W-001/step-1', '--manager-agent-id', 'manager', '--format', 'create',
                '--project-name', 'Review', '--worker-number', '1', '--model', 'gpt-6-luna',
                '--thinking', 'high', '--executor-result', result, '--assignment-file', assignment]
            for content in (None, '', ' \n\t'):
                extra = []
                if content is not None:
                    facts.write_text(content, encoding='utf-8')
                    extra = ['--supplemental-context', facts]
                failed = self.run_cli(package, 'build_dispatch_prompt.py', *args, *extra, ok=False, raw=True)
                self.assertEqual(failed.stdout, '')
                self.assertIn('--supplemental-context', failed.stderr)
                self.assertIn('review boundary', failed.stderr)
                self.assertFalse(assignment.exists())
            facts.write_text('Initial review of the completed W-001/step-1 change against its Acceptance. No earlier assessments.', encoding='utf-8')
            payload = self.run_cli(package, 'build_dispatch_prompt.py', *args, '--supplemental-context', facts)
            self.assertIn(str(assignment), payload['message'])
            self.assertIn(facts.read_text(encoding='utf-8'), assignment.read_text(encoding='utf-8'))
            assignment.unlink()

    def test_automatic_assignments_are_complete_unique_external_files(self):
        self.profile()
        temporary = self.base / "Research and Development before tests ü ' $()"
        temporary.mkdir()
        environment = dict(os.environ, TMPDIR=str(temporary), TEMP=str(temporary), TMP=str(temporary))
        request = self.project / 'automatic-request.txt'
        request.write_text(QUESTION, encoding='utf-8', newline='\n')
        result = self.project / 'executor-result.txt'
        result.write_text('Completed the assigned fixture only.', encoding='utf-8', newline='\n')
        facts = self.project / 'review-facts.txt'
        facts.write_text('Initial review of W-001/step-1 against its Acceptance. No earlier assessments.', encoding='utf-8')
        paths = []
        for package in packages('scoville-workflow-for-codex'):
            report = self.run_cli(package, 'run_feedback.py', 'create', '--project-root', self.project)['report_file']
            payloads = []
            for role in ('executor', 'reviewer'):
                extra = ['--executor-result', result, '--supplemental-context', facts] if role == 'reviewer' else []
                payloads.append(self.run_cli(package, 'build_dispatch_prompt.py', '--role', role,
                    '--project-root', self.project, '--unit', 'W-001/step-1', '--manager-agent-id', 'manager',
                    '--format', 'create', '--project-name', 'Grüße "quoted" 中文', '--worker-number', '1',
                    '--model', 'gpt-6-luna', '--thinking', 'high', *extra, env=environment))
            common = ['--runner-id', 'runner', '--project-name', 'Grüße 中文', '--manager-number', '1', '--report-file', report]
            start = self.run_cli(package, 'build_manager_handoff.py', '--mode', 'start', *common,
                '--project-root', self.project, '--request-file', request, env=environment)
            payloads.append(start)
            payloads.append(self.run_cli(package, 'build_manager_handoff.py', '--mode', 'successor', *common,
                '--predecessor-id', 'old-manager', '--model', start['model'], '--thinking', start['reasoning_effort'], env=environment))
            for payload in payloads:
                self.assertEqual(set(payload), {'task_name', 'message', 'fork_turns', 'model', 'reasoning_effort'})
                match = re.search(r'assignment from (.+) before any (?:other )?project work', payload['message'])
                self.assertIsNotNone(match, payload['message'])
                path = Path(match[1])
                self.addCleanup(path.unlink, missing_ok=True)
                self.assertTrue(path.is_absolute())
                self.assertFalse(path.resolve().is_relative_to(self.project.resolve()))
                self.assertEqual(path.parent.resolve(), temporary.resolve())
                self.assertNotIn(path, paths)
                paths.append(path)
                content = path.read_bytes().decode('utf-8', errors='strict')
                self.assertTrue(content.endswith('\n'))
                self.assertIn(str(self.project), content)
                self.assertIn('Grüße', content)
                if 'manager assignment from' in payload['message']:
                    self.assertLess(payload['message'].index('START'), payload['message'].index('read the complete'))
                else:
                    self.assertEqual(content.count('## Non-goals'), 1)
                    self.assertNotIn('## Plan-wide exclusions', content)
            original = paths[-1].read_bytes()
            self.run_cli(package, 'build_manager_handoff.py', '--mode', 'start', *common,
                '--project-root', self.project, '--request-file', request, '--assignment-file', paths[-1], ok=False)
            self.assertEqual(paths[-1].read_bytes(), original)

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

    def test_generated_checkpoint_command_reaches_host_shell(self):
        shell = (shutil.which('pwsh') or shutil.which('powershell')) if os.name == 'nt' else shutil.which('sh')
        self.assertIsNotNone(shell, 'The runtime matrix must provide its host shell')
        self.project = self.base / "Project's $value with spaces"
        self.project.mkdir()
        self.profile()
        result_file = self.project / 'result.txt'
        result_file.write_text('completed: assigned fixture checked', encoding='utf-8')
        facts = self.project / 'review-facts.txt'
        facts.write_text('Initial review of the W-001/step-1 fixture change against its Acceptance. No earlier assessments.', encoding='utf-8')
        home = self.base / 'empty-test-home'
        home.mkdir()
        environment = dict(os.environ, CODEX_HOME=str(home), CODEX_THREAD_ID='checkpoint-shell-fixture')
        for package_number, package in enumerate(packages('scoville-workflow-for-codex')):
            for role in ('executor', 'reviewer'):
                extra = ['--executor-result', result_file, '--supplemental-context', facts] if role == 'reviewer' else []
                assignment_file = self.project / f'checkpoint-{package_number}-{role}.txt'
                assignment = self.run_cli(package, 'build_dispatch_prompt.py', '--role', role,
                    '--project-root', self.project, '--unit', 'W-001/step-1',
                    '--manager-agent-id', 'manager', '--format', 'create', '--project-name', 'fixture',
                    '--worker-number', '1', '--model', 'gpt-6-luna', '--thinking', 'high',
                    '--assignment-file', assignment_file, *extra)
                self.assertIn(str(assignment_file), assignment['message'])
                commands = [line for line in assignment_file.read_text(encoding='utf-8').splitlines() if 'check_context_checkpoint.py' in line]
                self.assertEqual(len(commands), 1)
                invocation = ([shell, '-NoProfile', '-NonInteractive', '-Command', commands[0]]
                              if os.name == 'nt' else [shell, '-c', commands[0]])
                observed = subprocess.run(invocation, cwd=self.project, env=environment,
                    text=True, encoding='utf-8', capture_output=True, timeout=25)
                self.assertEqual(observed.returncode, 0, observed.stdout + observed.stderr)
                checkpoint = json.loads(observed.stdout)
                self.assertEqual(checkpoint['role'], role)
                self.assertEqual(checkpoint['thread_id'], 'checkpoint-shell-fixture')
                self.assertEqual(checkpoint['telemetry'], 'unavailable')
                config = self.project / '.scoville/config.json'
                config.parent.mkdir(exist_ok=True)
                config.write_text(json.dumps({'workflow': {'context': {'worker_percent': 'invalid'}}}), encoding='utf-8')
                invalid = subprocess.run(invocation, cwd=self.project, env=environment,
                    text=True, encoding='utf-8', capture_output=True, timeout=25)
                self.assertNotEqual(invalid.returncode, 0)
                self.assertEqual(json.loads(invalid.stdout)['reason'], 'configuration_invalid')
                config.unlink()

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
                         request={'workflow': {'manager': {'model': 'test-model', 'reasoning': 'high'}},
                                  'ask': {'presets': {'sol': {'name': 'Prüfung 東京 🌶'}}}})
            self.assertTrue(saved['saved'])
            shown = self.run_cli(package, 'setup.py', 'show', '--project-root', self.project)
            workflow = package.parent.parent / 'scoville-workflow-for-codex/scoville-workflow-for-codex'
            consumed = self.run_cli(workflow, 'resolve_model_pair.py', '--show-config', '--project-root', self.project)
            self.assertEqual(consumed['config']['manager'], shown['effective']['workflow']['manager'])
            self.assertEqual(consumed['config']['manager'], {'model': 'test-model', 'reasoning': 'high'})
            ask = package.parent.parent / 'scoville-ask-for-codex/scoville-ask-for-codex'
            advice = self.run_cli(ask, 'ask.py', '--project-root', self.project, '--adviser', 'sol')
            self.assertEqual(advice['config']['advisers'][0]['name'], 'Prüfung 東京 🌶')

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
                # Intended next consumer uses metadata unchanged, verifies and reads the ENTIRE bytes.
                received = retained.read_bytes()
                self.assertEqual(hashlib.sha256(received).hexdigest(), published['sha256'])
                self.assertEqual(received, combined)
                self.assertIn('END REQUIRED Grüße 中文', received.decode('utf-8'))
                again = self.run_cli(package, 'check_text_size.py', '--file', text_file, '--max-output-tokens', 10000, '--publish-full', '--project-root', self.project)
                self.assertEqual(again['full_file'], str(retained))
                # An authenticated transfer may require a file independently of size.
                unmeasured = self.run_cli(package, 'check_text_size.py', '--file', text_file, '--publish-full', '--project-root', self.project)
                self.assertEqual(set(unmeasured), {'status', 'utf8_bytes', 'full_file', 'sha256', 'instruction'})
                self.assertEqual(unmeasured['status'], 'complete_file')
                self.assertEqual(unmeasured['utf8_bytes'], len(combined))
                received = Path(unmeasured['full_file']).read_bytes()
                self.assertEqual(hashlib.sha256(received).hexdigest(), unmeasured['sha256'])
                self.assertEqual(received, combined)
                self.assertFalse(list(retained.parent.glob('tmp*')))

    def test_bounded_utf8_parts_reconstruct_complete_input_and_reject_bad_reads(self):
        source = self.base / 'parts ä →.txt'
        samples = [b'', 'ASCII\r\nä → 😀\r\n' .encode('utf-8'),
                   ('long ' + '😀ä' * 100 + '\nFINAL →\n\n').encode('utf-8')]
        for package in packages('scoville-code'):
            for data in samples:
                source.write_bytes(data)
                for limit in (100, 10000):
                    received = b''
                    part = 1
                    while True:
                        result = subprocess.run([sys.executable, '-X', 'utf8', str(package / 'scripts/check_text_size.py'),
                            '--file', str(source), '--max-output-tokens', str(limit), '--part', str(part)],
                            capture_output=True, timeout=25)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertLessEqual(len(result.stdout) + len(result.stderr), limit * 4 // 5)
                        label, payload = result.stdout.split(b'\n', 1)
                        match = re.fullmatch(rb'part=(\d+) bytes=(\d+):(\d+)/(\d+) (last|next=(\d+))', label)
                        self.assertIsNotNone(match)
                        number, start, end, total = map(int, match.groups()[:4])
                        self.assertEqual((number, start, total), (part, len(received), len(data)))
                        self.assertEqual(end - start, len(payload))
                        payload.decode('utf-8', errors='strict')
                        self.assertTrue(payload or not data)
                        received += payload
                        if end == total:
                            self.assertEqual(match.group(5), b'last')
                            break
                        self.assertEqual(int(match.group(6)), part + 1)
                        part = int(match.group(6))
                    self.assertEqual(received, data)
                    self.assertEqual(source.read_bytes(), data)
            # Tiny budgets, malformed input, out-of-range parts and incompatible
            # modes never emit partial content or publish an input copy.
            for data, limit, extra in [(b'a', 1, []), (b'\xff', 100, []),
                    (b'a', 100, ['--part', '2']), (b'a', 100, ['--part', '0']),
                    (b'a', 100, ['--publish-full', '--project-root', str(self.project)])]:
                source.write_bytes(data)
                result = subprocess.run([sys.executable, str(package / 'scripts/check_text_size.py'),
                    '--file', str(source), '--max-output-tokens', str(limit), '--part', '1', *extra], capture_output=True)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, b'')
                self.assertLessEqual(len(result.stderr), limit * 4 // 5)
                self.assertFalse((self.project / '.scoville/temp').exists())
            source.write_bytes(b'a')
            for limit, expected in ((31, 2), (32, 0)):
                result = subprocess.run([sys.executable, str(package / 'scripts/check_text_size.py'),
                    '--file', str(source), '--max-output-tokens', str(limit), '--part', '1'], capture_output=True)
                self.assertEqual(result.returncode, expected)
                self.assertLessEqual(len(result.stdout) + len(result.stderr), limit * 4 // 5)
                if expected == 0:
                    self.assertEqual(result.stdout, b'part=1 bytes=0:1/1 last\na')
            # The final frame fits, while the longer nonfinal label does not.
            source.write_bytes(b'ab')
            result = subprocess.run([sys.executable, '-X', 'utf8', str(package / 'scripts/check_text_size.py'),
                '--file', str(source), '--max-output-tokens', '33', '--part', '1'], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, b'part=1 bytes=0:2/2 last\nab')
            self.assertEqual(len(result.stdout), 26)

    def test_generated_part_read_and_memory_capture_reach_host_shell(self):
        shells = ([value for name in ('powershell', 'pwsh') if (value := shutil.which(name))]
                  if os.name == 'nt' else [shutil.which('sh')])
        self.assertTrue(shells and all(shells))
        source = self.base / "Required input ü ' $().txt"
        data = ('Required → 😀\r\n' * 20).encode('utf-8')
        source.write_bytes(data)
        package = next(packages('scoville-workflow-for-codex'))
        spec = importlib.util.spec_from_file_location('case_native_arguments', package / 'scripts/native_task_arguments.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        instruction = module.file_read_instruction(source, package / 'scripts/check_text_size.py', sys.executable)
        prefix = '& {' if os.name == 'nt' else shlex.quote(sys.executable)
        command = instruction[instruction.index(prefix):].splitlines()[0].replace('<limit>', '100')
        producer = self.base / 'producer.py'
        producer.write_text("import sys\nsys.stdout.buffer.write('Grüße → 😀\\n\\n'.encode('utf-8'))\nsys.stderr.buffer.write('Fehler ä\\n\\n'.encode('utf-8'))\nsys.exit(7)\n", encoding='utf-8')
        out, err = 'Grüße → 😀\n\n'.encode('utf-8'), 'Fehler ä\n\n'.encode('utf-8')
        expected = f'exit=7 stdout_bytes={len(out)} stderr_bytes={len(err)}\n'.encode('ascii') + b'stdout:\n' + out + b'\nstderr:\n' + err
        for shell in shells:
            flags = ['-NoProfile', '-NonInteractive', '-Command'] if os.name == 'nt' else ['-c']
            read = subprocess.run([shell, *flags, command], capture_output=True, timeout=25)
            self.assertEqual(read.returncode, 0, read.stderr)
            label, body = read.stdout.split(b'\n', 1)
            self.assertRegex(label, rb' next=2$')
            self.assertLessEqual(len(read.stdout) + len(read.stderr), 80)
            self.assertEqual(body, data[:len(body)])
            body.decode('utf-8', errors='strict')
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
        self.assertEqual(hashlib.sha256(received).hexdigest(), meta['sha256'])
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

    def test_startup_location_reaches_status_consumer_with_complete_arguments(self):
        for package in packages('scoville-workflow-for-codex'):
            bad = self.run_cli(package, 'run_feedback.py', 'status', '--kind', 'blocked',
                '--project', 'Unicode ä →', '--plan', 'PLAN-0001', '--point', 'Startup',
                '--text', 'Interpreter unavailable; waiting for setup.', ok=False, raw=True)
            self.assertEqual(bad.stdout, '')
            good = self.run_cli(package, 'run_feedback.py', 'status', '--kind', 'blocked',
                '--project', 'Unicode ä →', '--text', 'Interpreter unavailable; waiting for setup.')
            self.assertIn('Startup', good['text'])
            self.assertIn('Interpreter unavailable', good['message'])

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
        self.assertEqual(hashlib.sha256(received).hexdigest(), corrected_publication['sha256'])
        digest = hashlib.sha256(missing.read_bytes()).hexdigest()
        target = self.project / '.scoville/temp' / (digest + '.txt')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b'existing content must survive')
        rejected = self.run_cli(package, 'check_text_size.py', '--file', missing, '--max-output-tokens', 10000, '--publish-full', '--project-root', self.project, ok=False, raw=True)
        self.assertEqual(rejected.stdout, '')
        self.assertIn(str(target), rejected.stderr)
        self.assertEqual(target.read_bytes(), b'existing content must survive')
        self.assertFalse(list(target.parent.glob('tmp*')))
        safe = self.base / 'corrected project Ä 中文'
        safe.mkdir()
        corrected = self.run_cli(package, 'check_text_size.py', '--file', missing,
                                 '--publish-full', '--project-root', safe)
        received = Path(corrected['full_file']).read_bytes()
        self.assertEqual(received, missing.read_bytes())
        self.assertEqual(hashlib.sha256(received).hexdigest(), corrected['sha256'])
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
        self.assertEqual(hashlib.sha256(received).hexdigest(), corrected['sha256'])
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
