#!/usr/bin/env python3
"""Build standalone distribution trees without publishing or modifying a checkout."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import posixpath
from urllib.parse import unquote, urlsplit


def shared_root() -> Path:
    """Use the sources beside this builder, including published snapshots."""
    return Path(__file__).resolve().parents[1]


def within(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or '\\' in relative or ':' in relative:
        raise ValueError('expected a nonempty portable relative path')
    candidate = root / relative
    if Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError(f'unsafe path: {relative}')
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f'path escapes source: {relative}')
    if any(p.is_symlink() or (hasattr(p, 'is_junction') and p.is_junction()) for p in (candidate, *candidate.parents) if p != root.parent):
        raise ValueError(f'symlink not allowed: {relative}')
    return resolved


def load(root: Path) -> dict:
    data = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
    if data['schema_version'] != 1:
        raise ValueError('unsupported suite manifest')
    if type(data.get('member_previews', True)) is not bool:
        raise ValueError('member_previews must be boolean')
    names = [m['name'] for m in data['members']]
    if len(names) != len(set(names)):
        raise ValueError('duplicate member')
    for name in [data['name'], *names]:
        if not name or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in name):
            raise ValueError('invalid member name')
    for member in data['members']:
        distribution = member.get('distribution', 'standalone')
        if distribution not in {'standalone', 'suite'}:
            raise ValueError('invalid distribution kind')
        expected_repository = 'benjaminstelzer/' + (data['name'] if distribution == 'suite' else member['name'])
        if member['repository'] != expected_repository:
            raise ValueError('unexpected distribution repository')
        if member['visibility'] not in {'public', 'private'} or type(member['public_distribution']) is not bool:
            raise ValueError('invalid distribution policy')
        if member['public_distribution'] and member['visibility'] != 'public':
            raise ValueError('private member cannot enter public builds')
    return data


def readme_source(root: Path, reference: str) -> Path:
    if reference.startswith('shared:'):
        return within(shared_root() / 'readme', reference.removeprefix('shared:'))
    return within(root, reference)


def package_path(config: dict, member: dict) -> str:
    if member.get('distribution', 'standalone') == 'suite':
        return config['name'] + '/packages/' + member['name']
    return member['name']


def readme_references(entries: list, audience: str) -> list[str]:
    if audience not in {'suite', 'release'}:
        raise ValueError('unknown README audience')
    references = []
    for entry in entries:
        if isinstance(entry, str):
            references.append(entry)
        elif (isinstance(entry, dict) and set(entry) == {'source', 'audience'}
              and entry['audience'] == 'suite' and isinstance(entry['source'], str)):
            if audience == 'suite':
                references.append(entry['source'])
        else:
            raise ValueError('invalid README fragment entry')
    return references


def development_links(root: Path, config: dict, member: dict) -> str:
    repository = config.get('repository')
    if repository != 'benjaminstelzer/' + config['name']:
        raise ValueError('missing or unexpected suite repository')
    metadata = member.get('development', {})
    if set(metadata) != {'source', 'tests', 'notes'}:
        raise ValueError(f'missing development links: {member["name"]}')
    links = []
    for key, label in (('source', 'Source'), ('tests', 'Tests'), ('notes', 'Notes')):
        relative = metadata[key]
        target = within(root, relative)
        if not target.exists():
            raise ValueError(f'missing development target: {relative}')
        kind = 'tree' if target.is_dir() else 'blob'
        links.append(f'[{label}](https://github.com/{repository}/{kind}/main/{relative})')
    return ' | '.join(links)


def readme(root: Path, member: dict, audience: str = 'release') -> bytes:
    references = readme_references(member['readme'], audience)
    text = ''.join(readme_source(root, p).read_text(encoding='utf-8').rstrip() + '\n\n' for p in references)
    text = expand_variables(text, member)
    return expand_fragments(root, text, member, audience=audience).encode('utf-8')


def expand_variables(text: str, member: dict) -> str:
    def replace(match):
        key = match[1]
        value = member.get('variables', {}).get(key)
        if not isinstance(value, str) or '{{' in value:
            raise ValueError(f'missing or invalid variant variable: {key}')
        return value
    result = re.sub(r'\{\{ var: ([a-z_]+) \}\}', replace, text)
    if '{{ var:' in result:
        raise ValueError('unresolved variant variable')
    return result


def expand_fragments(root: Path, text: str, member: dict | None = None, *, audience: str = 'release') -> str:
    """Resolve build-only family projections; packages contain plain Markdown."""
    config = load(root)
    members = config['members']
    ranks = [m.get('family', {}).get('order') for m in members]
    if any(rank is not None for rank in ranks):
        if any(type(rank) is not int or rank < 0 for rank in ranks) or len(ranks) != len(set(ranks)):
            raise ValueError('family order must be a unique nonnegative integer per member')
        members = sorted(members, key=lambda m: m['family']['order'])
    order = [m['name'] for m in members]
    by_name = {m['name']: m for m in members}

    def replace(match):
        key = match[1].strip()
        if key == 'member.development':
            if member is None:
                raise ValueError('member.development requires a member')
            if audience != 'suite':
                raise ValueError('development block requires suite audience')
            return development_links(root, config, member)
        if key == 'suite.development':
            if member is not None:
                raise ValueError('suite.development is only valid in the suite README')
            return '\n'.join(f'- **{item["name"]}**: {development_links(root, config, item)}'
                             for item in members)
        if key == 'suite.repository':
            repository = config.get('repository')
            if repository != 'benjaminstelzer/' + config['name']:
                raise ValueError('missing or unexpected suite repository')
            return 'https://github.com/' + repository
        if key == 'suite.exclusions':
            if member is None:
                raise ValueError('suite.exclusions requires a member')
            return ', '.join(m['name'] for m in members if m['name'] != member['name'])
        if key == 'family.neighbors':
            if member is None:
                raise ValueError('family.neighbors requires a member')
            rows = []
            for entry in member['family']['neighbors']:
                name = entry.get('member', entry.get('external'))
                if 'member' in entry and name not in by_name:
                    raise ValueError(f'unknown neighbor: {name}')
                prefix = 'optional ' if entry.get('optional') else ''
                rows.append(f'- {prefix}`{name}`: {entry["description"]}')
            return '\n'.join(rows)
        if key == 'suite.members':
            if not config.get('member_previews', True):
                return '\n'.join(f'- [{name}](https://github.com/{by_name[name]["repository"]}).'
                                 for name in order if by_name[name]['public_distribution'])
            return '\n'.join(f'- [{name}](members/{name}/README.md).' +
                             (' Private development only. Codex desktop required.'
                             if not by_name[name]['public_distribution'] else '') for name in order)
        if key == 'suite.descriptions':
            if member is not None:
                raise ValueError('suite.descriptions is only valid in the suite README')
            featured = config.get('featured_member')
            if featured is not None and featured not in by_name:
                raise ValueError('unknown featured member')
            selected = ([by_name[featured]] if featured else []) + [m for m in members if m['name'] != featured]
            sections = []
            for item in selected:
                references = item.get('readme', [])
                if not references:
                    raise ValueError(f'missing description: {item["name"]}')
                description = readme_source(root, references[0]).read_text(encoding='utf-8').strip()
                heading, separator, body = description.partition('\n')
                if not heading.startswith('# ') or not separator or not body.strip():
                    raise ValueError(f'expected title and description: {item["name"]}')
                # Descriptions stay self-contained so moving them cannot break relative links.
                if '{{ include:' in description or re.search(r'\]\((?!https?://)[^)]+\)', description):
                    raise ValueError(f'description must use absolute links and no includes: {item["name"]}')
                sections.append('## ' + heading[2:] + '\n' + expand_variables(body, item))
            return '\n\n'.join(sections)
        formats = {'family.owners', 'family.links', 'family.install'}
        if key not in formats:
            raise ValueError(f'unknown build fragment: {key}')
        # Public consumers never inherit a private member through a full list.
        selected = [by_name[name] for name in order if by_name[name]['public_distribution']]
        if key == 'family.links' and member and not member['public_distribution']:
            selected = [by_name[name] for name in order]
        rows = []
        for item in selected:
            name = item['name']
            meta = item['family']
            if key == 'family.owners':
                rows.append(f'- `{name}`: {meta["owner"]}')
            elif key == 'family.links':
                rows.append(f'- [{meta["label"]}](https://github.com/{item["repository"]}) {meta["summary"]}')
            else:
                install_path = ('packages/' + name + '/' + name
                                if item.get('distribution') == 'suite' else name)
                rows.append(f'https://github.com/{item["repository"]}/tree/main/{install_path}')
        return '\n'.join(rows)

    result = re.sub(r'\{\{\s*include:\s*([^{}]+?)\s*\}\}', replace, text)
    if '{{ include:' in result:
        raise ValueError('unresolved build fragment')
    return result


def render_readmes(root: Path, write: bool) -> list[str]:
    config = load(root)
    rendered = {f'members/{m["name"]}/README.md': readme(root, m, 'suite') for m in config['members']} if config.get('member_previews', True) else {}
    rendered['README.md'] = expand_fragments(root, ''.join(readme_source(root, p).read_text(encoding='utf-8').rstrip() + '\n\n' for p in config['readme'])).encode('utf-8')
    changed = []
    for relative, content in rendered.items():
        target = within(root, relative)
        if not target.exists() or target.read_bytes().replace(b'\r\n', b'\n') != content:
            changed.append(relative)
            if write:
                target.write_bytes(content)
    return changed


def package_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix.lower() in {'.md', '.txt', '.py', '.js', '.json', '.svg', '.toml', '.yaml', '.yml'} or path.name in {'LICENSE', '.gitattributes'}:
        data.decode('utf-8')
        return data.replace(b'\r\n', b'\n')
    return data


def payload(root: Path, member: dict) -> dict[str, bytes]:
    result = {'README.md': readme(root, member)}
    for item in member['files']:
        target = item['target']
        within(root, target)
        if target in result:
            raise ValueError(f'duplicate output: {target}')
        if any(p.lower() in {'.git', 'development', '__pycache__', '.env', 'node_modules', '.tmp'} for p in Path(target).parts) or target.lower().endswith(('.pyc', '.pyo')):
            raise ValueError(f'development or local file in package: {target}')
        if target.split('/')[0] != member['name'] and target not in {'LICENSE', 'LICENSE.md', 'LICENSE.txt', 'CHANGELOG.md', '.gitattributes'}:
            raise ValueError(f'non-distribution file: {target}')
        result[target] = package_bytes(within(root, item['source']))
        if item.get('template'):
            result[target] = expand_variables(result[target].decode('utf-8'), member).encode('utf-8')
        if target.endswith('.md') and b'{{' in result[target]:
            result[target] = expand_fragments(root, result[target].decode('utf-8'), member).encode('utf-8')
    for item in member.get('shared_helpers', []):
        target = item['target']
        if target in result:
            raise ValueError(f'duplicate shared output: {target}')
        if not target.startswith(member['name'] + '/scripts/'):
            raise ValueError('shared helper must be bundled in the member scripts directory')
        within(root, target)
        result[target] = package_bytes(within(shared_root(), item['source']))
    if member['name'] + '/SKILL.md' not in result:
        raise ValueError('missing entrypoint')
    validate_package_links(result)
    return result


def validate_package_links(files: dict[str, bytes]) -> None:
    """Check Markdown file destinations against the complete generated inventory."""
    for source, content in files.items():
        # Changelogs retain historical links, not current runtime dependencies.
        if not source.endswith('.md') or Path(source).name == 'CHANGELOG.md':
            continue
        text = content.decode('utf-8')
        text = re.sub(r'^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$', '', text,
                      flags=re.MULTILINE | re.DOTALL)
        text = re.sub(r'(`+).*?\1', '', text)
        destinations = re.findall(r'\]\(\s*(<[^>]+>|(?:[^\s()]|\([^()]*\))+)', text)
        destinations += re.findall(r'^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)', text, re.MULTILINE)
        destinations += re.findall(r'(?:href|src)=["\']([^"\']+)["\']', text)
        for destination in destinations:
            destination = destination.strip('<>')
            parsed = urlsplit(destination)
            if parsed.scheme == 'file' or re.match(r'^[A-Za-z]:', destination):
                raise ValueError(f'local link escapes package: {source}: {destination}')
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            relative = unquote(parsed.path)
            target = posixpath.normpath(posixpath.join(posixpath.dirname(source), relative))
            if ('\\' in relative or relative.startswith('/') or target == '..'
                    or target.startswith('../')):
                raise ValueError(f'local link escapes package: {source}: {destination}')
            if target != '.' and target not in files and not any(p.startswith(target.rstrip('/') + '/') for p in files):
                raise ValueError(f'missing package link target: {source}: {destination}')


def render_sources(root: Path, write: bool) -> list[str]:
    """Maintain declared template previews only, never runtime-helper copies."""
    changed = []
    config = load(root)
    if not config.get('member_previews', True):
        for member in config['members']:
            payload(root, member)
        return changed
    for member in config['members']:
        for item in member['files']:
            if not item.get('template'):
                continue
            content = expand_variables(within(root, item['source']).read_text(encoding='utf-8'), member).encode('utf-8')
            if item['target'].endswith('.md'):
                content = expand_fragments(root, content.decode('utf-8'), member).encode('utf-8')
            relative = f'members/{member["name"]}/{item["target"]}'
            target = within(root, relative)
            if not target.exists() or target.read_bytes().replace(b'\r\n', b'\n') != content:
                changed.append(relative)
                if write:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(content)
    return changed


def build(root: Path, output: Path, public: bool, selected: list[str]) -> dict:
    root, output = root.resolve(), output.resolve()
    if output == root or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError('output must be outside the suite source tree')
    if output.exists():
        raise ValueError('output must not exist; never overwrite a checkout')
    config = load(root)
    known = {m['name'] for m in config['members']}
    if set(selected) - known:
        raise ValueError('unknown selected member')
    members = [m for m in config['members'] if not selected or m['name'] in selected]
    if public and selected and any(not m['public_distribution'] for m in members):
        raise ValueError('selected member is not approved for public distribution')
    if public:
        members = [m for m in members if m['public_distribution']]
    prepared = [(m, payload(root, m)) for m in members]
    revision = subprocess.run(['git', '-C', str(root), 'rev-parse', '--verify', 'HEAD'], capture_output=True, text=True)
    dirty = subprocess.run(['git', '-C', str(root), 'status', '--porcelain'], capture_output=True, text=True, check=True)
    shared_sources = {'build/build_suite.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    for member in members:
        for reference in readme_references(member['readme'], 'release'):
            if reference.startswith('shared:'):
                key = 'readme/' + reference.removeprefix('shared:')
                shared_sources[key] = hashlib.sha256(readme_source(root, reference).read_bytes()).hexdigest()
        for helper in member.get('shared_helpers', []):
            shared_sources[helper['source']] = hashlib.sha256(within(shared_root(), helper['source']).read_bytes()).hexdigest()
    receipt = {'schema_version': 1, 'suite': config['name'], 'source_commit': revision.stdout.strip() if revision.returncode == 0 else None,
               'manifest_sha256': hashlib.sha256((root / 'suite.json').read_bytes()).hexdigest(),
               'shared_sources': shared_sources,
               'source_dirty': bool(dirty.stdout), 'public_only': public, 'members': []}
    output.mkdir(parents=True, exist_ok=False)
    for member, files in prepared:
        hashes = {}
        for relative, content in sorted(files.items()):
            target = within(output / package_path(config, member), relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
            hashes[relative] = hashlib.sha256(content).hexdigest()
        receipt['members'].append({'name': member['name'], 'repository': member['repository'],
                                  'distribution': member.get('distribution', 'standalone'),
                                  'package_path': package_path(config, member),
                                  'visibility': member['visibility'], 'files': hashes})
    (output / 'build-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    return receipt


def verify_shared_helpers(root: Path, output: Path) -> list[str]:
    """Compare generated copies with their current canonical sources, read-only."""
    config = load(root)
    members = {m['name']: m for m in config['members']}
    receipt = json.loads((output / 'build-receipt.json').read_text(encoding='utf-8'))
    errors = []
    for built in receipt['members']:
        member = members[built['name']]
        for helper in member.get('shared_helpers', []):
            source = package_bytes(within(shared_root(), helper['source']))
            target = within(output / package_path(config, member), helper['target'])
            if not target.is_file() or target.read_bytes() != source:
                errors.append(member['name'] + ': shared helper drift: ' + helper['target'])
    return errors


def verify_packages(root: Path, output: Path) -> list[str]:
    """Detect edited packages and stale projections against current suite sources."""
    config = load(root)
    members = {m['name']: m for m in config['members']}
    receipt = json.loads((output / 'build-receipt.json').read_text(encoding='utf-8'))
    errors = []
    for built in receipt['members']:
        member = members[built['name']]
        expected = payload(root, member)
        folder = within(output, package_path(config, member))
        actual = {p.relative_to(folder).as_posix(): p.read_bytes()
                  for p in folder.rglob('*') if p.is_file()}
        if actual != expected:
            errors.append(member['name'] + ': package differs from current sources')
    return errors


def main(default_root: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=default_root)
    parser.add_argument('--output', type=Path)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--check-readmes', action='store_true')
    modes.add_argument('--write-readmes', action='store_true')
    modes.add_argument('--check-helpers', action='store_true')
    modes.add_argument('--check-packages', action='store_true')
    modes.add_argument('--check-sources', action='store_true')
    modes.add_argument('--write-sources', action='store_true')
    parser.add_argument('--public-only', action='store_true')
    parser.add_argument('--member', action='append', default=[])
    args = parser.parse_args()
    if args.root is None:
        parser.error('--root is required when running the shared builder directly')
    try:
        if args.check_sources or args.write_sources:
            changed = render_sources(args.root, args.write_sources)
            print(json.dumps({'changed': changed, 'written': args.write_sources}))
            return int(bool(changed) and args.check_sources)
        if args.check_readmes or args.write_readmes:
            changed = render_readmes(args.root, args.write_readmes)
            print(json.dumps({'changed': changed, 'written': args.write_readmes}))
            return int(bool(changed) and args.check_readmes)
        if args.output is None:
            parser.error('--output is required for package builds')
        if args.check_helpers or args.check_packages:
            check = verify_packages if args.check_packages else verify_shared_helpers
            errors = check(args.root, args.output)
            print(json.dumps({'valid': not errors, 'errors': errors}))
            return int(bool(errors))
        result = build(args.root, args.output, args.public_only, args.member)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'BUILD FAILED: {error}\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'members'} | {'members': [m['name'] for m in result['members']]}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
