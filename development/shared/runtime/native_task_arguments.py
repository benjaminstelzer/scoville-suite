"""Build native creation arguments; no transport, configuration or lifecycle state."""
from __future__ import annotations

import re


EFFORTS = ('none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra')


def takeover_instruction(predecessor: str, manager: str) -> str:
    single_line(predecessor, '--predecessor-agent-id')
    single_line(manager, '--manager-agent-id')
    if predecessor == manager:
        raise ValueError('--predecessor-agent-id must identify the prior child, not --manager-agent-id')
    return (
        'FIRST ACTION: retain the supplied continuation information. If an essential fact '
        'is missing, report it to the manager before project work. Otherwise call '
        f'send_message with target={manager} and message=HANDOFF_ACCEPTED {predecessor}. '
        'The manager owns the retained handoff and completed predecessor. Never send a '
        'routine receipt to that predecessor. After delivery, wait actively with wait_agent '
        'for TAKEOVER_COMPLETE from that exact manager, at most 60 seconds. Do no project '
        'work before this release. A failed send, missing release or user stop blocks '
        'takeover with its diagnostic. After verified release, continue the remaining '
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


def creation_arguments(prompt: str, task_name: str, model: str, thinking: str) -> dict:
    if not prompt.strip():
        raise ValueError('the assignment must be nonempty')
    if not re.fullmatch(r'[a-z0-9_]+', task_name):
        raise ValueError('task_name must use lowercase letters, digits and underscores')
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
                         '; supply the project name, role number and resolved model/effort')
