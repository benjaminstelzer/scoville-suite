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
    if Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError(f'unsafe path: {relative}')
    requested_root = root.absolute()
    candidate = requested_root / relative
    resolved_root = requested_root.resolve()
    resolved = candidate.resolve()
    if not resolved.is_relative_to(resolved_root):
        raise ValueError(f'path escapes source: {relative}')
    current = candidate
    while True:
        if current.is_symlink() or (hasattr(current, 'is_junction') and current.is_junction()):
            raise ValueError(f'symlink not allowed: {relative}')
        if current == requested_root:
            break
        current = current.parent
    return resolved


def load(root: Path, profile: str | None = None, layout: str | None = None) -> dict:
    data = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
    profiles = data.pop('profiles', {})
    if profiles:
        default_profile = data.pop('default_profile')
        selected = profile or default_profile
        if selected not in profiles:
            raise ValueError('unknown build profile: ' + str(selected))
        settings = profiles[selected]
        if set(settings) - {'name', 'repository', 'readme'}:
            raise ValueError('unsupported profile setting')
        data.update(settings)
        data['profile'] = selected
        data['catalog'] = [
            {'name': m['name'], 'repository': m['repository'],
             'availability': m.get('availability', '')}
            for m in data['members'] if selected in m.get('catalog_profiles', [])
            and selected not in m.get('profiles', list(profiles)) and m['public_distribution']]
        def included(entry):
            choices = entry.pop('profiles', list(profiles))
            if not isinstance(choices, list) or not choices or set(choices) - profiles.keys():
                raise ValueError('invalid profile selection')
            return selected in choices
        all_names = {m['name'] for m in data['members']}
        data['members'] = [m for m in data['members'] if included(m)]
        names = {m['name'] for m in data['members']}
        if data.get('featured_member') not in names:
            data.pop('featured_member', None)
        for member in data['members']:
            member['files'] = [item for item in member['files'] if included(item)]
            if member.get('distribution') == 'suite':
                member['repository'] = data['repository']
            neighbors = member.get('family', {}).get('neighbors', [])
            member.get('family', {})['neighbors'] = [entry for entry in neighbors
                if not (entry.get('optional') and entry.get('member') in all_names and entry.get('member') not in names)]
    elif profile is not None and profile != data.get('profile'):
        raise ValueError('unknown build profile: ' + profile)
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
    selected_layout = layout or data.get('layout', 'suite' if data.get('profile') == 'codex' else 'standalone')
    if data.get('profile') == 'codex' and selected_layout == 'standalone':
        data['members'] = [m for m in data['members'] if 'codex' in m.get('standalone_profiles', [])]
        if not data['members']:
            raise ValueError('Codex edition is suite-only without explicitly standalone members')
        if data.get('featured_member') not in {m['name'] for m in data['members']}:
            data.pop('featured_member', None)
    if selected_layout not in {'standalone', 'suite'}:
        raise ValueError('unknown package layout')
    if 'layout' in data and selected_layout != data['layout']:
        raise ValueError('exported sources retain their package layout')
    data['layout'] = selected_layout
    if selected_layout == 'suite':
        for member in data['members']:
            member['distribution'] = 'suite'
            member['repository'] = data['repository']
    for member in data['members']:
        prefix = 'packages/' + member['name'] + '/' if member.get('distribution') == 'suite' else ''
        member.setdefault('variables', {})['contract_url'] = (
            'https://github.com/' + member['repository'] + '/blob/main/' + prefix + member['name'] + '/SKILL.md')
    return data


def select_text(text: str, kind: str, selected: str | None, allowed: set[str]) -> str:
    pattern = r'\{\{ ' + kind + r': ([a-z]+) \}\}(.*?)\{\{ /' + kind + r' \}\}'
    def replace(match):
        if match[1] not in allowed or '{{ ' + kind + ':' in match[2] or selected not in allowed:
            raise ValueError('invalid or unselected ' + kind + ' block')
        return match[2] if match[1] == selected else ''
    result = re.sub(pattern, replace, text, flags=re.S)
    if '{{ ' + kind + ':' in result or '{{ /' + kind in result:
        raise ValueError('unknown or unclosed ' + kind + ' block')
    return result


def profile_text(text: str, profile: str | None) -> str:
    return select_text(text, 'profile', profile, {'general', 'codex'})


def variant_text(text: str, config: dict) -> str:
    return select_text(profile_text(text, config.get('profile')), 'package',
                       config.get('layout', 'standalone'), {'standalone', 'suite'})


def readme_source(root: Path, reference: str) -> Path:
    if reference.startswith('shared:'):
        return within(shared_root() / 'readme', reference.removeprefix('shared:'))
    return within(root, reference)


def file_source(root: Path, reference: str) -> Path:
    if reference.startswith('shared:'):
        return within(shared_root(), reference.removeprefix('shared:'))
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


def readme(root: Path, member: dict, audience: str = 'release', config: dict | None = None) -> bytes:
    config = config if config is not None else load(root)
    references = readme_references(member['readme'], audience)
    if config.get('layout') == 'suite':
        references = [p for p in references if p != 'shared:family.md']
    text = ''.join(expand_fragments(root, expand_variables(readme_source(root, p).read_text(encoding='utf-8'), member), member, audience=audience, config=config).rstrip() + '\n\n' for p in references)
    if 'description_fragments' in member:
        expected = ['How it works', 'What it enforces', 'What it costs',
                    'How it was developed', 'Compatibility', 'Install',
                    'How to use', 'Sources', 'Family', 'License']
        if config.get('layout') == 'suite':
            expected.remove('Family')
        actual = re.findall(r'^## (.+)$', text, re.M)
        # Shared family and license headings are expanded from their files above.
        if actual != expected:
            raise ValueError(f'noncanonical README sections for {member["name"]}: {actual}')
        if member['readme'][:4] != member['description_fragments']:
            raise ValueError('description_fragments must be the first four README entries')
    return (text.rstrip() + '\n').encode('utf-8')


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


def expand_fragments(root: Path, text: str, member: dict | None = None, *, audience: str = 'release', config: dict | None = None) -> str:
    """Resolve build-only family projections; packages contain plain Markdown."""
    config = config if config is not None else load(root)
    text = variant_text(text, config)
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
        if key == 'family.contract':
            return variant_text(within(shared_root(), 'runtime/skill_composition.md').read_text(encoding='utf-8'), config).strip()
        if key.startswith('family.') and config.get('layout') == 'suite':
            if key not in {'family.catalog', 'family.owners', 'family.neighbors', 'family.links', 'family.install'}:
                raise ValueError('unknown build fragment: ' + key)
            return ''
        if key == 'prompting.defaults':
            return within(shared_root(), 'prompting/models.toml').read_text(encoding='utf-8').strip()
        if key == 'member.defaults':
            if member is None:
                raise ValueError('member.defaults requires a member')
            target = member['name'] + '/config.default.json'
            sources = [item['source'] for item in member['files'] if item['target'] == target]
            if len(sources) != 1:
                raise ValueError('member.defaults requires one canonical config.default.json')
            return within(root, sources[0]).read_text(encoding='utf-8').strip()
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
        if key == 'suite.catalog':
            if member is not None:
                raise ValueError('suite.catalog is only valid in the suite README')
            entries = config.get('catalog', [])
            if not entries:
                return ''
            return '## Additional Scoville Skills\n\n' + '\n\n'.join(
                f'### {item["name"]}\n\n{item["availability"]}. Available as a standalone Skill.\n\n'
                f'Ask your Codex host:\n\n```text\nInstall this Skill for all my projects from this exact package directory:\n'
                f'https://github.com/{item["repository"]}/tree/main/{item["name"]}\n'
                'Preserve personal settings and unrelated Skills. Report the installed location\n'
                'and whether the host discovers the Skill.\n```'
                for item in entries)
        if key == 'suite.repository':
            repository = config.get('repository')
            if repository != 'benjaminstelzer/' + config['name']:
                raise ValueError('missing or unexpected suite repository')
            return 'https://github.com/' + repository
        if key == 'suite.exclusions':
            if member is None:
                raise ValueError('suite.exclusions requires a member')
            return ', '.join(m['name'] for m in members if m['name'] != member['name'])
        if key == 'family.catalog':
            return '\n'.join(f'- [{m.get("family", {}).get("label", m["name"])}](https://github.com/{m["repository"]})'
                             + (' ' + m['family']['summary'] if 'family' in m else '.')
                             for m in members if m['public_distribution'])
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
                references = item.get('description_fragments', item.get('readme', [])[:1])
                if not references:
                    raise ValueError(f'missing description: {item["name"]}')
                description = '\n\n'.join(variant_text(readme_source(root, ref).read_text(encoding='utf-8'), config).strip() for ref in references)
                description = expand_variables(description, item)
                heading, separator, body = description.partition('\n')
                if not heading.startswith('# ') or not separator or not body.strip():
                    raise ValueError(f'expected title and description: {item["name"]}')
                # Descriptions stay self-contained so moving them cannot break relative links.
                if '{{ include:' in description or re.search(r'\]\((?!https?://)[^)]+\)', description):
                    raise ValueError(f'description must use absolute links and no includes: {item["name"]}')
                title = heading[2:]
                full_readme = readme(root, item, 'suite', config).decode()
                if '\n## How to use\n' not in full_readme:
                    raise ValueError(f'missing How to use section: {item["name"]}')
                description += (f'\n\n[How to use {title}]'
                                f'(members/{item["name"]}/README.md#how-to-use).')
                lines = []
                fenced = False
                for line in description.splitlines():
                    if line.startswith('```'):
                        fenced = not fenced
                    if not fenced and re.match(r'^#{1,5} ', line):
                        line = '#' + line
                    lines.append(line)
                sections.append('\n'.join(lines))
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


def render_readmes(root: Path, write: bool, config: dict | None = None, destination: Path | None = None) -> list[str]:
    config = config if config is not None else load(root)
    destination = destination or root
    rendered = {f'members/{m["name"]}/README.md': readme(root, m, 'suite', config) for m in config['members']} if config.get('member_previews', True) else {}
    rendered['README.md'] = ''.join(expand_fragments(root, readme_source(root, p).read_text(encoding='utf-8'), config=config).rstrip() + '\n\n' for p in config['readme']).encode('utf-8')
    changed = []
    for relative, content in rendered.items():
        target = within(destination, relative)
        if not target.exists() or target.read_bytes().replace(b'\r\n', b'\n') != content:
            changed.append(relative)
            if write:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    return changed


def package_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix.lower() in {'.md', '.txt', '.py', '.js', '.json', '.svg', '.toml', '.yaml', '.yml'} or path.name in {'LICENSE', '.gitattributes'}:
        data.decode('utf-8')
        return data.replace(b'\r\n', b'\n')
    return data


def payload(root: Path, member: dict, config: dict | None = None) -> dict[str, bytes]:
    result = {'README.md': readme(root, member, config=config)}
    for item in member['files']:
        target = item['target']
        within(root, target)
        if target in result:
            raise ValueError(f'duplicate output: {target}')
        if any(p.lower() in {'.git', 'development', '__pycache__', '.env', 'node_modules', '.tmp'} for p in Path(target).parts) or target.lower().endswith(('.pyc', '.pyo')):
            raise ValueError(f'development or local file in package: {target}')
        if target.split('/')[0] != member['name'] and target not in {'LICENSE', 'LICENSE.md', 'LICENSE.txt', 'CHANGELOG.md', '.gitattributes'}:
            raise ValueError(f'non-distribution file: {target}')
        result[target] = package_bytes(file_source(root, item['source']))
        if item.get('template'):
            result[target] = expand_variables(result[target].decode('utf-8'), member).encode('utf-8')
        if target.endswith(('.md', '.toml')) and b'{{' in result[target]:
            result[target] = expand_fragments(root, result[target].decode('utf-8'), member, config=config).encode('utf-8')
    for item in member.get('shared_helpers', []):
        target = item['target']
        if target in result:
            raise ValueError(f'duplicate shared output: {target}')
        if not target.startswith(member['name'] + '/scripts/'):
            raise ValueError('shared helper must be bundled in the member scripts directory')
        within(root, target)
        result[target] = package_bytes(file_source(root, 'shared:' + item['source']))
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


def render_sources(root: Path, write: bool, config: dict | None = None) -> list[str]:
    """Maintain declared template previews only, never runtime-helper copies."""
    changed = []
    config = config if config is not None else load(root)
    if not config.get('member_previews', True):
        for member in config['members']:
            payload(root, member, config)
        return changed
    for member in config['members']:
        for item in member['files']:
            if not item.get('template'):
                continue
            content = expand_variables(within(root, item['source']).read_text(encoding='utf-8'), member).encode('utf-8')
            if item['target'].endswith('.md'):
                content = expand_fragments(root, content.decode('utf-8'), member, config=config).encode('utf-8')
            relative = f'members/{member["name"]}/{item["target"]}'
            target = within(root, relative)
            if not target.exists() or target.read_bytes().replace(b'\r\n', b'\n') != content:
                changed.append(relative)
                if write:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(content)
    return changed


def build(root: Path, output: Path, public: bool, selected: list[str], profile: str | None = None, layout: str | None = None, refresh: bool = False) -> dict:
    root, output = root.resolve(), output.resolve()
    if output == root or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError('output must be outside the suite source tree')
    if output.exists() and not refresh:
        raise ValueError('output must not exist; never overwrite a checkout')
    config = load(root, profile, layout)
    known = {m['name'] for m in config['members']}
    if set(selected) - known:
        raise ValueError('unknown selected member')
    if config.get('layout') == 'suite' and selected and set(selected) != known:
        raise ValueError('suite packages require the complete member set')
    members = [m for m in config['members'] if not selected or m['name'] in selected]
    if public and selected and any(not m['public_distribution'] for m in members):
        raise ValueError('selected member is not approved for public distribution')
    if public and config.get('layout') == 'suite' and any(not m['public_distribution'] for m in members):
        raise ValueError('complete suite contains a member not approved for public distribution')
    if public:
        members = [m for m in members if m['public_distribution']]
    prepared = [(m, payload(root, m, config)) for m in members]
    revision = subprocess.run(['git', '-C', str(root), 'rev-parse', '--verify', 'HEAD'], capture_output=True, text=True)
    dirty = subprocess.run(['git', '-C', str(root), 'status', '--porcelain'], capture_output=True, text=True, check=True)
    shared_sources = {'build/build_suite.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    for member in members:
        for reference in readme_references(member['readme'], 'release'):
            if reference.startswith('shared:'):
                key = 'readme/' + reference.removeprefix('shared:')
                shared_sources[key] = hashlib.sha256(readme_source(root, reference).read_bytes()).hexdigest()
        for item in member.get('files', []):
            if item['source'].startswith('shared:'):
                key = item['source'].removeprefix('shared:')
                shared_sources[key] = hashlib.sha256(file_source(root, item['source']).read_bytes()).hexdigest()
            elif b'{{ include: prompting.defaults }}' in file_source(root, item['source']).read_bytes():
                key = 'prompting/models.toml'
                shared_sources[key] = hashlib.sha256(within(shared_root(), key).read_bytes()).hexdigest()
        for helper in member.get('shared_helpers', []):
            shared_sources[helper['source']] = hashlib.sha256(within(shared_root(), helper['source']).read_bytes()).hexdigest()
    shared_sources['runtime/skill_composition.md'] = hashlib.sha256(within(shared_root(), 'runtime/skill_composition.md').read_bytes()).hexdigest()
    receipt = {'layout': config.get('layout'), 'profile': config.get('profile'), 'schema_version': 1, 'suite': config['name'], 'source_commit': revision.stdout.strip() if revision.returncode == 0 else None,
               'manifest_sha256': hashlib.sha256((root / 'suite.json').read_bytes()).hexdigest(),
               'shared_sources': shared_sources,
               'source_dirty': bool(dirty.stdout), 'public_only': public, 'members': []}
    if output.exists():
        receipt_path = within(output, 'build-receipt.json')
        old = json.loads(receipt_path.read_text(encoding='utf-8'))
        if (old.get('suite'), old.get('profile'), old.get('layout')) != (config['name'], config.get('profile'), config.get('layout')):
            raise ValueError('refresh requires the same suite/profile/layout')
        expected_paths = {'build-receipt.json'} | {
            package_path(config, member) + '/' + relative
            for member, files in prepared for relative in files}
        actual_paths = {p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file()}
        if actual_paths != expected_paths:
            raise ValueError('refresh inventory changed; reconcile obsolete staging files first')
        old_hashes = {m['package_path'] + '/' + name: digest
                      for m in old['members'] for name, digest in m['files'].items()}
        if set(old_hashes) != expected_paths - {'build-receipt.json'}:
            raise ValueError('refresh receipt inventory mismatch')
        for relative, digest in old_hashes.items():
            if hashlib.sha256(within(output, relative).read_bytes()).hexdigest() != digest:
                raise ValueError('refresh refuses changed staging file: ' + relative)
    else:
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
                                  'visibility': member['visibility'], 'files': hashes,
                                  'sizes': size_report(member['name'], files)})
    (output / 'build-receipt.json').write_text(
        json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
    return receipt


def size_report(member_name: str, files: dict[str, bytes], traces: list[dict] | None = None) -> dict:
    """Report bytes, not token estimates or mandatory limits."""
    sizes = {name: len(content) for name, content in sorted(files.items())}
    routes = []
    for trace in traces or []:
        served = trace.get('served_files')
        if not isinstance(served, list):
            raise ValueError('load trace must contain served_files from an existing runner summary')
        paths, matched = [], True
        for entry in served:
            path = member_name + '/' + entry['path']
            if path not in files:
                raise ValueError('trace references a file absent from the current package: ' + path)
            paths.append(path)
            matched = matched and entry.get('sha256') == hashlib.sha256(files[path]).hexdigest()
        count = sum(sizes[path] for path in paths)
        routes.append({'case_id': trace.get('case_id'), 'reference_reads': paths,
                       'matches_current_files': matched,
                       'observed_reference_bytes': count if matched else None,
                       'current_equivalent_reference_bytes': count})
    return {'package_bytes': sum(sizes.values()),
            'entrypoint_bytes': sizes[member_name + '/SKILL.md'],
            'file_bytes': sizes, 'observed_routes': routes}


def verify_shared_helpers(root: Path, output: Path) -> list[str]:
    """Compare generated copies with their current canonical sources, read-only."""
    receipt = json.loads((output / 'build-receipt.json').read_text(encoding='utf-8'))
    config = load(root, receipt.get('profile'), receipt.get('layout'))
    members = {m['name']: m for m in config['members']}
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
    receipt = json.loads((output / 'build-receipt.json').read_text(encoding='utf-8'))
    config = load(root, receipt.get('profile'), receipt.get('layout'))
    members = {m['name']: m for m in config['members']}
    errors = []
    for built in receipt['members']:
        member = members[built['name']]
        expected = payload(root, member, config)
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
    modes.add_argument('--size-report', action='store_true', help='Report package bytes without writing a build')
    parser.add_argument('--load-trace', nargs=2, action='append', default=[], metavar=('MEMBER', 'SUMMARY'), help='Existing runner summary for observed reference loads; use with --size-report')
    modes.add_argument('--check-readmes', action='store_true')
    modes.add_argument('--write-readmes', action='store_true')
    modes.add_argument('--check-helpers', action='store_true')
    modes.add_argument('--check-packages', action='store_true')
    modes.add_argument('--check-sources', action='store_true')
    modes.add_argument('--write-sources', action='store_true')
    parser.add_argument('--refresh', action='store_true', help='Refresh an intact staging build with the same inventory; never delete files')
    parser.add_argument('--public-only', action='store_true')
    parser.add_argument('--profile')
    parser.add_argument('--layout', choices=['standalone', 'suite'])
    parser.add_argument('--member', action='append', default=[])
    args = parser.parse_args()
    if args.root is None:
        parser.error('--root is required when running the shared builder directly')
    try:
        if args.load_trace and not args.size_report:
            raise ValueError('--load-trace requires --size-report')
        if args.size_report:
            config = load(args.root, args.profile, args.layout)
            selected = set(args.member) or {m['name'] for m in config['members']}
            known = {m['name'] for m in config['members']}
            if selected - known or any(name not in selected for name, _ in args.load_trace):
                raise ValueError('unknown or unselected size-report member')
            reports = []
            for member in config['members']:
                if member['name'] not in selected:
                    continue
                traces = [json.loads(Path(path).read_text(encoding='utf-8'))
                          for name, path in args.load_trace if name == member['name']]
                reports.append({'name': member['name'], **size_report(member['name'], payload(args.root, member, config), traces)})
            print(json.dumps({'profile': config.get('profile'), 'members': reports}))
            return 0
        if args.check_sources or args.write_sources:
            config = load(args.root, args.profile, args.layout)
            if (args.profile or args.layout) and (config.get('profile'), config.get('layout')) != (load(args.root).get('profile'), load(args.root).get('layout')):
                raise ValueError('source previews use the default profile only')
            changed = render_sources(args.root, args.write_sources, config)
            print(json.dumps({'changed': changed, 'written': args.write_sources}))
            return int(bool(changed) and args.check_sources)
        if args.check_readmes or args.write_readmes:
            config = load(args.root, args.profile, args.layout)
            if (args.profile or args.layout) and args.output is None and (config.get('profile'), config.get('layout')) != (load(args.root).get('profile'), load(args.root).get('layout')):
                raise ValueError('non-default README profiles require --output')
            changed = render_readmes(args.root, args.write_readmes, config, args.output)
            print(json.dumps({'changed': changed, 'written': args.write_readmes}))
            return int(bool(changed) and args.check_readmes)
        if args.output is None:
            parser.error('--output is required for package builds')
        if args.check_helpers or args.check_packages:
            check = verify_packages if args.check_packages else verify_shared_helpers
            errors = check(args.root, args.output)
            print(json.dumps({'valid': not errors, 'errors': errors}))
            return int(bool(errors))
        result = build(args.root, args.output, args.public_only, args.member, args.profile, args.layout, args.refresh)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'BUILD FAILED: {error}\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'members'} | {'members': [m['name'] for m in result['members']]}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
