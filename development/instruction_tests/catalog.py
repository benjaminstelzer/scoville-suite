"""Read a verified private instruction-test dataset; never run model tests."""
import argparse
import hashlib
import json
from pathlib import Path


class UnknownSkillError(ValueError):
    pass


def load_catalog(data_root: Path, skill: str | None = None, selection: str = 'owner') -> dict:
    identity = json.loads(Path(__file__).with_name('dataset.json').read_text(encoding='utf-8'))
    for name, digest in identity['files'].items():
        path = data_root / name
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f'dataset file {name} differs from {identity["dataset_id"]}; supply the frozen dataset or register a justified new revision')
    catalog = json.loads((data_root / 'catalog.json').read_text(encoding='utf-8'))
    if catalog['dataset_id'] != identity['dataset_id']:
        raise ValueError('catalog dataset_id does not match the registered identity')
    if skill is not None:
        known = sorted({case['skill'] for case in catalog['cases']})
        if skill not in known:
            raise UnknownSkillError(f'unknown --skill {skill}; expected one of: {", ".join(known)}')
        catalog['cases'] = [case for case in catalog['cases'] if case['skill'] == skill or
                            selection == 'involved' and case['type'] == 'trigger' and
                            skill in case.get('required', []) + case.get('allowed', []) + case.get('forbidden', [])]
    return catalog


def project(catalog: dict, data_root: Path, view: str) -> dict:
    if view == 'catalog':
        return catalog
    fixtures = json.loads((data_root / catalog['fixture_file']).read_text(encoding='utf-8'))
    environments = json.loads((data_root / catalog['environment_file']).read_text(encoding='utf-8'))
    cases = []
    for case in catalog['cases']:
        identity = hashlib.sha256(case['id'].encode('utf-8')).hexdigest()[:16]
        fixture = fixtures.get(case.get('fixture_ref'), {})
        environment = environments.get(case.get('environment_ref'), {})
        if view == 'keys':
            row = {'id': identity, 'source_id': case['id'], 'expect': case['expect'],
                   'checks': fixture.get('checks', {}), 'variants': case['variants']}
            for key in ('required', 'allowed', 'forbidden', 'grading', 'observation_scope',
                        'equivalent_variants', 'execution_gate', 'context_contract'):
                if key in case:
                    row[key] = case[key]
        elif view == 'runner':
            row = {'id': identity, 'fixture': fixture, 'environment': environment}
            for key in ('context_packages', 'context_contract', 'execution_gate',
                        'environment_contract'):
                if key in case:
                    row[key] = case[key]
        else:
            row = {'id': identity, 'prompt': fixture.get('user_request', case['given'])}
            # Conversation is visible. Files and simulated tool state belong to
            # the runner and become visible only through permitted observations.
            if 'prior_turns' in fixture or 'prior_turns' in environment:
                row['prior_turns'] = fixture.get('prior_turns', environment.get('prior_turns'))
        cases.append(row)
    return {'dataset_id': catalog['dataset_id'], 'view': view, 'cases': cases}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, epilog='Example: python development/instruction_tests/catalog.py --data-root <private-dataset-directory> --skill scoville-ui')
    parser.add_argument('--data-root', type=Path, required=True, help='Directory containing the frozen private dataset files; missing data is unverified, not a pass.')
    parser.add_argument('--skill', help='Optional exact Skill name, such as scoville-ui.')
    parser.add_argument('--selection', choices=['owner', 'involved'], default='owner', help='With --skill, select its own cases or every trigger where it is required, allowed or forbidden.')
    parser.add_argument('--view', choices=['questions', 'keys', 'runner', 'catalog'], default='questions', help='Questions contain visible conversation only. Keys are evaluator-only. Runner supplies private setup and tool state; catalog supplies full case definitions.')
    args = parser.parse_args()
    try:
        result = project(load_catalog(args.data_root, args.skill, args.selection), args.data_root, args.view)
    except UnknownSkillError as error:
        parser.error(str(error))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(3, f'private test data unverified: {error}. Correct invocation: python development/instruction_tests/catalog.py --data-root <private-dataset-directory> --skill scoville-ui\n')
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
