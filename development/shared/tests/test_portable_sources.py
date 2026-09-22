import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED / 'build'))
from sync_suite_sources import sync


class PortableSourcesTests(unittest.TestCase):
    def test_isolated_suites_match_all_canonical_payloads(self):
        spec = importlib.util.spec_from_file_location('canonical', SHARED / 'build/build_suite.py')
        canonical = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(canonical)
        for name in ('scoville-suite', 'ask-suite-for-codex'):
            source = SHARED.parent / name
            with self.subTest(suite=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary) / name
                shutil.copytree(source, root, ignore=shutil.ignore_patterns(
                    '.git', '__pycache__', 'node_modules', 'target', '.tmp', 'packages'))
                self.assertFalse((root.parent / 'shared').exists())
                self.assertEqual([], sync(root, SHARED, check=True))
                command = [sys.executable, '-B', str(root / 'development/build_suite.py'), '--check-sources']
                subprocess.run(command, check=True, capture_output=True)
                spec = importlib.util.spec_from_file_location('isolated', root / 'development/shared/build/build_suite.py')
                isolated = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(isolated)
                for member in canonical.load(source)['members']:
                    self.assertEqual(canonical.payload(source, member), isolated.payload(root, member))
                target = root / 'development/shared/readme/license.md'
                target.write_text('drift', encoding='utf-8')
                self.assertIn('readme/license.md', sync(root, SHARED, check=True))
                target.with_name('unknown.md').write_text('preserve', encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'Unmanaged'):
                    sync(root, SHARED)


if __name__ == '__main__':
    unittest.main()
