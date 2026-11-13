import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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

    def prepared(self):
        """A source repository and one target with a staged change, as prepare leaves them."""
        source = self.base / 'source'
        source.mkdir()
        git(source, 'init', '-q', '--initial-branch=main')
        (source / 'suite.json').write_text('{}\n', encoding='utf-8')
        git(source, 'add', '-A')
        git(source, 'commit', '-q', '-m', 'source')
        work = self.checkout('owner/alpha')
        (work / 'README.md').write_text('new\n', encoding='utf-8')
        git(work, 'add', '-A')
        target = self.target('owner/alpha', work)
        target.update(changes=['M\tREADME.md'], head=release.head(work))
        stage = self.base / 'release'
        stage.mkdir()
        (stage / release.STATE).write_text(json.dumps({'source_commit': release.head(source), 'targets': [target]}), encoding='utf-8')
        return source, work, stage

    def test_publish_commits_pushes_and_verifies(self):
        source, work, stage = self.prepared()
        git(work, 'config', 'user.name', 'test')
        git(work, 'config', 'user.email', 'test@example.invalid')
        published = release.publish(source, stage, ['Release', 'Trailer: yes'])
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


if __name__ == '__main__':
    unittest.main()
