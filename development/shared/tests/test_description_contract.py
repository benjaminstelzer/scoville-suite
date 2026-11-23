import importlib.util
import unittest
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('description_builder', SHARED/'build/build_suite.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class DescriptionContractTests(unittest.TestCase):
    def test_workflow_chart_is_rendered(self):
        root=SHARED.parent/'scoville-suite'
        config=builder.load(root, 'codex')
        workflow=next(m for m in config['members'] if m['name']=='scoville-workflow-for-codex')
        text=builder.readme(root,workflow,config=config).decode()
        self.assertRegex(text, r'```mermaid\n(?:%%[^\n]*\n)*flowchart TD\n')


if __name__=='__main__':
    unittest.main()
