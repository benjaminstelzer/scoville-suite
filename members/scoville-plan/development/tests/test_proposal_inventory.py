"""Exercise project-wide discovery and consume the returned canonical paths."""
import json
import unittest
import test_select_context as base


class ProposalInventoryTests(unittest.TestCase):
    setUp = base.SelectContextTests.setUp
    tearDown = base.SelectContextTests.tearDown
    write = base.SelectContextTests.write
    run_cli = base.SelectContextTests.run_cli

    def add_proposal(self, number=2):
        text = base.DECISION.replace("ADR-0001", f"ADR-{number:04d}").replace("status: accepted", "status: proposed")
        text = text.replace("accepted: 2026-09-19\n", "")
        return self.write(f"docs/decisions/{number:04d}-unlinked.md", text)

    def test_unlinked_proposal_path_is_directly_readable_without_mutation(self):
        expected = self.add_proposal()
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_cli("--proposals")
        self.assertEqual(0, result.returncode, result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual({"proposals"}, set(payload))
        self.assertEqual([{"id": "ADR-0002", "title": "Preserve exact Unicode",
                           "scope": "project/testing", "path": "docs/decisions/0002-unlinked.md"}],
                         payload["proposals"])
        for proposal in payload["proposals"]:
            # The documented next consumer is a direct read of the relevant body.
            content = (self.root / proposal["path"]).read_text(encoding="utf-8")
            self.assertEqual(expected.read_text(encoding="utf-8"), content)
            self.assertIn("id: " + proposal["id"], content)
            self.assertIn("café", content)
        self.assertNotIn("## Decision", result.stdout)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_idle_project_and_empty_inventory(self):
        self.write("PROJECT_INDEX.md", "---\nformat_version: 1\nactive_plan: null\n---\n")
        result = self.run_cli("--proposals")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual({"proposals": []}, json.loads(result.stdout))
        self.add_proposal()
        result = self.run_cli("--proposals")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual("ADR-0002", json.loads(result.stdout)["proposals"][0]["id"])

    def test_conflicting_selection_reports_corrected_invocation(self):
        for extra in (("--plan", "PLAN-0001"), ("--position",), ("--unit", "W-003"), ("--work-item", "W-003")):
            result = self.run_cli("--proposals", *extra)
            self.assertEqual(2, result.returncode)
            payload = json.loads(result.stdout)
            self.assertNotIn("proposals", payload)
            issue = payload["diagnostics"][0]
            self.assertIn("--proposals --format json", issue["expected"])
            self.assertIn("omit", issue["message"])
        corrected = self.run_cli("--proposals")
        self.assertEqual(0, corrected.returncode, corrected.stdout)

    def test_invalid_metadata_has_no_partial_inventory_and_can_be_corrected(self):
        self.add_proposal(2)
        file = self.add_proposal(3)
        original = file.read_text(encoding="utf-8")
        cases = (
            ("status: proposed", "status: proposal", "DECISION_STATUS_INVALID", "proposed"),
            ("scope: project/testing", "scope: Project/testing", "DECISION_SCOPE_INVALID", "lowercase"),
            ("id: ADR-0003", "id: ADR-0099", "DECISION_ID_MISMATCH", "ADR-0003"),
            ("# Preserve exact Unicode", "# ", "DECISION_TITLE_INVALID", "nonempty H1"),
        )
        for old, bad, code, expected in cases:
            with self.subTest(code=code):
                file.write_text(original.replace(old, bad), encoding="utf-8", newline="\n")
                result = self.run_cli("--proposals")
                self.assertEqual(1, result.returncode)
                payload = json.loads(result.stdout)
                self.assertNotIn("proposals", payload)
                issue = payload["diagnostics"][0]
                self.assertEqual(code, issue["code"])
                self.assertEqual("docs/decisions/0003-unlinked.md", issue["path"])
                self.assertIn(expected, issue["expected"])
                file.write_text(original, encoding="utf-8", newline="\n")
                corrected = self.run_cli("--proposals")
                self.assertEqual(0, corrected.returncode, corrected.stdout)
                self.assertEqual(2, len(json.loads(corrected.stdout)["proposals"]))

    def test_ambiguous_identity_is_not_an_empty_inventory(self):
        original = self.add_proposal()
        duplicate = self.write("docs/decisions/0002-duplicate.md", original.read_text(encoding="utf-8"))
        result = self.run_cli("--proposals")
        issue = json.loads(result.stdout)["diagnostics"][0]
        self.assertEqual(1, result.returncode)
        self.assertEqual("DECISION_ID_DUPLICATE", issue["code"])
        duplicate.unlink()
        self.assertEqual(0, self.run_cli("--proposals").returncode)

    def test_budget_failure_emits_no_partial_list(self):
        for number in range(2, 8):
            self.add_proposal(number)
        result = self.run_cli("--proposals", "--max-output-bytes", "512")
        self.assertEqual(1, result.returncode)
        payload = json.loads(result.stdout)
        self.assertNotIn("proposals", payload)
        issue = payload["diagnostics"][0]
        self.assertEqual("OUTPUT_BUDGET_EXCEEDED", issue["code"])
        corrected = self.run_cli("--proposals", "--max-output-bytes", str(issue["observed"]["required_bytes"]))
        self.assertEqual(0, corrected.returncode, corrected.stdout)
        self.assertEqual(6, len(json.loads(corrected.stdout)["proposals"]))

    def test_invalid_filename_diagnostic_can_be_corrected(self):
        canonical = self.add_proposal()
        malformed = canonical.with_name("2-unlinked.md")
        canonical.rename(malformed)
        result = self.run_cli("--proposals")
        self.assertEqual(1, result.returncode)
        issue = json.loads(result.stdout)["diagnostics"][0]
        self.assertEqual("DECISION_FILENAME_INVALID", issue["code"])
        self.assertIn("NNNN-lowercase-subject.md", issue["expected"])
        malformed.rename(canonical)
        self.assertEqual(0, self.run_cli("--proposals").returncode)
