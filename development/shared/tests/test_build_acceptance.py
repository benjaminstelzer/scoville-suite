"""Regression probes for package inventory, runtime exemptions and release sync."""
import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SHARED = Path(__file__).resolve().parents[1]
def module(name, file):
    spec = importlib.util.spec_from_file_location(name, SHARED / 'build' / file)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result
builder = module('acceptance_builder', 'build_suite.py')
gate = module('acceptance_runtime', 'runtime_ci.py')

class BuildAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.root = SHARED.parent / 'scoville-suite'
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / 'packages'
        self.receipt = builder.build(self.root, self.output, False, ['scoville-code'], 'general', 'standalone')
        self.receipt_path = self.output / 'build-receipt.json'

    def save(self, receipt):
        self.receipt_path.write_text(json.dumps(receipt), encoding='utf-8')

    def test_legitimate_standalone_subset_and_changed_receipts(self):
        self.assertEqual([], builder.verify_packages(self.root, self.output))
        for mutate in ('empty', 'duplicate', 'hash', 'path', 'manifest'):
            with self.subTest(mutate=mutate):
                receipt = copy.deepcopy(self.receipt)
                if mutate == 'empty': receipt['members'] = []
                elif mutate == 'duplicate': receipt['members'] *= 2
                elif mutate == 'hash':
                    name = next(iter(receipt['members'][0]['files']))
                    receipt['members'][0]['files'][name] = '0' * 64
                elif mutate == 'path': receipt['members'][0]['package_path'] = '../escape'
                else: receipt['manifest_sha256'] = '0' * 64
                self.save(receipt)
                self.assertTrue(builder.verify_packages(self.root, self.output))
        self.save(self.receipt)
        (self.output / 'extra.txt').write_bytes(b'extra')
        self.assertTrue(builder.verify_packages(self.root, self.output))
        (self.output / 'extra.txt').unlink()
        (self.output / 'empty-extra').mkdir()
        self.assertTrue(builder.verify_packages(self.root, self.output))

    def test_malformed_receipts_produce_diagnostics_without_traceback(self):
        cases = [[], {'members': [None]}, {'members': [{'name': [], 'files': {}}]},
                 {'members': [{'name': 'scoville-code', 'files': []}]}]
        for values in cases:
            with self.subTest(values=values):
                receipt = values if isinstance(values, list) else dict(self.receipt, **values)
                self.save(receipt)
                self.assertTrue(builder.verify_packages(self.root, self.output))
                result = subprocess.run([sys.executable, str(self.root / 'development/build_suite.py'),
                    '--check-packages', '--output', str(self.output)], capture_output=True,
                    text=True, encoding='utf-8')
                self.assertEqual(1, result.returncode)
                self.assertFalse(json.loads(result.stdout)['valid'])
                self.assertNotIn('Traceback', result.stderr)

    def test_suite_requires_all_configured_members(self):
        self.receipt['layout'] = 'suite'
        self.save(self.receipt)
        self.assertIn('complete member set', '; '.join(builder.verify_packages(self.root, self.output)))

    def test_python_outside_registered_scripts_is_rejected(self):
        member = {'name': 'example', 'helper_contracts': {}}
        files = {'example/SKILL.md': b'# Example', 'example/references/helper.py': b'print(1)'}
        with self.assertRaisesRegex(ValueError, 'registered under scripts'):
            builder.validate_helper_contracts(files, member, {'profile': 'general'})
        with self.assertRaisesRegex(ValueError, 'Unregistered'):
            gate.verify(SimpleNamespace(payload=lambda *args: files, runtime_scope=builder.runtime_scope), self.root, None,
                        {'members': [member]})

    def test_exemption_binds_the_exact_candidate_and_cannot_replace_pending(self):
        payload = {'example/SKILL.md': b'current'}
        proof = gate.verify(SimpleNamespace(payload=lambda *args: payload, runtime_scope=builder.runtime_scope), self.root, None,
                            {'members': [{'name': 'example', 'helper_contracts': {}}]})
        receipt = {'members': [{'name': 'example', 'files': {k: gate.digest(v) for k,v in payload.items()}}],
                   'runtime_validation': {'status': 'not_applicable'}}
        gate.bind_receipt(receipt, proof)
        receipt['members'][0]['files']['example/SKILL.md'] = 'changed'
        with self.assertRaisesRegex(ValueError, 'changed during'):
            gate.bind_receipt(receipt, proof)
        receipt['members'][0]['files']['example/SKILL.md'] = gate.digest(b'current')
        receipt['runtime_validation'] = {'status': 'pending'}
        with self.assertRaisesRegex(ValueError, 'helper-bearing'):
            gate.bind_receipt(receipt, proof)
        self.assertEqual({'status': 'pending'}, receipt['runtime_validation'])

    def test_release_sync_consumer_rejects_mismatch_and_accepts_sync(self):
        with patch.object(builder.subprocess, 'run', return_value=SimpleNamespace(returncode=1,stderr='',stdout='changed snapshot')):
            with self.assertRaisesRegex(ValueError, 'not in sync'):
                builder.check_shared_snapshot(self.root)
        with patch.object(builder.subprocess, 'run', return_value=SimpleNamespace(returncode=0,stderr='',stdout='')) as run:
            builder.check_shared_snapshot(self.root)
            self.assertIn('--check', run.call_args.args[0])

if __name__ == '__main__':
    unittest.main()
