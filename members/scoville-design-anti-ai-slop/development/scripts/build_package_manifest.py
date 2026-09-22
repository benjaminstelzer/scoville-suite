#!/usr/bin/env python3
"""Build or check the schema-declared executable-package manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml

def executable_paths(root: Path) -> list[Path]:
    registry = yaml.safe_load((root / "modules.yaml").read_text(encoding="utf-8"))
    module_paths = [Path(item["path"]) for item in registry["modules"]]
    non_routed = [Path(path) for path in registry.get("non_routed_references", [])]
    distribution = [Path(path) for path in registry.get("distribution_files", [])]
    relative = [
        Path("SKILL.md"),
        Path("modules.yaml"),
        Path("agents/openai.yaml"),
        *module_paths,
        *non_routed,
        *distribution,
    ]
    unique = {path.as_posix(): path for path in relative}
    if len(unique) != len(relative):
        raise ValueError("modules.yaml declares duplicate executable paths")
    invalid = [
        path
        for path in unique.values()
        if path.is_absolute() or ".." in path.parts
    ]
    if invalid:
        raise ValueError(f"invalid executable path: {invalid[0].as_posix()}")
    return sorted(unique.values(), key=lambda path: path.as_posix())


def build(root: Path) -> dict[str, object]:
    files: list[dict[str, object]] = []
    canonical_parts: list[str] = []
    for relative in executable_paths(root):
        data = (root / relative).read_bytes()
        digest = hashlib.sha256(data).hexdigest().upper()
        normalized = relative.as_posix()
        files.append({"path": normalized, "bytes": len(data), "sha256": digest})
        canonical_parts.append(f"{normalized}\0{len(data)}\0{digest}\n")
    canonical = "".join(canonical_parts).encode("utf-8")
    return {
        "schema_version": 1,
        "algorithm": "sha256(path\\0byte_count\\0file_sha256\\n), sorted by path",
        "file_count": len(files),
        "manifest_sha256": hashlib.sha256(canonical).hexdigest().upper(),
        "files": files,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2] / "scoville-design-anti-ai-slop")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    current = build(args.root.resolve())
    if args.check:
        recorded = json.loads(args.output.read_text(encoding="utf-8"))
        if recorded != current:
            print("package manifest is stale")
            return 1
        print(f"package manifest is current: {current['manifest_sha256']}")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(current, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"wrote package manifest: {current['manifest_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
