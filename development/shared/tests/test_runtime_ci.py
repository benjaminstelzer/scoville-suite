"""Runtime build acceptance requires actual successful matrix provenance and bytes."""
import base64
import ast
import copy
import importlib.util
import json
import re
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
spec = importlib.util.spec_from_file_location('runtime_builder_test', SHARED / 'build/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class RuntimeGateTests(unittest.TestCase):
    def test_workflow_and_gate_cover_the_same_platforms_and_python_versions(self):
        workflow = (SHARED / 'runtime-tests/runtime-helpers.yml').read_text(encoding='utf-8')
        systems = tuple(part.strip() for part in re.search(r'^\s+os: \[(.+)\]$', workflow, re.M)[1].split(','))
        pythons = tuple(ast.literal_eval(re.search(r'^\s+python: (\[.+\])$', workflow, re.M)[1]))
        self.assertEqual(gate.SYSTEMS, systems)
        self.assertEqual({'windows', 'macos', 'ubuntu'}, {name.split('-')[0] for name in systems})
        self.assertEqual(3, len(systems))
        self.assertEqual(('3.11', '3.x'), pythons)
        self.assertEqual(gate.PYTHONS, pythons)

    def test_minimum_python_workflow_selects_existing_tests(self):
        workflow = (SHARED / 'runtime-tests/runtime-helpers.yml').read_text(encoding='utf-8')
        selection = re.search(r'names = (\[.*?\]);', workflow, re.S)
        self.assertIsNotNone(selection)
        names = ast.literal_eval(selection.group(1))
        tree = ast.parse((SHARED / 'runtime-tests/test_runtime_helpers.py').read_text(encoding='utf-8'))
        case = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'RuntimeHelpers')
        methods = {node.name for node in case.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue(names)
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(set(names) - methods, set())

    def setUp(self):
        self.root = SHARED.parent / 'scoville-suite'
        self.member = {'name': 'example', 'helper_contracts': {'scripts/helper.py': {'kind': 'helper'}},
                       'files': [{'target': 'example/operations.md', 'runtime_role': 'instruction'}]}
        self.config = {'profile': 'codex', 'layout': 'suite', 'members': [self.member]}
        self.payload = {'example/scripts/helper.py': b'print("ok")\n', 'example/SKILL.md': b'skill\n',
                        'example/operations.md': b'instruction\n', 'example/writing.md': b'input\n',
                        'example/config.json': b'{}\n'}
        self.builder = SimpleNamespace(payload=lambda *args: self.payload, runtime_scope=builder.runtime_scope)
        self.files = {'example/' + name: gate.digest(data) for name, data in self.payload.items()}
        scope = builder.runtime_scope([self.member])
        self.meta = {'schema_version': 2, 'variants': {'codex-suite': {'files': dict(self.files), **scope,
            'runtime_inputs': {p: h for p, h in self.files.items() if p not in scope['instruction_files']}}},
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
        receipt = {'runtime_validation': {'status': 'pending'}, 'runtime_scope': builder.runtime_scope([self.member]),
                   'members': [{'name': 'example',
            'files': {name: gate.digest(data) for name, data in self.payload.items()}}]}
        gate.bind_receipt(receipt, proof)
        self.assertEqual(receipt['runtime_validation']['status'], 'passed')
        receipt['runtime_validation'] = {'status': 'pending'}
        receipt['members'][0]['files']['example/SKILL.md'] = 'changed'
        with self.assertRaisesRegex(ValueError, 'changed during'):
            gate.bind_receipt(receipt, proof)
        self.assertEqual(receipt['runtime_validation']['status'], 'pending')

    def test_non_python_delta_reuses_proof_but_binds_current_bytes_and_scope(self):
        self.payload['example/operations.md'] = b'clearer instruction\n'
        proof = self.verify()
        self.assertEqual(proof['evidence'], 'reused')
        self.assertEqual(proof['non_python_deltas'], ['example/example/operations.md'])
        self.assertNotEqual(proof['packages_sha256'], proof['tested_packages_sha256'])
        receipt = {'runtime_validation': {'status': 'pending'},
                   'runtime_scope': builder.runtime_scope([self.member]),
                   'members': [{'name': 'example', 'files': {p: gate.digest(b) for p, b in self.payload.items()}}]}
        gate.bind_receipt(receipt, proof)
        for mutate in ('classification', 'contract', 'evidence', 'delta'):
            with self.subTest(mutate=mutate):
                candidate, altered = copy.deepcopy(receipt), copy.deepcopy(proof)
                candidate['runtime_validation'] = {'status': 'pending'}
                if mutate == 'classification': candidate['runtime_scope']['instruction_files'] = []
                elif mutate == 'contract': candidate['runtime_scope']['helper_contracts'] = {}
                elif mutate == 'evidence': altered['evidence'] = 'exact'
                else: altered['non_python_deltas'] = ['example/example/scripts/helper.py']
                with self.assertRaises(ValueError): gate.bind_receipt(candidate, altered)
                self.assertEqual(candidate['runtime_validation']['status'], 'pending')

    def test_python_content_and_inventory_changes_require_new_evidence(self):
        original = dict(self.payload)
        for path in ('example/scripts/helper.py', 'example/unknown.py'):
            with self.subTest(path=path):
                self.payload[path] = b'changed'
                with self.assertRaisesRegex(ValueError, 'Python packages differ'): self.verify()
                self.payload = dict(original)
        del self.payload['example/scripts/helper.py']
        with self.assertRaisesRegex(ValueError, 'Python packages differ'): self.verify()

    def test_non_python_content_inventory_and_classification_reuse_successful_matrix(self):
        original = dict(self.payload)
        for path in ('example/SKILL.md', 'example/writing.md', 'example/config.json',
                     'example/assets/workflow.toml', 'README.md', 'example/new.md'):
            with self.subTest(path=path):
                self.payload[path] = b'changed'
                proof = self.verify()
                self.assertEqual(proof['evidence'], 'reused')
                self.assertIn('example/' + path, proof['non_python_deltas'])
                self.payload = dict(original)
        del self.payload['example/config.json']
        self.assertIn('example/example/config.json', self.verify()['non_python_deltas'])
        self.payload = dict(original)
        self.member['files'][0].pop('runtime_role')
        self.assertEqual(self.verify()['evidence'], 'exact')
        self.member['files'][0]['runtime_role'] = 'instruction'
        self.member['files'].append({'target': 'example/writing.md', 'runtime_role': 'instruction'})
        self.assertEqual(self.verify()['evidence'], 'exact')

    def test_scope_metadata_cannot_hide_unknown_or_protected_inputs(self):
        original = copy.deepcopy(self.meta)
        for mutate in ('missing', 'extra', 'inconsistent', 'duplicate', 'unknown_instruction'):
            with self.subTest(mutate=mutate):
                row = self.meta['variants']['codex-suite']
                if mutate == 'missing': row.pop('runtime_inputs')
                elif mutate == 'extra': row['exempt_all'] = True
                elif mutate == 'inconsistent': row['runtime_inputs'].pop('example/example/writing.md')
                elif mutate == 'duplicate': row['instruction_files'] *= 2
                else: row['instruction_files'].append('example/example/missing.md')
                with self.assertRaisesRegex(ValueError, 'scope metadata'): self.verify()
                self.meta = copy.deepcopy(original)

    def test_schema_one_proof_also_covers_unchanged_python(self):
        self.meta['schema_version'] = 1
        row = self.meta['variants']['codex-suite']
        row.pop('runtime_inputs')
        row.pop('instruction_files')
        self.assertEqual(self.verify()['evidence'], 'exact')
        row['exempt_all'] = True
        with self.assertRaisesRegex(ValueError, 'scope metadata'): self.verify()
        row.pop('exempt_all')
        self.payload['example/operations.md'] = b'changed'
        self.assertEqual(self.verify()['evidence'], 'reused')

    def test_invalid_instruction_classification_is_rejected_by_manifest_loader(self):
        original = json.loads((self.root / 'suite.json').read_text(encoding='utf-8'))
        for target, value, shared in (('scripts/helper.py', 'instruction', False),
                                      ('config.json', 'instruction', False),
                                      ('instruction.md', 'unknown', False),
                                      ('instruction.md', 'instruction', True)):
            with self.subTest(target=target, shared=shared), tempfile.TemporaryDirectory() as temporary:
                raw = copy.deepcopy(original)
                member = raw['members'][0]
                item = {'source': 'irrelevant', 'target': target, 'runtime_role': value}
                member.setdefault('shared_helpers' if shared else 'files', []).append(item)
                path = Path(temporary)
                (path / 'suite.json').write_text(json.dumps(raw), encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'runtime_role'): builder.load(path)

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
        original = copy.deepcopy(self.meta)
        self.meta['variants']['codex-suite']['helper_contracts'] = {}
        with self.assertRaisesRegex(ValueError, 'scope metadata'): self.verify()
        self.meta = copy.deepcopy(original)
        self.meta['test_assets']['tests/test_runtime_helpers.py'] = 'stale'
        with self.assertRaisesRegex(ValueError, 'tests changed'): self.verify()
        self.meta = copy.deepcopy(original)
        self.meta['test_assets']['unknown.py'] = gate.digest(b'unknown')
        with self.assertRaisesRegex(ValueError, 'tests changed'): self.verify()

    def test_non_python_ci_asset_change_does_not_require_new_matrix(self):
        self.meta['test_assets'][gate.WORKFLOW] = 'earlier workflow'
        self.assertEqual(self.verify()['evidence'], 'exact')

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
