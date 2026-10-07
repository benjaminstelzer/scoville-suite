"""Prepare one frozen case locally. This command never starts a model or service."""
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import sys

from catalog import load_catalog, project
from case_binding import case_identity, render_prompt

RUNNER_DIR = Path(__file__).resolve().parents[1] / 'luna-tests'
sys.path.insert(0, str(RUNNER_DIR))
from run_codex_cli_case import load_package_receipt, contained_path, ProtocolError, isolated_environment


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=True, indent=2) + '\n', encoding='utf-8', newline='\n')


def destination(root, relative):
    if not isinstance(relative, str) or not relative or '\\' in relative or ':' in relative:
        raise ValueError(f'expected a relative POSIX fixture path, got {relative!r}')
    if any(part in ('', '.', '..') for part in relative.split('/')):
        raise ValueError(f'fixture path must stay inside workspace: {relative!r}')
    return root.joinpath(*relative.split('/'))


def prepare(data_root, case_id, variant, package_root, receipt, output, private_output):
    output, private_output = output.resolve(), private_output.resolve()
    catalog = load_catalog(data_root)
    cases = [c for c in catalog['cases'] if c['id'] == case_id]
    if len(cases) != 1:
        raise ValueError('--case-id must name exactly one case in catalog --view catalog')
    case = cases[0]
    if case.get('context_packages'):
        raise ValueError('--case-id requires multiple context_packages; this preparer cannot yet serve those verified comparison roots. Leave this case unverified; choose a supported case')
    if variant not in case['variants']:
        raise ValueError('--variant must be one of: ' + ', '.join(case['variants']))
    receipt_data = json.loads(receipt.read_text(encoding='utf-8'))
    profile, layout = variant.split('-')[:2]
    if (receipt_data.get('profile'), receipt_data.get('layout')) != (profile, layout):
        raise ValueError('--receipt profile/layout must match --variant')
    member = '@suite' if layout == 'suite' else case['skill']
    inventory = load_package_receipt(receipt, member, package_root)
    entrypoint = f'packages/{case["skill"]}/{case["skill"]}/SKILL.md' if layout == 'suite' else 'SKILL.md'
    if entrypoint not in inventory:
        raise ValueError('--package-root must contain the case Skill in the selected variant')
    skill_files = {}
    if case['type'] == 'trigger':
        for row in receipt_data['members']:
            name = row['name']
            relative_root = f'{row["package_path"]}/{name}'
            root = contained_path(receipt.parent, relative_root,
                                  f'package member {name}: expected receipt-relative directory {relative_root} below {receipt.parent}')
            for relative in load_package_receipt(receipt, name, root):
                skill_files[f'{name}/{name}/{relative}'] = root / relative
    selected = {**catalog, 'cases': [case]}
    question = project(selected, data_root, 'questions')['cases'][0]
    key = project(selected, data_root, 'keys')['cases'][0]
    private = project(selected, data_root, 'runner')['cases'][0]
    workspace = output / 'workspace'
    # Verify all inputs before creating output. Never execute strings from fixtures.
    files, directories = {}, set()
    for source in (private['environment'], private['fixture']):
        directories.update(source.get('directories', []))
        for relative, literal in source.get('files', {}).items():
            destination(workspace, relative)
            pinned = contained_path(data_root, source['input_files'][relative], 'unsafe_dataset_path').read_bytes()
            if pinned.decode('utf-8') != literal:
                raise ValueError(f'fixture text and pinned input disagree: {relative}')
            content = literal.replace('<FIXTURE_ROOT>', workspace.as_posix()).encode('utf-8')
            if relative in files and files[relative] != content:
                raise ValueError(f'fixture/environment file conflict: {relative}')
            files[relative] = content
    for relative in directories:
        destination(workspace, relative)
    if (private_output.is_relative_to(output) or output.is_relative_to(private_output)
            or private_output.parent == output.parent):
        raise ValueError('--private-output must be in a separate private tree, not inside, above or directly beside --output')
    if output.exists() or private_output.exists():
        raise ValueError('--output and --private-output must be new directories; preserve previous attempts')
    output.mkdir(parents=True)
    workspace.mkdir()
    for relative in sorted(directories):
        destination(workspace, relative).mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        target = destination(workspace, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    host_home = output / 'host-home'
    for relative in ('.codex', '.claude', '.config', 'AppData/Roaming', 'AppData/Local', 'tmp'):
        (host_home / relative).mkdir(parents=True, exist_ok=True)
    for relative, source in skill_files.items():
        target = destination(host_home / '.codex/skills', relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    question['prompt'] = question['prompt'].replace('<FIXTURE_ROOT>', workspace.as_posix())
    write_json(output / 'question.json', question)
    private_output.mkdir(parents=True)
    write_json(private_output / 'evaluator-key.json', key)
    write_json(private_output / 'runner-private.json', private)
    (output / 'prompt.txt').write_bytes(render_prompt(question, case, entrypoint, workspace))
    metadata = {
        'schema_version': 1, 'dataset_id': catalog['dataset_id'], 'case_id': case_id,
        'data_root': str(data_root), 'output_root': str(output),
        'case_binding': case_identity(catalog, case, variant),
        'prompt_sha256': digest(output / 'prompt.txt'),
        'opaque_id': question['id'], 'type': case['type'], 'variant': variant,
        'prepared_date': date.today().isoformat(), 'execution_date': None,
        'status': 'prepared_not_executed', 'package_root': str(package_root),
        'receipt': str(receipt), 'receipt_member': member, 'receipt_sha256': digest(receipt),
        'package_files': inventory, 'fixture_files': {r: digest(workspace / r) for r in files},
        'runner_sha256': digest(Path(__file__)),
        'discovery_files': {r: digest(host_home / '.codex/skills' / r) for r in skill_files},
        'catalog_reader_sha256': digest(Path(__file__).with_name('catalog.py')),
        'dataset_registry_sha256': digest(Path(__file__).with_name('dataset.json')),
        'host_environment': {k: v for k, v in isolated_environment(host_home).items()
                             if k in ('HOME', 'USERPROFILE', 'CODEX_HOME', 'CLAUDE_CONFIG_DIR', 'APPDATA', 'LOCALAPPDATA', 'XDG_CONFIG_HOME', 'TEMP', 'TMP')},
        'requested_model': 'gpt-6-luna' if variant.endswith('luna-high') else 'claude-opus-5-5',
        'requested_effort': 'high', 'actual_model': None, 'actual_effort': None,
        'host_qualification': 'unverified', 'execution_authorized': False,
        'open_requirements': ['shared ADR-0161 register before Luna dispatch; Claude budget remains open', 'qualified isolated host and authentication',
                              'execution date at dispatch', 'actual runtime and prelude evidence from runner-private.json'],
    }
    if case['type'] != 'comprehension':
        metadata['open_requirements'].append('OS isolation must hide evaluator keys, real user files and external tools from shell/browser')
    write_json(private_output / 'preparation.json', metadata)
    return {'status': metadata['status'], 'id': question['id'], 'output': str(output), 'private_output': str(private_output)}


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog='Example: python development/instruction_tests/prepare.py --data-root <dataset> --case-id <catalog-id> --variant codex-suite-luna-high --package-root <built-suite> --receipt <build-receipt.json> --output <runs/case> --private-output <vault/case>')
    for name in ('data-root', 'package-root', 'receipt', 'output', 'private-output'):
        parser.add_argument('--' + name, required=True, type=Path)
    parser.add_argument('--case-id', required=True)
    parser.add_argument('--variant', required=True)
    args = parser.parse_args()
    try:
        result = prepare(args.data_root.resolve(), args.case_id, args.variant,
                         args.package_root.resolve(), args.receipt.resolve(), args.output.resolve(), args.private_output.resolve())
    except (OSError, ValueError, KeyError, TypeError, ProtocolError) as error:
        parser.exit(3, f'case preparation failed: {error}. Correct inputs using --help; use a new --output after a partial filesystem failure.\n')
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
