"""Freeze five WordPress comprehension cases against built packages."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from run_codex_cli_case import load_receipt, verify_hash

HERE = Path(__file__).resolve().parent
MEMBER = 'scoville-wordpress-ui-backend-anti-ai-slop'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('build', 'output', 'catalog', 'codex'):
        parser.add_argument('--' + key, required=True, type=Path)
    args = parser.parse_args()
    receipt = args.build / 'build-receipt.json'
    package = args.build / MEMBER / MEMBER
    load_receipt(receipt, MEMBER, package)
    verify_hash(args.catalog, '0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0', 'catalog')
    verify_hash(args.codex, 'bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226', 'codex')
    verify_hash(HERE / 'run_codex_cli_case.py', '4cb9ea0f660c3bfee33f3d555a7549998e78c89a1e8ec2ddad85038488725519', 'runner')
    args.output.mkdir(parents=True, exist_ok=False)
    cases_path = HERE / 'wordpress-cases.md'
    key_path = HERE / 'wordpress-expected.md'
    sections = re.split(r'^## (wp-\d+)\n', cases_path.read_text(encoding='utf-8'), flags=re.M)
    if len(sections) != 11:
        raise ValueError('Expected exactly five cases')
    core = (package / 'SKILL.md').read_text(encoding='utf-8')
    discovery = []
    for name in (MEMBER, 'scoville-ui-anti-ai-slop'):
        root = args.build / name / name
        load_receipt(receipt, name, root)
        text = (root / 'SKILL.md').read_text(encoding='utf-8')
        discovery.append(text.split('---', 2)[1])
    manifest = {'model': 'gpt-5.6-luna', 'effort': 'medium',
                'cases_sha256': digest(cases_path), 'hidden_key_sha256': digest(key_path),
                'runner_sha256': digest(HERE / 'run_codex_cli_case.py'),
                'lifetime_sha256': digest(HERE / 'process_lifetime.py'),
                'receipt_sha256': digest(receipt), 'package': str(package), 'cases': []}
    for index in range(1, len(sections), 2):
        case_id, case = sections[index:index + 2]
        is_discovery = case_id in ('wp-04', 'wp-05')
        supplied = '\n\n'.join(discovery) if is_discovery else core
        instruction = ('Select from the supplied discovery metadata only. Do not load references.' if is_discovery else
                       'Apply the supplied Skill to this hypothetical case. Source/read results in the case are fixtures. '
                       'If the Skill requires a packaged text file not yet supplied, first reply only with READ <relative-path>, one file per line. We will supply it as text.')
        prompt = (supplied + '\n\nCase ' + case_id + ':\n' + case + '\n' + instruction +
                  '\nDo not execute project actions or use tools. Otherwise answer the case concisely. State unavailable facts as unknown. Do not invent source content or completed work.\n')
        path = args.output / (case_id + '.md')
        path.write_text(prompt, encoding='utf-8', newline='\n')
        command = [sys.executable, '-B', str(HERE / 'run_codex_cli_case.py'),
                   '--case-id', case_id, '--prompt', str(path), '--package-root', str(package),
                   '--receipt', str(receipt), '--receipt-member', MEMBER,
                   '--catalog', str(args.catalog), '--codex', str(args.codex),
                   '--output', str(args.output / (case_id + '-run')), '--model', manifest['model'],
                   '--effort', 'medium', '--expected-prompt-sha256', digest(path),
                   '--expected-receipt-sha256', digest(receipt), '--expected-catalog-sha256', digest(args.catalog),
                   '--expected-codex-sha256', digest(args.codex), '--timeout-seconds', '90', '--max-turns', '4']
        manifest['cases'].append({'id': case_id, 'prompt_sha256': digest(path), 'command': command})
    (args.output / 'frozen.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'cases': 5, 'manifest': str(args.output / 'frozen.json')}))


if __name__ == '__main__':
    main()
