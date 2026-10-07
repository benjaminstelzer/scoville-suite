"""One private, single-writer register for the authorized Luna test attempts."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import uuid

LIMIT = 591
AUTHORITY = 'ADR-0168'
POOL_LIMITS = {'suite': 300, 'workflow': 100}


def output_key(value):
    return os.path.normcase(str(Path(value).resolve()))


def initialize(path):
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        stream.write(json.dumps({'authority': AUTHORITY, 'limit': LIMIT,
                                 'model': 'gpt-6-luna', 'effort': 'high'}) + '\n')


def read(path, with_limit=False):
    if path.suffix == '.json':
        record = json.loads(path.read_text(encoding='utf-8'))
        expected = {'schema_version': 1, 'plan_id': 'PLAN-0035',
                    'model': 'gpt-6-luna', 'effort': 'high'}
        if not isinstance(record, dict) or any(record.get(key) != value for key, value in expected.items()):
            raise ValueError('expected the authorized PLAN-0035 Luna/high register; no historical budget applies')
        efforts = record.get('allowed_efforts', ['high'])
        if efforts not in (['high'], ['high', 'medium']):
            raise ValueError('allowed_efforts must retain high and may explicitly add medium')
        limit = record.get('limit')
        if limit != 80 and not ((limit == 100 and record.get('authority') == 'ADR-0185')
                               or (limit == 120 and record.get('authority') == 'ADR-0187')
                               or (limit == 300 and record.get('authority') == 'ADR-0192')):
            raise ValueError('expected the original 80-attempt register, ADR-0185 100, ADR-0187 120, or ADR-0192 300')
        attempts = record.get('attempts')
        if not isinstance(attempts, list) or len(attempts) > limit:
            raise ValueError('invalid PLAN-0035 attempt count; preserve the register')
        if any(not isinstance(row, dict) or
               any(not isinstance(row.get(key), str) or not row[key] for key in ('attempt_id', 'case_id', 'output')) or
               row.get('model') != 'gpt-6-luna' or row.get('effort') not in efforts
               or row.get('pool', 'suite') not in POOL_LIMITS
               for row in attempts):
            raise ValueError('invalid PLAN-0035 attempt identity or model settings')
        if len({row['attempt_id'] for row in attempts}) != len(attempts):
            raise ValueError('duplicate PLAN-0035 attempt identity')
        if len({output_key(row['output']) for row in attempts}) != len(attempts):
            raise ValueError('duplicate PLAN-0035 output path; preserve the register')
        return (attempts, limit) if with_limit else attempts
    rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
    allowed = [{'authority': authority, 'limit': limit, 'model': 'gpt-6-luna', 'effort': 'high'}
               for authority, limit in [('ADR-0161', 150), ('ADR-0166', 300), ('ADR-0167', 400), (AUTHORITY, LIMIT)]]
    if not rows or rows[0] not in allowed:
        raise ValueError('expected an approved ADR-0161/ADR-0166/ADR-0167/ADR-0168 register; initialize new registers with evaluation.py init and preserve existing attempts')
    limit = rows[0]['limit']
    attempts = rows[1:]
    if len(attempts) > limit or len({row['attempt_id'] for row in attempts}) != len(attempts):
        raise ValueError('invalid attempt register; preserve it and investigate')
    if any(row.get('pool', 'suite') not in POOL_LIMITS for row in attempts):
        raise ValueError('invalid attempt pool; expected suite or workflow')
    if limit == 400 and any(sum(row.get('pool', 'suite') == pool for row in attempts) > cap for pool, cap in POOL_LIMITS.items()):
        raise ValueError('invalid attempt register: per-pool budget exceeded')
    return (attempts, limit) if with_limit else attempts


def reserve(path, case_id, output, variant=None, run_set=None, pool='suite', effort='high'):
    if pool not in POOL_LIMITS or (pool == 'workflow' and not case_id.startswith('workflow-')):
        raise ValueError('pool must be suite, or workflow for a workflow-* case')
    lock = path.with_suffix(path.suffix + '.lock')
    try:
        token = lock.open('x', encoding='utf-8')
    except FileExistsError as error:
        raise ValueError('attempt register is locked; finish or reconcile its previous writer before retrying') from error
    try:
        token.close()
        rows, limit = read(path, with_limit=True)
        if path.suffix == '.json':
            record = json.loads(path.read_text(encoding='utf-8'))
            if effort not in record.get('allowed_efforts', ['high']):
                raise ValueError('requested effort is not in the register allowed_efforts; retain the approved settings')
        elif effort != 'high':
            raise ValueError('historical JSONL registers permit only high effort')
        if len(rows) >= limit:
            raise ValueError(f'{limit}-attempt budget exhausted; no process started')
        if pool == 'workflow' and limit not in (80, 100, 120, 400, LIMIT) and not (path.suffix == '.json' and limit == 300):
            raise ValueError('workflow pool requires PLAN-0035 or an approved ADR-0167/ADR-0168 register')
        if limit == 400 and sum(row.get('pool', 'suite') == pool for row in rows) >= POOL_LIMITS[pool]:
            raise ValueError(f'{POOL_LIMITS[pool]}-attempt budget exhausted for {pool}; no process started')
        output = str(output.resolve())
        if any(output_key(row['output']) == output_key(output) for row in rows):
            raise ValueError('each attempt needs a fresh output directory')
        row = {'attempt_id': uuid.uuid4().hex, 'case_id': case_id, 'variant': variant, 'run_set': run_set, 'output': output, 'pool': pool,
               'reserved_at': datetime.now(timezone.utc).isoformat()}
        if path.suffix == '.json':
            row.update(status='reserved', model='gpt-6-luna', effort=effort,
                       reserved_before_start=True)
            record = json.loads(path.read_text(encoding='utf-8'))
            record['attempts'].append(row)
            temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
            try:
                with temporary.open('x', encoding='utf-8', newline='\n') as stream:
                    stream.write(json.dumps(record, ensure_ascii=True, indent=2) + '\n')
                    stream.flush()
                    os.fsync(stream.fileno())
                os.replace(temporary, path)
            finally:
                temporary.unlink(missing_ok=True)
        else:
            with path.open('a', encoding='utf-8', newline='\n') as stream:
                stream.write(json.dumps(row, ensure_ascii=True) + '\n')
                stream.flush()
                os.fsync(stream.fileno())
        return row
    finally:
        lock.unlink()

