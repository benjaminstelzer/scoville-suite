import re
import os
from pathlib import Path
import unittest

PACKAGE = Path(os.environ.get("WORKFLOW_PACKAGE_ROOT", str(Path(__file__).resolve().parents[2] / "scoville-workflow-for-codex")))
NAMES = {"activation", "selection", "dispatch", "scope", "wait", "results",
         "compaction", "checkpoint", "review", "accepted", "rollover", "stop"}

class PhaseRouteTests(unittest.TestCase):
    def test_all_phases_have_one_reachable_owner_and_valid_links(self):
        core = (PACKAGE / "references/operations.md").read_text(encoding="utf-8")
        phases = list((PACKAGE / "references").glob("operations-*.md"))
        self.assertEqual({p.stem.removeprefix("operations-") for p in phases}, NAMES)
        headings = []
        for path in phases:
            self.assertIn(f"({path.name})", core)
            source = path.read_text(encoding="utf-8")
            headings.extend(re.findall(r"^## (.+)$", source, re.M))
            for link in re.findall(r"\]\(([^)]+)\)", source):
                if "://" not in link:
                    target = path.parent / link.split("#")[0]
                    if not target.is_file() and "WORKFLOW_PACKAGE_ROOT" not in os.environ:
                        import json
                        suite = Path(__file__).resolve().parents[4]
                        member = next(m for m in json.loads((suite / "suite.json").read_text())["members"] if m["name"] == PACKAGE.name)
                        mapping = {h["target"]: suite.parent / "shared" / h["source"] for h in member["shared_helpers"]}
                        target = mapping.get(PACKAGE.name + "/scripts/" + target.name, target)
                    self.assertTrue(target.is_file(), link)
        self.assertEqual(len(headings), 12)
        self.assertEqual(len(set(headings)), 12)
        self.assertNotIn("completely before the first Plan", (PACKAGE / "SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("After\ncompaction or context loss", core)
        self.assertIn("A read marker or hash alone is not the contents", core)
        self.assertIn("Unknown dispatch uses activation", core)
