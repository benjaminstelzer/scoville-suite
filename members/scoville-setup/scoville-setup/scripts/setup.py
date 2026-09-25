#!/usr/bin/env python3
"""Show or explicitly save the project's Scoville settings."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tempfile

from ask_settings import merge_config_layer, resolve_settings
from scoville_config import merge, read_config
from workflow_settings import load_config, read_thresholds

ROOT = Path(__file__).resolve().parents[1]


def effective(project_root: Path) -> dict:
    return {
        "ask": resolve_settings(ROOT / "assets/ask.default.json", {"project_root": project_root}),
        "workflow": load_config(ROOT / "assets/workflow.toml", project_root),
    }


def validate(project_root: Path) -> dict:
    values = effective(project_root)
    read_thresholds(ROOT / "assets/workflow.toml", project_root)
    return values


def validate_setup_choices(value: dict) -> None:
    for key, item in value.items():
        if key in {"effort", "reasoning"} and item not in ("low", "medium", "high", "xhigh"):
            raise ValueError("Setup supports low/medium/high/xhigh; add other levels manually to .scoville/config.json")
        if isinstance(item, dict):
            validate_setup_choices(item)
        elif isinstance(item, list):
            for entry in item:
                if isinstance(entry, dict):
                    validate_setup_choices(entry)


def apply(project_root: Path, patch: dict) -> dict:
    if not isinstance(patch, dict) or not patch or set(patch) - {"ask", "workflow"}:
        raise ValueError("supply a nonempty object with ask and/or workflow changes")
    if "workflow" in patch and (not isinstance(patch["workflow"], dict)
            or set(patch["workflow"]) - {"execute", "review", "context"}):
        raise ValueError("Setup changes workflow execute, review and context only")
    validate_setup_choices(patch)
    current = read_config(project_root)
    proposed = merge(current, patch)
    if "ask" in patch:
        proposed["ask"] = merge_config_layer(current.get("ask", {}), patch["ask"])
    # Reuse the consumers against the proposed file before touching the project.
    with tempfile.TemporaryDirectory(prefix="scoville-setup-") as temporary:
        candidate = Path(temporary)
        (candidate / ".scoville").mkdir()
        (candidate / ".scoville/config.json").write_text(
            json.dumps(proposed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        values = validate(candidate)
    path = project_root / ".scoville/config.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(proposed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return values


def main() -> int:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("show", "set"))
    parser.add_argument("--project-root", type=Path, required=True)
    args = parser.parse_args()
    try:
        values = (apply(args.project_root, json.load(sys.stdin))
                  if args.operation == "set" else validate(args.project_root))
        print(json.dumps({"ok": True, "saved": args.operation == "set",
                          "file": str(args.project_root / ".scoville/config.json"),
                          "effective": values}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError) as error:
        print(json.dumps({"ok": False, "diagnostic": str(error)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
