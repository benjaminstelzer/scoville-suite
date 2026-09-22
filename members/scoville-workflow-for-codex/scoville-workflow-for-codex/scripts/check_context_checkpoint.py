#!/usr/bin/env python3
"""Read-only role-specific context decision from the caller's native rollout."""
from __future__ import annotations

import argparse
import os
import tomllib
from pathlib import Path

from inspect_native_context import (
    InspectionError, compact, configure_utf8, event_payload, load_events,
    resolve_rollout,
)


def read_thresholds(path: Path) -> dict:
    with path.open("rb") as stream:
        config = tomllib.load(stream)
    if type(config.get("schema_version")) is not int or config["schema_version"] != 1:
        raise ValueError("unsupported workflow schema_version")
    thresholds = config.get("context")
    if not isinstance(thresholds, dict) or set(thresholds) != {"coordinator_percent", "worker_percent"}:
        raise ValueError("context requires exactly coordinator_percent and worker_percent")
    if any(type(value) is not int or not 1 <= value <= 99 for value in thresholds.values()):
        raise ValueError("context percentages must be integers from 1 through 99")
    return thresholds


def decide(events: list[dict], thread_id: str, role: str, thresholds: dict) -> dict:
    if role not in {"coordinator", "executor", "reviewer", "repair"}:
        raise InspectionError("unknown checkpoint role")
    meta = [e for e in events if e.get("type") == "session_meta"]
    if len(meta) != 1 or event_payload(meta[0]).get("session_id") != thread_id:
        raise InspectionError("rollout does not identify the calling task")
    contexts = [e for e in events if e.get("type") == "turn_context"]
    samples = [e for e in events if event_payload(e).get("type") == "token_count"]
    if not contexts or not samples:
        raise InspectionError("context or telemetry is missing")
    context, sample = contexts[-1], samples[-1]
    turn_id = event_payload(context).get("turn_id")
    if not isinstance(turn_id, str) or not turn_id:
        raise InspectionError("current turn identity is missing")
    boundaries = [context["ordinal"]] + [
        e["ordinal"] for e in events if e.get("type") == "compacted"
    ]
    if sample["ordinal"] <= max(boundaries):
        raise InspectionError("telemetry precedes the current context or compaction")
    for e in events:
        if e["ordinal"] <= context["ordinal"]:
            continue
        payload = event_payload(e)
        if payload.get("turn_id", turn_id) != turn_id:
            raise InspectionError("telemetry interval has conflicting turn identity")
        if payload.get("type") in {"task_started", "task_complete", "task_failed", "task_aborted"}:
            raise InspectionError("telemetry interval crosses a turn boundary")
    info = event_payload(sample).get("info")
    if not isinstance(info, dict) or not isinstance(info.get("last_token_usage"), dict):
        raise InspectionError("telemetry fields are missing")
    used = info["last_token_usage"].get("input_tokens")
    window = info.get("model_context_window")
    if type(used) is not int or type(window) is not int or not 0 < used <= window:
        raise InspectionError("telemetry values are invalid")
    return {
        "action": (
            ("rollover" if used * 100 >= window * thresholds["coordinator_percent"] else "continue")
            if role == "coordinator" else
            ("context_handoff" if used * 100 > window * thresholds["worker_percent"] else "continue")
        ),
        "telemetry": "fresh", "input_tokens": used,
        "model_context_window": window, "sample_ordinal": sample["ordinal"],
        "turn_id": turn_id,
    }


def main() -> int:
    configure_utf8()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", choices=("coordinator", "executor", "reviewer", "repair"), required=True)
    parser.add_argument("--accepted-unit")
    args = parser.parse_args()
    from manage_workflow_guard import GuardError, validate_unit
    try:
        if args.role == "coordinator":
            validate_unit(args.accepted_unit, "accepted_unit")
        elif args.accepted_unit is not None:
            raise GuardError("invalid_argument", "accepted-unit is coordinator-only")
    except GuardError as error:
        print(compact({"action": "blocked", "diagnostic": str(error)}))
        return 1
    thread_id = os.environ.get("CODEX_THREAD_ID")
    try:
        thresholds = read_thresholds(Path(__file__).resolve().parents[1] / "assets" / "workflow.toml")
    except (OSError, ValueError) as error:
        print(compact({"action": "blocked", "reason": "configuration_invalid", "diagnostic": str(error)}))
        return 1
    try:
        path = resolve_rollout(argparse.Namespace(
            thread_id=thread_id, rollout=None, sessions_root=None,
        ))
        result = decide(load_events(path), thread_id, args.role, thresholds)
    except (InspectionError, OSError, ValueError, TypeError, KeyError) as error:
        result = {"action": "continue", "telemetry": "unavailable", "diagnostic": str(error)}
    result.update(thread_id=thread_id, role=args.role)
    result["threshold_percent"] = thresholds["coordinator_percent" if args.role == "coordinator" else "worker_percent"]
    if args.role == "coordinator":
        result["accepted_unit"] = args.accepted_unit
    print(compact(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
