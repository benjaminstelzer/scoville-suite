"""Bind comprehension prompts and results to the frozen dataset and preparation."""
import hashlib
import json
from pathlib import Path

from catalog import load_catalog, project


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def case_identity(catalog, case, variant):
    if variant not in case['variants']:
        raise ValueError('--variant must be an applicable frozen case variant')
    return {
        'dataset_id': catalog['dataset_id'],
        'registry_sha256': digest(Path(__file__).with_name('dataset.json')),
        'case_id': case['id'], 'variant': variant,
        'case_sha256': hashlib.sha256(json.dumps(case, sort_keys=True, ensure_ascii=True).encode()).hexdigest(),
    }


def render_prompt(question, case, entrypoint, workspace):
    parts = []
    if question.get('prior_turns'):
        parts.append('Visible prior conversation:\n' + json.dumps(question['prior_turns'], ensure_ascii=False))
    if case['type'] == 'comprehension':
        parts.append(f'Apply the hypothetical case using the selected package. Request its entrypoint with READ {entrypoint}.')
    parts.append(question['prompt'].replace('<FIXTURE_ROOT>', workspace.as_posix()))
    return ('\n\n'.join(parts) + '\n').encode('utf-8')


def frozen_prompt(catalog, data_root, case, variant, workspace):
    question = project({**catalog, 'cases': [case]}, data_root, 'questions')['cases'][0]
    entrypoint = f'packages/{case["skill"]}/{case["skill"]}/SKILL.md' if variant.split('-')[1] == 'suite' else 'SKILL.md'
    return render_prompt(question, case, entrypoint, workspace)


def verify_preparation(path, case_id, variant, package_root, receipt, prompt):
    metadata = json.loads(path.read_text(encoding='utf-8'))
    data_root = Path(metadata['data_root'])
    catalog = load_catalog(data_root)
    cases = [case for case in catalog['cases'] if case['id'] == case_id]
    if len(cases) != 1 or cases[0]['type'] != 'comprehension':
        raise ValueError('--case-id must match a frozen comprehension case')
    case = cases[0]
    identity = case_identity(catalog, case, variant)
    if metadata['case_binding'] != identity or metadata['case_id'] != case_id or metadata['variant'] != variant:
        raise ValueError('--preparation must match --case-id, --variant and the registered dataset')
    if Path(metadata['package_root']).resolve() != package_root.resolve() or Path(metadata['receipt']).resolve() != receipt.resolve():
        raise ValueError('--preparation must match --package-root and --receipt')
    output = Path(metadata['output_root'])
    if prompt.resolve() != (output / 'prompt.txt').resolve():
        raise ValueError('--prompt must be the prompt.txt produced by --preparation')
    expected = frozen_prompt(catalog, data_root, case, variant, output / 'workspace')
    if prompt.read_bytes() != expected or digest(prompt) != metadata['prompt_sha256']:
        raise ValueError('--prompt differs from the frozen case; prepare a new case, never replace its prompt')
    if digest(receipt) != metadata['receipt_sha256']:
        raise ValueError('--receipt changed after preparation; prepare the current candidate again')
    return {'case_binding': identity, 'fixture_root': str(output / 'workspace')}


def verify_recorded_prompt(catalog, data_root, case, variant, manifest, run_root):
    if manifest['case_binding'] != case_identity(catalog, case, variant):
        raise ValueError('run case/dataset identity does not match the frozen evaluation case')
    expected = frozen_prompt(catalog, data_root, case, variant, Path(manifest['fixture_root']))
    if hashlib.sha256(expected).hexdigest() != manifest['hashes']['prompt']:
        raise ValueError('run prompt hash does not match the frozen case prompt')
    recorded = run_root / 'turn-01-prompt.md'
    if recorded.exists() and recorded.read_bytes() != expected:
        raise ValueError('recorded first-turn prompt does not match the frozen case')
