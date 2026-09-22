#!/usr/bin/env python3
"""Build a new isolated runtime directory; never install or overwrite a package."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_package_manifest import build, executable_paths
from generate_module_index import GENERATED, INDEX_PATH
from validate_package import CURRENT_SCHEMA, validate_package


def runtime_bytes(path: str, data: bytes) -> bytes:
    if path not in {"SKILL.md", INDEX_PATH.as_posix()}:
        return data
    marker = (GENERATED + "\n").encode("utf-8")
    if data.count(marker) > 1:
        raise ValueError("source Core must not contain duplicate generator comments")
    return data.replace(marker, b"", 1)


def build_runtime(root: Path, destination: Path, *, development_root: Path | None = None) -> dict:
    root = root.resolve()
    destination = destination.resolve()
    if destination == root or root in destination.parents or destination in root.parents:
        raise ValueError("runtime destination must be outside the source tree")
    if development_root is not None and development_root.resolve().parent == root.parent:
        repository = root.parent
        if destination == repository or repository in destination.parents:
            raise ValueError("runtime destination must be outside the canonical repository")
    if destination.exists():
        raise ValueError("runtime destination already exists; refusing to overwrite")
    result = validate_package(root, CURRENT_SCHEMA, development_root=development_root)
    if result.errors:
        raise ValueError("invalid source package: " + "; ".join(result.errors))
    source = build(root)
    payload = {}
    for relative in executable_paths(root):
        path = root / relative
        if not path.resolve().is_relative_to(root):
            raise ValueError(f"source path escapes package: {relative}")
        payload[relative] = runtime_bytes(relative.as_posix(), path.read_bytes())
    if build(root) != source:
        raise ValueError("source changed during build preparation")
    destination.mkdir(parents=True, exist_ok=False)
    for relative, data in payload.items():
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    runtime = build(destination)
    errors = validate_package(destination, CURRENT_SCHEMA, runtime=True).errors
    if errors:
        raise ValueError("invalid runtime derivative: " + "; ".join(errors))
    for relative, expected in payload.items():
        if (destination / relative).read_bytes() != expected:
            raise ValueError(f"runtime bytes changed: {relative}")
    return {
        "schema_version": 1,
        "transform": "copy canonical package bytes; strip the legacy generator comment only when present",
        "source_root": str(root),
        "runtime_root": str(destination),
        "source": source,
        "runtime": runtime,
        "validation": "source and runtime structural checks passed; not behavioural proof",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2] / "scoville-design-anti-ai-slop")
    parser.add_argument("--development-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    receipt_path = args.receipt.resolve()
    destination = args.destination.resolve()
    if receipt_path.exists() or receipt_path == destination or destination in receipt_path.parents:
        parser.error("receipt must be new and outside the runtime directory")
    try:
        receipt = build_runtime(args.root, destination, development_root=args.development_root)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"BUILD FAILED: {exc}\n")
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"BUILT {receipt['runtime']['file_count']} files: {receipt['runtime']['manifest_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
