"""Distribution boundaries, repeatability and isolated rebuilds for both profiles."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SHARED = Path(__file__).resolve().parents[1]
ROOT = SHARED.parent / 'scoville-suite'
sys.path.insert(0, str(SHARED / 'build'))
import build_suite as builder
import export_suite


class DistributionProfilesTests(unittest.TestCase):
    def test_membership_fallbacks_invocations_and_repeatability(self):
        for profile, layout, count in [('general', 'standalone', 5), ('general', 'suite', 5), ('codex', 'suite', 6)]:
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as temp:
                config = builder.load(ROOT, profile, layout)
                self.assertEqual(count, len(config['members']))
                self.assertEqual(profile == 'codex', any(m['name'] == 'scoville-workflow-for-codex' for m in config['members']))
                first = Path(temp) / 'a'
                second = Path(temp) / 'b'
                a = builder.build(ROOT, first, True, [], profile, layout)
                b = builder.build(ROOT, second, True, [], profile, layout)
                self.assertEqual(a, b)
                self.assertEqual([], builder.verify_packages(ROOT, first))
                for member in config['members']:
                    package = builder.payload(ROOT, member, config)
                    self.assertFalse(any(b'{{' in data for name, data in package.items() if name.endswith(('.md', '.toml'))))
                    if profile == 'codex':
                        self.assertFalse(any('without-python' in name for name in package))
                        self.assertFalse(any(b'without-python' in data for name, data in package.items() if name.endswith('.md') and name != 'CHANGELOG.md'))
                    usage = package['README.md'].decode().split('## How to use\n', 1)[1].split('\n## ', 1)[0]
                    # Invocation examples precede optional usage subsections and task-title illustration.
                    examples = usage.split('\n### ', 1)[0].split('Task titles identify', 1)[0]
                    self.assertEqual(1 if member['name'] == 'scoville-workflow-for-codex' else 2, examples.count('```text'))
                    core = package[member['name'] + '/SKILL.md'].decode()
                    readme = package['README.md'].decode()
                    if layout == 'suite':
                        self.assertNotIn('## Family', readme)
                        self.assertNotIn('Family owners', core)
                        self.assertNotIn('Relevant neighboring owners', core)
                        self.assertIn('installed and enabled', core)
                        self.assertIn('Partial installation is not supported', readme)
                        install = readme.split('## Install', 1)[1].split('## How to use', 1)[0]
                        self.assertIn(config['repository'] + '/tree/main/packages', install)
                        self.assertNotIn('https://github.com/benjaminstelzer/' + member['name'] + '/tree/', install)
                        for name, data in package.items():
                            if name.endswith('.md') and name != 'CHANGELOG.md':
                                for stale in ('independently available', 'unknown availability', 'Without Plan', 'If Plan is absent', 'optional Skill', 'When Plan is available', 'instructions are present and applicable'):
                                    self.assertNotIn(stale, data.decode(), (member['name'], name))
                    else:
                        self.assertIn('## Family', readme)
                        self.assertIn('This Skill works independently', core)
                        self.assertIn('This Skill works on its own', readme)
                if profile == 'general':
                    plan = next(m for m in config['members'] if m['name'] == 'scoville-plan')
                    self.assertEqual(4, sum('without-python' in name for name in builder.payload(ROOT, plan, config)))

    def test_refresh_preserves_inventory_and_refuses_local_changes(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'current'
            first = builder.build(ROOT, output, True, ['scoville-plan'], 'general', 'standalone')
            refreshed = builder.build(ROOT, output, True, ['scoville-plan'], 'general', 'standalone', refresh=True)
            self.assertEqual(first, refreshed)
            self.assertEqual([], builder.verify_packages(ROOT, output))
            with self.assertRaisesRegex(ValueError, 'same suite/profile/layout'):
                builder.build(ROOT, output, True, [], 'codex', 'suite', refresh=True)
            extra = output / 'unexpected.txt'
            extra.write_text('retain me', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'inventory changed'):
                builder.build(ROOT, output, True, ['scoville-plan'], 'general', 'standalone', refresh=True)
            self.assertEqual('retain me', extra.read_text(encoding='utf-8'))
            extra.unlink()
            readme = output / first['members'][0]['package_path'] / 'README.md'
            readme.write_text('local edit', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'changed staging file'):
                builder.build(ROOT, output, True, ['scoville-plan'], 'general', 'standalone', refresh=True)
            self.assertEqual('local edit', readme.read_text(encoding='utf-8'))

    def test_profile_errors_fail_closed(self):
        with self.assertRaisesRegex(ValueError, 'unknown build profile'):
            builder.load(ROOT, 'typo')
        with self.assertRaisesRegex(ValueError, 'suite-only'):
            builder.load(ROOT, 'codex', 'standalone')
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'complete member set'):
                builder.build(ROOT, Path(temp) / 'partial', True, ['scoville-plan'], 'general', 'suite')
        for text in ('{{ profile: typo }}x{{ /profile }}', '{{ profile: codex }}x', '{{ profile: codex }}{{ profile: general }}x{{ /profile }}{{ /profile }}'):
            with self.assertRaises(ValueError):
                builder.profile_text(text, 'codex')
        with self.assertRaisesRegex(ValueError, 'unknown build fragment'):
            builder.expand_fragments(ROOT, '{{ include: typo }}', config=builder.load(ROOT, 'codex'))

    def test_exports_replace_stale_packages_and_rebuild_in_isolation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'source'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.tmp', 'packages', 'node_modules', 'target'))
            stale = root / 'packages/obsolete/private.txt'
            stale.parent.mkdir(parents=True)
            stale.write_text('must never export', encoding='utf-8')
            def git(*args):
                return subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)
            git('init')
            git('add', '--force', '.')
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-m', 'fixture')
            for profile in ('general', 'codex'):
                output = Path(temp) / profile
                receipt = export_suite.export(root, output, profile)
                self.assertEqual(profile, receipt['profile'])
                self.assertFalse((output / 'packages/obsolete').exists())
                self.assertEqual(profile == 'codex', (output / 'members/scoville-workflow-for-codex').exists())
                if profile == 'codex':
                    self.assertFalse(list((output / 'members').rglob('*without-python.md')))
                config = builder.load(output)
                self.assertNotIn('profiles', config)
                isolated_path = output / 'development/shared/build/build_suite.py'
                spec = importlib.util.spec_from_file_location('isolated_profile_builder', isolated_path)
                isolated = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(isolated)
                for member in config['members']:
                    expected = builder.payload(ROOT, member, builder.load(ROOT, profile, 'suite'))
                    rebuilt = isolated.payload(output, member, config)
                    self.assertEqual(expected, rebuilt, member['name'])
                    actual = {p.relative_to(output / 'packages' / member['name']).as_posix(): p.read_bytes()
                              for p in (output / 'packages' / member['name']).rglob('*') if p.is_file()}
                    self.assertEqual(expected, actual)
                self.assertEqual([], isolated.render_readmes(output, False))


if __name__ == '__main__':
    unittest.main()
