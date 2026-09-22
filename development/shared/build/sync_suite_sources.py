#!/usr/bin/env python3
"""Generate a suite's declared shared build dependencies. No runtime imports."""
import argparse
import hashlib
import json
from pathlib import Path
from build_suite import load, readme_references, within


def snapshot(root, source):
    config = load(root)
    paths = {'build/build_suite.py', 'build/sync_suite_sources.py', 'build/export_suite.py',
             'build/verify_package_set.py', 'build/fragments.md',
             'instruction-writing.md', 'luna-release-gate.md'}
    # Retain shared development sources and tests, not only runtime consumers.
    for folder in ('build', 'readme', 'runtime', 'tests'):
        paths.update(p.relative_to(source).as_posix() for p in (source / folder).rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts
                     and p.suffix not in ('.pyc', '.pyo'))
    entries = list(config.get('readme', []))
    for member in config['members']:
        entries.extend(member['readme'])
        paths.update(item['source'] for item in member.get('shared_helpers', []))
    for reference in readme_references(entries, 'suite'):
        if reference.startswith('shared:'):
            paths.add('readme/' + reference.removeprefix('shared:'))
    files = {name: within(source, name).read_bytes() for name in sorted(paths)}
    receipt = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
    files['sources.json'] = (json.dumps(receipt, indent=2) + '\n').encode()
    return files


def sync(root, source, check=False):
    files = snapshot(root, source)
    destination = within(root, 'development/shared')
    actual = {p.relative_to(destination).as_posix(): p.read_bytes()
              for p in destination.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    extras = sorted(actual.keys() - files.keys())
    if extras:
        raise ValueError('Unmanaged snapshot files; reconcile before updating: ' + ', '.join(extras))
    changed = sorted(name for name, data in files.items() if actual.get(name) != data)
    if not check:
        for name in changed:
            target = within(destination, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(files[name])
    return changed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    changed = sync(args.root.resolve(), args.source.resolve(), args.check)
    print(json.dumps({'changed': changed, 'written': not args.check}))
    raise SystemExit(int(args.check and bool(changed)))
