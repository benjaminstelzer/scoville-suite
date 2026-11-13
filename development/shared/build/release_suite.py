#!/usr/bin/env python3
"""Prepare and publish a suite release from committed sources.

prepare  builds every package view, checks its publication receipt, exports and
         validates the suite sources, scans them for personal paths and stages
         the result in each local target repository. It commits and pushes nothing.
publish  commits exactly the content prepare staged, pushes main and compares
         every remote with its local commit. Run it only after the user approved
         the push. After a failed push, run it again: it continues.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent
STATE = 'release-state.json'
PUBLISHED = 'published.json'
# Targets are pushed only to these hosts; a local path has host None.
HOSTS = ('github.com',)


class ReleaseError(Exception):
    """A refusal with its cause and the correction."""


def run(argv, cwd=None):
    return subprocess.run([str(a) for a in argv], cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')


def git(repo, *args):
    done = run(['git', '-C', repo, *args])
    if done.returncode:
        raise ReleaseError(f'git {" ".join(args)} failed in {repo}: {done.stderr.strip() or done.stdout.strip()}')
    return done.stdout


def head(repo):
    return git(repo, 'rev-parse', '--verify', 'HEAD').strip()


def require_clean_main(repo, role):
    branch = git(repo, 'branch', '--show-current').strip()
    if branch != 'main':
        raise ReleaseError(f'{role} {repo} is on branch "{branch}", not main. Switch it to main and rerun.')
    if git(repo, 'status', '--porcelain').strip():
        raise ReleaseError(f'{role} {repo} has uncommitted changes. Commit them and rerun; a release is built from committed sources.')


def targets(manifest, release, public):
    """Each local target repository with the staging tree that fills it."""
    result = []
    for profile, entry in manifest['profiles'].items():
        name = entry['repository'].rsplit('/', 1)[-1]
        result.append({'repository': entry['repository'], 'directory': str(Path(public) / name),
                       'source': str(Path(release) / f'export-{profile}'), 'kind': 'suite', 'profile': profile})
    default = manifest['default_profile']
    for member in manifest['members']:
        if member.get('distribution') == 'suite' or member.get('visibility') != 'public':
            continue
        profiles = member.get('profiles') or list(manifest['profiles'])
        profile = default if default in profiles else profiles[0]
        name = member['repository'].rsplit('/', 1)[-1]
        result.append({'repository': member['repository'], 'directory': str(Path(public) / name),
                       'source': str(Path(release) / f'standalone-{profile}' / name), 'kind': 'member', 'profile': profile})
    return result


def remote_identity(url):
    """Host and owner/repository of a remote URL; the host of a local path is None."""
    url = url.strip().replace('\\', '/').removesuffix('/').removesuffix('.git')
    scp = re.fullmatch(r'[\w.-]+@([\w.-]+):(.+)', url)
    if scp:
        host, path = scp.group(1), scp.group(2)
    elif '://' in url:
        parts = urlsplit(url)
        host, path = parts.hostname, parts.path
    else:
        host, path = None, url
    return (host.lower() if host else None), '/'.join(path.strip('/').split('/')[-2:]).lower()


def check_target(target):
    """Refuse a directory that is not the expected checkout, pushes elsewhere or holds unstaged changes."""
    directory, repository = Path(target['directory']), target['repository']
    if not (directory / '.git').exists():
        raise ReleaseError(f'Target {directory} is not a Git checkout. Clone https://github.com/{repository} there and rerun.')
    # Fetch and push addresses can differ: publish verifies through the first and writes through the others.
    urls = (git(directory, 'remote', 'get-url', 'origin').splitlines()
            + git(directory, 'remote', 'get-url', '--push', '--all', 'origin').splitlines())
    for url in urls:
        host, name = remote_identity(url)
        if host not in HOSTS or name != repository.lower():
            raise ReleaseError(f'Target {directory} has the origin address {url.strip()}, expected {repository} on {HOSTS[0]}. '
                               'Set the fetch and push address of origin to that repository and rerun.')
    branch = git(directory, 'branch', '--show-current').strip()
    if branch != 'main':
        raise ReleaseError(f'Target {directory} is on branch "{branch}", not main. Switch it to main and rerun.')
    loose = [line for line in git(directory, 'status', '--porcelain').splitlines() if line[:2] == '??' or line[1] != ' ']
    if loose:
        raise ReleaseError(f'Target {directory} has changes this command did not stage ({loose[0].strip()}). '
                           'Targets are generated; move the edit to its source, discard it in the target and rerun.')


def mirror(source, target):
    """Make target equal to source, leaving the target's .git untouched."""
    source, target = Path(source), Path(target)
    if not source.is_dir():
        raise ReleaseError(f'Staging tree {source} is missing. The build or export for it did not run; rerun prepare.')
    wanted = {p.relative_to(source) for p in source.rglob('*') if p.is_file()}
    for path in sorted(target.rglob('*'), reverse=True):
        relative = path.relative_to(target)
        if relative.parts[0] == '.git':
            continue
        if path.is_file() or path.is_symlink():
            if relative not in wanted:
                path.unlink()
        elif not any(path.iterdir()):
            path.rmdir()
    for relative in sorted(wanted):
        destination = target / relative
        data = (source / relative).read_bytes()
        if not destination.is_file() or destination.read_bytes() != data:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)


def personal_needles():
    home = Path.home()
    name = home.name
    return sorted({str(home), home.as_posix(), f'Users/{name}', f'Users\\{name}', f'home/{name}'}, key=len, reverse=True)


def scan_personal(roots, needles):
    """Lines in text files that contain one of the needles, as path:line."""
    lowered = [n.lower().encode() for n in needles if n]
    hits = []
    for root in roots:
        for path in sorted(Path(root).rglob('*')):
            if not path.is_file() or '.git' in path.relative_to(root).parts:
                continue
            data = path.read_bytes()
            if b'\0' in data[:4096] or not any(n in data.lower() for n in lowered):
                continue
            for number, line in enumerate(data.splitlines(), 1):
                if any(n in line.lower() for n in lowered):
                    hits.append(f'{path}:{number}')
    return hits


def remove_tree(path, trash):
    """Delete a generated tree; a sync client may hold files open, so retry and then move it aside."""
    path = Path(path)
    for _ in range(4):
        shutil.rmtree(path, ignore_errors=True)
        if not path.exists():
            return
        time.sleep(3)
    if trash:
        Path(trash).mkdir(parents=True, exist_ok=True)
        moved = Path(trash) / f'{path.name}-{uuid.uuid4().hex[:8]}'
        try:
            shutil.move(str(path), str(moved))
            return
        except OSError as error:
            raise ReleaseError(f'Could not delete or move {path}: {error}. Close the program holding it open and rerun.') from error
    raise ReleaseError(f'Could not delete {path}; another program holds a file open. '
                       'Close it and rerun, or pass --trash <directory> to move the tree aside.')


def recorded_run(release):
    for receipt in sorted(Path(release).glob('*/build-receipt.json')):
        try:
            value = json.loads(receipt.read_text(encoding='utf-8')).get('runtime_validation', {}).get('run')
        except (OSError, ValueError):
            continue
        if value:
            return value
    return None


def tool(root, name):
    local = Path(root) / 'development' / name
    return local if local.is_file() else HERE / name


def step(label, argv, cwd):
    done = run(argv, cwd)
    if done.returncode:
        detail = (done.stderr.strip() or done.stdout.strip())[-1500:]
        raise ReleaseError(f'{label} failed:\n{detail}')
    return done.stdout


def build_view(root, release, profile, layout, runtime_run, trash):
    output = Path(release) / f'{layout}-{profile}'
    base = [sys.executable, '-X', 'utf8', tool(root, 'build_suite.py'), '--profile', profile, '--layout', layout, '--public-only', '--output', output]
    build = [*base, '--runtime-run', runtime_run]
    if output.exists():
        done = run([*build, '--refresh'], root)
        if done.returncode and 'refresh' in (done.stderr + done.stdout):
            # The file inventory changed; staging is generated output, so rebuild it from scratch.
            remove_tree(output, trash)
            step(f'Build {layout}-{profile}', build, root)
        elif done.returncode:
            raise ReleaseError(f'Build {layout}-{profile} failed:\n{(done.stderr.strip() or done.stdout.strip())[-1500:]}')
    else:
        step(f'Build {layout}-{profile}', build, root)
    receipt = step(f'Publication check {layout}-{profile}', [*base, '--check-publication'], root)
    try:
        valid = json.loads(receipt.strip().splitlines()[-1]).get('valid') is True
    except (ValueError, IndexError):
        valid = False
    if not valid:
        raise ReleaseError(f'Publication check {layout}-{profile} did not report valid: {receipt.strip()[-600:]}')


def export_view(root, release, profile, trash):
    output = Path(release) / f'export-{profile}'
    receipt = Path(release) / f'export-{profile}-receipt.json'
    if output.exists():
        remove_tree(output, trash)
    receipt.unlink(missing_ok=True)
    step(f'Export {profile}', [sys.executable, '-X', 'utf8', HERE / 'export_suite.py', '--root', root, '--output', output,
                               '--profile', profile, '--receipt', receipt], root)
    validators = sorted(output.glob('members/*/*/scripts/validate_profile.py'))
    if len(validators) == 1:
        step(f'Plan validation of export-{profile}', [sys.executable, '-X', 'utf8', validators[0], '--root', output, '--format', 'text'], root)
    return output


def prepare(root, release, public, runtime_run=None, trash=None):
    root, release, public = Path(root).resolve(), Path(release).resolve(), Path(public).resolve()
    manifest = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
    shared = HERE.parent
    require_clean_main(root, 'Suite source')
    if (shared / '.git').exists():
        require_clean_main(shared, 'Shared source')
    step('Shared snapshot check', [sys.executable, '-X', 'utf8', HERE / 'sync_suite_sources.py', '--root', root, '--check'], root)
    planned = targets(manifest, release, public)
    for target in planned:
        check_target(target)
    runtime_run = runtime_run or recorded_run(release)
    if not runtime_run:
        raise ReleaseError('No runtime run is recorded in the staging receipts. Pass --runtime-run <Actions URL of the passed Runtime helpers run>.')
    release.mkdir(parents=True, exist_ok=True)
    scanned = []
    for profile in manifest['profiles']:
        for layout in ('suite', 'standalone'):
            build_view(root, release, profile, layout, runtime_run, trash)
        scanned.append(export_view(root, release, profile, trash))
    scanned += [Path(t['source']) for t in planned if t['kind'] == 'member']
    hits = scan_personal(scanned, personal_needles())
    if hits:
        raise ReleaseError('Personal paths found in release content; fix the source, commit and rerun:\n' + '\n'.join(hits[:40]))
    for target in planned:
        mirror(target['source'], target['directory'])
        git(target['directory'], 'add', '-A')
        target['changes'] = git(target['directory'], 'diff', '--cached', '--name-status').splitlines()
        target['head'] = head(target['directory'])
        # publish commits this tree and no other.
        target['tree'] = git(target['directory'], 'write-tree').strip()
        ahead = run(['git', '-C', target['directory'], 'rev-list', '--count', 'origin/main..HEAD'])
        target['unpublished'] = int(ahead.stdout.strip() or 0) if not ahead.returncode else 0
    state = {'source_commit': head(root), 'shared_commit': head(shared) if (shared / '.git').exists() else None,
             'runtime_run': runtime_run, 'targets': planned}
    (release / STATE).write_text(json.dumps(state, indent=1) + '\n', encoding='utf-8')
    (release / PUBLISHED).unlink(missing_ok=True)
    return state


def target_stage(target):
    """'prepared', 'committed' by an earlier publish run, or None when the content is not what prepare staged."""
    directory = target['directory']
    if git(directory, 'write-tree').strip() != target['tree']:
        return None
    if head(directory) == target['head']:
        return 'prepared'
    parent = run(['git', '-C', directory, 'rev-parse', '--verify', '-q', 'HEAD^']).stdout.strip()
    committed = git(directory, 'rev-parse', 'HEAD^{tree}').strip()
    return 'committed' if parent == target['head'] and committed == target['tree'] else None


def remote_head(directory):
    found = git(directory, 'ls-remote', 'origin', 'refs/heads/main').split()[:1]
    return found[0] if found else None


def publish(root, release, message):
    root, release = Path(root).resolve(), Path(release).resolve()
    state_path = release / STATE
    if not state_path.is_file():
        raise ReleaseError(f'{state_path} is missing. Run prepare first.')
    state = json.loads(state_path.read_text(encoding='utf-8'))
    sources = [('suite', root, state['source_commit'])]
    if state.get('shared_commit'):
        sources.append(('shared', HERE.parent, state['shared_commit']))
    for role, repo, commit in sources:
        require_clean_main(repo, f'{role.capitalize()} source')
        if head(repo) != commit:
            raise ReleaseError(f'The {role} source moved from {commit[:7]} to {head(repo)[:7]} since prepare. Run prepare again.')
    # Decide for every target before the first commit or push.
    stages = []
    for target in state['targets']:
        check_target(target)
        stage = target_stage(target)
        if not stage:
            raise ReleaseError(f'Target {target["directory"]} no longer holds the content prepare staged. '
                               'Nothing was committed or pushed. Run prepare again and have the new list approved.')
        stages.append(stage)
    results = []
    published = {'source_commit': state['source_commit'], 'complete': False, 'targets': results}
    for target, stage in zip(state['targets'], stages):
        directory = target['directory']
        if stage == 'prepared' and git(directory, 'diff', '--cached', '--name-only').strip():
            git(directory, 'commit', '-q', *[part for text in message for part in ('-m', text)])
        local, remote = head(directory), remote_head(directory)
        try:
            if remote != local:
                git(directory, 'push', '-q', 'origin', 'main')
                remote = remote_head(directory)
        finally:
            # Keep what was reached: a rerun of publish continues with the targets that are not yet pushed.
            results.append({'repository': target['repository'], 'commit': local, 'remote': remote,
                            'verified': remote == local, 'changed': local != target['head']})
            (release / PUBLISHED).write_text(json.dumps(published, indent=1) + '\n', encoding='utf-8')
    published['complete'] = True
    (release / PUBLISHED).write_text(json.dumps(published, indent=1) + '\n', encoding='utf-8')
    return published


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=('prepare', 'publish'))
    parser.add_argument('--root', type=Path, default=Path.cwd(), help='Suite source root (default: current directory)')
    parser.add_argument('--release', type=Path, help='Staging directory (default: <skills>/temp/release beside private/)')
    parser.add_argument('--public', type=Path, help='Directory holding the target checkouts (default: <skills>/public)')
    parser.add_argument('--runtime-run', help='prepare: passed Runtime helpers Actions URL (default: the one in the staging receipts)')
    parser.add_argument('--trash', type=Path, help='prepare: where to move a staging tree that cannot be deleted')
    parser.add_argument('--message', '-m', action='append', help='publish: commit message paragraph; repeat for trailers')
    args = parser.parse_args()
    root = args.root.resolve()
    skills = root.parents[1]
    release = args.release or skills / 'temp' / 'release'
    public = args.public or skills / 'public'
    try:
        if args.command == 'prepare':
            state = prepare(root, release, public, args.runtime_run, args.trash)
            for target in state['targets']:
                ahead = f', {target["unpublished"]} earlier local commit(s) not on origin' if target['unpublished'] else ''
                print(f'{target["repository"]}: {len(target["changes"])} staged change(s){ahead}')
                for change in target['changes']:
                    print('   ' + change)
            print(f'Prepared source {state["source_commit"][:7]}. Nothing is committed or pushed. State: {release / STATE}')
        else:
            if not args.message:
                raise ReleaseError('publish needs --message "<commit message>".')
            published = publish(root, release, args.message)
            for target in published['targets']:
                print(f'{target["repository"]}: {target["commit"][:7]} remote={"verified" if target["verified"] else "MISMATCH " + str(target["remote"])}')
            if not all(t['verified'] for t in published['targets']):
                raise ReleaseError(f'At least one remote differs from its local commit; see {release / PUBLISHED}.')
            print(f'Published source {published["source_commit"][:7]}. Result: {release / PUBLISHED}')
    except ReleaseError as error:
        print(f'release_suite: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
