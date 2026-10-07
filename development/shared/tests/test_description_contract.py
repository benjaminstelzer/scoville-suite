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
            config = builder.load(root, profile, 'suite')
            combined = builder.expand_fragments(root, '{{ include: suite.descriptions }}', config=config)
            for member in config['members']:
                with self.subTest(member=member['name']):
                    text = builder.readme(root, member, config=config).decode()
                    description = text.split('## How it was developed', 1)[0]
                    # Historical examples extend the member README, not the shared description.
                    description = description.split('### One recorded workflow sequence', 1)[0].strip()
                    lines = []
                    fenced = False
                    for line in description.splitlines():
                        if line.startswith('```'):
                            fenced = not fenced
                        lines.append('#'+line if not fenced and re.match(r'^#{1,5} ',line) else line)
                    self.assertIn('\n'.join(lines), combined)
                    self.assertNotIn('{{', text)
                    self.assertNotIn('## How it was developed', combined)

    def test_workflow_chart_is_rendered(self):
        root=SHARED.parent/'scoville-suite'
        config=builder.load(root, 'codex')
        workflow=next(m for m in config['members'] if m['name']=='scoville-workflow-for-codex')
        text=builder.readme(root,workflow,config=config).decode()
        self.assertRegex(text, r'```mermaid\n(?:%%[^\n]*\n)*flowchart TD\n')


if __name__=='__main__':
    unittest.main()
