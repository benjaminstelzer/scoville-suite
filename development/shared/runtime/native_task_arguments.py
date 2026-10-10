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


def single_line(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip() or any(c in value for c in '\r\n'):
        raise ValueError(f'{name} must be nonempty single-line text')
    return value


def workflow_title(project_name: str, role: str, number: int, identity: str) -> str:
    labels = {'executor': 'SC-WRK', 'reviewer': 'SC-REV', 'explorer': 'SC-EXP'}
    if role not in labels or type(number) is not int or number < 1:
        raise ValueError('supply an existing role and a positive role number')
    unit = r'W-[0-9]{3}(?:/step-[1-9][0-9]*|/steps-([1-9][0-9]*)-([1-9][0-9]*))?'
    pattern = r'PLAN-[0-9]{4}/' + unit
    if role == 'explorer' and identity == 'question':
        return f'{labels[role]}-{number}: {single_line(project_name, "project name")} · question'
    match = re.fullmatch(pattern, identity)
    if not match or (match[1] and int(match[1]) >= int(match[2])):
        raise ValueError('use PLAN-NNNN/W-NNN[/step-N or /steps-N-M] with an ascending range')
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
        return ("& { $ErrorActionPreference = 'Stop'; try { "
                "$scovilleProcess = New-Object System.Diagnostics.ProcessStartInfo; "
                "$scovilleProcess.FileName = " + quote(arguments[0]) + "; "
                "$scovilleProcess.Arguments = " + quote(subprocess.list2cmdline(arguments[1:])) + "; "
                "$scovilleProcess.UseShellExecute = $false; "
                "$scovilleChild = [System.Diagnostics.Process]::Start($scovilleProcess); "
                "if ($null -eq $scovilleChild) { throw 'Process.Start returned no process' }; "
                "$scovilleChild.WaitForExit() "
                "} catch { $scovilleDiagnostic = [Text.Encoding]::UTF8.GetBytes('Process start or wait failed for ' + "
                + quote(arguments[0]) + " + ': ' + $_.Exception.ToString() + [Environment]::NewLine); "
                "$scovilleError = [Console]::OpenStandardError(); "
                "$scovilleError.Write($scovilleDiagnostic, 0, $scovilleDiagnostic.Length); "
                "$scovilleError.Flush(); exit 125 }; "
                "if ($scovilleChild.ExitCode -ne 0) { exit $scovilleChild.ExitCode } }")
    return shlex.join(arguments)


def file_read_command(target: Path, checker: Path, interpreter: str) -> str:
    """Prepare the complete argv for one document without rebuilding shell quoting."""
    return shell_command([interpreter, '-X', 'utf8', str(checker), '--file', str(target),
                          '--max-output-tokens', '<limit>', '--part', '1'])


def file_read_instruction(target: Path, checker: Path, interpreter: str) -> str:
    """Prepare a complete bounded UTF-8 read for file-backed native assignments."""
    if not checker.is_file():
        raise ValueError(f'bundled text-size checker is missing at {checker}; use the intact matching package before assigning work')
    command = file_read_command(target, checker, interpreter)
    return (
        f'Python runs {checker} after -X utf8. The checker reads every document only through --file, '
        'including SKILL.md files and references of any Skill, assignments, and .py files read as text. '
        'Keep the verified launcher, checker path and quoting unchanged.\n\n'
        'Use separate outer tool calls unless their complete combined output has '
        'been measured and fits; a script joining reads returns one combined output.\n\n'
        '1. Replace '
        '<limit> with the smallest declared or explicitly selected output limit '
        'of the command and every enclosing tool output.\n'
        '2. Reader command: copy the whole command into the current tool shell. '
        'For the next part, copy the last correct complete command and change only --part to the reported next value. '
        'Do not nest another shell:\n\n```text\n'
        + command + '\n```\n\n'
        '3. Read the unchanged file bytes and part=N bytes=start:end/total next=M label. '
        'Follow next=M with --part M; last marks end equal to total. Read every part through last in order '
        'before dependent work. Use one limit for the whole sequence. If an applicable limit changes, '
        'restart at part 1 with the new smallest limit; never raise a binding limit to keep the old sequence. '
        'Each invocation includes its label in the byte budget.\n\n'
        'For another document, change only the --file value and reset --part to 1. '
        'Preserve the generated shell quoting and all other arguments. '
        + ('In the Windows command, double any apostrophe inside its single-quoted PowerShell strings. '
           'Put a replacement --file value containing spaces in double quotes inside the Arguments string. '
           if os.name == 'nt' else '')
        + '\n\nFailure: a nonzero exit leaves this read incomplete, even with an empty diagnostic '
        'when the declared budget cannot fit it. Correct a visible cause and restart at part 1. '
        'Do not repeat an unchanged failed call or raise a binding limit. Otherwise report the unread '
        'document and stop dependent work. Do not alter or copy the input. '
        'Never truncate, skip text or start with an oversized full read. The named '
        'read and size-check commands are permitted even for external assignment, '
        'interpreter and checker paths; this grants no unrelated inspection or writes. '
    )


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
        return ('\nCorrected invocation (one effect-free input correction only):\n' + shell_command(corrected)
                + '\nThis is an internal selection budget, not the tool display limit. '
                  'An agent-chosen budget may be explicitly corrected to the required size. '
                  'A binding user, Plan or host cap still requires a decision if exceeded. '
                  'Never raise it automatically or display unchecked output.')
    return ''
