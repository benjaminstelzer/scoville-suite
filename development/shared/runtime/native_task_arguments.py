"""Build native creation arguments; no transport, configuration or lifecycle state."""
from __future__ import annotations

import re


EFFORTS = ('none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra')


def takeover_instruction(predecessor: str) -> str:
    single_line(predecessor, 'predecessor thread ID')
    return (
        'FIRST ACTION — once the required continuation information is retained, before '
        'ordinary Skill/Plan/source reading or project work, call '
        f'send_message_to_thread with threadId={predecessor} and this exact prompt:\n'
        'I have the information. You can archive yourself now. Call set_thread_archived '
        'with archived=true for your own chat as your last action.\n'
        'The supplied handoff normally provides that information. If an essential fact '
        'is missing, recover only that fact first; do not begin the work. Then send this '
        'notice before ordinary reading or implementation. A reply in your own chat is not delivery. '
        'If the host forbids the send or the tool fails, report the concrete limitation '
        'and stop this takeover; do not silently skip the notice. After a successful send, '
        'continue below without waiting for archival.\n\n')


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


def creation_arguments(prompt: str, title: str, project_id: str,
                       model: str, thinking: str) -> dict:
    if not prompt.strip():
        raise ValueError('the assignment must be nonempty')
    if thinking not in EFFORTS:
        raise ValueError('thinking must be one of: ' + ', '.join(EFFORTS))
    return {'prompt': prompt, 'title': single_line(title, 'title'),
            'model': single_line(model, 'model'), 'thinking': thinking,
            'target': {'type': 'project', 'projectId': single_line(project_id, 'project ID'),
                       'environment': {'type': 'local'}}}


def add_creation_options(parser, *, project_name=True) -> None:
    parser.add_argument('--format', choices=('prompt', 'create'), default='prompt')
    parser.add_argument('--project-id')
    if project_name:
        parser.add_argument('--project-name')
    parser.add_argument('--model')
    parser.add_argument('--thinking', choices=EFFORTS)


def validate_creation_options(args) -> None:
    if args.format != 'create':
        native = ('project_id', 'project_name', 'model', 'thinking', 'worker_number', 'caller_title', 'adviser_id')
        supplied = ['--' + name.replace('_', '-') for name in native if getattr(args, name, None) is not None]
        if supplied:
            raise ValueError('use --format create with native creation arguments: ' + ', '.join(supplied))
        return
    required = ('project_id', 'model', 'thinking') + (('project_name',) if hasattr(args, 'project_name') else ())
    missing = ['--' + name.replace('_', '-') for name in required if not getattr(args, name)]
    if missing:
        raise ValueError('--format create requires ' + ', '.join(missing) +
                         '; supply the saved project and the resolved model/effort')
