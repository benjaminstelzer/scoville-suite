"""Check documented complete invocations against actual argparse declarations."""
import ast
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
MEMBERS = ('scoville-workflow-for-codex', 'scoville-ask-for-codex', 'scoville-plan', 'scoville-setup')


def signature(path):
    flags, required = set(), []
    for node in ast.walk(ast.parse(path.read_text(encoding='utf-8'))):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute) or node.func.attr != 'add_argument':
            continue
        names = {a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str) and a.value.startswith('--')}
        flags.update(names)
        if names and any(k.arg == 'required' and isinstance(k.value, ast.Constant) and k.value.value is True for k in node.keywords):
            required.append(names)
    return flags, required


class RuntimeHelperExamples(unittest.TestCase):
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
                        flags, required = signature(script)
                        supplied = set(re.findall(r'--[a-z][a-z-]*', match[2]))
                        self.assertFalse(supplied - flags, f'unknown flags: {supplied - flags}')
                        for alternatives in required:
                            self.assertTrue(supplied & alternatives, f'missing {alternatives}')
                    checked += 1
        self.assertGreaterEqual(checked, 10, 'runtime examples unexpectedly disappeared')

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
