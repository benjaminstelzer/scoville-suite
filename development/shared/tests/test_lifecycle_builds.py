import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SHARED = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('builder', SHARED / 'build/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class LifecycleBuildTests(unittest.TestCase):
    def test_isolated_exported_consumers_and_receipt(self):
        for suite, expected in [('scoville-suite', 2)]:
            root = SHARED.parent / suite
            profile = 'codex' if suite == 'scoville-suite' else None
            members = [m for m in builder.load(root, profile)['members'] if any(h['source'] == 'runtime/task_lifecycle.py' for h in m.get('shared_helpers', []))]
            self.assertEqual(expected, len(members))
            with tempfile.TemporaryDirectory() as temp:
                output = Path(temp) / 'build'
                receipt = builder.build(root, output, False, [] if profile else [m['name'] for m in members], profile)
                for member in members:
                    name = member['name']
                    relative = f'scoville-suite-for-codex/packages/{name}' if profile == 'codex' else name
                    script = output / relative / name / 'scripts/task_lifecycle.py'
                    built = next(m for m in receipt['members'] if m['name'] == name)
                    self.assertEqual(relative, built['package_path'])
                    if profile == 'codex':
                        self.assertEqual('benjaminstelzer/scoville-suite-for-codex', built['repository'])
                        self.assertEqual('suite', built['distribution'])
                        self.assertFalse((output / name).exists())
                    self.assertEqual((SHARED / 'runtime/task_lifecycle.py').read_bytes(), script.read_bytes())
                    self.assertEqual(hashlib.sha256(script.read_bytes()).hexdigest(), receipt['shared_sources']['runtime/task_lifecycle.py'])
                    # -I excludes source-checkout and environment import paths.
                    process = subprocess.run([sys.executable, '-I', '-B', str(script)],
                        input=json.dumps({'operation': 'verify_archive', 'handle': {'state': 'ready', 'threadId': 'child'},
                                          'reply': {'threadId': 'child', 'archived': True}}),
                        text=True, capture_output=True, cwd=temp)
                    self.assertEqual(0, process.returncode, process.stderr)
                    self.assertTrue(json.loads(process.stdout)['verified'])
                    title_request = {'operation': 'task_title', 'family': 'ask', 'role': 'adviser',
                                     'subject': 'Review', 'adviser': 'SOL', 'attempt': 1}
                    process = subprocess.run([sys.executable, '-I', '-B', str(script)],
                        input=json.dumps(title_request), text=True, capture_output=True, cwd=temp)
                    self.assertEqual(0, process.returncode, process.stderr)
                    self.assertEqual('ASK Review SOL RUN [#1]', json.loads(process.stdout)['title'])
                self.assertEqual([], builder.verify_shared_helpers(root, output))
                original = script.read_bytes()
                script.write_bytes(original + b'\n# drift')
                self.assertTrue(any('shared helper drift' in e for e in builder.verify_shared_helpers(root, output)))
                script.write_bytes(original)
                self.assertEqual([], builder.verify_shared_helpers(root, output))

    def test_duplicate_mapping_cannot_shadow_shared_owner(self):
        root = SHARED.parent / 'scoville-suite'
        member = copy.deepcopy(next(m for m in builder.load(root, 'codex')['members'] if any(h['source'] == 'runtime/task_lifecycle.py' for h in m.get('shared_helpers', []))))
        member['shared_helpers'].append(member['shared_helpers'][0])
        with self.assertRaisesRegex(ValueError, 'duplicate shared output'):
            builder.payload(root, member, builder.load(root, 'codex'))


if __name__ == '__main__':
    unittest.main()
