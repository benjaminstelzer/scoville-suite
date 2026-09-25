#!/usr/bin/env python3
"""Pure native-task payload checks. No host calls, retries or permission grants.

Read one JSON request from stdin and print one JSON result. The caller retains
the returned handle in its existing record before performing the next action.
Host replies must be the actual decoded tool payload, not invented summaries.
"""
from __future__ import annotations

import json
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
        if role == 'coordinator':
            title = f'{label("coordinator_title", 32)} G{number("generation")} [{label("workflow_id", 64)}]'
        else:
            roles = {'executor': 'WORK', 'reviewer': 'REVIEW', 'repair': 'REPAIR'}
            require(role in roles, 'invalid workflow title role')
            title = f'SCW {label("unit", 80)} {roles[role]} RUN [#{number("attempt")}]'
    elif family == 'ask':
        require(role == 'adviser', 'invalid Ask title role')
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
        require(handle.get('role') in {'executor', 'reviewer', 'repair'}, 'coordinator archive requires rollover handshake')
        require(status in {'completed', 'pass', 'changes_requested', 'blocked', 'context_handoff', 'failed', 'unassigned_parking'}, 'unrecognized terminal status')
        if status == 'unassigned_parking':
            require(request.get('parking_turn_completed') is True and request.get('assignment_not_sent') is True,
                    'unassigned parking proof missing')
    else:
        raise ValueError('unknown family')
    return {'arguments': {'threadId': thread, 'hostId': text(handle.get('hostId'), 'hostId'), 'archived': True}}


def verify_archive(request):
    thread = ready(request['handle'])
    reply = request['reply']
    require(reply.get('threadId') == thread and reply.get('archived') is True,
            'exact-ID archived:true proof missing')
    return {'verified': True, 'threadId': thread}


def rollover_record(request):
    """Validate retained handoff identity and terminal predecessor evidence."""
    successor, predecessor = request['successor'], request['predecessor']
    successor_id, predecessor_id = ready(successor), ready(predecessor)
    for handle in (successor, predecessor):
        text(handle.get('hostId'), 'hostId')
        require(handle.get('family') == 'workflow' and handle.get('role') == 'coordinator', 'rollover requires coordinator handles')
    require(successor_id != predecessor_id, 'successor cannot be predecessor')
    text(request.get('workflow_id'), 'workflow_id')
    require(type(request.get('generation')) is int and request['generation'] > 0, 'invalid generation')
    completed = request['predecessor_turn']
    require(completed.get('threadId') == predecessor_id and completed.get('hostId') == predecessor['hostId']
            and completed.get('turnId') == text(request.get('activation_turn_id'), 'activation_turn_id')
            and completed.get('status') == 'completed', 'exact predecessor activation turn completion unproven')
    return {key: request[key] for key in
            ('workflow_id', 'generation', 'successor', 'predecessor', 'activation_turn_id', 'predecessor_turn')}


def rollover_readiness(request):
    """Require a listed or exact-read active successor before predecessor archive."""
    archive_record = rollover_record(request)
    successor, predecessor = request['successor'], request['predecessor']
    successor_id, predecessor_id = ready(successor), ready(predecessor)
    guard = request['guard']
    require(request.get('guard_capability_verified') is True, 'fresh guard capability verification required')
    require(guard.get('workflow_id') == text(request.get('workflow_id'), 'workflow_id'), 'wrong workflow')
    generation = request.get('generation')
    require(type(generation) is int and generation > 0 and guard.get('generation') == generation, 'wrong generation')
    require(guard.get('coordinator_id') == successor_id and guard.get('state') == 'coordinator_active', 'successor is not active guard owner')
    require(guard.get('writer') is None and guard.get('rollover') is None, 'handoff is not quiescent')
    reachable = request['exact_successor']
    require(reachable.get('threadId') == successor_id and reachable.get('hostId') == successor['hostId']
            and reachable.get('reachable') is True, 'exact successor reachability unproven')
    listing = request['listing']
    def matches(entry):
        return entry.get('id') == successor_id and entry.get('hostId') == successor['hostId'] and entry.get('kind') == 'codex'
    visible = any(matches(entry) for entry in listing.get('threads', []))
    active_exact = reachable.get('status') == 'active'
    pinned = any(matches(entry) for entry in listing.get('pinnedThreads', []))
    key = 'codex:thread:' + successor['hostId'] + ':' + successor_id
    sectioned = any(key in section.get('itemKeys', []) for section in listing.get('sections', []))
    complete_listing = all(isinstance(listing.get(key), list) for key in ('threads', 'pinnedThreads', 'sections'))
    complete_listing = complete_listing and all(isinstance(section.get('itemKeys'), list)
                                               for section in listing.get('sections', []))
    complete_listing = complete_listing and not (listing.get('unavailableHosts') or listing.get('unavailableSources'))
    archive_blockers = []
    for condition, reason in ((not complete_listing, 'listing_incomplete'),
                              (not visible and not active_exact, 'successor_not_listed'),
                              (pinned, 'successor_pinned'), (sectioned, 'successor_sectioned'),
                              (request.get('status_retained') is not True, 'status_not_retained')):
        if condition:
            archive_blockers.append(reason)
    archive_allowed = not archive_blockers
    return {'may_continue': True, 'may_archive_predecessor': archive_allowed,
            'retain_predecessor': not archive_allowed,
            'archive_blockers': archive_blockers,
            'archive_record': archive_record,
            'archive_arguments': {'threadId': predecessor_id, 'hostId': predecessor['hostId'], 'archived': True} if archive_allowed else None}


def recover_rollover_archives(request):
    """Authorize older predecessors only through a contiguous retained handoff chain."""
    current = rollover_readiness(request)
    records = request.get('archive_chain')
    require(isinstance(records, list) and bool(records), 'archive_chain must be nonempty')
    records = [rollover_record(record) for record in records]
    require(records[-1] == current['archive_record'], 'chain must end at current handoff')
    def identity(handle):
        return ready(handle), handle['hostId']
    seen = {identity(records[0]['predecessor'])}
    previous = None
    for record in records:
        require(record['workflow_id'] == request['workflow_id'], 'chain workflow mismatch')
        if previous is not None:
            require(record['generation'] == previous['generation'] + 1
                    and identity(record['predecessor']) == identity(previous['successor']),
                    'handoff chain is not contiguous')
        require(identity(record['successor']) not in seen, 'handoff chain repeats a coordinator')
        seen.add(identity(record['successor']))
        previous = record
    replies = request.get('archive_receipts', [])
    require(isinstance(replies, list), 'archive_receipts must be a list')
    predecessors = {identity(record['predecessor']): record['predecessor'] for record in records}
    archived = set()
    for receipt in replies:
        target = (receipt.get('threadId'), receipt.get('hostId'))
        require(target in predecessors and target not in archived, 'unknown or duplicate archive receipt')
        verify_archive({'handle': predecessors[target], 'reply': receipt['reply']})
        archived.add(target)
    pending = [handle for key, handle in predecessors.items() if key not in archived]
    return {'may_continue': True, 'archive_blockers': current['archive_blockers'],
            'pending_predecessors': pending,
            'archive_arguments': [{'threadId': handle['threadId'], 'hostId': handle['hostId'], 'archived': True}
                                  for handle in pending] if current['may_archive_predecessor'] else []}


OPERATIONS = {function.__name__: function for function in
              (task_title, create, creation_result, reconcile, message, match_delivery, archive, verify_archive,
               rollover_readiness, recover_rollover_archives)}


def run(request):
    require(isinstance(request, dict), 'request must be an object')
    operation = request.get('operation')
    require(operation in OPERATIONS, 'unknown operation')
    return OPERATIONS[operation](request)


def main():
    try:
        result = run(json.load(sys.stdin))
    except (ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps({'ok': False, 'error': str(error)}))
        return 1
    print(json.dumps({'ok': True, **result}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
