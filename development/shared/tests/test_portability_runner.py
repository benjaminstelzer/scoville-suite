import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SHARED = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'portability_runner', SHARED / 'build/run_portability.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class PortabilityRunnerTests(unittest.TestCase):
    def test_source_paths_follow_manifest_and_deduplicate(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'suite'
            shared = Path(temporary) / 'shared'
            manifest = {'members': [
                {'development': {'tests': 'members/a/tests'}},
                {'development': {'tests': 'development/tests'}},
            ]}
            for path in (shared / 'tests', root / 'development/tests',
                         root / 'members/a/tests'):
                path.mkdir(parents=True)
            self.assertEqual([
                (shared / 'tests').resolve(),
                (root / 'development/tests').resolve(),
                (root / 'members/a/tests').resolve(),
            ], runner.source_test_paths(root, shared, manifest))

    def test_export_validation_checks_exact_packages_and_layout(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'suite'
            shared = Path(temporary) / 'shared'
            package = root / 'packages/test-skill'
            package.mkdir(parents=True)
            (root / 'suite.json').write_text(json.dumps({
                'name': 'test-suite', 'profile': 'general', 'layout': 'suite',
                'members': [{'name': 'test-skill'}],
            }), encoding='utf-8')
            (package / 'test-skill').mkdir()
            (package / 'test-skill/SKILL.md').write_text('skill', encoding='utf-8')
            config = {'profile': 'general', 'layout': 'suite',
                      'members': [{'name': 'test-skill'}]}

            class Builder:
                @staticmethod
                def load(unused_root, profile=None, layout=None):
                    if layout == 'standalone':
                        raise ValueError('exported sources retain their package layout')
                    return config

                @staticmethod
                def render_readmes(*args):
                    return []

                @staticmethod
                def render_sources(*args):
                    return []

                @staticmethod
                def payload(*args):
                    return {'test-skill/SKILL.md': b'skill'}

            with patch.object(runner, 'load_builder', return_value=Builder):
                result = runner.validate_export(
                    root, shared, json.loads((root / 'suite.json').read_text()))
                self.assertEqual({'profile': 'general', 'members': 1,
                                  'python_files': 0}, result)
                (package / 'extra.txt').write_text('unexpected', encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'differs from selected sources'):
                    runner.validate_export(
                        root, shared, json.loads((root / 'suite.json').read_text()))

    def test_empty_test_directory_is_reported_without_discovery(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary)
            with patch.object(runner.subprocess, 'run') as process:
                self.assertFalse(runner.run_test_path(path))
            process.assert_not_called()
            with self.assertRaisesRegex(ValueError, 'does not exist'):
                runner.run_test_path(path / 'missing')

    def test_run_routes_projected_manifest_without_source_tests(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'suite'
            root.mkdir()
            (root / 'suite.json').write_text(json.dumps({
                'profile': 'general', 'layout': 'suite', 'members': []
            }), encoding='utf-8')
            with patch.object(runner, 'validate_export', return_value={
                    'profile': 'general', 'members': 0, 'python_files': 0}) as validate:
                with patch.object(runner, 'run_test_path') as run_test:
                    result = runner.run(root, Path(temporary) / 'shared')
            self.assertEqual('export', result['mode'])
            validate.assert_called_once()
            run_test.assert_not_called()


if __name__ == '__main__':
    unittest.main()
