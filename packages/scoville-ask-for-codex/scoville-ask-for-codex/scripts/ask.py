#!/usr/bin/env python3
"""Resolve advisers and prepare native payloads; execute only explicit Claude requests."""
from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path
import re
import subprocess
import sys

import ask_claude
from list_models import list_models
import task_lifecycle
from ask_settings import resolve_settings

ROOT = Path(__file__).resolve().parent.parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, name):
    require(isinstance(value, str) and bool(value.strip()), f'{name} must be nonempty text')
    return value


def resolve(request):
    config = resolve_settings(ROOT / 'config.default.json', request)
    advisers = config['advisers']
    catalog = None
    if any(a['route'] == 'native' for a in advisers):
        catalog = request.get('catalog')
        if catalog is None:
            catalog = list_models()
        require(isinstance(catalog, dict) and catalog.get('source') == 'model/list', 'fresh model/list catalog required')
        rows = catalog.get('models')
        require(isinstance(rows, list), 'invalid model catalog')
        allowed = {}
        for row in rows:
            require(isinstance(row, dict) and isinstance(row.get('efforts'), list), 'invalid catalog entry')
            model = text(row.get('model'), 'catalog model')
            require(model not in allowed, 'duplicate catalog model')
            allowed[model] = row['efforts']
    for adviser in advisers:
        if adviser['route'] == 'native':
            require(adviser['model'] in allowed, f'model unavailable: {adviser["model"]}')
            require(adviser['effort'] in allowed[adviser['model']], f'effort unavailable for {adviser["model"]}')
        else:
            require(ask_claude.MODEL_PATTERN.fullmatch(adviser['model']), 'invalid Claude model')
            require(adviser['effort'] in ask_claude.EFFORT_LEVELS, 'unsupported Claude CLI effort')
    return {'config': config, 'catalog': catalog}


def prepare(request):
    mode = request.get('mode')
    require(mode in {'review', 'consultation'}, 'clarify ambiguous intent before preparing advisers')
    question = text(request.get('question'), 'question')
    scope = text(request.get('scope'), 'scope')
    reference = text(request.get('reference'), 'reference')
    settings = resolve(request)['config']
    role = (ROOT / 'references/adviser.md').read_text(encoding='utf-8')
    prompt = role + '\n\n' + json.dumps({'mode': mode, 'scope': scope, 'question': question}, ensure_ascii=False)
    entries = []
    for adviser in settings['advisers']:
        ref = reference + ':' + adviser['id']
        entry = {'adviser': adviser, 'reference': ref, 'scope': scope, 'context_mode': 'fresh'}
        if adviser['route'] == 'native':
            result = task_lifecycle.create({
                'creation_authorized': request.get('creation_authorized'), 'prior_state': request.get('prior_state'),
                'family': 'ask', 'role': 'adviser', 'prompt': prompt + '\n\n' + (ROOT / 'references/native-delivery.md').read_text(encoding='utf-8'),
                'projectId': request.get('projectId'), 'caller_title': request.get('caller_title'),
                'return_to_thread_id': request.get('caller_id'), 'reference': ref,
                'prior_task_ids': request.get('prior_task_ids', []),
                'model': adviser['model'], 'thinking': adviser['effort']})
            result['handle'].update(adviser=adviser, scope=scope, return_to_thread_id=request['caller_id'])
            entry.update(result)
        else:
            entry['request'] = {'operation': 'claude', 'adviser': adviser, 'claude': settings['claude'],
                'prompt': prompt, 'reference': ref, 'scope': scope, 'cwd': request.get('cwd'), 'authorized': request.get('creation_authorized')}
        entries.append(entry)
    return {'mode': mode, 'entries': entries}


def claude(request):
    require(request.get('authorized') is True, 'Claude consultation requires authorization')
    adviser, config = request['adviser'], request['claude']
    require(adviser.get('route') == 'claude-cli', 'Claude route required')
    # Reuse configuration validation without reading unrelated native defaults.
    resolved = resolve({'overrides': {'advisers': [adviser], 'claude': config}})['config']
    config = resolved['claude']
    adviser = resolved['advisers'][0]
    cwd = Path(text(request.get('cwd'), 'cwd'))
    require(cwd.is_absolute() and cwd.is_dir(), 'cwd must be an existing absolute directory')
    resume = request.get('session_id')
    if resume is not None:
        text(resume, 'session_id')
    timeout = request.get('timeout_seconds', config['timeout_seconds'])
    require(type(timeout) in (int, float) and math.isfinite(timeout) and timeout > 0, 'invalid Claude deadline')
    args = argparse.Namespace(model=adviser['model'], effort=adviser['effort'],
        max_budget_usd=config['max_budget_usd'], fresh=False, persistent=False,
        resume=resume, continue_session=False, session_name=None,
        session_persistence_default=config['session_persistence'], customizations_enabled=config['customizations'], web_tools=config['web_tools'])
    command = ask_claude.build_command(args, ask_claude.resolve_claude_command())
    result = ask_claude.run_command(command, cwd, text(request.get('prompt'), 'prompt'), timeout)
    if result.returncode != 0:
        detail = result.stderr.strip()
        if not detail and result.stdout.strip():
            detail = ask_claude.claude_error_details(ask_claude.parse_claude_result(result.stdout)) or 'no error details in response'
        raise ValueError(f'Claude exited {result.returncode}: {detail or "no error details"}')
    payload = ask_claude.parse_claude_result(result.stdout)
    require(ask_claude.claude_error_details(payload) is None, 'Claude failed: ' + str(ask_claude.claude_error_details(payload)))
    answer = text(payload.get('result'), 'Claude answer')
    session = payload.get('session_id')
    return {'reference': request.get('reference'), 'scope': request.get('scope'), 'answer': answer,
        'session_id': session, 'continuation_available': bool(session) and config['session_persistence'],
        'context_mode': 'continued' if resume else 'fresh',
        'requested_model': adviser['model'], 'requested_effort': adviser['effort'],
        'reported_model': payload.get('model'), 'reported_effort': payload.get('effort'),
        'permission_denials': payload.get('permission_denials') or []}


def followup(request):
    handle = copy.deepcopy(request['handle'])
    require(request.get('archived') is False, 'follow-up needs an unarchived task')
    require(handle.get('family') == 'ask', 'Ask handle required')
    reference = text(request.get('reference'), 'new reference')
    require(reference != handle.get('reference'), 'follow-up needs a new reference')
    adviser = copy.deepcopy(handle['adviser'])
    overrides = request.get('overrides', {})
    require(isinstance(overrides, dict) and set(overrides) <= {'model', 'effort', 'name'}, 'follow-up may only override model, effort or display name')
    adviser.update(overrides)
    require(adviser.get('route') == 'native', 'native continuation cannot change route')
    resolve({'overrides': {'advisers': [adviser]}, **({'catalog': request['catalog']} if 'catalog' in request else {})})
    scope = text(request.get('scope'), 'scope')
    prompt = 'ask_role=adviser\nconsultation_reference=' + reference + '\nreturn_to_thread_id=' + text(handle.get('return_to_thread_id'), 'return destination')
    prompt += '\n' + (ROOT / 'references/adviser.md').read_text(encoding='utf-8')
    prompt += '\n' + (ROOT / 'references/native-delivery.md').read_text(encoding='utf-8')
    prompt += '\n' + json.dumps({'scope': scope, 'question': text(request.get('question'), 'question')}, ensure_ascii=False)
    result = task_lifecycle.message({'handle': handle, 'delivery_state': request.get('delivery_state'), 'prompt': prompt,
        'model': adviser['model'], 'thinking': adviser['effort']})
    handle.update(reference=reference, scope=scope, adviser=adviser)
    return {**result, 'handle': handle, 'context_mode': 'continued'}


OPERATIONS = {'resolve': resolve, 'prepare': prepare, 'claude': claude, 'followup': followup}


def main():
    try:
        request = json.load(sys.stdin)
        require(isinstance(request, dict) and request.get('operation') in OPERATIONS, 'unknown operation')
        result = OPERATIONS[request['operation']](request)
        print(json.dumps({'ok': True, **result}, ensure_ascii=False))
        return 0
    except (ValueError, KeyError, TypeError, OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        failure = {'ok': False, 'error': str(error)}
        if isinstance(error, ask_claude.ClaudeTimeout):
            failure['code'] = 'claude_timeout'
        print(json.dumps(failure, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    ask_claude.configure_standard_streams()
    raise SystemExit(main())
