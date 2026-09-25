import re
import os
from pathlib import Path
import unittest

from test_contract import PACKAGE as BUILT_PACKAGE
from native_startup_fixture import contract_module
PACKAGE = Path(os.environ.get("WORKFLOW_PACKAGE_ROOT", str(BUILT_PACKAGE)))
NAMES = {"activation", "selection", "dispatch", "scope", "wait", "results",
         "compaction", "checkpoint", "review", "accepted", "rollover", "stop"}

class PhaseRouteTests(unittest.TestCase):
    def test_all_phases_have_one_reachable_owner_and_valid_links(self):
        core = (PACKAGE / "references/operations.md").read_text(encoding="utf-8")
        phases = list((PACKAGE / "references").glob("operations-*.md"))
        self.assertEqual({p.stem.removeprefix("operations-") for p in phases}, NAMES)
        compiled = contract_module(PACKAGE).runtime_contract(PACKAGE)
        headings = []
        for path in phases:
            source = path.read_text(encoding="utf-8")
            owned = re.findall(r"^## (.+)$", source, re.M)
            headings.extend(owned)
            if path.stem.removeprefix("operations-") in contract_module(PACKAGE).PHASES:
                for heading in owned:
                    self.assertIn("## " + heading, compiled)
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
        self.assertEqual(len(headings), 15)
        self.assertEqual(len(set(headings)), len(headings))
        self.assertNotIn("completely before the first Plan", (PACKAGE / "SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("After compaction or context loss", core)
        self.assertIn("A read marker or hash alone is not the contents", " ".join(core.split()))
        self.assertIn("coordinator_contract.py", core)

    def test_ambiguous_guard_state_keeps_the_complete_normal_contract(self):
        module = contract_module(PACKAGE)
        compiled = module.runtime_contract(PACKAGE)
        core = (PACKAGE / "references" / "operations.md").read_text(encoding="utf-8")
        for phase in module.PHASES:
            source = PACKAGE / "references" / f"operations-{phase}.md"
            for heading in re.findall(r"^## (.+)$", source.read_text(encoding="utf-8"), re.M):
                self.assertIn("## " + heading, compiled)
        self.assertNotIn("--phase", (PACKAGE / "scripts" / "coordinator_contract.py").read_text(encoding="utf-8"))
        self.assertIn("does not uniquely distinguish selection, review, acceptance, Stop or recovery", " ".join(core.split()))

    def test_scenario_stripping_keeps_normative_followup(self):
        module = contract_module(PACKAGE)
        compiled = module.runtime_contract(PACKAGE)
        self.assertIsNone(re.search(r"^### .*scenarios", compiled, re.M | re.I))
        for required in (
            "at most three repair executors",
            "record the exact unresolved findings",
            "continuation_intent=resume_active_plan",
            "dispatch_contract=SCOVILLE_DISPATCH_V1",
        ):
            self.assertIn(required, compiled)

    def test_entrypoint_sections_are_projected_once_independent_of_order(self):
        module = contract_module(PACKAGE)
        compiled = module.runtime_contract(PACKAGE)
        self.assertEqual(1, compiled.count("## Complete coordinator startup"))
        self.assertEqual(1, compiled.count("## Coordinator boundary"))
        self.assertNotIn("## First operation: role gate", compiled)
        self.assertNotIn("## Prompt writing", compiled)

    def test_rollover_reachability_precedes_predecessor_wait_and_readiness(self):
        source = " ".join((PACKAGE / "references" / "operations-rollover.md").read_text(encoding="utf-8").split())
        reachability = source.index("Read its own exact task ID and host")
        predecessor_wait = source.index("Only after that read succeeds, wait for the exact predecessor")
        readiness = source.index("With both proofs retained, call `list_threads`")
        self.assertLess(reachability, predecessor_wait)
        self.assertLess(predecessor_wait, readiness)
        self.assertIn("Guard ownership never proves host reachability or native status", source)
