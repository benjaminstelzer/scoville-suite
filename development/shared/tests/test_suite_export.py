import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED / 'build'))
import export_suite


class SuiteExportTests(unittest.TestCase):
    def test_full_sources_packages_and_no_local_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'source'
            root.mkdir()
            def git(*args):
                subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)
            git('init')
            git('config', 'core.autocrlf', 'false')
            (root / '.gitattributes').write_bytes(b'*.py text eol=lf\n')
            (root / '.gitignore').write_text('private.local\n')
            (root / 'private.local').write_text('not for export')
            (root / 'development').mkdir()
            (root / 'development/test.py').write_text('# retained development\n')
            config = {'name': 'test-suite', 'members': [{'name': 'test-skill', 'public_distribution': True}]}
            (root / 'suite.json').write_text(json.dumps(config))
            git('add', '.')
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-m', 'fixture')
            (root / 'development/test.py').write_bytes(b'# retained development\r\n')
            git('add', 'development/test.py')
            self.assertEqual(b'', export_suite.git(root, 'status', '--porcelain'))
            output = Path(temporary) / 'export'
            with patch.object(export_suite, 'render_readmes', return_value=[]), patch.object(export_suite, 'sync', return_value=[]), patch.object(export_suite, 'load', return_value=config), patch.object(export_suite, 'payload', return_value={'README.md': b'readme', 'test-skill/SKILL.md': b'skill'}):
                receipt = export_suite.export(root, output)
                self.assertIn('development/test.py', receipt['files'])
                self.assertEqual(b'# retained development\n', (output / 'development/test.py').read_bytes())
                self.assertEqual(b'skill', (output / 'packages/test-skill/test-skill/SKILL.md').read_bytes())
                self.assertFalse((output / 'private.local').exists())
                self.assertFalse((output / '.git').exists())
                (root / 'uncommitted.txt').write_text('dirty')
                with self.assertRaisesRegex(ValueError, 'Commit and inspect'):
                    export_suite.export(root, Path(temporary) / 'blocked')
                self.assertFalse((Path(temporary) / 'blocked').exists())


if __name__ == '__main__':
    unittest.main()
