"""Read native rollout records for the context checkpoint."""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


class InspectionError(ValueError):
    pass


def configure_utf8() -> None:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")


def compact(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def default_sessions_root() -> Path:
    configured = os.environ.get("CODEX_HOME")
    if configured:
        return Path(configured) / "sessions"
    return Path.home() / ".codex" / "sessions"


def resolve_rollout(args: argparse.Namespace) -> Path:
    if not args.thread_id or not re.fullmatch(r"[A-Za-z0-9._:-]{1,128}", args.thread_id):
        raise InspectionError("thread identity is missing or invalid")
    if args.rollout:
        candidate = Path(args.rollout)
        if not candidate.is_file():
            raise InspectionError("the requested rollout is not a regular file")
        return candidate
    root = Path(args.sessions_root) if args.sessions_root else default_sessions_root()
    if not root.is_dir():
        raise InspectionError("the active sessions root is unavailable")
    candidates = list(root.rglob(f"*{args.thread_id}.jsonl"))
    if len(candidates) != 1:
        raise InspectionError("the exact active rollout is missing or ambiguous")
    return candidates[0]


def load_events(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise InspectionError(f"rollout line {line_number} is not an object")
                events.append(value)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise InspectionError(f"the rollout is unreadable ({type(error).__name__})") from error
    ordinals = [event.get("ordinal") for event in events]
    if not events or any(not isinstance(value, int) for value in ordinals):
        raise InspectionError("the rollout has missing or invalid ordinals")
    if ordinals != sorted(ordinals) or len(ordinals) != len(set(ordinals)):
        raise InspectionError("the rollout ordinals are duplicated or unordered")
    return events


def event_payload(event: dict[str, Any]) -> dict[str, Any]:
    payload = event.get("payload")
    return payload if isinstance(payload, dict) else {}
