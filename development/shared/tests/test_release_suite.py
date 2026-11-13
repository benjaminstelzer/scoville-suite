import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'build'))
import release_suite as release  # noqa: E402

MANIFEST = {
    'default_profile': 'general',
    'profiles': {'general': {'repository': 'owner/suite'}, 'codex': {'repository': 'owner/suite-codex'}},
    'members': [
        {'name': 'alpha', 'repository': 'owner/alpha', 'visibility': 'public'},
        {'name': 'beta', 'repository': 'owner/beta', 'visibility': 'public', 'profiles': ['codex']},
        {'name': 'gamma', 'repository': 'owner/suite', 'distribution': 'suite', 'visibility': 'public'},
        {'name': 'delta', 'repository': 'owner/delta', 'visibility': 'private'},
    ],
}


def git(cwd, *args):
    subprocess.run(['git', '-c', 'user.name=test', '-c', 'user.email=test@example.invalid', '-c', 'core.autocrlf=false', *args],
                   cwd=cwd, check=True, capture_output=True)


class ReleaseSuiteTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name).resolve()
        self.addCleanup(self.temporary.cleanup)
        # The fixtures push to local bare repositories, whose host is None.
        hosts = mock.patch.object(release, 'HOSTS', (None,))
        hosts.start()
        self.addCleanup(hosts.stop)

    def checkout(self, repository, files=None):
        """A local checkout on main whose origin is a bare repository named like the target."""
        bare = self.base / 'remotes' / (repository + '.git')
        bare.mkdir(parents=True)
        git(bare, 'init', '-q', '--bare', '--initial-branch=main')
        work = self.base / 'public' / repository.rsplit('/', 1)[-1]
        work.mkdir(parents=True)
        git(work, 'init', '-q', '--initial-branch=main')
        git(work, 'remote', 'add', 'origin', str(bare))
        for name, text in (files or {'README.md': 'old\n'}).items():
            (work / name).parent.mkdir(parents=True, exist_ok=True)
            (work / name).write_text(text, encoding='utf-8')
        git(work, 'add', '-A')
        git(work, 'commit', '-q', '-m', 'initial')
        git(work, 'push', '-q', 'origin', 'main')
        return work

    def target(self, repository, work):
        return {'repository': repository, 'directory': str(work), 'source': str(self.base / 'stage'), 'kind': 'member', 'profile': 'general'}

    def test_targets_follow_the_manifest(self):
        found = release.targets(MANIFEST, self.base / 'release', self.base / 'public')
        by_repository = {t['repository']: t for t in found}
        self.assertEqual(sorted(by_repository), ['owner/alpha', 'owner/beta', 'owner/suite', 'owner/suite-codex'])
        self.assertTrue(by_repository['owner/suite']['source'].endswith('export-general'))
        self.assertTrue(by_repository['owner/suite-codex']['source'].endswith('export-codex'))
        self.assertEqual(Path(by_repository['owner/alpha']['source']), self.base / 'release' / 'standalone-general' / 'alpha')
        self.assertEqual(Path(by_repository['owner/beta']['source']), self.base / 'release' / 'standalone-codex' / 'beta')

    def test_mirror_adds_changes_and_removes_but_keeps_git(self):
        work = self.checkout('owner/alpha', {'README.md': 'old\n', 'gone/old.txt': 'x\n', 'same.txt': 'same\n'})
        stage = self.base / 'stage'
        (stage / 'new').mkdir(parents=True)
        (stage / 'README.md').write_text('new\n', encoding='utf-8')
        (stage / 'same.txt').write_text('same\n', encoding='utf-8')
        (stage / 'new' / 'file.txt').write_text('n\n', encoding='utf-8')
        release.mirror(stage, work)
        self.assertEqual((work / 'README.md').read_text(encoding='utf-8'), 'new\n')
        self.assertTrue((work / 'new' / 'file.txt').is_file())
        self.assertFalse((work / 'gone').exists())
        self.assertTrue((work / '.git').is_dir())
        release.git(work, 'add', '-A')
        self.assertEqual(sorted(line.split('\t')[1] for line in release.git(work, 'diff', '--cached', '--name-status').splitlines()),
                         ['README.md', 'gone/old.txt', 'new/file.txt'])

    def test_missing_staging_tree_is_refused(self):
        work = self.checkout('owner/alpha')
        with self.assertRaisesRegex(release.ReleaseError, 'is missing'):
            release.mirror(self.base / 'absent', work)

    def test_target_with_unstaged_edit_is_refused_and_staged_one_is_accepted(self):
        work = self.checkout('owner/alpha')
        target = self.target('owner/alpha', work)
        release.check_target(target)
        (work / 'README.md').write_text('edited\n', encoding='utf-8')
        with self.assertRaisesRegex(release.ReleaseError, 'did not stage'):
            release.check_target(target)
        git(work, 'add', '-A')
        release.check_target(target)

    def test_target_with_wrong_origin_or_branch_is_refused(self):
        work = self.checkout('owner/alpha')
        with self.assertRaisesRegex(release.ReleaseError, 'expected owner/other'):
            release.check_target(self.target('owner/other', work))
        git(work, 'checkout', '-q', '-b', 'side')
        with self.assertRaisesRegex(release.ReleaseError, 'not main'):
            release.check_target(self.target('owner/alpha', work))

    def test_scan_reports_file_and_line(self):
        root = self.base / 'tree'
        root.mkdir()
        (root / 'a.md').write_text('fine\nsee C:\\Users\\Someone\\notes\n', encoding='utf-8')
        (root / 'b.md').write_text('fine\n', encoding='utf-8')
        hits = release.scan_personal([root], ['Users\\someone'])
        self.assertEqual(hits, [f'{root / "a.md"}:2'])

    def repository(self, name):
        repo = self.base / name
        repo.mkdir()
        git(repo, 'init', '-q', '--initial-branch=main')
        (repo / 'suite.json').write_text('{}\n', encoding='utf-8')
        git(repo, 'add', '-A')
        git(repo, 'commit', '-q', '-m', name)
        return repo

    def staged_target(self, repository):
        """A target checkout with a staged change and the record prepare writes for it."""
        work = self.checkout(repository)
        git(work, 'config', 'user.name', 'test')
        git(work, 'config', 'user.email', 'test@example.invalid')
        (work / 'README.md').write_text('new\n', encoding='utf-8')
        git(work, 'add', '-A')
        target = self.target(repository, work)
        target.update(changes=['M\tREADME.md'], head=release.head(work), tree=release.git(work, 'write-tree').strip(), unpublished=0)
        return work, target

    def prepared(self, repositories=('owner/alpha',), shared=None):
        """A source repository and targets with a staged change, as prepare leaves them."""
        source = self.repository('source')
        works, targets = zip(*(self.staged_target(repository) for repository in repositories))
        stage = self.base / 'release'
        stage.mkdir()
        state = {'source_commit': release.head(source), 'shared_commit': release.head(shared) if shared else None,
                 'targets': list(targets)}
        (stage / release.STATE).write_text(json.dumps(state), encoding='utf-8')
        return source, (works[0] if len(works) == 1 else works), stage

    def remote_main(self, repository):
        bare = self.base / 'remotes' / (repository + '.git')
        return release.git(bare, 'rev-parse', 'main').strip()

    def test_publish_commits_pushes_and_verifies(self):
        source, work, stage = self.prepared()
        published = release.publish(source, stage, ['Release', 'Trailer: yes'])
        self.assertTrue(published['complete'])
        entry = published['targets'][0]
        self.assertTrue(entry['verified'])
        self.assertEqual(entry['commit'], release.head(work))
        self.assertEqual(release.git(work, 'log', '-1', '--format=%B').strip(), 'Release\n\nTrailer: yes')
        self.assertEqual(json.loads((stage / release.PUBLISHED).read_text(encoding='utf-8'))['targets'][0]['remote'], entry['commit'])

    def test_publish_refuses_a_source_that_moved(self):
        source, work, stage = self.prepared()
        (source / 'more.txt').write_text('x\n', encoding='utf-8')
        git(source, 'add', '-A')
        git(source, 'commit', '-q', '-m', 'later')
        with self.assertRaisesRegex(release.ReleaseError, 'Run prepare again'):
            release.publish(source, stage, ['Release'])
        self.assertEqual(release.git(work, 'diff', '--cached', '--name-only').strip(), 'README.md')

    def test_publish_without_prepare_is_refused(self):
        with self.assertRaisesRegex(release.ReleaseError, 'Run prepare first'):
            release.publish(self.base, self.base, ['Release'])

    def assert_refused_untouched(self, source, work, stage, pattern):
        """publish refuses, and the target has no new commit and its remote no new content."""
        before, remote = release.head(work), self.remote_main('owner/alpha')
        with self.assertRaisesRegex(release.ReleaseError, pattern):
            release.publish(source, stage, ['Release'])
        self.assertEqual(release.head(work), before)
        self.assertEqual(self.remote_main('owner/alpha'), remote)
        self.assertFalse((stage / release.PUBLISHED).exists())

    def refused_after(self, text, name='README.md'):
        source, work, stage = self.prepared()
        (work / name).write_text(text, encoding='utf-8')
        git(work, 'add', '-A')
        self.assert_refused_untouched(source, work, stage, 'no longer holds the content prepare staged')

    def test_publish_refuses_an_extra_staged_file(self):
        self.refused_after('x\n', 'extra.txt')

    def test_publish_refuses_other_content_in_a_prepared_file(self):
        self.refused_after('other\n')

    def test_publish_refuses_when_the_prepared_change_is_gone(self):
        self.refused_after('old\n')

    def test_publish_refuses_a_target_someone_else_committed_to(self):
        source, work, stage = self.prepared()
        (work / 'extra.txt').write_text('x\n', encoding='utf-8')
        git(work, 'add', '-A')
        git(work, 'commit', '-q', '-m', 'foreign')
        remote = self.remote_main('owner/alpha')
        with self.assertRaisesRegex(release.ReleaseError, 'no longer holds the content prepare staged'):
            release.publish(source, stage, ['Release'])
        self.assertEqual(self.remote_main('owner/alpha'), remote)

    def test_publish_refuses_a_push_address_that_differs_from_origin(self):
        source, work, stage = self.prepared()
        elsewhere = self.base / 'remotes' / 'other' / 'place.git'
        elsewhere.mkdir(parents=True)
        git(elsewhere, 'init', '-q', '--bare', '--initial-branch=main')
        git(work, 'remote', 'set-url', '--push', 'origin', str(elsewhere))
        self.assert_refused_untouched(source, work, stage, 'expected owner/alpha')
        self.assertEqual(release.run(['git', '-C', elsewhere, 'rev-parse', '--verify', '-q', 'main']).stdout.strip(), '')

    def test_remote_identity_binds_host_and_repository(self):
        for url in ('https://github.com/Owner/Alpha.git', 'git@github.com:owner/alpha.git', 'ssh://git@github.com/owner/alpha'):
            self.assertEqual(release.remote_identity(url), ('github.com', 'owner/alpha'), url)
        self.assertEqual(release.remote_identity('https://example.invalid/owner/alpha'), ('example.invalid', 'owner/alpha'))
        self.assertEqual(release.remote_identity('C:\\remotes\\owner\\alpha.git'), (None, 'owner/alpha'))
        work = self.checkout('owner/alpha')
        with mock.patch.object(release, 'HOSTS', ('github.com',)):
            with self.assertRaisesRegex(release.ReleaseError, 'expected owner/alpha on github.com'):
                release.check_target(self.target('owner/alpha', work))

    def test_publish_continues_after_a_failed_push(self):
        source, (first, second), stage = self.prepared(('owner/alpha', 'owner/beta'))
        real = release.git

        def failing(repo, *args):
            if args[:1] == ('push',) and Path(repo) == second:
                raise release.ReleaseError('push failed')
            return real(repo, *args)
        with mock.patch.object(release, 'git', failing):
            with self.assertRaisesRegex(release.ReleaseError, 'push failed'):
                release.publish(source, stage, ['Release'])
        partial = json.loads((stage / release.PUBLISHED).read_text(encoding='utf-8'))
        self.assertFalse(partial['complete'])
        self.assertEqual([entry['verified'] for entry in partial['targets']], [True, False])
        self.assertEqual(self.remote_main('owner/alpha'), release.head(first))
        self.assertNotEqual(self.remote_main('owner/beta'), release.head(second))
        commits = release.head(first), release.head(second)
        published = release.publish(source, stage, ['Release'])
        self.assertTrue(published['complete'])
        self.assertEqual([entry['verified'] for entry in published['targets']], [True, True])
        self.assertEqual((release.head(first), release.head(second)), commits)
        self.assertEqual(self.remote_main('owner/beta'), release.head(second))

    def test_publish_refuses_a_shared_source_that_moved_or_is_dirty(self):
        shared = self.repository('shared')
        (shared / 'build').mkdir()
        source, work, stage = self.prepared(shared=shared)
        with mock.patch.object(release, 'HERE', shared / 'build'):
            (shared / 'loose.txt').write_text('x\n', encoding='utf-8')
            self.assert_refused_untouched(source, work, stage, 'Shared source .* has uncommitted changes')
            git(shared, 'add', '-A')
            git(shared, 'commit', '-q', '-m', 'later')
            self.assert_refused_untouched(source, work, stage, 'The shared source moved')


if __name__ == '__main__':
    unittest.main()
