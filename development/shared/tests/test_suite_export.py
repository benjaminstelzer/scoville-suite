import hashlib
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
    def test_private_records_cannot_hide_public_code_or_escape_the_tree(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for path in ('../secret.md', 'members/skill/SKILL.md', 'docs/testing/../code.py', 'docs/testing/probe.py'):
                (root / 'suite.json').write_text(json.dumps({'private_records': [path]}), encoding='utf-8')
                with self.subTest(path=path), self.assertRaises(ValueError):
                    build_suite.private_record_paths(root)

    def test_snapshot_entrypoints_use_canonical_sources_or_isolated_fallback(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root, canonical = base / 'suite', base / 'shared'
            root.mkdir()
            shutil.copytree(SHARED, canonical, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
            (canonical / 'prompting/common.md').write_bytes(b'Use exact source paths.\r\n')
            binary = b'\x00\xff\r\n'
            (canonical / 'prompting/fixture.bin').write_bytes(binary)
            config = {'schema_version': 1, 'name': 'test-suite', 'profile': 'general',
                      'repository': 'benjaminstelzer/test-suite', 'readme': [],
                      'members': [{'name': 'test-skill', 'repository': 'benjaminstelzer/test-skill',
                                   'visibility': 'public', 'public_distribution': True, 'readme': [],
                                   'files': [{'source': 'skill.md', 'target': 'test-skill/SKILL.md'},
                                             {'source': 'shared:prompting/common.md',
                                              'target': 'test-skill/references/writing.md'}]}]}
            (root / 'suite.json').write_text(json.dumps(config), encoding='utf-8')
            (root / 'skill.md').write_text('# Test skill\n', encoding='utf-8')
            (root / '.gitattributes').write_text('* text=auto eol=lf\n*.bin binary\n', encoding='utf-8')
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
                    shared = output / 'development/shared'
                    hashes = json.loads((shared / 'sources.json').read_text(encoding='utf-8'))
                    exported = {p.relative_to(shared).as_posix(): p.read_bytes()
                                for p in shared.rglob('*') if p.is_file()
                                and p != shared / 'sources.json'}
                    self.assertEqual(hashes, {name: hashlib.sha256(data).hexdigest()
                                              for name, data in exported.items()})
                    self.assertEqual(b'Use exact source paths.\n', exported['prompting/common.md'])
                    self.assertEqual(binary, exported['prompting/fixture.bin'])
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
            historical = ('development/instruction_tests/catalog.py',
                          'development/luna-tests/run_codex_cli_case.py',
                          'development/tests/test_instruction_evaluation.py',
                          'development/tests/test_codex_cli_case.py',
                          'development/tests/test_attempt_budget.py',
                          'development/claude-code/capabilities.md')
            for name in historical:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b'Historical evidence.\n')
            config = {'name': 'test-suite', 'members': [{'name': 'test-skill', 'public_distribution': True}]}
            config['private_records'] = ['docs/plans/0001-private.md', 'docs/testing/local.md']
            (root / 'docs/plans').mkdir(parents=True)
            (root / 'docs/testing').mkdir()
            (root / 'docs/plans/0001-private.md').write_text('---\nid: PLAN-0001\n---\nPrivate plan\n')
            (root / 'docs/testing/local.md').write_text('Private local evidence\n')
            (root / 'PROJECT_INDEX.md').write_text('---\nformat_version: 1\nactive_plan: PLAN-0001\n---\n')
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
                for name in historical:
                    self.assertNotIn(name, receipt['files'])
                    self.assertFalse((output / name).exists())
                    self.assertEqual(b'Historical evidence.\n', (root / name).read_bytes())
                self.assertEqual(b'# retained development\n', (output / 'development/test.py').read_bytes())
                self.assertEqual(b'skill', (output / 'packages/test-skill/test-skill/SKILL.md').read_bytes())
                self.assertFalse((output / 'private.local').exists())
                self.assertFalse((output / '.git').exists())
                self.assertFalse((output / 'docs/plans/0001-private.md').exists())
                self.assertFalse((output / 'docs/testing/local.md').exists())
                self.assertIn('active_plan: null', (output / 'PROJECT_INDEX.md').read_text())
                self.assertNotIn('private_records', json.loads((output / 'suite.json').read_text()))
                config['members'][0]['files'] = [{'source': 'docs/testing/local.md', 'target': 'test-skill/private.md'}]
                with self.assertRaisesRegex(ValueError, 'private record is required by a public package'):
                    export_suite.export(root, Path(temporary) / 'blocked-private-package')
                self.assertFalse((Path(temporary) / 'blocked-private-package').exists())
                config['members'][0]['files'] = []
                (root / 'uncommitted.txt').write_text('dirty')
                with self.assertRaisesRegex(ValueError, 'Commit and inspect'):
                    export_suite.export(root, Path(temporary) / 'blocked')
                self.assertFalse((Path(temporary) / 'blocked').exists())


if __name__ == '__main__':
    unittest.main()
