#!/usr/bin/env python3
"""Pure native-task payload checks. No host calls, retries or permission grants.

Read one JSON request from stdin and print one JSON result. The caller retains
the returned handle in its existing record before performing the next action.
Host replies must be the actual decoded tool payload, not invented summaries.
"""
from __future__ import annotations

import json
import re
import sys


def require(value, message):
    if not value:
        raise ValueError(message)


def text(value, name):
    require(isinstance(value, str) and bool(value.strip()), name + ' must be nonempty text')
    return value


def ready(handle):
    require(handle.get('state') == 'ready', 'pending or unknown handle is not usable')
    thread = text(handle.get('threadId'), 'threadId')
    require(thread != handle.get('clientThreadId'), 'clientThreadId is not a ready ID')
    return thread


def task_title(request):
    """Format new-task labels only; never rename or identify an existing task."""
    def label(key, maximum):
        value = text(request.get(key), key)
        require(value == value.strip() and len(value) <= maximum
                and not any(ord(c) < 32 or c in '[]' for c in value),
                key + ' exceeds its limit or contains controls/brackets')
        return value

    def number(key):
        value = request.get(key)
        require(type(value) is int and value >= 1, key + ' must be a positive integer')
        return value

    family, role = request.get('family'), request.get('role')
    if family == 'workflow':
        roles = {'coordinator': 'MNGR', 'executor': 'WORK', 'reviewer': 'REVW', 'repair': 'FIXR'}
        require(role in roles, 'invalid workflow title role')
        title_key = 'plan_id' if role == 'coordinator' else 'unit'
        title = text(request.get(title_key), title_key)
        pattern = r'PLAN-[0-9]{4}' if role == 'coordinator' else r'W-[0-9]{3}(?:/step-[1-9][0-9]*)?'
        require(re.fullmatch(pattern, title) is not None, title_key + ' has invalid ID format')
        return {'title': f'S-{roles[role]}-#{number("run_number")}-{title.upper()}'}
    elif family == 'ask':
        require(role == 'adviser', 'invalid Ask title role')
        if 'caller_title' in request:
            caller_title = text(request['caller_title'], 'caller_title')
            require(not any(ord(c) < 32 for c in caller_title), 'caller_title contains controls')
            model = label('model', 128)
            return {'title': f'Ask {model} · {caller_title}'}
        title = f'ASK {label("subject", 80)} {label("adviser", 32)} RUN [#{number("attempt")}]'
    else:
        raise ValueError('unknown title family')
    require(len(title) <= 160, 'title exceeds helper limit of 160 characters')
    return {'title': title}


def create(request):
    require(request.get('creation_authorized') is True, 'task creation needs existing authority')
    require(request.get('prior_state') == 'not_started', 'reconcile prior creation; do not duplicate it')
    family = request.get('family')
    role = request.get('role')
    require(family in {'workflow', 'ask'}, 'unknown family')
    require(role in ({'coordinator', 'executor', 'reviewer', 'repair'} if family == 'workflow' else {'adviser'}), 'invalid role')
    prompt = text(request.get('prompt'), 'prompt')
    if family == 'workflow':
        require(prompt.startswith('scoville_role=' + role + '\n'), 'workflow role must start at byte zero')
    project = text(request.get('projectId'), 'projectId')
    title = task_title(request)['title']
    if 'title' in request:
        require(request['title'] == title, 'supplied title differs from generated title')
    reference = text(request.get('reference'), 'reference')
    if family == 'workflow':
        first, rest = prompt.split('\n', 1)
        prompt = first + '\nworkflow_reference=' + reference + '\n' + rest
    prior_ids = request.get('prior_task_ids', [])
    require(isinstance(prior_ids, list) and all(isinstance(i, str) and i for i in prior_ids),
            'prior_task_ids must contain known predecessor task IDs')
    if family == 'ask':
        destination = text(request.get('return_to_thread_id'), 'return_to_thread_id')
        prompt = ('ask_role=adviser\nconsultation_reference=' + reference
                  + '\nreturn_to_thread_id=' + destination + '\n' + prompt)
    require(request.get('thinking') in {'none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra'}, 'invalid host effort')
    args = {'target': {'type': 'project', 'projectId': project, 'environment': {'type': 'local'}},
            'prompt': prompt, 'title': title,
            'model': text(request.get('model'), 'model'),
            'thinking': text(request.get('thinking'), 'thinking')}
    return {'arguments': args, 'handle': {'state': 'creation_unknown', 'family': family,
            'role': role, 'projectId': project, 'title': title, 'reference': reference,
            **({'reference_identity_required': True} if family == 'workflow' or 'caller_title' in request else {}),
            'prior_task_ids': prior_ids}}


def creation_result(request):
    handle = dict(request['handle'])
    require(handle.get('state') == 'creation_unknown', 'creation reply already consumed')
    reply = request['reply']
    require(isinstance(reply, dict), 'reply must be an object')
    require(reply.get('isError') is not True, 'creation failed; preserve unknown handle and reconcile')
    if reply.get('threadId'):
        thread = text(reply['threadId'], 'threadId')
        require(thread != reply.get('clientThreadId'), 'provisional ID cannot become ready by relabeling')
        handle.update(state='ready', threadId=thread, hostId=text(reply.get('hostId'), 'hostId'))
    elif reply.get('clientThreadId'):
        handle.update(state='pending', clientThreadId=text(reply['clientThreadId'], 'clientThreadId'))
    # Missing or ambiguous transport results deliberately stay unknown.
    return {'handle': handle, 'may_create_again': False}


def reconcile(request):
    handle = dict(request['handle'])
    require(handle.get('state') in {'pending', 'creation_unknown'}, 'only unresolved creation can reconcile')
    candidates = [entry for entry in request['entries']
                  if entry.get('kind') == 'codex'
                  and (not handle.get('reference_identity_required')
                       or entry.get('workflow_reference' if handle.get('family') == 'workflow' else 'consultation_reference') == handle['reference'])
                  and entry.get('id') not in handle.get('prior_task_ids', [])
                  and entry.get('projectId') == handle['projectId'] and entry.get('title') == handle['title']]
    require(len(candidates) <= 1, 'multiple exact matches; identity is ambiguous')
    if candidates:
        entry = candidates[0]
        thread = text(entry.get('id'), 'list entry id')
        require(thread != handle.get('clientThreadId'), 'pending ID is not ready')
        handle.update(state='ready', threadId=thread, hostId=text(entry.get('hostId'), 'hostId'))
    return {'handle': handle, 'may_create_again': False}


def message(request):
    handle = request['handle']
    args = {'threadId': ready(handle), 'hostId': text(handle.get('hostId'), 'hostId'),
            'prompt': text(request.get('prompt'), 'prompt')}
    require(request.get('delivery_state') == 'not_sent', 'reconcile prior delivery before sending again')
    for key in ('model', 'thinking'):
        if key in request:
            args[key] = text(request[key], key)
    return {'arguments': args}


def match_delivery(request):
    handle, delivery = request['handle'], request['delivery']
    require(delivery.get('threadId') == ready(handle), 'wrong delivery sender')
    require(delivery.get('reference') == handle['reference'], 'wrong delivery reference')
    require(delivery.get('scope') == request['expected_scope'], 'wrong delivery scope')
    require(delivery.get('complete') is True, 'receipt or partial content is not a complete result')
    text(delivery.get('body'), 'result body')
    return {'matched': True}


def archive(request):
    handle = request['handle']
    thread = ready(handle)
    require(request.get('result_retained') is True, 'retain result or observed failure before archive')
    status = request.get('status')
    require(status not in {'active', 'needs_user_decision', 'pending'}, 'nonterminal task remains open')
    if handle.get('family') == 'ask':
        require(status in {'completed', 'failed', 'cancelled', 'replaced'}, 'unrecognized Ask terminal status')
        require((status == 'completed' and request.get('explicit_yes_in_adviser') is True)
                or (status == 'failed' and request.get('failure_rule_applies') is True)
                or request.get('explicit_cleanup_authorized') is True, 'Ask task must remain open')
    elif handle.get('family') == 'workflow':
        require(handle.get('role') in {'coordinator', 'executor', 'reviewer', 'repair'}, 'invalid workflow role')
        require(status in {'completed', 'pass', 'changes_requested', 'blocked', 'context_handoff', 'failed', 'replaced'}, 'unrecognized terminal status')
        if handle['role'] == 'coordinator' or status == 'context_handoff':
            require(request.get('predecessor_ended') is True and request.get('successor_started') is True,
                    'rollover archive requires an ended predecessor and a started successor')
    else:
        raise ValueError('unknown family')
    return {'arguments': {'threadId': thread, 'hostId': text(handle.get('hostId'), 'hostId'), 'archived': True}}


def verify_archive(request):
    thread = ready(request['handle'])
    reply = request['reply']
    require(reply.get('isError') is not True and reply.get('threadId') == thread and reply.get('archived') is True,
            'exact-ID archived:true proof missing')
    return {'verified': True, 'threadId': thread}


OPERATIONS = {function.__name__: function for function in
              (task_title, create, creation_result, reconcile, message, match_delivery, archive, verify_archive)}


def run(request):
    require(isinstance(request, dict), 'request must be an object')
    operation = request.get('operation')
    require(operation in OPERATIONS, 'unknown operation')
    return OPERATIONS[operation](request)


def main():
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='strict')
    try:
        result = run(json.load(sys.stdin))
    except (ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps({'ok': False, 'error': str(error)}))
        return 1
    print(json.dumps({'ok': True, **result}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
