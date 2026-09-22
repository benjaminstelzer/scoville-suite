#!/usr/bin/env python3
"""Export committed suite sources and self-contained packages to a new tree."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from build_suite import load, payload, within
from sync_suite_sources import sync


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          capture_output=True).stdout


def export(root, output):
    root, output = root.resolve(), output.resolve()
    if output.exists() or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError('Use a new external output directory')
    if git(root, 'status', '--porcelain').strip():
        raise ValueError('Commit and inspect suite sources before export')
    revision = git(root, 'rev-parse', '--verify', 'HEAD').decode().strip()
    source = Path(__file__).resolve().parents[1]
    if sync(root, source, check=True):
        raise ValueError('Shared snapshot is stale')
    config = load(root)
    if any(not m['public_distribution'] for m in config['members']):
        raise ValueError('Full suite export requires approval for every member')
    files = {}
    sources = []
    for entry in git(root, 'ls-files', '--stage', '-z').split(b'\0'):
        if not entry:
            continue
        metadata, path = entry.split(b'\t', 1)
        mode, object_id, stage = metadata.decode().split()
        name = path.decode('utf-8')
        if mode not in ('100644', '100755') or stage != '0':
            raise ValueError('Unsupported source entry: ' + name)
        if name.startswith('packages/'):
            raise ValueError('Source checkout must not own generated packages')
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
        files[name] = objects[start:end]
        offset = end + 1
    if offset != len(objects):
        raise ValueError('Unexpected trailing source objects')
    for member in config['members']:
        for relative, data in payload(root, member).items():
            files['packages/' + member['name'] + '/' + relative] = data
    # Stage only after every source and package has passed validation.
    output.mkdir(parents=True)
    for name, data in files.items():
        target = within(output, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return {'source_commit': revision, 'suite': config['name'],
            'files': {name: hashlib.sha256(data).hexdigest()
                      for name, data in sorted(files.items())}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--receipt', required=True, type=Path)
    args = parser.parse_args()
    if args.receipt.exists() or args.receipt.resolve().is_relative_to(args.output.resolve()):
        parser.error('Receipt must be new and outside the exported tree')
    result = export(args.root, args.output)
    args.receipt.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'suite': result['suite'], 'files': len(result['files']),
                      'source_commit': result['source_commit']}))
