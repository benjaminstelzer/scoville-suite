"""Read-only exact inventory/hash check for a union of suite build receipts."""
import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath


def relative(value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError('invalid relative path')
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ('', '.', '..') for p in value.split('/')):
        raise ValueError('unsafe relative path: ' + value)
    return value


def verify(root, receipts):
    root = Path(root).resolve(strict=True)
    expected = {}
    packages = set()
    suites = set()
    for receipt_path in receipts:
        receipt_path = Path(receipt_path).resolve(strict=True)
        raw = receipt_path.read_bytes()
        receipt = json.loads(raw)
        if receipt.get('schema_version') != 1 or not receipt.get('members'):
            raise ValueError('unsupported or empty receipt')
        suite = receipt.get('suite')
        if not isinstance(suite, str) or suite in suites:
            raise ValueError('missing or duplicate suite')
        suites.add(suite)
        for member in receipt['members']:
            package = relative(member['package_path'])
            if any(package == p or package.startswith(p + '/') or p.startswith(package + '/') for p in packages):
                raise ValueError('overlapping package: ' + package)
            packages.add(package)
            if not member['files']:
                raise ValueError('empty package: ' + package)
            for name, digest in member['files'].items():
                key = package + '/' + relative(name)
                if not isinstance(digest, str) or not re.fullmatch('[0-9a-f]{64}', digest):
                    raise ValueError('invalid SHA-256: ' + key)
                expected[key] = digest
        if receipt_path.is_relative_to(root):
            key = receipt_path.relative_to(root).as_posix()
            if key in expected:
                raise ValueError('receipt overlaps package')
            expected[key] = hashlib.sha256(raw).hexdigest()
    directories = set()
    for name in expected:
        directories.update(p.as_posix() for p in PurePosixPath(name).parents if p.as_posix() != '.')
    actual = {}
    actual_directories = set()
    for path in root.rglob('*'):
        if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
            raise ValueError('redirected path: ' + str(path))
        key = path.relative_to(root).as_posix()
        if path.is_dir():
            actual_directories.add(key)
        elif path.is_file():
            actual[key] = hashlib.sha256(path.read_bytes()).hexdigest()
        else:
            raise ValueError('unsupported entry: ' + key)
    errors = []
    for key in sorted(expected.keys() - actual.keys()):
        errors.append('missing: ' + key)
    for key in sorted(actual.keys() - expected.keys()):
        errors.append('extra: ' + key)
    for key in sorted(expected.keys() & actual.keys()):
        if expected[key] != actual[key]:
            errors.append('hash mismatch: ' + key)
    for key in sorted(actual_directories - directories):
        errors.append('extra directory: ' + key)
    return {'valid': not errors, 'packages': len(packages), 'files': len(actual), 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--receipt', required=True, action='append', type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.root, args.receipt)
    except (OSError, ValueError, KeyError, TypeError) as error:
        result = {'valid': False, 'errors': [str(error)]}
    print(json.dumps(result))
    return 0 if result['valid'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
