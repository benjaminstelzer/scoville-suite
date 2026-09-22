"""Freeze three focused Terra prompts from one built Workflow package."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from run_codex_cli_case import load_receipt, verify_hash

HERE = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('build', 'output', 'catalog', 'codex'):
        parser.add_argument('--' + key, required=True, type=Path)
    args = parser.parse_args()
    receipt = args.build / 'build-receipt.json'
    package = args.build / 'scoville-suite/packages/scoville-workflow-for-codex/scoville-workflow-for-codex'
    load_receipt(receipt, 'scoville-workflow-for-codex', package)
    verify_hash(args.catalog, '0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0', 'catalog')
    verify_hash(args.codex, 'bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226', 'codex')
    args.output.mkdir(parents=True, exist_ok=False)
    cases_path = HERE / 'workflow-context-cases.md'
    key_path = HERE / 'workflow-context-expected.md'
    sections = re.split(r'^## (context-\d+)\n', cases_path.read_text(encoding='utf-8'), flags=re.M)
    supplied = ['SKILL.md', 'references/operations.md']
    core = '\n\n'.join(f'Built packaged text {name}:\n```text\n{(package/name).read_text(encoding="utf-8")}\n```' for name in supplied)
    manifest = {'model': 'gpt-5.6-terra', 'effort': 'medium',
        'cases_sha256': digest(cases_path), 'hidden_key_sha256': digest(key_path),
        'runner_sha256': digest(HERE/'run_codex_cli_case.py'),
        'lifetime_sha256': digest(HERE/'process_lifetime.py'),
        'receipt_sha256': digest(receipt), 'package': str(package), 'cases': []}
    for index in range(1, len(sections), 2):
        case_id, case = sections[index:index+2]
        prompt = ('Apply the supplied Workflow rules to this hypothetical case. Earlier gates explicitly stated complete are fixtures; do not repeat them. Analyze only the listed next-action choices, not execution of the whole Plan.\n\n'
            + core + '\n\nCase '+case_id+':\n'+case
            + '\nDo not use tools or execute actions. If a required packaged text is missing, reply only READ <relative-path>, one file per line. We will supply exact built text. Otherwise answer each numbered situation concisely. Do not invent observations.\n')
        path = args.output / (case_id+'.md')
        path.write_text(prompt, encoding='utf-8', newline='\n')
        command = [sys.executable, '-B', str(HERE/'run_codex_cli_case.py'),
            '--case-id', case_id, '--prompt', str(path), '--package-root', str(package),
            '--receipt', str(receipt), '--receipt-member', 'scoville-workflow-for-codex',
            '--catalog', str(args.catalog), '--codex', str(args.codex),
            '--output', str(args.output/(case_id+'-run')), '--model', manifest['model'],
            '--effort', 'medium', '--expected-prompt-sha256', digest(path),
            '--expected-receipt-sha256', digest(receipt), '--expected-catalog-sha256', digest(args.catalog),
            '--expected-codex-sha256', digest(args.codex), '--timeout-seconds', '90', '--max-turns', '4']
        manifest['cases'].append({'id':case_id,'prompt_sha256':digest(path),'command':command})
    (args.output/'frozen.json').write_text(json.dumps(manifest, indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'cases':len(manifest['cases']),'frozen_manifest':str(args.output/'frozen.json'), 'hidden_key_sha256':manifest['hidden_key_sha256']}))

if __name__ == '__main__':
    main()
