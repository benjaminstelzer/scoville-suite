from __future__ import annotations

import tempfile
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from build_runtime_package import build_runtime, runtime_bytes
from generate_module_index import GENERATED, render_index
from test_validate_package import SOURCE_ID, _module, _write_registry, _write_skill, build_successor
from validate_package import CURRENT_CANONICAL_IDS, CURRENT_SCHEMA, SUCCESSOR_SCHEMA, validate_package


def build_current(root: Path) -> dict:
    registry = build_successor(root)
    registry["package_schema"] = CURRENT_SCHEMA
    registry["distribution_files"] = ["LICENSE"]
    (root / "LICENSE").write_bytes(b"Synthetic license fixture\n")
    for index, module_id in enumerate(CURRENT_CANONICAL_IDS[28:], start=29):
        registry["modules"].append(_module(module_id, index, True))
        registry["signal_enum"].append(f"signal_{index:02d}")
    for module in registry["modules"]:
        module.update(status="draft", evidence=[])
        (root / module["path"]).write_text(
            f"# {module['id']}\n\nStatus: `draft`  \nIntervention: `focus`  \nSources: `{SOURCE_ID}`\n\nOwned rule.\n",
            encoding="utf-8", newline="\n",
        )
    source_index = root / "references/source-index.md"
    source_index.write_text(source_index.read_text(encoding="utf-8") +
        "\n### SRC-PACKAGE-LOCAL-SYNTHESIS\n\nClass: local-synthesis\nScope: local heuristic.\n",
        encoding="utf-8", newline="\n")
    _write_registry(root, registry)
    _write_skill(root, registry)
    return registry


class CurrentSchemaTests(unittest.TestCase):
    def test_current_thirty_modules_and_statusless_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_current(root)
            result = validate_package(root, CURRENT_SCHEMA)
            self.assertEqual([], result.errors)
            self.assertEqual(30, result.metrics["modules"])
            self.assertNotIn("(draft)", render_index(registry))
            self.assertIn(GENERATED, render_index(registry))

    def test_large_content_and_all_modules_validate_without_size_policy(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_current(root)
            registry["planned_common_loads"][0]["modules"] = list(CURRENT_CANONICAL_IDS)
            for item in registry["modules"]:
                item["route_label"] += " descriptive route" * 150
                path = root / item["path"]
                path.write_text(path.read_text(encoding="utf-8") + " instruction" * 5000, encoding="utf-8")
            _write_registry(root, registry)
            _write_skill(root, registry)
            path = root / "SKILL.md"
            path.write_text(path.read_text(encoding="utf-8") + " core instruction" * 5000, encoding="utf-8")
            result = validate_package(root, CURRENT_SCHEMA)
            self.assertEqual([], result.errors)
            self.assertEqual([], result.warnings)

    def test_common_load_ids_and_shape_remain_structural(self):
        for value, signature in (([], "non-empty string list"), (["missing"], "unknown module IDs"), ([CURRENT_CANONICAL_IDS[0]] * 2, "duplicate module IDs")):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                registry["planned_common_loads"][0]["modules"] = value
                _write_registry(root, registry)
                self.assertTrue(any(signature in e for e in validate_package(root, CURRENT_SCHEMA).errors))

    def test_historical_schema_does_not_accept_draft_or_thirty(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            self.assertIn("(stub)", render_index(registry))
            registry["modules"][0]["status"] = "draft"
            _write_registry(root, registry)
            self.assertTrue(any("invalid status" in e for e in validate_package(root, SUCCESSOR_SCHEMA).errors))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_current(root)
            self.assertTrue(any("canonical module" in e for e in validate_package(root, SUCCESSOR_SCHEMA).errors))

    def test_current_rejects_old_status_and_header_drift(self):
        for mutation, signature in (("status", "invalid status"), ("header", "Status header")):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                if mutation == "status":
                    registry["modules"][0]["status"] = "stub"
                else:
                    path = root / registry["modules"][0]["path"]
                    path.write_text(path.read_text(encoding="utf-8").replace("Status: `draft`", "Status: `stub`"), encoding="utf-8")
                _write_registry(root, registry)
                self.assertTrue(any(signature in e for e in validate_package(root, CURRENT_SCHEMA).errors))

    def test_current_still_rejects_missing_module_source_and_sibling_load(self):
        for mutation, signature in (("module", "missing reference"), ("source", "local-synthesis"), ("sibling", "sibling reference")):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                path = root / registry["modules"][-1]["path"]
                if mutation == "module":
                    path.unlink()
                elif mutation == "source":
                    path = root / "references/source-index.md"
                    path.write_text(path.read_text(encoding="utf-8").replace("Class: local-synthesis", "Class: empirical"), encoding="utf-8")
                else:
                    path.write_text(path.read_text(encoding="utf-8") + "\n[Other](other.md)\n", encoding="utf-8")
                self.assertTrue(any(signature in e for e in validate_package(root, CURRENT_SCHEMA).errors))

    def test_raw_evidence_ids_are_not_retained(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_current(root)
            registry["modules"][0]["evidence"] = ["RF51-planned"]
            _write_registry(root, registry)
            self.assertTrue(any("evidence must be empty" in e for e in validate_package(root, CURRENT_SCHEMA).errors))

    def test_packaged_tool_links_require_declaration_and_existing_file(self):
        for mutation, signature in ((None, None), ("typo", "script link"),
                                    ("undeclared", "script link"), ("missing", "missing distribution"),
                                    ("escape", "invalid distribution")):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                tool = root / "scripts/measure.js"
                tool.parent.mkdir()
                tool.write_text("(() => 1)\n", encoding="utf-8")
                registry["distribution_files"].append("scripts/measure.js")
                module = root / registry["modules"][0]["path"]
                link = "../scripts/typo.js" if mutation == "typo" else "../scripts/measure.js"
                module.write_text(module.read_text(encoding="utf-8") + f"\n[Tool]({link})\n", encoding="utf-8")
                if mutation == "undeclared": registry["distribution_files"].pop()
                if mutation == "missing": tool.unlink()
                if mutation == "escape": registry["distribution_files"].append("../outside.js")
                _write_registry(root, registry)
                errors = validate_package(root, CURRENT_SCHEMA).errors
                if signature:
                    self.assertTrue(any(signature in e for e in errors), errors)
                else:
                    self.assertEqual([], errors)

    def test_packaged_example_links_require_declaration_and_package_boundary(self):
        for mutation, signature in ((None, None), ("undeclared", "example link"),
                                    ("missing", "missing distribution"),
                                    ("escape", "invalid distribution")):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                asset = root / "examples/spatial/example.svg"
                asset.parent.mkdir(parents=True)
                asset.write_text("<svg xmlns='http://www.w3.org/2000/svg'/>", encoding="utf-8")
                registry["distribution_files"].append("examples/spatial/example.svg")
                module = root / registry["modules"][0]["path"]
                module.write_text(module.read_text(encoding="utf-8") +
                                  "\n[Example](../examples/spatial/example.svg)\n", encoding="utf-8")
                if mutation == "undeclared": registry["distribution_files"].pop()
                if mutation == "missing": asset.unlink()
                if mutation == "escape": registry["distribution_files"].append("../outside.svg")
                _write_registry(root, registry)
                errors = validate_package(root, CURRENT_SCHEMA).errors
                if signature:
                    self.assertTrue(any(signature in e for e in errors), errors)
                else:
                    self.assertEqual([], errors)

    def test_build_preserves_every_byte_except_exact_comment_and_never_overwrites(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "source"
            root.mkdir()
            build_current(root)
            destination = parent / "runtime"
            receipt = build_runtime(root, destination)
            self.assertEqual(35, receipt["runtime"]["file_count"])
            self.assertEqual((root / "LICENSE").read_bytes(), (destination / "LICENSE").read_bytes())
            self.assertNotEqual(receipt["source"]["manifest_sha256"], receipt["runtime"]["manifest_sha256"])
            self.assertFalse((destination / "docs").exists())
            for record in receipt["source"]["files"]:
                path = record["path"]
                self.assertEqual(runtime_bytes(path, (root / path).read_bytes()), (destination / path).read_bytes())
            self.assertEqual([], validate_package(destination, CURRENT_SCHEMA, runtime=True).errors)
            self.assertEqual([], validate_package(destination, CURRENT_SCHEMA).errors)
            with self.assertRaisesRegex(ValueError, "already exists"):
                build_runtime(root, destination)
            with self.assertRaisesRegex(ValueError, "outside"):
                build_runtime(root, root / "runtime")
            path = destination / "SKILL.md"
            path.write_text(path.read_text(encoding="utf-8").replace("route 01", "wrong route"), encoding="utf-8")
            self.assertTrue(any("index drift" in e for e in validate_package(destination, CURRENT_SCHEMA, runtime=True).errors))


if __name__ == "__main__":
    unittest.main()
