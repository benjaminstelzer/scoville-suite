"""Build native creation arguments; no transport, configuration or lifecycle state."""
from __future__ import annotations

import re
import json
import shlex
import subprocess
import os
import tempfile
from pathlib import Path
from uuid import uuid4


EFFORTS = ('none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra')


def takeover_instruction(predecessor: str, manager: str) -> str:
    single_line(predecessor, '--predecessor-agent-id')
    single_line(manager, '--manager-agent-id')
    if predecessor == manager:
        raise ValueError('--predecessor-agent-id must identify the prior child, not --manager-agent-id')
    return (
        'FIRST ACTION: retain the supplied continuation information. If an essential fact '
        'is missing, report it to the manager before project work. Otherwise call '
        f'collaboration.send_message with target={manager} and message=HANDOFF_ACCEPTED {predecessor}. '
        'Use native collaboration agent handles, not chat or thread messaging. '
        'The manager owns the retained handoff and completed predecessor. Never send a '
        'routine receipt to that predecessor. After delivery, use bounded collaboration.wait_agent '
        'calls until TAKEOVER_COMPLETE arrives from that exact manager. A wait timeout '
        'alone does not end the wait or permit project work. Do no project work before '
        'this release. A failed send, STOP or BLOCKED halts takeover with its diagnostic. '
        'If a mismatch, uncertain state, user stop or unanswered decision prevents '
        'release, the manager sends STOP for a stop, or BLOCKED otherwise, to you. '
        'Accept either signal only from that exact manager. Remain write-inactive '
        'and return a blocked result with the signal and reason to the manager; '
        'do not keep waiting after that signal. '
        'After verified release, continue the remaining '
        'assignment. The predecessor stays write-inactive; no archival or close tool '
        'is required.\n\n')


def single_line(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip() or any(c in value for c in '\r\n'):
        raise ValueError(f'{name} must be nonempty single-line text')
    return value


def workflow_title(project_name: str, role: str, number: int, identity: str) -> str:
    labels = {'coordinator': 'SC-MGR', 'executor': 'SC-WRK', 'reviewer': 'SC-REV'}
    if role not in labels or type(number) is not int or number < 1:
        raise ValueError('supply an existing role and a positive role number')
    unit = r'W-[0-9]{3}(?:/step-[1-9][0-9]*|/steps-([1-9][0-9]*)-([1-9][0-9]*))?'
    pattern = r'PLAN-[0-9]{4}(?:/' + unit + (')?' if role == 'coordinator' else ')')
    match = re.fullmatch(pattern, identity)
    if not match or (match[1] and int(match[1]) >= int(match[2])):
        raise ValueError('use PLAN-NNNN for a manager or PLAN-NNNN/W-NNN[/step-N or /steps-N-M] with an ascending range')
    return f'{labels[role]}-{number}: {single_line(project_name, "project name")} · {identity}'


def unique_task_name(base: str) -> str:
    if not re.fullmatch(r'[a-z0-9_]+', base):
        raise ValueError('task_name must use lowercase letters, digits and underscores')
    return f'{base}_{uuid4().hex}'


def creation_arguments(prompt: str, task_name: str, model: str, thinking: str) -> dict:
    if not prompt.strip():
        raise ValueError('the assignment must be nonempty')
    task_name = unique_task_name(task_name)
    if thinking not in EFFORTS:
        raise ValueError('thinking must be one of: ' + ', '.join(EFFORTS))
    return {'message': prompt, 'task_name': task_name, 'fork_turns': 'none',
            'model': single_line(model, '--model'), 'reasoning_effort': thinking}


def add_creation_options(parser) -> None:
    parser.add_argument('--format', choices=('prompt', 'create'), default='prompt')
    parser.add_argument('--project-name')
    parser.add_argument('--model')
    parser.add_argument('--thinking', choices=EFFORTS)


def validate_creation_options(args) -> None:
    native = ('project_name', 'model', 'thinking', 'worker_number')
    if args.format != 'create':
        supplied = ['--' + name.replace('_', '-') for name in native if getattr(args, name, None) is not None]
        if supplied:
            raise ValueError('use --format create with native creation arguments: ' + ', '.join(supplied))
        return
    missing = ['--' + name.replace('_', '-') for name in native if getattr(args, name, None) is None]
    if missing:
        raise ValueError('--format create requires ' + ', '.join(missing) +
                         '; supply the project name, role number, resolved model and reasoning effort')


def assignment_path(explicit: Path | None, project_root: Path) -> Path:
    """Choose an external platform temp path; explicit paths keep their contract."""
    if explicit is None:
        folder = Path(tempfile.gettempdir()).resolve()
        if folder.is_relative_to(project_root.resolve()):
            raise ValueError('system temporary directory is inside --project-root; supply '
                             '--assignment-file "<new-absolute-file>" in a readable temporary directory outside the project')
        target = folder / ('scoville-assignment-' + uuid4().hex + '.txt')
    else:
        target = explicit
    if not target.is_absolute() or not target.parent.is_dir():
        raise ValueError('--assignment-file must name a new file in an existing absolute directory; '
                         'use --assignment-file "<existing-temp-directory>/<new-name>.txt" or omit it for automatic selection')
    if target.exists() or target.is_symlink():
        raise ValueError('--assignment-file already exists; use a new unique path without overwriting an assignment')
    return target


def publish_assignment(target: Path, text: str) -> None:
    """Publish complete UTF-8 bytes atomically without replacing another file."""
    data = text.encode('utf-8', errors='strict')
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent, prefix='.scoville-assignment-',
                                         suffix='.tmp', delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
        # Both files use the same filesystem. link is atomic and fails if target exists.
        os.link(temporary, target)
    except FileExistsError as error:
        raise ValueError('--assignment-file already exists; use a new unique path without overwriting an assignment') from error
    except OSError as error:
        raise ValueError(f'cannot publish --assignment-file {target}: {error}; supply '
                         '--assignment-file "<new-absolute-file>" in a readable writable temporary directory '
                         'supporting atomic hard links; do not bypass the consumer sandbox') from error
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def shell_command(arguments: list[str]) -> str:
    """Quote an unchanged argv for PowerShell on Windows or a POSIX shell."""
    if os.name == 'nt':
        # ProcessStartInfo bypasses PowerShell's version-dependent native argv
        # conversion (Legacy drops empty strings and consumes literal quotes).
        quote = lambda value: "'" + value.replace("'", "''") + "'"
        return ("& { $scovilleProcess = New-Object System.Diagnostics.ProcessStartInfo; "
                "$scovilleProcess.FileName = " + quote(arguments[0]) + "; "
                "$scovilleProcess.Arguments = " + quote(subprocess.list2cmdline(arguments[1:])) + "; "
                "$scovilleProcess.UseShellExecute = $false; "
                "$scovilleChild = [System.Diagnostics.Process]::Start($scovilleProcess); "
                "$scovilleChild.WaitForExit(); "
                "if ($scovilleChild.ExitCode -ne 0) { exit $scovilleChild.ExitCode } }")
    return shlex.join(arguments)


def budget_retry(diagnostic: str, arguments: list[str]) -> str:
    """Suggest a complete corrected invocation, never raise the caller's budget."""
    try:
        payload = json.loads(diagnostic)
    except (ValueError, TypeError):
        return ''
    if not isinstance(payload, dict):
        return ''
    diagnostics = payload.get('diagnostics')
    if not isinstance(diagnostics, list):
        return ''
    for entry in diagnostics:
        if not isinstance(entry, dict) or entry.get('code') != 'OUTPUT_BUDGET_EXCEEDED':
            continue
        observed = entry.get('observed')
        required = observed.get('required_bytes') if isinstance(observed, dict) else None
        if type(required) is not int or required < 1:
            return ''
        corrected = []
        skip = False
        for value in arguments:
            if skip:
                skip = False
            elif value == '--max-output-bytes':
                skip = True
            elif not value.startswith('--max-output-bytes='):
                corrected.append(value)
        corrected.extend(['--max-output-bytes', str(required)])
        return ('\nCorrected invocation (run only within the caller-approved budget; '
                'otherwise request a decision):\n' + shell_command(corrected))
    return ''
