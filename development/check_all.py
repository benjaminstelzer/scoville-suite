#!/usr/bin/env python3
"""Run every local mechanical pre-commit check; finish checks after failures."""
from datetime import date
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]


def load_runner(shared):
    path = shared / 'build/run_portability.py'
    spec = importlib.util.spec_from_file_location('suite_check_portability', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def stale_codex_readmes(root, shared, preview):
    builder = load_runner(shared).load_builder(shared)
    general = {member['name'] for member in builder.load(root, 'general')['members']}
    stale = []
    for member in builder.load(root, 'codex')['members']:
        if member['name'] in general:
            continue
        relative = Path('members') / member['name'] / 'README.md'
        if (root / relative).read_bytes().replace(b'\r\n', b'\n') != (preview / relative).read_bytes():
            stale.append(relative.as_posix())
    return stale


def cleanup_temporary(directory, allowed_root):
    source = Path(directory.name).resolve()
    allowed_root = allowed_root.resolve()
    if source == allowed_root or not source.is_relative_to(allowed_root):
        raise ValueError(f'unsafe temporary cleanup target: {source}')
    try:
        directory.cleanup()
    except OSError as deletion_error:
        destination_root = (Path.home() / 'Desktop/_delete').resolve()
        destination_root.mkdir(parents=True, exist_ok=True)
        destination = (destination_root / f'{source.name}-{uuid.uuid4().hex}').resolve()
        if destination.parent != destination_root or destination.exists():
            raise ValueError(f'unsafe cleanup destination: {destination}') from deletion_error
        try:
            shutil.move(str(source), str(destination))
        except OSError as move_error:
            raise OSError(f'temporary cleanup failed: source={source}; destination={destination}; '
                          f'delete={deletion_error}; move={move_error}') from move_error
        print(f'CLEANUP moved locked temporary inputs to {destination}', flush=True)


def run(root=ROOT):
    root = root.resolve()
    shared = root.parent / 'shared'
    failed = []
    completed = []
    empty = []

    def fail(name, error):
        failed.append(name)
        print(f'FAIL {name}: {error}', flush=True)

    def check(name, arguments):
        try:
            result = subprocess.run([sys.executable, '-X', 'utf8', '-B', *arguments],
                                    cwd=root, capture_output=True, text=True,
                                    encoding='utf-8')
        except (OSError, UnicodeError) as error:
            fail(name, error)
            return False
        if result.returncode:
            fail(name, f'exit {result.returncode}')
            for label, output in (('stdout', result.stdout), ('stderr', result.stderr)):
                if output:
                    print(f'{label}:\n{output}', end='' if output.endswith('\n') else '\n')
            return False
        summary = re.search(r'Ran (\d+) tests? in ', result.stderr)
        if arguments[:3] == ['-m', 'unittest', 'discover'] and (summary is None or int(summary[1]) == 0):
            fail(name, 'unittest discovery did not report any executed tests')
            for output in (result.stdout, result.stderr):
                if output:
                    print(output, end='' if output.endswith('\n') else '\n')
            return False
        completed.append(name)
        count = f' ({summary[1]} Python tests)' if summary is not None else ''
        print(f'PASS {name}{count}', flush=True)
        return True

    try:
        manifest = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
        if not isinstance(manifest.get('profiles'), dict):
            raise ValueError('run this gate in canonical suite source with a profile manifest and sibling ../shared')
        paths = load_runner(shared).source_test_paths(root, shared, manifest)
    except (OSError, ValueError, KeyError) as error:
        fail('test inventory', error)
        paths = []
    for path in paths:
        name = str(path.relative_to(root)) if path.is_relative_to(root) else '../shared/tests'
        if path.is_dir() and not any(path.rglob('test*.py')):
            empty.append(name)
            print(f'EMPTY {name}: no Python tests (model cases are not executed)', flush=True)
        else:
            arguments = [str(path)] if path.is_file() else ['-m', 'unittest', 'discover', '-s', str(path)]
            check(name, arguments)

    builder = shared / 'build/build_suite.py'
    base = [str(builder), '--root', str(root)]
    check('source previews', [*base, '--check-sources'])
    check('general README previews', [*base, '--profile', 'general', '--check-readmes'])

    temporary_root = root.parents[2] / 'temp' / f'{date.today().isoformat()}-suite-check-all'
    try:
        temporary_root.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(prefix='checks-', dir=temporary_root)
        try:
            temporary = directory.name
            snapshot = Path(temporary) / 'runtime'
            # Canonical runtime tests require metadata and complete profile packages.
            # Running their generated snapshot once covers the canonical test asset.
            if check('runtime snapshot preparation', [*base, '--prepare-runtime-ci', str(snapshot)]):
                check('canonical runtime tests (all profile packages)',
                      ['-m', 'unittest', 'discover', '-s', str(snapshot / 'tests')])
            else:
                print('BLOCKED runtime tests: snapshot preparation failed', flush=True)
            preview = Path(temporary) / 'codex-readmes'
            if check('Codex README preparation',
                     [*base, '--profile', 'codex', '--write-readmes', '--output', str(preview)]):
                check('Codex README previews',
                      [*base, '--profile', 'codex', '--check-readmes', '--output', str(preview)])
                try:
                    stale = stale_codex_readmes(root, shared, preview)
                    if stale:
                        fail('Codex-only maintained README previews', '; '.join(stale))
                    else:
                        completed.append('Codex-only maintained README previews')
                        print('PASS Codex-only maintained README previews', flush=True)
                except (OSError, ValueError, KeyError) as error:
                    fail('Codex-only maintained README previews', error)
            else:
                print('BLOCKED Codex README check: preview preparation failed', flush=True)
        finally:
            try:
                cleanup_temporary(directory, temporary_root)
            except (OSError, ValueError) as error:
                print(f'CLEANUP WARNING: {error}', flush=True)
    except (OSError, ValueError) as error:
        fail('temporary check inputs', error)
    print(f'CHECK ALL (mechanical/Python; models not run): {len(completed)} passed; '
          f'{len(failed)} failed; {len(empty)} empty test paths', flush=True)
    if failed:
        print('Failed checks: ' + '; '.join(failed), flush=True)
    return int(bool(failed))


if __name__ == '__main__':
    raise SystemExit(run())
