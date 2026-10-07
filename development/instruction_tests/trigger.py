"""Prepare a Codex trigger command or inspect its JSONL read evidence. Never launches it."""
import argparse
import json
from pathlib import Path
import shlex
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'luna-tests'))
from run_codex_cli_case import DISABLED_FEATURES


def read_command_tokens(command_text):
    """Recognize direct reads and one explicit PowerShell -Command wrapper.

    Keep Windows backslashes literal. Complex scripts remain unverified.
    """
    def split(text):
        return [token[1:-1] if len(token) >= 2 and token[0] == token[-1] and token[0] in "\"'" else token
                for token in shlex.split(text, posix=False)]
    tokens = split(command_text)
    if tokens and tokens[0].replace('\\', '/').rsplit('/', 1)[-1].lower() in ('pwsh', 'pwsh.exe', 'powershell', 'powershell.exe'):
        options = [t.lower() for t in tokens]
        if '-command' not in options:
            return []
        at = options.index('-command')
        if any(t not in ('-noprofile', '-nologo', '-noninteractive') for t in options[1:at]) or len(tokens) != at + 2:
            return []
        return split(tokens[-1])
    return tokens


def command(codex, workspace, thread_id=None):
    argv = [str(codex), '--ask-for-approval', 'never', '--model', 'gpt-6-luna']
    settings = ['sandbox_mode="read-only"', 'model_reasoning_effort="high"',
                'mcp_servers={}', 'web_search="disabled"', 'features.code_mode=false',
                'features.skip_host_skill_discovery=false', 'skills.include_instructions=true']
    for setting in settings:
        argv.extend(['-c', setting])
    for feature in DISABLED_FEATURES:
        if feature not in ('shell_tool', 'skill_search', 'unified_exec'):
            argv.extend(['--disable', feature])
    argv += ['--enable', 'shell_tool', '--enable', 'skill_search', 'exec']
    if thread_id:
        argv += ['resume']
    argv += ['--ignore-user-config', '--ignore-rules', '--strict-config', '--skip-git-repo-check', '--json']
    return argv + ([thread_id, '-'] if thread_id else ['-C', str(workspace), '-'])


def observe(events, skills):
    """Full byte-equivalent text in a successful shell result is a positive read signal.

    This deliberately does not infer a negative activation verdict or validate
    semantic use. Truncated/alternative reads require a qualified host observer.
    """
    seen, evidence = set(), []
    started = completed = False
    for event in events:
        kind = event.get('type')
        if kind == 'turn.started':
            if started:
                raise ValueError('supply only the scored target turn, excluding prelude/resume turns')
            started = True
        elif kind == 'turn.completed':
            completed = True
        elif kind in ('turn.failed', 'error'):
            return {'transport': 'FAIL', 'activation': 'UNVERIFIED', 'observed_reads': []}
        elif kind == 'item.completed' and started and not completed:
            item = event.get('item', {})
            if item.get('type') == 'command_execution' and item.get('exit_code') == 0:
                output = item.get('aggregated_output', '').replace('\r\n', '\n')
                try:
                    tokens = read_command_tokens(item.get('command', ''))
                except ValueError:
                    tokens = []
                operands = [t for t in tokens[1:] if t not in ('-Raw', '-LiteralPath', '-Path', '--')]
                for name, path in skills.items():
                    text = path.read_text(encoding='utf-8').replace('\r\n', '\n')
                    literal_read = (tokens and tokens[0] in ('Get-Content', 'cat', 'type')
                                    and len(operands) == 1 and Path(operands[0]).is_absolute()
                                    and Path(operands[0]).resolve() == path.resolve())
                    if literal_read and text and text in output:
                        seen.add(name)
                        evidence.append({'skill': name, 'item_id': item.get('id'), 'signal': 'full_skill_text_in_successful_command_output'})
    return {'transport': 'PASS' if started and completed else 'FAIL',
            'activation': 'UNVERIFIED', 'observed_reads': sorted(seen), 'evidence': evidence,
            'limit': 'Positive read signals only. Native discovery, hidden loads, prelude reads and absence of activation require host qualification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='mode', required=True)
    prepare = commands.add_parser('command')
    prepare.add_argument('--codex', type=Path, required=True)
    prepare.add_argument('--prepared', type=Path, required=True)
    prepare.add_argument('--private-prepared', type=Path, required=True)
    prepare.add_argument('--thread-id')
    observe_parser = commands.add_parser('observe')
    observe_parser.add_argument('--events', type=Path, required=True)
    observe_parser.add_argument('--skills-root', type=Path, required=True, help='Isolated root containing <member>/<member>/SKILL.md')
    args = parser.parse_args()
    try:
        if args.mode == 'command':
            meta = json.loads((args.private_prepared / 'preparation.json').read_text(encoding='utf-8'))
            if meta['type'] != 'trigger':
                raise ValueError('--prepared must contain a trigger case')
            if meta['requested_model'] != 'gpt-6-luna':
                raise ValueError('Claude trigger route is unverified; this command prepares only Codex/Luna')
            result = {'argv': command(args.codex, args.prepared / 'workspace', args.thread_id),
                      'cwd': str(args.prepared / 'workspace'), 'environment_overrides': meta['host_environment'],
                      'stdin_file': str(args.prepared / 'prompt.txt'), 'launch_allowed': False,
                      'limit': 'Preparation only. Qualify OS read isolation and host discovery before any launch; count its attempt in the shared register.'}
        else:
            skills = {p.parent.name: p for p in args.skills_root.glob('*/*/SKILL.md')}
            if not skills:
                raise ValueError('--skills-root must contain verified <member>/<member>/SKILL.md files')
            events = [json.loads(line) for line in args.events.read_text(encoding='utf-8').splitlines()]
            result = observe(events, skills)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(3, f'trigger preparation failed: {error}. See command --help or observe --help.\n')
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
