"""Runtime build acceptance requires actual successful matrix provenance and bytes."""
import base64
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SHARED = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('runtime_gate_test', SHARED / 'build/runtime_ci.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class RuntimeGateTests(unittest.TestCase):
    def setUp(self):
        self.root = SHARED.parent / 'scoville-suite'
        self.member = {'name': 'example', 'helper_contracts': {'scripts/helper.py': {'kind': 'helper'}}}
        self.config = {'profile': 'codex', 'layout': 'suite', 'members': [self.member]}
        self.payload = {'example/scripts/helper.py': b'print("ok")\n', 'example/SKILL.md': b'skill\n'}
        self.builder = SimpleNamespace(payload=lambda *args: self.payload)
        self.files = {'example/' + name: gate.digest(data) for name, data in self.payload.items()}
        self.meta = {'schema_version': 1, 'variants': {'codex-suite': {'files': dict(self.files),
            'helper_contracts': {'example/example/scripts/helper.py': 'helper'}}},
            'test_assets': {name: gate.digest(data) for name, data in gate.assets().items()}}
        self.run = {'status': 'completed', 'conclusion': 'success', 'path': gate.WORKFLOW, 'head_sha': 'a' * 40, 'run_attempt': 1}
        self.jobs = [{'name': f'runtime ({os}, {py})', 'conclusion': 'success'} for os in gate.SYSTEMS for py in gate.PYTHONS]
        self.url = f'https://github.com/{gate.REPOSITORY}/actions/runs/123'

    def api(self, route):
        if route == f'repos/{gate.REPOSITORY}': return {'private': True}
        if '/jobs?' in route: return {'total_count': len(self.jobs), 'jobs': self.jobs}
        if '/contents/' in route:
            name = route.split('/contents/')[1].split('?')[0]
            data = json.dumps(self.meta).encode() if name == 'runtime-input.json' else gate.assets()[name]
            return {'encoding': 'base64', 'content': base64.b64encode(data).decode()}
        return self.run

    def verify(self):
        with patch.object(gate, 'api', side_effect=self.api):
            return gate.verify(self.builder, self.root, self.url, self.config)

    def test_success_reaches_receipt_and_changed_candidate_stays_pending(self):
        proof = self.verify()
        receipt = {'runtime_validation': {'status': 'pending'}, 'members': [{'name': 'example',
            'files': {name: gate.digest(data) for name, data in self.payload.items()}}]}
        gate.bind_receipt(receipt, proof)
        self.assertEqual(receipt['runtime_validation']['status'], 'passed')
        receipt['runtime_validation'] = {'status': 'pending'}
        receipt['members'][0]['files']['example/SKILL.md'] = 'changed'
        with self.assertRaisesRegex(ValueError, 'changed during'):
            gate.bind_receipt(receipt, proof)
        self.assertEqual(receipt['runtime_validation']['status'], 'pending')

    def test_missing_failed_skipped_and_incomplete_matrix_are_rejected(self):
        with patch.object(gate, 'api') as api:
            with self.assertRaisesRegex(ValueError, '--runtime-run'):
                gate.verify(self.builder, self.root, None, self.config)
            api.assert_not_called()
        self.run['conclusion'] = 'failure'
        with self.assertRaisesRegex(ValueError, 'completed successfully'): self.verify()
        self.run['conclusion'] = 'success'
        self.jobs[0]['conclusion'] = 'skipped'
        with self.assertRaisesRegex(ValueError, 'Every Windows'): self.verify()
        self.jobs.pop(0)
        with self.assertRaisesRegex(ValueError, 'Every Windows'): self.verify()

    def test_old_package_dependency_registry_or_test_cannot_authorize_build(self):
        self.payload['example/SKILL.md'] = b'changed dependency'
        with self.assertRaisesRegex(ValueError, 'packages differ'): self.verify()
        self.payload['example/SKILL.md'] = b'skill\n'
        self.meta['variants']['codex-suite']['helper_contracts'] = {}
        with self.assertRaisesRegex(ValueError, 'registry changed'): self.verify()
        self.meta['test_assets'][gate.WORKFLOW] = 'stale'
        with self.assertRaisesRegex(ValueError, 'tests changed'): self.verify()

    def test_build_cli_without_evidence_does_not_write_packages(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'packages'
            process = subprocess.run([sys.executable, '-B', str(self.root / 'development/build_suite.py'),
                '--profile', 'codex', '--output', str(output)], capture_output=True, text=True, encoding='utf-8')
            self.assertNotEqual(process.returncode, 0)
            self.assertIn('--runtime-run', process.stderr)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
