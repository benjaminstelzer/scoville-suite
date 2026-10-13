import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).resolve().parents[1] / 'runtime' / 'check_text_size.py'
LARGE = ('complete result Grüße 中文\n' * 400).encode('utf-8')


class CaptureFixture(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='capture-ignore-')
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.project = self.base / 'Projekt ä'
        self.project.mkdir()
        self.source = self.base / 'result.txt'
        self.source.write_bytes(LARGE)

    def publish(self):
        result = subprocess.run([sys.executable, '-X', 'utf8', str(CHECKER), '--file', str(self.source),
            '--max-output-tokens', '1000', '--publish-full', '--project-root', str(self.project)],
            capture_output=True, text=True, encoding='utf-8', timeout=25)
        self.assertEqual(result.returncode, 0, result.stderr)
        meta = json.loads(result.stdout)
        self.assertEqual(meta['status'], 'complete_file')
        self.assertEqual(Path(meta['full_file']).read_bytes(), LARGE)
        return meta

    def assertIgnorePattern(self):
        # The created marker must contain only the pattern *; any valid line ending is accepted.
        marker = self.project / '.scoville/temp/.gitignore'
        self.assertEqual(marker.read_text(encoding='utf-8').splitlines(), ['*'])

    def capture(self, payload):
        return subprocess.run([sys.executable, '-X', 'utf8', str(CHECKER), '--max-output-tokens', '1000',
            '--publish-full', '--project-root', str(self.project), '--run', '--',
            sys.executable, '-c', f'import sys; sys.stdout.write({payload!r})'], capture_output=True, timeout=25)


class PublicationWithoutGit(CaptureFixture):
    def test_publication_needs_no_git_repository(self):
        meta = self.publish()
        self.assertEqual(Path(meta['full_file']).name, hashlib.sha256(LARGE).hexdigest() + '.txt')
        self.assertIgnorePattern()

    def test_inline_capture_creates_no_ignore_file(self):
        inline = self.capture('small')
        self.assertEqual(inline.returncode, 0, inline.stderr)
        self.assertIn(b'stdout:\nsmall', inline.stdout)
        self.assertFalse((self.project / '.scoville/temp/.gitignore').exists())

    def test_linked_ignore_file_is_not_followed(self):
        outside = self.base / 'outside.txt'
        outside.write_bytes(b'outside content\n')
        directory = self.project / '.scoville/temp'
        directory.mkdir(parents=True)
        try:
            os.symlink(outside, directory / '.gitignore')
        except OSError as error:
            self.skipTest(f'file symlink unavailable: {error}')
        self.publish()
        self.assertTrue((directory / '.gitignore').is_symlink())
        self.assertEqual(outside.read_bytes(), b'outside content\n')


@unittest.skipUnless(shutil.which('git'), 'Git is unavailable')
class PublicationInGit(CaptureFixture):
    def setUp(self):
        super().setUp()
        home = self.base / 'home'
        home.mkdir()
        # Isolate from user and system ignore rules so only the fixture decides.
        self.env = {**os.environ, 'HOME': str(home), 'USERPROFILE': str(home), 'XDG_CONFIG_HOME': str(home),
                    'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': str(home / 'gitconfig')}
        self.git('init', '--quiet', '--template=')
        (self.project / 'README.md').write_text('fixture\n', encoding='utf-8')
        self.commit()

    def git(self, *args):
        result = subprocess.run(['git', '-c', 'core.autocrlf=false', *args], cwd=self.project, env=self.env,
            capture_output=True, text=True, encoding='utf-8', timeout=25)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def commit(self):
        self.git('add', '--all')
        self.git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                 'commit', '--quiet', '--no-verify', '-m', 'fixture')

    def status(self):
        return self.git('status', '--porcelain', '--untracked-files=all')

    def test_file_and_command_publication_keep_status_clean(self):
        self.publish()
        published = self.capture('x' * 4000)
        self.assertEqual(published.returncode, 0, published.stderr)
        self.assertEqual(json.loads(published.stdout)['status'], 'complete_file')
        self.assertIgnorePattern()
        self.assertEqual(self.status(), '')

    def test_existing_ignore_policy_is_preserved(self):
        directory = self.project / '.scoville/temp'
        directory.mkdir(parents=True)
        policy = b'# Project keeps published results visible.\n'
        (directory / '.gitignore').write_bytes(policy)
        self.commit()
        meta = self.publish()
        self.assertEqual((directory / '.gitignore').read_bytes(), policy)
        self.assertEqual(self.status(), f'?? .scoville/temp/{Path(meta["full_file"]).name}\n')

    def test_tracked_paths_remain_tracked(self):
        directory = self.project / '.scoville/temp'
        directory.mkdir(parents=True)
        (directory / 'tracked.txt').write_bytes(b'tracked\n')
        self.commit()
        self.publish()
        self.assertEqual(self.git('ls-files', '.scoville/temp'), '.scoville/temp/tracked.txt\n')
        self.assertEqual((directory / 'tracked.txt').read_bytes(), b'tracked\n')
        self.assertEqual(self.status(), '')
        (directory / 'tracked.txt').write_bytes(b'changed\n')
        self.assertEqual(self.status(), ' M .scoville/temp/tracked.txt\n')


if __name__ == '__main__':
    unittest.main()
