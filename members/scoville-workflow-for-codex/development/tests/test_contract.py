from pathlib import Path
import hashlib
import html
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[2]
# Exercise the actual package, including bundled shared helpers and defaults.
SUITE_ROOT = ROOT.parents[1]
_build_spec = importlib.util.spec_from_file_location("workflow_test_build", SUITE_ROOT / "development/build_suite.py")
_builder = importlib.util.module_from_spec(_build_spec)
_build_spec.loader.exec_module(_builder)
_test_package = tempfile.TemporaryDirectory(prefix="workflow-tests-", ignore_cleanup_errors=True)
PACKAGE = Path(_test_package.name) / "scoville-workflow-for-codex"
_config = _builder.load(SUITE_ROOT, 'codex')
_member = next(m for m in _config['members'] if m['name'] == PACKAGE.name)
for _name, _data in _builder.payload(SUITE_ROOT, _member, _config).items():
    _target = Path(_test_package.name) / _name
    _target.parent.mkdir(parents=True, exist_ok=True)
    _target.write_bytes(_data)
ROLE_RESULT_PARSER = PACKAGE / "scripts/parse_role_result.py"
MODEL_RESOLVER = PACKAGE / "scripts/resolve_model_pair.py"
SELECTOR = SUITE_ROOT / "members/scoville-plan/scoville-plan/scripts/select_context.py"
sys.path.insert(0, str(PACKAGE / "scripts"))
import resolve_model_pair as model_resolver
import parse_role_result as role_result_parser
import build_dispatch_prompt as prompt_builder

class NativeWorkflowContractTests(unittest.TestCase):
    @staticmethod
    def run_result_parser(raw, role="executor"):
        return subprocess.run(
            [sys.executable, "-B", str(ROLE_RESULT_PARSER), "--role", role],
            input=raw,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )

    @staticmethod
    def run_result_parser_bytes(raw, role="executor"):
        return subprocess.run(
            [sys.executable, "-B", str(ROLE_RESULT_PARSER), "--role", role],
            input=raw,
            capture_output=True,
            check=False,
        )

    def test_role_result_helper_accepts_only_ordered_line_protocol(self):
        valid = {
            "executor": (
                "SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\n"
                "code_changed=yes\ncritical_docs_changed=no\nsummary=Implemented.\n"
                "finding=One issue remains."
            ),
            "repair": (
                "SCOVILLE_RESULT_V1\nrole=repair\nstatus=completed\n"
                "code_changed=no\ncritical_docs_changed=yes\nsummary=Documentation corrected."
            ),
            "reviewer": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=Review passed.",
        }
        for role, raw in valid.items():
            with self.subTest(role=role):
                completed = self.run_result_parser(raw, role)
                self.assertEqual(0, completed.returncode, completed.stdout)
                payload = json.loads(completed.stdout)
                self.assertTrue(payload["valid"])
                self.assertEqual(role_result_parser.parse_role_result(raw, role), payload["result"])
        self.assertEqual(
            "pass",
            role_result_parser.parse_role_result(
                "SCOVILLE_RESULT_V1\r\nrole=reviewer\r\nstatus=pass\r\nsummary=Review passed.\r\n",
                "reviewer",
            )["status"],
        )
        eight_findings = (
            "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\nsummary=One\n"
            + "\n".join("finding=x" for _ in range(8))
        )
        self.assertEqual(0, self.run_result_parser(eight_findings, "reviewer").returncode)

        invalid = {
            "json": '{"status":"pass","summary":"Review passed.","findings":[]}',
            "fence": "```text\nSCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=Review passed.\n```",
            "missing": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass",
            "duplicate": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\nsummary=Two",
            "unknown": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\nnote=Two",
            "unordered": "SCOVILLE_RESULT_V1\nstatus=pass\nrole=reviewer\nsummary=One",
            "wrong_role": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=pass\nsummary=One",
            "bad_status": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=completed\nsummary=One",
            "pass_finding": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\nfinding=Two",
            "empty": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=blocked\nsummary=",
            "multiline": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=blocked\nsummary=First\nsecond line",
            "trailing_blank": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\n\n",
            "nine_findings": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\nsummary=One\n" + "\n".join("finding=x" for _ in range(9)),
            "long_summary": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=blocked\nsummary=" + "x" * 801,
            "long_finding": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\nsummary=One\nfinding=" + "x" * 401,
            "completion_fields_missing": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\nsummary=One",
            "completion_fields_on_block": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=blocked\ncode_changed=no\ncritical_docs_changed=no\nsummary=One",
        }
        for name, raw in invalid.items():
            with self.subTest(name=name):
                completed = self.run_result_parser(raw, "reviewer" if name not in {"completion_fields_missing", "completion_fields_on_block"} else "executor")
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertFalse(json.loads(completed.stdout)["valid"])
        with self.assertRaises(role_result_parser.RoleResultError):
            role_result_parser.parse_role_result(
                "SCOVILLE_RESULT_V1\rrole=reviewer\nstatus=pass\nsummary=One", "reviewer"
            )
        bare_cr = self.run_result_parser_bytes(
            b"SCOVILLE_RESULT_V1\rrole=reviewer\nstatus=pass\nsummary=One", "reviewer"
        )
        self.assertEqual(1, bare_cr.returncode, bare_cr.stdout)
        self.assertEqual("LINE_ENDING_INVALID", json.loads(bare_cr.stdout)["diagnostics"][0]["code"])

    def test_original_result_is_valid_but_flattened_snapshot_is_not(self):
        raw = "SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\ncode_changed=yes\ncritical_docs_changed=no\nsummary=Work and checks finished."
        self.assertEqual(role_result_parser.parse_role_result(raw, 'executor')['status'], 'completed')
        with self.assertRaises(ValueError):
            role_result_parser.parse_role_result(raw.replace('\n', ' '), 'executor')
        operations = (PACKAGE / 'references/operations.md').read_text(encoding='utf-8')
        self.assertIn('agentMessage.text', operations)
        self.assertIn('phase:final_answer', operations)
        self.assertIn('never parse that snapshot as the original result', operations)

    def test_model_resolver_rejects_malformed_user_config(self):
        source = (PACKAGE / "assets" / "workflow.toml").read_text(encoding="utf-8")
        for altered, diagnostic in (
            (source.replace('schema_version = 1', 'schema_version = true', 1), "schema_version"),
            (source.replace('reasoning = "low"', 'reasoning = []', 1), "invalid execute.ultra_low values"),
            (source.replace('reasoning = "low"', 'reasoning = { bad = true }', 1), "invalid execute.ultra_low values"),
        ):
            with self.subTest(diagnostic=diagnostic), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "workflow.toml"
                path.write_text(altered, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, diagnostic):
                    model_resolver.load_config(path)

    def test_models_preserve_five_routes_and_executor_overrides(self):
        config = model_resolver.load_config(PACKAGE / 'assets/workflow.toml', PACKAGE)
        self.assertEqual(set(config), {'schema_version', 'context', 'execute', 'review'})
        routes = ('ultra_low', 'low', 'medium', 'high', 'ultra_high')
        for role, table in [('executor', 'execute'), ('reviewer', 'review')]:
            self.assertEqual(set(config[table]), set(routes))
            for route in routes:
                pair = model_resolver.resolve(config, role, route)
                self.assertEqual(pair['model'], config[table][route]['model'])
                self.assertEqual(pair['thinking'], config[table][route]['reasoning'])
        pair = model_resolver.resolve(config, 'executor', 'low', 'custom', 'high')
        self.assertEqual(pair, dict(model='custom', thinking='high', route='low'))
        with self.assertRaises(ValueError):
            model_resolver.resolve(config, 'reviewer', 'low', 'custom')

    def test_explicit_plan_reasoning_reaches_dispatch_and_resolver(self):
        fixture_spec = importlib.util.spec_from_file_location('reasoning_fixture',
            SUITE_ROOT / 'members/scoville-plan/development/tests/test_select_context.py')
        fixture = importlib.util.module_from_spec(fixture_spec)
        fixture_spec.loader.exec_module(fixture)
        config = model_resolver.load_config(PACKAGE / 'assets/workflow.toml', PACKAGE)
        for level in ('none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra'):
            with self.subTest(level=level), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                (root / 'docs/plans').mkdir(parents=True)
                (root / 'docs/decisions').mkdir()
                (root / 'PROJECT_INDEX.md').write_text('---\nformat_version: 1\nactive_plan: PLAN-0001\n---\n', encoding='utf-8')
                annotation = '[execute: reasoning=' + level + ']'
                (root / 'docs/plans/0001-test.md').write_text(fixture.plan().replace(
                    '1. Inspect the producer.', '1. ' + annotation + ' Inspect the producer.'), encoding='utf-8')
                (root / 'docs/decisions/0001-test.md').write_text(fixture.DECISION, encoding='utf-8')
                context = prompt_builder.select_unit(SELECTOR, root, 'W-003/step-1')
                self.assertIn(annotation, context['work_item']['source_text'])
                prompt = prompt_builder.build_prompt('executor', root, 'manager', 'test', context, {})
                self.assertIn(annotation, prompt)
                pair = model_resolver.resolve(config, 'executor', 'low', override_reasoning=level)
                self.assertEqual(pair['thinking'], level)

    def test_repairs_use_original_pair_and_stop_after_three(self):
        config = model_resolver.load_config(PACKAGE / 'assets/workflow.toml', PACKAGE)
        expected = [('gpt-6-sol', 'high'), ('gpt-6-sol', 'xhigh'), ('gpt-6-astra', 'high')]
        for attempt, pair in enumerate(expected, 1):
            result = model_resolver.resolve(config, 'repair', original_model='gpt-6-sol',
                                            original_reasoning='high', repair_number=attempt)
            self.assertEqual((result['model'], result['thinking']), pair)
        for attempt in (0, 4):
            with self.assertRaises(ValueError):
                model_resolver.resolve(config, 'repair', original_model='gpt-6-sol',
                                       original_reasoning='high', repair_number=attempt)
        self.assertEqual(model_resolver.resolve(config, 'repair', original_model='custom',
                          original_reasoning='medium', repair_number=1),
                         dict(model='custom', thinking='medium'))
        with self.assertRaisesRegex(ValueError, 'not in the current execute route table'):
            model_resolver.resolve(config, 'repair', original_model='custom',
                                   original_reasoning='medium', repair_number=2)

    def test_actual_selector_source_and_crlf_survive_dispatch(self):
        fixture_spec = importlib.util.spec_from_file_location('plan_fixture',
            SUITE_ROOT / 'members/scoville-plan/development/tests/test_select_context.py')
        fixture = importlib.util.module_from_spec(fixture_spec)
        fixture_spec.loader.exec_module(fixture)
        for ending in ('\n', '\r\n'):
            with self.subTest(ending=repr(ending)), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary) / 'Änderung 中文'
                (root / 'docs/plans').mkdir(parents=True)
                (root / 'docs/decisions').mkdir()
                files = {'PROJECT_INDEX.md': '---\nformat_version: 1\nactive_plan: PLAN-0001\n---\n',
                         'docs/plans/0001-test.md': fixture.plan(10).replace(
                             'Evidence: [old executor attempt, old reviewer attempt]',
                             'Evidence: Prüfung mit Komma, Ergebnis erhalten.'),
                         'docs/decisions/0001-test.md': fixture.DECISION}
                for name, content in files.items():
                    (root / name).write_bytes(content.replace('\n', ending).encode('utf-8'))
                before = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
                for unit in ('W-004', 'W-003/step-2'):
                    context = prompt_builder.select_unit(SELECTOR, root, unit)
                    completed = subprocess.run([sys.executable, '-B', str(PACKAGE / 'scripts/build_dispatch_prompt.py'),
                        '--selector', str(SELECTOR), '--plan-root', str(root), '--unit', unit,
                        '--role', 'executor', '--workspace-root', str(root),
                        '--return-to-thread-id', 'manager', '--delivery-reference', 'dispatch'],
                        input='{}', text=True, encoding='utf-8', capture_output=True,
                        env={**os.environ, 'PYTHONIOENCODING': 'cp1252'})
                    self.assertEqual(completed.returncode, 0, completed.stderr)
                    embedded = next(line for line in completed.stdout.splitlines() if line.startswith('plan_context='))
                    self.assertEqual(json.loads(embedded.split('=', 1)[1]), context)
                    self.assertEqual(context['work_item']['unit'], unit)
                    self.assertTrue(context['work_item']['source_text'])
                for unit in ('W-003/step-1..2', 'W-003/step-0', 'W-999', 'W-003/step-4'):
                    with self.assertRaises(ValueError):
                        prompt_builder.select_unit(SELECTOR, root, unit)
                self.assertEqual(before, {p: p.read_bytes() for p in root.rglob('*') if p.is_file()})

    def test_role_inputs_preserve_handoff_and_reject_premature_review(self):
        context = {'work_item': {'unit': 'W-001', 'source_text': 'Exact assignment ✓'}}
        completed = dict(status='completed', summary='Fixed file, checked behavior.', findings=[],
                         review=dict(code_changed='yes', critical_docs_changed='no'))
        def build(role, data):
            return prompt_builder.build_prompt(role, PACKAGE, 'manager', 'dispatch', context, data)
        handoff = {'context_handoff': 'Finished first change; remaining check in module A.',
                   'supplemental_context': 'Preserve unrelated work.'}
        for role in ('executor', 'reviewer', 'repair'):
            data = dict(handoff)
            if role == 'reviewer':
                data['executor_result'] = completed
            if role == 'repair':
                data.update(reviewer_result=dict(status='changes_requested', summary='One defect.',
                                                 findings=['A: wrong output.', 'B: Plan correction.']),
                            repair_assignment=dict(finding_indices=[0]))
            prompt = build(role, data)
            self.assertIn('while your own assigned work remains unfinished', prompt)
            self.assertIn("The coordinator's later review and acceptance are not your unfinished work", prompt)
            self.assertIn(str(Path(sys.executable)), prompt)
            value = next(line for line in prompt.splitlines() if line.startswith('role_input='))
            self.assertEqual(json.loads(value.split('=', 1)[1]), data)
        for status in ('blocked', 'needs_user_decision', 'context_handoff'):
            with self.assertRaisesRegex(ValueError, 'review requires a completed'):
                build('reviewer', {'executor_result': dict(status=status, summary='Pending', findings=[])})
        findings = dict(status='changes_requested', summary='Two defects.', findings=['A', 'B'])
        for indices in ([], [2], [-1], [True], [1, 0], [0, 0]):
            with self.assertRaises(ValueError):
                build('repair', dict(reviewer_result=findings, repair_assignment=dict(finding_indices=indices)))
        with self.assertRaises(ValueError):
            build('repair', dict(reviewer_result=dict(status='pass', summary='Good', findings=[]),
                                 repair_assignment=dict(finding_indices=[0])))
        with self.assertRaises(ValueError):
            build('executor', {'unknown': True})


if __name__ == '__main__':
    unittest.main()
