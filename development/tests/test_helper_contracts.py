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

    def test_policy_owners_are_unique_reachable_and_profile_safe(self):
        for profile in ('general', 'codex'):
            for change in ('missing', 'duplicate', 'moved', 'unreachable', 'example_only', 'bad_owner', 'library_owner'):
                config, member, files = self.package(profile)
                owner = 'scoville-plan/references/output-delivery.md'
                policy = builder.helper_policy(member, 'references/output-delivery.md').encode()
                if change == 'missing': files[owner] = files[owner].replace(policy, b'')
                elif change == 'duplicate': files['scoville-plan/SKILL.md'] += b'\n' + policy
                elif change == 'moved':
                    files[owner] = files[owner].replace(policy, b'')
                    files['scoville-plan/SKILL.md'] += b'\n' + policy
                elif change in ('unreachable', 'example_only'):
                    for path in files:
                        if path.endswith('.md') and path != owner:
                            files[path] = files[path].replace(b'](references/output-delivery.md)', b'](#output)').replace(b'](output-delivery.md)', b'](#output)')
                    if change == 'example_only':
                        files['scoville-plan/SKILL.md'] += b'\n```markdown\n[Output](references/output-delivery.md)\n```\n'
                elif change == 'bad_owner': member['helper_contracts']['scripts/check_text_size.py']['policy'] = '../sibling/SKILL.md'
                else: member['helper_contracts']['scripts/markdown_structure.py']['policy'] = 'SKILL.md'
                with self.subTest(profile=profile, change=change), self.assertRaises(ValueError):
                    builder.validate_helper_contracts(files, member)

    def test_each_profile_projects_task_policy_to_its_operation_owner(self):
        for profile, layout in [('general', 'standalone'), ('general', 'suite'), ('codex', 'suite'), ('codex', 'standalone')]:
            config = builder.load(ROOT, profile, layout)
            for member in config['members']:
                files = builder.payload(ROOT, member, config)
                for helper, rule in member.get('helper_contracts', {}).items():
                    if rule['kind'] != 'helper':
                        continue
                    owner = rule.get('policy', 'SKILL.md')
                    expected_owner = ('references/output-delivery.md' if helper == 'scripts/check_text_size.py'
                                      else {'scoville-ask-for-codex': 'references/configuration.md',
                                            'scoville-workflow-for-codex': 'references/operations.md'}.get(member['name'], 'SKILL.md'))
                    self.assertEqual(expected_owner, owner)
                    policy = builder.helper_policy(member, owner).encode()
                    self.assertIn(policy, files[member['name'] + '/' + owner])
                    if helper == 'scripts/check_text_size.py':
                        self.assertNotIn(policy, files[member['name'] + '/SKILL.md'])
                builder.validate_package_links(files)

    def test_missing_registration_and_library_misclassification_fail_build(self):
        for change in ('missing', 'library', 'unknown_key'):
            config, member, _ = self.package()
            rule = member['helper_contracts']['scripts/select_context.py']
            if change == 'missing':
                del member['helper_contracts']['scripts/select_context.py']
            elif change == 'library':
                rule.clear(); rule['kind'] = 'library'
            else:
                rule['route'] = 'references/route.md'
            with self.subTest(change=change), self.assertRaises(ValueError):
                builder.payload(ROOT, member, config)

    def test_mutated_packages_fail_at_the_contract_boundary(self):
        for change in ('new_script', 'missing_used_helper'):
            _, member, files = self.package()
            if change == 'new_script': files['scoville-plan/scripts/unregistered.py'] = b'print("new")'
            else: files['scoville-plan/SKILL.md'] += b'\nRun scripts/missing.py to complete selection.\n'
            with self.subTest(change=change), self.assertRaises(ValueError):
                builder.validate_helper_contracts(files, member)

    def test_verify_rejects_file_injected_after_build(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'built'
            receipt = builder.build(ROOT, output, True, [], 'codex', 'suite')
            member = next(m for m in receipt['members'] if m['name'] == 'scoville-plan')
            target = output / member['package_path'] / 'scoville-plan/references/extra.md'
            target.write_text('Unexpected instructions', encoding='utf-8')
            self.assertIn('scoville-plan: package differs from current sources', builder.verify_packages(ROOT, output))


if __name__ == '__main__':
    unittest.main()
