import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SHARED = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SHARED / 'build'))
import export_suite
import build_suite
import sync_suite_sources


class SuiteExportTests(unittest.TestCase):
    def test_snapshot_entrypoints_use_canonical_sources_or_isolated_fallback(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root, canonical = base / 'suite', base / 'shared'
            root.mkdir()
            shutil.copytree(SHARED, canonical, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
            (canonical / 'prompting/common.md').write_bytes(b'Use exact source paths.\n')
            config = {'schema_version': 1, 'name': 'test-suite', 'profile': 'general',
                      'repository': 'benjaminstelzer/test-suite', 'readme': [],
                      'members': [{'name': 'test-skill', 'repository': 'benjaminstelzer/test-skill',
                                   'visibility': 'public', 'public_distribution': True, 'readme': [],
                                   'files': [{'source': 'skill.md', 'target': 'test-skill/SKILL.md'},
                                             {'source': 'shared:prompting/common.md',
                                              'target': 'test-skill/references/writing.md'}]}]}
            (root / 'suite.json').write_text(json.dumps(config), encoding='utf-8')
            (root / 'skill.md').write_text('# Test skill\n', encoding='utf-8')
            (root / '.gitattributes').write_text('* -text\n', encoding='utf-8')
            sync_suite_sources.sync(root, canonical)
            def git(*args):
                subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)
            git('init')
            git('add', '.')
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-m', 'fixture')
            snapshot = root / 'development/shared/build'
            def probe(label, succeeds):
                output, receipt = base / (label + '-export'), base / (label + '.json')
                result = subprocess.run([sys.executable, '-B', str(snapshot / 'export_suite.py'),
                    '--root', str(root), '--output', str(output), '--receipt', str(receipt)],
                    capture_output=True, text=True, encoding='utf-8')
                gate = subprocess.run([sys.executable, '-B', '-c',
                    'import sys; from pathlib import Path; sys.path.insert(0, sys.argv[1]); '
                    'import build_suite; build_suite.check_shared_snapshot(Path(sys.argv[2]))',
                    str(snapshot), str(root)], capture_output=True, text=True, encoding='utf-8')
                if not succeeds:
                    self.assertNotEqual(0, result.returncode)
                    self.assertIn('Shared snapshot is stale', result.stderr)
                    self.assertNotEqual(0, gate.returncode)
                    self.assertIn('Shared snapshot is not in sync', gate.stderr)
                    self.assertFalse(output.exists())
                    self.assertFalse(receipt.exists())
                else:
                    self.assertEqual(0, result.returncode, result.stderr)
                    self.assertEqual(0, gate.returncode, gate.stderr)
                    self.assertTrue(receipt.is_file())
                    loaded = build_suite.load(root, layout='suite')
                    with patch.object(build_suite, 'shared_root', return_value=canonical if canonical.exists()
                                      else root / 'development/shared'):
                        expected = build_suite.payload(root, loaded['members'][0], loaded)
                    package = output / 'packages/test-skill'
                    actual = {p.relative_to(package).as_posix(): p.read_bytes()
                              for p in package.rglob('*') if p.is_file()}
                    self.assertEqual(expected, actual)
            common = canonical / 'prompting/common.md'
            original = common.read_bytes()
            common.write_bytes(original + b'\nA new canonical instruction.\n')
            probe('stale', False)
            common.write_bytes(original)
            probe('synchronized', True)
            canonical.rename(base / 'canonical-away')
            probe('isolated', True)

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
