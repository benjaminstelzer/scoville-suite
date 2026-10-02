"""Prepare private runtime CI inputs and verify matching successful Actions runs."""
import base64
import hashlib
import json
from pathlib import Path
import re
import subprocess

REPOSITORY = 'benjaminstelzer/scoville-runtime-ci'
WORKFLOW = '.github/workflows/runtime-helpers.yml'
SYSTEMS = ('windows-latest', 'macos-latest', 'ubuntu-latest')
PYTHONS = ('3.11', '3.x')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def assets():
    source = Path(__file__).resolve().parents[1] / 'runtime-tests'
    return {WORKFLOW: (source / 'runtime-helpers.yml').read_bytes(),
            'tests/test_runtime_helpers.py': (source / 'test_runtime_helpers.py').read_bytes()}


def candidates(builder, root):
    raw = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
    variants = [(profile, layout) for profile in raw.get('profiles', {})
                for layout in ('standalone', 'suite')]
    if not variants:
        variants = [(raw.get('profile'), raw.get('layout'))]
    result = {}
    for profile, layout in variants:
        config = builder.load(root, profile, layout)
        files, contracts = {}, {}
        # Complete packages retain real dependencies such as the Code Skill.
        for member in config['members']:
            for name, data in builder.payload(root, member, config).items():
                files[member['name'] + '/' + name] = data
            for script, contract in member.get('helper_contracts', {}).items():
                contracts[member['name'] + '/' + member['name'] + '/' + script] = contract['kind']
        if contracts:
            result[f'{profile}-{layout}'] = (files, contracts)
    return result


def prepare(builder, root, destination, refresh=False):
    root, destination = root.resolve(), destination.absolute()
    if (destination.exists() and not refresh) or destination.is_relative_to(root) or root.is_relative_to(destination):
        raise ValueError('--prepare-runtime-ci requires a new directory outside the source tree')
    files = assets()
    variants = {}
    for variant, (payload, contracts) in candidates(builder, root).items():
        variants[variant] = {'files': {name: digest(data) for name, data in sorted(payload.items())},
                             'helper_contracts': contracts}
        files.update({f'packages/{variant}/{name}': data for name, data in payload.items()})
    if not variants:
        raise ValueError('No packaged runtime helpers were found in suite.json')
    metadata = {'schema_version': 1, 'variants': variants,
                'test_assets': {name: digest(data) for name, data in assets().items()}}
    files['runtime-input.json'] = (json.dumps(metadata, sort_keys=True, indent=2) + '\n').encode('utf-8')
    files['.gitattributes'] = b'* -text\n'
    if destination.exists():
        old = json.loads((destination / 'runtime-input.json').read_text(encoding='utf-8'))
        expected = dict(old['test_assets'])
        for variant, entry in old['variants'].items():
            expected.update({f'packages/{variant}/{name}': value for name, value in entry['files'].items()})
        expected['.gitattributes'] = digest(files['.gitattributes'])
        actual = {p.relative_to(destination).as_posix(): digest(p.read_bytes())
                  for p in destination.rglob('*') if p.is_file()
                  and '.git' not in p.relative_to(destination).parts and p.name != 'runtime-input.json'}
        if actual != expected or set(files) != set(expected) | {'runtime-input.json'}:
            raise ValueError('Runtime CI refresh requires intact files and unchanged inventory; reconcile staging first')
    else:
        destination.mkdir(parents=True)
    for name, data in files.items():
        target = builder.within(destination, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return {'status': 'runtime_ci_prepared', 'repository': REPOSITORY,
            'directory': str(destination), 'input_sha256': digest(files['runtime-input.json']),
            'variants': sorted(variants)}


def api(route):
    result = subprocess.run(['gh', 'api', route], capture_output=True)
    if result.returncode:
        raise ValueError('GitHub runtime verification failed: ' + result.stderr.decode('utf-8', errors='replace').strip())
    return json.loads(result.stdout)


def remote_file(commit, name):
    entry = api(f'repos/{REPOSITORY}/contents/{name}?ref={commit}')
    if entry.get('encoding') != 'base64':
        raise ValueError(f'Cannot read runtime CI file {name} at the tested commit')
    return base64.b64decode(entry['content'], validate=False)


def verify(builder, root, run_url, config, selected=()):
    members = [m for m in config['members'] if not selected or m['name'] in selected]
    if not any(m.get('helper_contracts') for m in members):
        return {'status': 'not_applicable', 'reason': 'no packaged Python runtime helpers'}
    match = re.fullmatch(r'https://github\.com/' + re.escape(REPOSITORY) + r'/actions/runs/(\d+)', run_url or '')
    if not match:
        raise ValueError('--runtime-run must name a successful private runtime matrix: '
                         f'https://github.com/{REPOSITORY}/actions/runs/ID; '
                         'first prepare current packages with --prepare-runtime-ci <new-directory>')
    if api(f'repos/{REPOSITORY}').get('private') is not True:
        raise ValueError('Runtime CI repository must remain private')
    run_id = match[1]
    run = api(f'repos/{REPOSITORY}/actions/runs/{run_id}')
    if run.get('status') != 'completed' or run.get('conclusion') != 'success' or run.get('path') != WORKFLOW:
        raise ValueError('Runtime Actions run must be completed successfully for runtime-helpers.yml')
    jobs = api(f'repos/{REPOSITORY}/actions/runs/{run_id}/attempts/{run["run_attempt"]}/jobs?per_page=100')
    expected = {f'runtime ({system}, {python})' for system in SYSTEMS for python in PYTHONS}
    rows = jobs['jobs']
    if (jobs['total_count'] != len(expected) or {job['name'] for job in rows} != expected
            or any(job['conclusion'] != 'success' for job in rows)):
        raise ValueError('Every Windows/macOS/Linux job on Python 3.11 and 3.x must succeed; skipped or missing jobs are not proof')
    commit = run['head_sha']
    metadata_bytes = remote_file(commit, 'runtime-input.json')
    metadata = json.loads(metadata_bytes)
    if metadata.get('schema_version') != 1:
        raise ValueError('Unsupported runtime CI input schema; prepare a current snapshot')
    for name, data in assets().items():
        if metadata.get('test_assets', {}).get(name) != digest(data) or remote_file(commit, name) != data:
            raise ValueError(f'Runtime CI tests changed: {name}; rerun the matrix with current tests')
    variant = f'{config["profile"]}-{config["layout"]}'
    tested = metadata.get('variants', {}).get(variant, {})
    required = {}
    for member in members:
        for name, data in builder.payload(root, member, config).items():
            required[member['name'] + '/' + name] = digest(data)
    # Compare the entire selected package inventory, including prompt/config dependencies.
    names = {m['name'] for m in members}
    observed = {name: value for name, value in tested.get('files', {}).items() if name.split('/')[0] in names}
    if observed != required:
        raise ValueError(f'Runtime CI packages differ from current {variant} sources; prepare and test the current build')
    contracts = {m['name'] + '/' + m['name'] + '/' + name: contract['kind']
                 for m in members for name, contract in m.get('helper_contracts', {}).items()}
    observed_contracts = {name: kind for name, kind in tested.get('helper_contracts', {}).items() if name.split('/')[0] in names}
    if contracts != observed_contracts:
        raise ValueError('Runtime helper registry changed; prepare and test the current build')
    return {'status': 'passed', 'run': run_url, 'attempt': run['run_attempt'],
            'commit': commit, 'input_sha256': digest(metadata_bytes), 'variant': variant,
            'packages_sha256': digest(json.dumps(required, sort_keys=True).encode('utf-8'))}


def bind_receipt(receipt, proof):
    files = {m['name'] + '/' + name: value for m in receipt['members'] for name, value in m['files'].items()}
    if proof['status'] == 'passed' and proof['packages_sha256'] != digest(json.dumps(files, sort_keys=True).encode('utf-8')):
        raise ValueError('Package sources changed during the verified build; candidate remains pending, rerun current runtime CI')
    receipt['runtime_validation'] = proof
