#!/usr/bin/env python3
"""Run source or exported-suite portability checks without mixing contracts."""
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


def load_builder(shared: Path):
    path = shared / 'build/build_suite.py'
    spec = importlib.util.spec_from_file_location('portability_builder', path)
    if spec is None or spec.loader is None:
        raise ValueError('cannot load shared builder')
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    return builder


def source_test_paths(root: Path, shared: Path, manifest: dict) -> list[Path]:
    paths = [shared / 'tests', root / 'development/tests']
    paths.extend(root / member['development']['tests'] for member in manifest['members'])
    result = []
    for path in paths:
        resolved = path.resolve()
        if not resolved.exists():
            raise ValueError('declared test path does not exist: ' + str(resolved))
        if not any(resolved == existing or
                   (existing.is_dir() and resolved.is_relative_to(existing))
                   for existing in result):
            result.append(resolved)
    return result


def run_test_path(path: Path) -> bool:
    if not path.exists():
        raise ValueError('declared test path does not exist: ' + str(path))
    if path.is_dir() and not any(path.rglob('test*.py')):
        return False
    command = ([sys.executable, '-B', str(path)] if path.is_file() else
               [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', str(path)])
    subprocess.run(command, check=True)
    return True


def validate_export(root: Path, shared: Path, manifest: dict) -> dict:
    builder = load_builder(shared)
    config = builder.load(root)
    if 'profiles' in manifest or not config.get('profile') or config.get('layout') != 'suite':
        raise ValueError('expected one exported suite profile')
    if builder.render_readmes(root, False, config):
        raise ValueError('exported README projection is stale')
    if builder.render_sources(root, False, config):
        raise ValueError('exported source projection is stale')
    expected_packages = {member['name'] for member in config['members']}
    package_root = root / 'packages'
    actual_packages = {path.name for path in package_root.iterdir() if path.is_dir()}
    if actual_packages != expected_packages:
        raise ValueError('exported package directory set differs from the manifest')
    python_files = 0
    for member in config['members']:
        expected = builder.payload(root, member, config)
        folder = package_root / member['name']
        actual = {path.relative_to(folder).as_posix(): path.read_bytes()
                  for path in folder.rglob('*') if path.is_file()}
        if actual != expected:
            raise ValueError(member['name'] + ': exported package differs from selected sources')
        for name, data in actual.items():
            if name.endswith('.py'):
                compile(data, str(folder / name), 'exec')
                python_files += 1
    other_layout = 'standalone' if config['layout'] == 'suite' else 'suite'
    try:
        builder.load(root, config['profile'], other_layout)
    except ValueError as error:
        if 'retain their package layout' not in str(error):
            raise
    else:
        raise ValueError('exported suite accepted a different package layout')
    return {'profile': config['profile'], 'members': len(config['members']),
            'python_files': python_files}


def run(root: Path, shared: Path) -> dict:
    root, shared = root.resolve(), shared.resolve()
    manifest = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
    if 'profiles' not in manifest:
        return {'mode': 'export', **validate_export(root, shared, manifest)}
    paths = source_test_paths(root, shared, manifest)
    executed, empty = [], []
    for path in paths:
        (executed if run_test_path(path) else empty).append(str(path))
    return {'mode': 'source', 'executed_test_paths': len(executed),
            'empty_test_paths': empty}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--shared', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = run(args.root, args.shared)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, 'PORTABILITY FAILED: ' + str(error) + '\n')
    print(json.dumps(result))
