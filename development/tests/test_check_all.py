"""Protect aggregate failure reporting and canonical test ownership."""
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('suite_check_all', ROOT / 'development/check_all.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class CheckAllTests(unittest.TestCase):
    def test_inventory_includes_canonical_shared_suite_and_members_once(self):
        shared = ROOT.parent / 'shared'
        manifest = json.loads((ROOT / 'suite.json').read_text(encoding='utf-8'))
        paths = gate.load_runner(shared).source_test_paths(ROOT, shared, manifest)
        self.assertEqual(len(paths), len(set(paths)))
        self.assertIn((shared / 'tests').resolve(), paths)
        self.assertIn((ROOT / 'development/tests').resolve(), paths)
        for member in manifest['members']:
            declared = (ROOT / member['development']['tests']).resolve()
            self.assertTrue(any(declared == path or declared.is_relative_to(path) for path in paths))
        self.assertFalse(any(path.is_relative_to(ROOT / 'development/shared') for path in paths))

    def test_failure_finishes_other_checks_and_preserves_both_diagnostics(self):
        commands = []

        def execute(arguments, **options):
            commands.append(arguments)
            failed = len(commands) == 1
            return subprocess.CompletedProcess(arguments, int(failed),
                                               'stdout failure\n' if failed else '',
                                               'stderr failure\n' if failed else 'Ran 1 test in 0.001s\nOK\n')

        with tempfile.TemporaryDirectory() as temporary:
            output = io.StringIO()
            with patch.object(gate.subprocess, 'run', side_effect=execute), \
                    patch.object(gate.tempfile, 'TemporaryDirectory') as directory, \
                    patch.object(gate, 'stale_codex_readmes', return_value=[]), \
                    patch.object(gate.Path, 'mkdir'), redirect_stdout(output):
                directory.return_value.name = temporary
                self.assertEqual(1, gate.run())
        text = output.getvalue()
        self.assertIn('stdout failure', text)
        self.assertIn('stderr failure', text)
        self.assertIn('Failed checks: ../shared/tests', text)
        self.assertTrue(any('--check-sources' in command for command in commands))
        self.assertEqual(1, sum('--prepare-runtime-ci' in command for command in commands))
        self.assertEqual(1, sum(str(Path(temporary) / 'runtime/tests') in command for command in commands))
        self.assertTrue(any('--check-readmes' in command and 'general' in command for command in commands))
        self.assertTrue(any('--check-readmes' in command and 'codex' in command for command in commands))

    def test_zero_discovery_fails_instead_of_reporting_a_pass(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = io.StringIO()
            with patch.object(gate.subprocess, 'run', return_value=subprocess.CompletedProcess(
                    [], 0, '', 'Ran 0 tests in 0.001s\nOK\n')), \
                    patch.object(gate.tempfile, 'TemporaryDirectory') as directory, \
                    patch.object(gate, 'stale_codex_readmes', return_value=[]), \
                    patch.object(gate.Path, 'mkdir'), redirect_stdout(output):
                directory.return_value.name = temporary
                self.assertEqual(1, gate.run())
        self.assertIn('unittest discovery did not report any executed tests', output.getvalue())
        self.assertNotIn('PASS ../shared/tests', output.getvalue())

    def test_codex_only_maintained_preview_drift_fails_comparison(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, preview = Path(temporary) / 'suite', Path(temporary) / 'preview'
            relative = Path('members/codex-only/README.md')
            for folder in (root, preview):
                (folder / relative).parent.mkdir(parents=True)
                (folder / relative).write_bytes(b'current\n')
            with patch.object(gate, 'load_runner') as runner:
                builder = runner.return_value.load_builder.return_value
                builder.load.side_effect = lambda unused, profile: {'members': [
                    {'name': 'common'}, *([{'name': 'codex-only'}] if profile == 'codex' else [])]}
                self.assertEqual([], gate.stale_codex_readmes(root, root.parent / 'shared', preview))
                (root / relative).write_bytes(b'stale\n')
                self.assertEqual([relative.as_posix()],
                                 gate.stale_codex_readmes(root, root.parent / 'shared', preview))

    def test_locked_temporary_inputs_move_within_named_delete_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'allowed/inputs'
            source.mkdir(parents=True)
            (source / 'result.txt').write_text('retained', encoding='utf-8')

            class LockedDirectory:
                name = str(source)

                def cleanup(self):
                    raise PermissionError('locked')

            with patch.object(gate.Path, 'home', return_value=root), redirect_stdout(io.StringIO()):
                gate.cleanup_temporary(LockedDirectory(), root / 'allowed')
            targets = list((root / 'Desktop/_delete').iterdir())
            self.assertEqual(1, len(targets))
            self.assertFalse(source.exists())
            self.assertEqual('retained', (targets[0] / 'result.txt').read_text(encoding='utf-8'))

    def test_cleanup_rejects_source_outside_allowed_temporary_root(self):
        cleanup_called = []
        class UnsafeDirectory:
            name = str(ROOT)

            def cleanup(self):
                cleanup_called.append(True)
                raise PermissionError('locked')

        with patch.object(gate.shutil, 'move') as move:
            with self.assertRaisesRegex(ValueError, 'unsafe temporary cleanup target'):
                gate.cleanup_temporary(UnsafeDirectory(), ROOT.parent / 'unrelated')
        move.assert_not_called()
        self.assertEqual([], cleanup_called, 'Reject an unsafe path before deletion starts.')

    def test_failed_cleanup_move_reports_both_paths_and_errors(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'allowed/inputs'
            source.mkdir(parents=True)

            class LockedDirectory:
                name = str(source)

                def cleanup(self):
                    raise PermissionError('delete locked')

            with patch.object(gate.Path, 'home', return_value=root), \
                    patch.object(gate.shutil, 'move', side_effect=PermissionError('move locked')):
                with self.assertRaises(OSError) as failed:
                    gate.cleanup_temporary(LockedDirectory(), root / 'allowed')
            diagnostic = str(failed.exception)
            self.assertIn(str(source), diagnostic)
            self.assertIn(str(root / 'Desktop/_delete'), diagnostic)
            self.assertIn('delete locked', diagnostic)
            self.assertIn('move locked', diagnostic)
            self.assertTrue(source.exists())

    def test_cleanup_warning_preserves_successful_technical_gate(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = io.StringIO()
            warning = f'source={temporary}; destination=Desktop/_delete/inputs; move=locked'
            with patch.object(gate.subprocess, 'run', return_value=subprocess.CompletedProcess(
                    [], 0, '', 'Ran 1 test in 0.001s\nOK\n')), \
                    patch.object(gate.tempfile, 'TemporaryDirectory') as directory, \
                    patch.object(gate, 'stale_codex_readmes', return_value=[]), \
                    patch.object(gate, 'cleanup_temporary', side_effect=OSError(warning)), \
                    patch.object(gate.Path, 'mkdir'), redirect_stdout(output):
                directory.return_value.name = temporary
                self.assertEqual(0, gate.run())
        self.assertIn('CLEANUP WARNING: ' + warning, output.getvalue())
        self.assertIn('0 failed', output.getvalue())
        self.assertNotIn('Failed checks:', output.getvalue())


if __name__ == '__main__':
    unittest.main()
