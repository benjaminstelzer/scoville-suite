import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('profile_resolver', ROOT / 'runtime/resolve_prompt_profile.py')
resolver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resolver)


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.config = resolver.read_config(ROOT / 'prompting/models.toml')

    def test_precedence_and_unknown_model(self):
        cases = [({}, 'medium'), ({'model': 'gpt-6-luna'}, 'low'),
                 ({'model': 'gpt-6-astra'}, 'high'),
                 ({'model': 'unknown', 'task_class': 'high'}, 'medium'),
                 ({'task_class': 'ultra_high'}, 'high'),
                 ({'explicit': 'low', 'model': 'gpt-6-astra'}, 'low')]
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertEqual(resolver.resolve(self.config, **args), expected)
        self.config['profile'] = 'high'
        self.assertEqual(resolver.resolve(self.config, model='gpt-6-luna'), 'high')
        self.assertEqual(resolver.resolve(self.config, explicit='low'), 'low')

    def test_independent_configs_and_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / 'plan.toml'
            second = Path(directory) / 'workflow.toml'
            original = (ROOT / 'prompting/models.toml').read_text()
            first.write_text(original.replace('profile = "auto"', 'profile = "low"'))
            second.write_text(original)
            self.assertEqual(resolver.resolve(resolver.read_config(first), model='gpt-6-astra'), 'low')
            self.assertEqual(resolver.resolve(resolver.read_config(second), model='gpt-6-astra'), 'high')
            first.write_text('[prompting]\nprofile="unknown"\nmodels={}\n')
            with self.assertRaises(ValueError):
                resolver.read_config(first)


if __name__ == '__main__':
    unittest.main()
