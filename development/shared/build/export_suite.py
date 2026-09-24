#!/usr/bin/env python3
"""Export committed suite sources and self-contained packages to a new tree."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from build_suite import load, payload, within, variant_text, render_readmes
from sync_suite_sources import sync


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          capture_output=True).stdout


def export(root, output, profile=None):
    root, output = root.resolve(), output.resolve()
    if output.exists() or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError('Use a new external output directory')
    if git(root, 'status', '--porcelain').strip():
        raise ValueError('Commit and inspect suite sources before export')
    revision = git(root, 'rev-parse', '--verify', 'HEAD').decode().strip()
    source = Path(__file__).resolve().parents[1]
    if sync(root, source, check=True):
        raise ValueError('Shared snapshot is stale')
    config = load(root, profile, 'suite')
    if any(not m['public_distribution'] for m in config['members']):
        raise ValueError('Full suite export requires approval for every member')
    files = {}
    sources = []
    raw = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
    kept = {m['name'] for m in config['members']}
    excluded_roots = []
    excluded_files = set()
    selected_sources = {f['source'] for m in config['members'] for f in m.get('files', [])}
    for member in raw['members']:
        if member['name'] not in kept:
            excluded_roots.append('members/' + member['name'] + '/')
            for ref in member.get('readme', []):
                ref = ref if isinstance(ref, str) else ref['source']
                if not ref.startswith('shared:'):
                    excluded_files.add(ref)
        for item in member.get('files', []):
            if item['source'] not in selected_sources and not item['source'].startswith('shared:'):
                excluded_files.add(item['source'])
    # A fragment shared with a retained member must remain available.
    for member in config['members']:
        for ref in member.get('readme', []):
            excluded_files.discard(ref if isinstance(ref, str) else ref['source'])
    for entry in git(root, 'ls-files', '--stage', '-z').split(b'\0'):
        if not entry:
            continue
        metadata, path = entry.split(b'\t', 1)
        mode, object_id, stage = metadata.decode().split()
        name = path.decode('utf-8')
        if mode not in ('100644', '100755') or stage != '0':
            raise ValueError('Unsupported source entry: ' + name)
        if (name.startswith('packages/') or name in excluded_files
                or any(name.startswith(prefix) for prefix in excluded_roots)):
            continue
        within(root, name)
        sources.append((name, object_id))
    objects = subprocess.run(
        ['git', '-C', str(root), 'cat-file', '--batch'],
        input=''.join(object_id + '\n' for _, object_id in sources).encode(),
        check=True, capture_output=True).stdout
    offset = 0
    for name, object_id in sources:
        header_end = objects.index(b'\n', offset)
        actual_id, kind, size = objects[offset:header_end].decode().split()
        if actual_id != object_id or kind != 'blob':
            raise ValueError('Unexpected source object: ' + name)
        start = header_end + 1
        end = start + int(size)
        if objects[end:end + 1] != b'\n':
            raise ValueError('Incomplete source object: ' + name)
        data = objects[start:end]
        if (not name.startswith('development/shared/')
                and name.endswith(('.md', '.toml')) and (b'{{ profile:' in data or b'{{ package:' in data)):
            data = variant_text(data.decode('utf-8'), config).encode('utf-8')
        files[name] = data
        offset = end + 1
    if offset != len(objects):
        raise ValueError('Unexpected trailing source objects')
    files['suite.json'] = (json.dumps(config, indent=2) + '\n').encode('utf-8')
    for member in config['members']:
        for relative, data in payload(root, member, config).items():
            files['packages/' + member['name'] + '/' + relative] = data
    # Stage only after every source and package has passed validation.
    output.mkdir(parents=True)
    for name, data in files.items():
        target = within(output, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    # README previews must reflect the selected profile, never source defaults.
    render_readmes(root, True, config, output)
    for path in output.rglob('*.md'):
        files[path.relative_to(output).as_posix()] = path.read_bytes()
    return {'layout': config.get('layout'), 'profile': config.get('profile'), 'source_commit': revision, 'suite': config['name'],
            'files': {name: hashlib.sha256(data).hexdigest()
                      for name, data in sorted(files.items())}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--profile')
    parser.add_argument('--receipt', required=True, type=Path)
    args = parser.parse_args()
    if args.receipt.exists() or args.receipt.resolve().is_relative_to(args.output.resolve()):
        parser.error('Receipt must be new and outside the exported tree')
    result = export(args.root, args.output, args.profile)
    args.receipt.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'suite': result['suite'], 'files': len(result['files']),
                      'source_commit': result['source_commit']}))
