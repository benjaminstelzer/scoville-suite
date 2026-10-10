"""Skill publication stays strict without an application-release dependency."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('publication_builder', Path(__file__).resolve().parents[1] / 'build/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class PublicationGateTests(unittest.TestCase):
    def check(self, failure=None):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            receipt = {'source_dirty': False, 'source_commit': 'a' * 40,
                       'members': [{'name': 'example'}], 'runtime_validation': {'run': 'run'}}
            if failure == 'stale': receipt['source_commit'] = 'b' * 40
            (root / 'build-receipt.json').write_text(json.dumps(receipt))
            runtime = SimpleNamespace(verify=lambda *a: {'status': 'passed'})
            if failure == 'runtime':
                runtime.verify = lambda *a: (_ for _ in ()).throw(ValueError('runtime mismatch'))
            with patch('sys.argv', ['build', '--check-publication', '--output', str(root)]), \
                 patch.object(builder, 'check_shared_snapshot', side_effect=ValueError('snapshot mismatch') if failure == 'snapshot' else None), \
                 patch.object(builder.subprocess, 'run', side_effect=[
                     SimpleNamespace(stdout=b' M changed' if failure == 'dirty' else b''),
                     SimpleNamespace(stdout='a' * 40)]), \
                 patch.object(builder, 'verify_packages', return_value=['package mismatch'] if failure == 'package' else []), \
                 patch.object(builder, 'load', return_value={}), \
                 patch.object(builder, 'runtime_ci', return_value=runtime), \
                 contextlib.redirect_stdout(io.StringIO()) as output, \
                 contextlib.redirect_stderr(io.StringIO()):
                if failure:
                    with self.assertRaises(SystemExit) as stop:
                        builder.main(root)
                    self.assertEqual(stop.exception.code, 1)
                else:
                    self.assertEqual(builder.main(root), 0)
                    self.assertEqual(json.loads(output.getvalue()), {'valid': True, 'runtime': {'status': 'passed'}})

    def test_clean_complete_skill_publication_needs_no_viewer(self):
        self.check()

    def test_publication_rejects_dirty_stale_snapshot_package_and_runtime(self):
        for failure in ('dirty', 'stale', 'snapshot', 'package', 'runtime'):
            with self.subTest(failure=failure): self.check(failure)

    def test_obsolete_release_arguments_fail_before_building(self):
        for option in ('--check-release', '--viewer-assets', '--release'):
            with self.subTest(option=option), patch('sys.argv', ['build', option]), \
                 contextlib.redirect_stderr(io.StringIO()), patch.object(builder, 'build') as build:
                with self.assertRaises(SystemExit) as stop: builder.main(Path('.'))
                self.assertEqual(stop.exception.code, 2)
                build.assert_not_called()


if __name__ == '__main__': unittest.main()
