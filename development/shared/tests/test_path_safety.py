import os
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'build'))
from build_suite import within


class PathSafetyTests(unittest.TestCase):
    def test_redirect_above_root_is_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            physical = temporary / 'physical'
            root = physical / 'project'
            root.mkdir(parents=True)
            (root / 'source.txt').write_text('content', encoding='utf-8')
            alias = temporary / 'alias'
            try:
                os.symlink(physical, alias, target_is_directory=True)
            except OSError as error:
                self.skipTest(f'directory symlink unavailable: {error}')

            self.assertEqual((root / 'source.txt').resolve(), within(alias / 'project', 'source.txt'))

    def test_redirect_inside_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            root = temporary / 'project'
            root.mkdir()
            target = root / 'target'
            target.mkdir()
            (target / 'source.txt').write_text('content', encoding='utf-8')
            redirect = root / 'redirect'
            try:
                os.symlink(target, redirect, target_is_directory=True)
            except OSError as error:
                self.skipTest(f'directory symlink unavailable: {error}')

            with self.assertRaisesRegex(ValueError, 'symlink not allowed'):
                within(root, 'redirect/source.txt')


if __name__ == '__main__':
    unittest.main()
