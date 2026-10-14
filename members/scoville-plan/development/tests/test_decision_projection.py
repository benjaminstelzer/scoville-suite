"""Lossless binding projection of explicitly normalized Decisions, not inference."""
import importlib.util
import sys
import unittest
from test_select_context import DECISION, SCRIPT

spec = importlib.util.spec_from_file_location('decision_projection_selector', SCRIPT)
selector = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = selector
spec.loader.exec_module(selector)

MARK = 'Binding sections: complete'
MARKED = DECISION.replace('## Decision\n', '## Decision\n\n' + MARK + '\n')
EXPECTED = (MARKED[:MARKED.index('## Problem')]
            + MARKED[MARKED.index('## Consequences'):])


class DecisionProjectionTests(unittest.TestCase):
    def test_marked_projection_preserves_exact_binding_slices_and_line_endings(self):
        for newline in ('\n', '\r\n'):
            with self.subTest(newline=newline):
                original = MARKED.replace('\n', newline)
                self.assertEqual(EXPECTED.replace('\n', newline), selector.project_decision_context(original))

    def test_unmarked_and_ambiguous_records_remain_complete(self):
        cases = [DECISION, MARKED.replace(MARK, MARK + ' '),
                 MARKED.replace(MARK, 'Unmarked preface.\n' + MARK),
                 MARKED.replace(MARK, '> ' + MARK),
                 MARKED.replace('## Problem', '## Problem\n\n## Problem'),
                 MARKED.replace('## Drivers', '## Unknown'),
                 MARKED.replace('## Drivers', '### Drivers'),
                 MARKED.replace('## Confirmation', '## Extra\n\n## Confirmation'),
                 MARKED.replace('# Preserve exact Unicode', '# Preserve exact Unicode\n\nDo not publish.'),
                 MARKED.replace('format_version: 1', 'format_version: 2')]
        for original in cases:
            with self.subTest(original=original):
                self.assertEqual(original, selector.project_decision_context(original))

    def test_mark_in_fence_does_not_enable_projection(self):
        for fence in ('```text', '~~~text'):
            original = DECISION.replace('## Decision\n', '## Decision\n' + fence + '\n' + MARK + '\n' + fence[:3] + '\n')
            self.assertEqual(original, selector.project_decision_context(original))

    def test_fenced_example_headings_inside_binding_text_survive_unchanged(self):
        for fence in ('```markdown', '~~~markdown'):
            example = fence + '\n## Drivers\n' + MARK + '\n# Example\n' + fence[:3] + '\n'
            original = MARKED.replace('## Confirmation\n', '## Confirmation\n' + example)
            expected = EXPECTED.replace('## Confirmation\n', '## Confirmation\n' + example)
            self.assertEqual(expected, selector.project_decision_context(original))

    def test_input_and_full_record_parser_remain_full(self):
        self.assertIn('## Drivers', selector.parse_record(MARKED, 'decision').body)
        selector.project_decision_context(MARKED)
        self.assertIn('## Problem', MARKED)


if __name__ == '__main__': unittest.main()
