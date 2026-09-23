#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path


VERSION = 1
START = b"<!-- scoville-workflow-contract:v1:start -->"
END = b"<!-- scoville-workflow-contract:v1:end -->"
ANY_MARKER = re.compile(rb"<!-- scoville-workflow-contract:v([0-9]+):(start|end) -->")
RESERVED_MARKER = re.compile(rb"scoville-workflow-contract", re.IGNORECASE)
LEGACY_BLOCKS: dict[int, bytes] = {
    0: (
        b"<!-- scoville-workflow-contract:v0:start -->\n"
        b"While Scoville Workflow is active, only its coordinator and assigned worker may write.\n"
        b"<!-- scoville-workflow-contract:v0:end -->\n"
    ),
}


class ContractError(Exception):
    def __init__(self, reason: str, diagnostic: str) -> None:
        super().__init__(diagnostic)
        self.reason = reason
        self.diagnostic = diagnostic


def compact(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def normalized(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def source_path() -> Path:
    return Path(__file__).resolve().parent.parent / "references" / "agents-contract.md"


def load_source() -> bytes:
    data = source_path().read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        raise ContractError("source_bom", "canonical contract must not contain a BOM")
    data = normalized(data)
    if not data.endswith(b"\n"):
        raise ContractError("source_newline", "canonical contract must end with LF")
    if data.count(START) != 1 or data.count(END) != 1 or not data.startswith(START + b"\n"):
        raise ContractError("source_markers", "canonical contract markers are invalid")
    if data.find(END) <= data.find(START):
        raise ContractError("source_markers", "canonical contract marker order is invalid")
    words = len(re.findall(rb"\S+", data))
    if words > 110 or len(data) > 900:
        raise ContractError("source_limit", "canonical contract exceeds 110 words or 900 UTF-8 bytes")
    data.decode("utf-8", errors="strict")
    return data


def result(workspace: Path, *, installed: bool, action: str, reason: str, diagnostics: list[str]) -> dict[str, object]:
    try:
        source_hash: str | None = hashlib.sha256(load_source()).hexdigest()
    except (OSError, UnicodeError, ContractError):
        source_hash = None
    return {
        "installed": installed,
        "version": VERSION,
        "sha256": source_hash,
        "path": str((workspace / "AGENTS.md").resolve()),
        "action": action,
        "reason": reason,
        "diagnostics": diagnostics,
    }


def split_bom(data: bytes) -> tuple[bytes, bytes]:
    bom = b"\xef\xbb\xbf"
    return (bom, data[len(bom):]) if data.startswith(bom) else (b"", data)


def marker_spans(body: bytes) -> list[tuple[int, int, int]]:
    matches = list(ANY_MARKER.finditer(body))
    if len(RESERVED_MARKER.findall(body)) != len(matches):
        raise ContractError("malformed_markers", "managed contract markers are malformed")
    if not matches:
        return []
    spans: list[tuple[int, int, int]] = []
    index = 0
    while index < len(matches):
        start = matches[index]
        if start.group(2) != b"start" or index + 1 >= len(matches):
            raise ContractError("malformed_markers", "managed contract markers are malformed")
        end = matches[index + 1]
        if end.group(2) != b"end" or end.group(1) != start.group(1):
            raise ContractError("malformed_markers", "managed contract markers are malformed")
        stop = end.end()
        if body[stop:stop + 2] == b"\r\n":
            stop += 2
        elif body[stop:stop + 1] == b"\n":
            stop += 1
        spans.append((start.start(), stop, int(start.group(1))))
        index += 2
    return spans


def inspect(workspace: Path) -> tuple[dict[str, object], bytes | None, list[tuple[int, int, int]]]:
    load_source()
    if not workspace.is_dir():
        return result(workspace, installed=False, action="none", reason="workspace_invalid", diagnostics=["workspace must be an existing directory"]), None, []
    path = workspace / "AGENTS.md"
    if not path.exists():
        return result(workspace, installed=False, action="none", reason="absent", diagnostics=[]), None, []
    if not path.is_file() or path.is_symlink():
        return result(workspace, installed=False, action="none", reason="not_regular_file", diagnostics=["AGENTS.md is not a regular file"]), None, []
    try:
        data = path.read_bytes()
        _, body = split_bom(data)
        spans = marker_spans(body)
    except (OSError, ContractError) as error:
        reason = error.reason if isinstance(error, ContractError) else "unreadable"
        return result(workspace, installed=False, action="none", reason=reason, diagnostics=[str(error)]), None, []
    if not spans:
        return result(workspace, installed=False, action="none", reason="missing", diagnostics=[]), data, []
    if len(spans) != 1:
        return result(workspace, installed=False, action="none", reason="duplicated", diagnostics=["exactly one managed block is required"]), data, spans
    start, stop, version = spans[0]
    observed = normalized(body[start:stop])
    canonical = load_source()
    if version == VERSION and observed != canonical:
        return result(workspace, installed=False, action="none", reason="changed", diagnostics=["the current managed block differs from its canonical source"]), data, spans
    if version != VERSION and (version not in LEGACY_BLOCKS or observed != normalized(LEGACY_BLOCKS[version])):
        return result(workspace, installed=False, action="none", reason="unknown_version", diagnostics=[f"managed block version {version} is not recognized"]), data, spans
    if start != 0:
        return result(workspace, installed=False, action="none", reason="misplaced", diagnostics=["the managed block is not the first AGENTS.md content"]), data, spans
    if version != VERSION:
        return result(workspace, installed=False, action="none", reason="recognized_old", diagnostics=[f"managed block version {version} can be upgraded"]), data, spans
    return result(workspace, installed=True, action="none", reason="valid", diagnostics=[]), data, spans


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix=".agents-contract-", dir=str(path.parent))
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def install(workspace: Path, approved: bool) -> dict[str, object]:
    if not approved:
        return result(workspace, installed=False, action="none", reason="approval_required", diagnostics=["install requires --approved"])
    state, data, spans = inspect(workspace)
    if state["installed"]:
        state["action"] = "unchanged"
        return state
    if state["reason"] not in {"absent", "missing", "misplaced", "recognized_old"}:
        state["diagnostics"] = list(state["diagnostics"]) + ["manual disposition is required"]
        return state
    canonical = load_source()
    path = workspace / "AGENTS.md"
    if data is None:
        output = canonical
        action = "created"
    else:
        bom, body = split_bom(data)
        if spans:
            start, stop, _ = spans[0]
            body = body[:start] + body[stop:]
        separator = b"" if not body else b"\n"
        output = bom + canonical + separator + body
        action = "moved" if state["reason"] == "misplaced" else "upgraded" if state["reason"] == "recognized_old" else "prepended"
    try:
        atomic_write(path, output)
    except OSError as error:
        return result(workspace, installed=False, action="none", reason="write_failed", diagnostics=[str(error)])
    verified, _, _ = inspect(workspace)
    if not verified["installed"]:
        verified["action"] = action
        verified["reason"] = "verification_failed"
        return verified
    verified["action"] = action
    verified["reason"] = "installed"
    return verified


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description="Verify or install the Scoville Workflow AGENTS.md contract.")
    value.add_argument("command", choices=("check", "install", "render"))
    value.add_argument("--workspace", required=True)
    value.add_argument("--approved", action="store_true")
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    workspace = Path(args.workspace).resolve()
    try:
        if args.command == "render":
            sys.stdout.buffer.write(load_source())
            return 0
        payload = inspect(workspace)[0] if args.command == "check" else install(workspace, args.approved)
    except (OSError, UnicodeError, ContractError) as error:
        reason = error.reason if isinstance(error, ContractError) else "helper_failure"
        payload = result(workspace, installed=False, action="none", reason=reason, diagnostics=[str(error)])
    except Exception as error:  # pragma: no cover - final containment boundary
        payload = result(
            workspace,
            installed=False,
            action="none",
            reason="helper_failure",
            diagnostics=[f"{type(error).__name__}: {error}"],
        )
    encoded = compact(payload)
    json.loads(encoded)
    sys.stdout.write(encoded + "\n")
    return 0 if payload["installed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
