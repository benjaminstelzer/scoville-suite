#!/usr/bin/env python3
"""Report comparable o200k_base sizes; these are not acceptance limits."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from generate_module_index import GENERATED, INDEX_PATH, load_registry, render_index
from validate_package import successor_core_text, tokens


def measure(root: Path) -> dict:
    registry = load_registry(root / "modules.yaml")
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    core = tokens(successor_core_text(skill))
    index = tokens(render_index(registry, relative_to_references=(root / INDEX_PATH).is_file()).replace(GENERATED + "\n", ""))
    modules = {item["id"]: tokens((root / item["path"]).read_text(encoding="utf-8"))
               for item in registry["modules"]}
    return {
        "tokenizer": "o200k_base",
        "core_excluding_index": core,
        "generated_package_index": index,
        "core_plus_index": core + index,
        "modules": modules,
        "common_loads": {item["id"]: core + index + sum(modules[x] for x in item["modules"])
                         for item in registry["planned_common_loads"]},
        "runtime_instruction_total": tokens(skill) + sum(modules.values()),
        "limit": "File token counts; not provider-total cost or a context gate.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2] / "scoville-design-anti-ai-slop")
    args = parser.parse_args()
    print(json.dumps(measure(args.root), indent=2))
