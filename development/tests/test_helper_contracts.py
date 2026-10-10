"""Build failures for unregistered helpers and broken progressive disclosure."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('helper_test_builder', ROOT / 'development/build_suite.py')
entry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(entry)
builder = entry._module


class HelperContractTests(unittest.TestCase):
    def package(self, profile='general', layout='suite'):
        config = builder.load(ROOT, profile, layout)
        member = next(m for m in config['members'] if m['name'] == 'scoville-plan')
        return config, member, builder.payload(ROOT, member, config)

    def test_general_layouts_and_codex_have_exact_routes(self):
        for profile, layout in [('general', 'standalone'), ('general', 'suite'), ('codex', 'suite')]:
            config, member, files = self.package(profile, layout)
            core = files['scoville-plan/SKILL.md'].decode()
            for stem in ('select_context', 'validate_profile'):
                path = f'scoville-plan/references/fallbacks/{stem}-fallback.md'
                self.assertEqual(path in files, profile == 'general')
                self.assertEqual(f'](references/fallbacks/{stem}-fallback.md)' in core, profile == 'general')
            if profile == 'general':
                self.assertIn('| No suitable Python 3.11+ | Read only the matching optional reference below. |', core)
                self.assertIn('| Missing script, missing dependency or helper error | Stop the affected operation;', core)
            builder.validate_helper_contracts(files, member, config)

    def test_missing_registration_and_library_misclassification_fail_build(self):
        for change in ('missing', 'library', 'fallback'):
            config, member, _ = self.package()
            rule = member['helper_contracts']['scripts/select_context.py']
            if change == 'missing':
                del member['helper_contracts']['scripts/select_context.py']
            elif change == 'library':
                rule.clear(); rule['kind'] = 'library'
            else:
                del rule['fallback']
            with self.subTest(change=change), self.assertRaises(ValueError):
                builder.payload(ROOT, member, config)

    def test_mutated_packages_fail_at_the_contract_boundary(self):
        for change in ('missing_file', 'wrong_identity', 'wrong_link', 'unconditional', 'inline', 'new_script', 'missing_used_helper'):
            config, member, files = self.package()
            fallback = 'scoville-plan/references/fallbacks/select_context-fallback.md'
            core = 'scoville-plan/SKILL.md'
            if change == 'missing_file': del files[fallback]
            elif change == 'wrong_identity': files[fallback] = files[fallback].replace(b'select_context.py', b'other.py', 1)
            elif change == 'wrong_link': files[core] = files[core].replace(b'fallbacks/select_context-fallback.md', b'fallbacks/validate_profile-fallback.md')
            elif change == 'unconditional':
                original = files[core]
                files[core] = original.replace(b'| No suitable Python 3.11+ |', b'| Always |')
                self.assertNotEqual(original, files[core], 'The mutation must alter the current route.')
            elif change == 'inline': files[core] += b'\n' + files[fallback]
            elif change == 'new_script': files['scoville-plan/scripts/unregistered.py'] = b'print("new")'
            else: files[core] += b'\nRun scripts/missing.py to complete selection.\n'
            with self.subTest(change=change), self.assertRaises(ValueError):
                builder.validate_helper_contracts(files, member, config)

    def test_codex_rejects_files_links_and_inline_manual_routes(self):
        _, _, general = self.package()
        fallback = 'scoville-plan/references/fallbacks/select_context-fallback.md'
        for change in ('file', 'link', 'inline'):
            config, member, files = self.package('codex')
            if change == 'file': files[fallback] = general[fallback]
            elif change == 'link': files['scoville-plan/references/read-only.md'] += b'\n[Manual](fallbacks/select_context-fallback.md)\n'
            else: files['scoville-plan/SKILL.md'] += general[fallback]
            with self.subTest(change=change), self.assertRaises(ValueError):
                builder.validate_helper_contracts(files, member, config)

    def test_verify_rejects_fallback_injected_after_build(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'built'
            receipt = builder.build(ROOT, output, True, [], 'codex', 'suite')
            member = next(m for m in receipt['members'] if m['name'] == 'scoville-plan')
            target = output / member['package_path'] / 'scoville-plan/references/fallbacks/extra.md'
            target.parent.mkdir(parents=True)
            target.write_text('Unexpected manual route', encoding='utf-8')
            self.assertTrue(any('fallback inventory' in e for e in builder.verify_packages(ROOT, output)))


if __name__ == '__main__':
    unittest.main()
