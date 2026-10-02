"""Check documented complete invocations against actual argparse declarations."""
import ast
import argparse
from pathlib import Path
import re
import runpy
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
MEMBERS = ('scoville-workflow-for-codex', 'scoville-ask-for-codex', 'scoville-plan', 'scoville-setup')


def signature(path, command=None):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    if path.name == 'build_dispatch_prompt.py' or any(
            isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr == 'add_subparsers' for node in ast.walk(tree)):
        captured = []

        class ParserReady(BaseException):
            pass

        def capture(parser, *args, **kwargs):
            captured.append(parser)
            raise ParserReady()

        previous_path = sys.path[:]
        try:
            sys.path.insert(0, str(path.parent))
            sys.path.insert(1, str(ROOT / 'development/shared/runtime'))
            namespace = runpy.run_path(str(path))
            with patch.object(argparse.ArgumentParser, 'parse_args', capture), patch.dict(namespace['main'].__globals__, configure_utf8=lambda: None):
                try:
                    namespace['main']()
                except ParserReady:
                    pass
        finally:
            sys.path[:] = previous_path
        parser = captured[0]
        actions = list(parser._actions)
        for action in parser._actions:
            if isinstance(action, argparse._SubParsersAction):
                if command not in action.choices:
                    raise ValueError(f'{path.name}: unknown or missing subcommand {command!r}')
                actions.extend(action.choices[command]._actions)
        return ({flag for action in actions for flag in action.option_strings},
                [set(action.option_strings) for action in actions if action.required and action.option_strings])
    flags, required = set(), []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'add_creation_options':
            shared_flags, shared_required = signature(ROOT / 'development/shared/runtime/native_task_arguments.py')
            if any(k.arg == 'project_name' and isinstance(k.value, ast.Constant) and k.value.value is False for k in node.keywords):
                shared_flags.discard('--project-name')
            flags.update(shared_flags)
            required.extend(shared_required)
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute) or node.func.attr != 'add_argument':
            continue
        names = {a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str) and a.value.startswith('--')}
        flags.update(names)
        if names and any(k.arg == 'required' and isinstance(k.value, ast.Constant) and k.value.value is True for k in node.keywords):
            required.append(names)
    return flags, required


class RuntimeHelperExamples(unittest.TestCase):
    def test_dispatch_signature_includes_generated_options_and_required_inputs(self):
        script = ROOT / 'members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/build_dispatch_prompt.py'
        flags, required = signature(script)
        self.assertTrue({'--executor-result', '--reviewer-result', '--context-handoff', '--supplemental-context'} <= flags)
        self.assertNotIn('--context', flags)
        self.assertIn({'--manager-agent-id'}, required)

    def test_markdown_invocations_use_existing_flags_and_supply_required_ones(self):
        checked = 0
        for member in MEMBERS:
            package = ROOT / 'members' / member / member
            for path in [package / 'SKILL.md', *sorted((package / 'references').glob('*.md'))]:
                for line in path.read_text(encoding='utf-8').splitlines():
                    match = re.match(r'python "[^"\n]*/scripts/([\w_]+\.py)" (.*)', line)
                    if not match:
                        continue
                    script = package / 'scripts' / match[1]
                    with self.subTest(path=path.name, command=line):
                        flags, required = signature(script, match[2].split()[0])
                        supplied = set(re.findall(r'--[a-z][a-z-]*', match[2]))
                        self.assertFalse(supplied - flags, f'unknown flags: {supplied - flags}')
                        for alternatives in required:
                            self.assertTrue(supplied & alternatives, f'missing {alternatives}')
                    checked += 1
        self.assertGreaterEqual(checked, 10, 'runtime examples unexpectedly disappeared')

    def test_subcommands_keep_their_own_required_arguments(self):
        script = ROOT / 'members/scoville-workflow-for-codex/scoville-workflow-for-codex/scripts/run_feedback.py'
        create_flags, create_required = signature(script, 'create')
        self.assertEqual(create_required, [{'--project-root'}])
        self.assertNotIn('--project', create_flags)
        _, resolve_required = signature(script, 'resolve')
        self.assertIn({'--issue-id'}, resolve_required)
        self.assertNotIn({'--project-root'}, resolve_required)
        _, add_required = signature(script, 'add')
        self.assertNotIn({'--issue-id'}, add_required)

    def test_worker_checkpoint_invocation_matches_actual_signature(self):
        package = ROOT / 'members/scoville-workflow-for-codex/scoville-workflow-for-codex'
        source = (package / 'scripts/build_dispatch_prompt.py').read_text(encoding='utf-8')
        line = next(line for line in source.splitlines() if '{checkpoint}' in line and '--role' in line)
        flags, required = signature(package / 'scripts/check_context_checkpoint.py')
        supplied = set(re.findall(r'--[a-z][a-z-]*', line))
        self.assertFalse(supplied - flags)
        for alternatives in required:
            self.assertTrue(supplied & alternatives)


if __name__ == '__main__':
    unittest.main()
