"""Package-level checks for immutable source text and profile-bound handoffs."""
import json
from pathlib import Path
import subprocess
import sys
import unittest
import test_contract as contract


class PromptProfilesTests(unittest.TestCase):
    def test_old_selector_is_rejected(self):
        context = contract.NativeWorkflowContractTests.dispatch_context('W-003/step-1', ['1. Preserve this text.'])
        del context['work_item']['source_text']
        result = contract.NativeWorkflowContractTests().run_prompt_builder(context, 'W-003/step-1')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('SELECTOR_INCOMPATIBLE', result.stdout)

    def test_profiles_preserve_source_and_add_separate_context(self):
        config = contract.PACKAGE / 'assets/workflow.toml'
        original = config.read_text(encoding='utf-8')
        context = contract.NativeWorkflowContractTests.dispatch_context('W-003/step-1', ['1. Preserve café and exact [execute: model=gpt-6-sol] text.'])
        harness = contract.NativeWorkflowContractTests()
        try:
            for profile in ('low', 'medium', 'high'):
                config.write_text(original.replace('profile = "auto"', f'profile = "{profile}"'), encoding='utf-8')
                result = harness.run_prompt_builder(context, 'W-003/step-1', role_input={
                    'supplemental_context': {'facts': ['The source is accessible only to the coordinator.']}})
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                lines = result.stdout.splitlines()
                decoded = json.loads(next(line.removeprefix('plan_context=') for line in lines if line.startswith('plan_context=')))
                self.assertEqual(decoded['work_item']['source_text'], context['work_item']['source_text'])
                self.assertIn(f'"profile":"{profile}"', result.stdout)
                self.assertTrue(any(line.startswith('supplemental_context=') for line in lines))
        finally:
            config.write_text(original, encoding='utf-8')

    def test_built_selector_and_builder_accept_the_same_source(self):
        selector = contract.ROOT.parent / 'scoville-plan/scoville-plan/scripts/select_context.py'
        fixture = contract.ROOT.parent / 'scoville-plan/development/tests/fixtures/valid-profile'
        result = subprocess.run([sys.executable, '-B', str(selector), '--root', str(fixture),
                                 '--unit', 'W-001/step-1', '--format', 'json'], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stdout)
        context = json.loads(result.stdout)
        result = contract.NativeWorkflowContractTests().run_prompt_builder(context, 'W-001/step-1')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn(json.dumps(context['work_item']['source_text'], ensure_ascii=False), result.stdout)


if __name__ == '__main__':
    unittest.main()
