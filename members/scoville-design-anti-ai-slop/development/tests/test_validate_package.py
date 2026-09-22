from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from generate_module_index import END, START, render_index, replace_index
from validate_package import (
    LEGACY_CANONICAL_IDS,
    LEGACY_SCHEMA,
    SUCCESSOR_CANONICAL_IDS,
    SUCCESSOR_SCHEMA,
    validate_package,
)


SOURCE_ID = "CUR.BK-01"


def _write_registry(root: Path, registry: dict) -> None:
    (root / "modules.yaml").write_text(
        yaml.safe_dump(registry, sort_keys=False), encoding="utf-8", newline="\n"
    )


def _write_skill(root: Path, registry: dict) -> None:
    base = f"# Test Skill\n\n{START}\n{END}\n"
    (root / "SKILL.md").write_text(
        replace_index(base, render_index(registry)), encoding="utf-8", newline="\n"
    )


def _write_agent(root: Path) -> None:
    agent = {
        "interface": {
            "default_prompt": "Use $scoville-design-anti-ai-slop for this task.",
            "short_description": "Professional graphic design guardrail",
        }
    }
    (root / "agents").mkdir(parents=True)
    (root / "agents" / "openai.yaml").write_text(
        yaml.safe_dump(agent, sort_keys=False), encoding="utf-8", newline="\n"
    )


def _module(module_id: str, index: int, successor: bool) -> dict:
    item = {
        "id": module_id,
        "status": "stub",
        "intervention": "focus",
        "path": f"references/{module_id}.md",
        "route_label": f"route {index:02d}",
        "when_any": [f"signal_{index:02d}"],
        "unless": [],
        "requires": [],
        "conflicts": [],
        "owns": [f"concern_{index:02d}"],
        "sources": [SOURCE_ID],
    }
    return item


def build_successor(root: Path) -> dict:
    (root / "references").mkdir(parents=True)
    modules = [
        _module(module_id, index, True)
        for index, module_id in enumerate(SUCCESSOR_CANONICAL_IDS, start=1)
    ]
    registry = {
        "format_version": 2,
        "package_schema": SUCCESSOR_SCHEMA,
        "signal_enum": [
            f"signal_{index:02d}"
            for index in range(1, len(SUCCESSOR_CANONICAL_IDS) + 1)
        ],
        "non_routed_references": ["references/source-index.md"],
        "planned_common_loads": [
            {
                "id": "common-four",
                "modules": SUCCESSOR_CANONICAL_IDS[:4],
            }
        ],
        "modules": modules,
    }
    _write_registry(root, registry)
    _write_skill(root, registry)
    _write_agent(root)
    for item in modules:
        (root / item["path"]).write_text(
            f"# {item['id']}\n\nSources: {SOURCE_ID}\n\n## Rules\n\nApply the owned rule.\n",
            encoding="utf-8",
            newline="\n",
        )
    (root / "references" / "source-index.md").write_text(
        f"# Source index\n\n### {SOURCE_ID} Canonical curriculum source\n\nRecord.\n",
        encoding="utf-8",
        newline="\n",
    )
    return registry


def build_legacy(root: Path) -> dict:
    (root / "references").mkdir(parents=True)
    modules = [
        _module(module_id, index, False)
        for index, module_id in enumerate(LEGACY_CANONICAL_IDS, start=1)
    ]
    registry = {
        "format_version": 1,
        "signal_enum": [f"signal_{index:02d}" for index in range(1, 15)],
        "modules": modules,
    }
    _write_registry(root, registry)
    _write_skill(root, registry)
    _write_agent(root)
    for item in modules:
        content = f"# {item['id']}\n\nSources: {SOURCE_ID}\n\nApply the owned rule.\n"
        if item["id"] == "sources-and-attribution":
            content += f"\n### {SOURCE_ID} Legacy source\n\nRecord.\n"
        (root / item["path"]).write_text(
            content, encoding="utf-8", newline="\n"
        )
    return registry


class SuccessorValidatorTests(unittest.TestCase):
    def test_valid_successor_fixture_and_generalized_source_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_successor(root)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertEqual([], result.errors)
            self.assertEqual([], result.warnings)
            self.assertEqual(28, result.metrics["modules"])

    def test_valid_explicit_legacy_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_legacy(root)
            result = validate_package(root, LEGACY_SCHEMA)
            self.assertEqual([], result.errors)

    def test_exact_module_order_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][0], registry["modules"][1] = (
                registry["modules"][1],
                registry["modules"][0],
            )
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("canonical module IDs/order differ" in error for error in result.errors))

    def test_signal_and_concern_ownership_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][1]["when_any"] = registry["modules"][0]["when_any"]
            registry["modules"][1]["owns"] = registry["modules"][0]["owns"]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("signal ownership collision" in error for error in result.errors))
            self.assertTrue(any("ownership collision" in error for error in result.errors))

    def test_hidden_dependencies_are_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][0]["requires"] = [SUCCESSOR_CANONICAL_IDS[1]]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("requires/conflicts" in error for error in result.errors))

    def test_source_index_declaration_and_orphans_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["non_routed_references"] = []
            _write_registry(root, registry)
            (root / "references" / "orphan.md").write_text("orphan", encoding="utf-8")
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("non_routed_references" in error for error in result.errors))
            self.assertTrue(any("orphan references" in error for error in result.errors))

    def test_unresolved_source_and_header_mismatch_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            item = registry["modules"][0]
            item["sources"] = ["AUD.TYPE-02"]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("unresolved source ID AUD.TYPE-02" in error for error in result.errors))
            self.assertTrue(any("Sources: header must equal" in error for error in result.errors))

    def test_sibling_link_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            path = root / registry["modules"][0]["path"]
            path.write_text(
                path.read_text(encoding="utf-8") + "\n[Sibling](other.md)\n",
                encoding="utf-8",
                newline="\n",
            )
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("sibling reference link" in error for error in result.errors))

    def test_common_load_and_source_structure_remains_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["planned_common_loads"][0]["modules"] = [
                SUCCESSOR_CANONICAL_IDS[0], SUCCESSOR_CANONICAL_IDS[0], "unknown-expert"
            ]
            registry["modules"][0]["sources"] = ["MISSING-SOURCE"]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            for signature in ("duplicate module IDs", "unknown module IDs", "unresolved source ID"):
                with self.subTest(signature=signature):
                    self.assertTrue(any(signature in error for error in result.errors))

    def test_generated_index_drift_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_successor(root)
            skill_path = root / "SKILL.md"
            skill_path.write_text(
                skill_path.read_text(encoding="utf-8").replace("route 01", "wrong route"),
                encoding="utf-8",
                newline="\n",
            )
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("generated module index drift" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
