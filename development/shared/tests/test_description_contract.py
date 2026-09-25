import importlib.util
import re
import unittest
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('description_builder', SHARED/'build/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class DescriptionContractTests(unittest.TestCase):
    def test_all_descriptions_are_shared_complete_blocks(self):
        for profile in ('general', 'codex'):
            root = SHARED.parent/'scoville-suite'
            config = builder.load(root, profile)
            combined = builder.expand_fragments(root, '{{ include: suite.descriptions }}', config=config)
            for member in config['members']:
                with self.subTest(member=member['name']):
                    text = builder.readme(root, member, config=config).decode()
                    description = text.split('## How it was developed', 1)[0].strip()
                    lines = []
                    fenced = False
                    for line in description.splitlines():
                        if line.startswith('```'):
                            fenced = not fenced
                        lines.append('#'+line if not fenced and re.match(r'^#{1,5} ',line) else line)
                    self.assertIn('\n'.join(lines), combined)
                    for heading in ('How it works','What it enforces','What it costs','How it was developed'):
                        section = text.split('## '+heading+'\n',1)[1].split('\n## ',1)[0]
                        self.assertRegex(section, r'(?m)^- \S')
                    self.assertNotIn('{{', text)
                    self.assertNotIn('## How it was developed', combined)

    def test_workflow_chart_and_both_thresholds_survive(self):
        root=SHARED.parent/'scoville-suite'
        workflow=next(m for m in builder.load(root, 'codex')['members'] if m['name']=='scoville-workflow-for-codex')
        text=builder.readme(root,workflow).decode()
        self.assertIn('```mermaid\nflowchart TD',text)
        self.assertIn('at or above 25%',text)
        self.assertIn('above 75%',text)


if __name__=='__main__':
    unittest.main()
