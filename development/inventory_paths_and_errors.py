#!/usr/bin/env python3
"""List path and error sites for review. This development inventory is no verdict."""
import argparse
import ast
import bisect
import hashlib
import json
import os
from pathlib import Path
import re
import sys

SKIPPED_DIRECTORIES = {
    '.git': 'version-control internals',
    '__pycache__': 'generated Python bytecode cache',
    'node_modules': 'external installed dependencies, not authored project files',
    '.venv': 'local interpreter environment',
    '.svelte-kit': 'generated frontend cache',
}
PATH_TEXT = re.compile(
    r'(?:https?://[^\s<>"\x27)]+|[A-Za-z]:[/\\][^\n\r"\x27<>]*'
    r'|(?:~|\.{1,2}|[A-Za-z0-9_.-]+)[/\\][^\s"\x27<>`(),;]+)'
)
BARE_FILE = re.compile(r'\b[A-Za-z0-9_.-]+\.(?:py|md|json|ya?ml|toml|txt|csv|tsx?|jsx?|svelte|rs|html|css|svg|png|exe|dll)\b')
MARKDOWN_LINK = re.compile(r'!?\[[^\]\n]*\]\(([^)\n]+)\)')
IMPORT_TEXT = re.compile(r'\b(?:from\s+|import\s*(?:\(\s*)?)["\x27]([^"\x27\n]+)["\x27]|\buse\s+([^;\n]+);')
ERROR_TEXT = re.compile(r'\b(?:raise|throw|except|catch|stderr|diagnostic|parser\.error)\b')
PATH_METHODS = {
    'join', 'joinpath', 'resolve', 'absolute', 'expanduser', 'glob', 'rglob',
    'open', 'read_text', 'read_bytes', 'write_text', 'write_bytes', 'mkdir',
    'is_file', 'is_dir', 'exists', 'unlink', 'rename', 'replace', 'relative_to',
    'is_relative_to', 'symlink_to', 'readlink', 'with_name', 'with_suffix',
}
PATH_CONSTRUCTORS = {'Path', 'PurePath', 'PurePosixPath', 'PureWindowsPath'}


def qualified(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return qualified(node.value) + '.' + node.attr
    return ''


def text_inventory(label, relative, text):
    records = []
    starts = [0] + [match.end() for match in re.finditer('\n', text)]
    lines = text.splitlines(keepends=True)

    def add(kind, start, end, detail=None):
        # Context is a named source window, not a purported copy of the whole file.
        line_index = bisect.bisect_right(starts, start) - 1
        context_start, context_end = max(0, start - 80), min(len(text), end + 80)
        record = {'root': label, 'file': relative, 'kind': kind,
                  'line': line_index + 1, 'column': start - starts[line_index] + 1,
                  'start_offset': start, 'end_offset': end,
                  'matched_text': text[start:end],
                  'context_start_offset': context_start, 'context_end_offset': context_end,
                  'context': text[context_start:context_end]}
        if detail:
            record['detail'] = detail
        records.append(record)

    for match in PATH_TEXT.finditer(text):
        add('path_literal_candidate', match.start(), match.end())
    for match in BARE_FILE.finditer(text):
        add('filename_candidate', match.start(), match.end())
    for match in MARKDOWN_LINK.finditer(text):
        add('markdown_reference', match.start(1), match.end(1))
    suffix = Path(relative).suffix.lower()
    if suffix != '.py':
        for match in IMPORT_TEXT.finditer(text):
            group = 1 if match.group(1) is not None else 2
            add('import_text_candidate', match.start(group), match.end(group))
        for match in ERROR_TEXT.finditer(text):
            add('error_text_candidate', match.start(), match.end())
        return records, {'method': 'lexical', 'limit': 'Non-Python syntax and dynamic references require review.'}

    try:
        tree = ast.parse(text, filename=relative)
    except SyntaxError as error:
        return records, {'method': 'python_parse_failed', 'line': error.lineno,
                         'column': error.offset, 'reason': str(error)}

    aliases = set(PATH_CONSTRUCTORS)
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module in ('pathlib', 'os.path'):
            aliases.update(item.asname or item.name for item in node.names)

    def offset(line, byte_column):
        source_line = lines[line - 1]
        # Python AST columns count UTF-8 bytes; inventory columns count characters.
        column = len(source_line.encode('utf-8')[:byte_column].decode('utf-8'))
        return starts[line - 1] + column

    def site(kind, node, detail=None):
        if not hasattr(node, 'end_lineno') or node.end_lineno is None:
            return
        add(kind, offset(node.lineno, node.col_offset),
            offset(node.end_lineno, node.end_col_offset), detail)

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            site('python_import', node)
        elif isinstance(node, ast.Call):
            name = qualified(node.func)
            last = name.rsplit('.', 1)[-1]
            classified = False
            if last in aliases or last in PATH_METHODS or name.startswith('os.path.'):
                site('python_path_operation_candidate', node, {'call': name, 'dynamic': True})
                classified = True
            if last in ('error', 'exception', 'exit', 'print') or name.endswith('.stderr.write'):
                site('python_error_output_candidate', node, {'call': name})
                classified = True
            if not classified:
                site('python_unclassified_call', node,
                     {'call': name, 'limit': 'May wrap path or error handling; follow its actual implementation.'})
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            site('python_path_division_candidate', node,
                 {'limit': 'May be numeric division; determine from its actual operands.'})
        elif isinstance(node, ast.Raise):
            site('python_raise', node)
        elif isinstance(node, ast.ExceptHandler):
            site('python_error_handler', node, {'limit': 'Review propagation and consumer behavior.'})
        elif isinstance(node, ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key, ast.Constant) and isinstance(key.value, str)]
            if set(keys) & {'diagnostic', 'error', 'errors', 'stderr'}:
                site('python_error_payload_candidate', node, {'keys': keys})
    return records, {'method': 'python_ast_and_lexical',
                     'limit': 'Candidates include fixtures and success output; no semantic correctness is inferred.'}


def inventory(roots):
    files, records, excluded = [], [], []
    for label, root in sorted(roots.items()):
        def walk(directory):
            for entry in sorted(os.scandir(directory), key=lambda item: item.name):
                path = Path(entry.path)
                relative = path.relative_to(root).as_posix()
                reparse_tag = getattr(entry.stat(follow_symlinks=False), 'st_reparse_tag', 0)
                if entry.is_symlink() or reparse_tag in (0xA0000003, 0xA000000C):
                    excluded.append({'root': label, 'file': relative,
                                     'reason': 'redirected path, not followed', 'target': os.readlink(path)})
                elif entry.is_dir(follow_symlinks=False):
                    if entry.name in SKIPPED_DIRECTORIES:
                        excluded.append({'root': label, 'file': relative,
                                         'reason': SKIPPED_DIRECTORIES[entry.name]})
                    else:
                        walk(path)
                elif entry.is_file(follow_symlinks=False):
                    before = path.stat()
                    data = path.read_bytes()
                    after = path.stat()
                    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                        raise OSError(f'File changed during inspection: {path}')
                    metadata = {'root': label, 'file': relative, 'bytes': len(data),
                                'sha256': hashlib.sha256(data).hexdigest()}
                    try:
                        text = data.decode('utf-8')
                        if '\0' in text or text.startswith('\ufeff'):
                            raise UnicodeError('Binary or BOM-prefixed content requires separate review.')
                        sites, analysis = text_inventory(label, relative, text)
                        records.extend(sites)
                        metadata['analysis'] = analysis
                    except UnicodeError as error:
                        metadata['analysis'] = {'method': 'not_parsed', 'reason': str(error)}
                    files.append(metadata)
                else:
                    excluded.append({'root': label, 'file': relative,
                                     'reason': 'special filesystem object, not read'})
        walk(root)
    records.sort(key=lambda row: (row['root'], row['file'], row['start_offset'], row['kind'], row['end_offset']))
    for number, record in enumerate(records, 1):
        record['id'] = f'SITE-{number:06d}'
    return {'schema_version': 1, 'verdict': 'unreviewed_candidates',
            'roots': {label: str(root) for label, root in sorted(roots.items())},
            'position_convention': 'One-based Unicode character columns; offsets are Unicode character offsets.',
            'context_convention': 'The complete match with up to 80 surrounding characters; source-window offsets are explicit.',
            'files': files, 'sites': records, 'excluded': excluded,
            'summary': {'files': len(files), 'sites': len(records), 'excluded': len(excluded)}}


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='strict')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', action='append', required=True, metavar='LABEL=PATH',
                        help='Repeat for Suite, Shared and each built package variant.')
    parser.add_argument('--output-file', type=Path, required=True,
                        help='New UTF-8 JSON file outside every inspected root.')
    args = parser.parse_args()
    try:
        roots = {}
        for supplied in args.root:
            label, separator, raw = supplied.partition('=')
            if not separator or not re.fullmatch(r'[a-z0-9_-]+', label) or not raw or label in roots:
                parser.error('--root requires a unique lowercase LABEL=PATH, for example suite=/absolute/project.')
            try:
                root = Path(raw).resolve(strict=True)
            except OSError as error:
                parser.error(f'--root "{supplied}" cannot be read as an existing directory; '
                             f'supply an existing readable source or package root. Original error: {error}')
            if not root.is_dir():
                parser.error(f'--root {supplied!r} is not a directory; supply an existing readable source or package root.')
            roots[label] = root
        output = args.output_file.resolve()
        if output.exists() or any(output.is_relative_to(root) for root in roots.values()):
            parser.error(f'--output-file "{output}" must be a new file outside the inspected roots; choose another temporary path.')
        result = inventory(roots)
        payload = (json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('xb') as stream:
            stream.write(payload)
    except (OSError, UnicodeError) as error:
        parser.error(f'Cannot complete the requested --root inventory or --output-file "{args.output_file}". '
                     f'Use existing readable roots and a writable new output location. Original error: {error}')
    print(json.dumps({'status': 'inventory_created', 'output_file': str(output),
                      'output_sha256': hashlib.sha256(payload).hexdigest(),
                      'verdict': result['verdict'], **result['summary']}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
