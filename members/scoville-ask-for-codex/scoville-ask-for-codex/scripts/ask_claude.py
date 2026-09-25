#!/usr/bin/env python3
"""Claude CLI command and response adapter; settings belong to config.default.json."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

EFFORT_LEVELS = ("low", "medium", "high", "xhigh", "max")
READ_ONLY_TOOLS = "Read,Grep,Glob,WebSearch,WebFetch"
MODEL_PATTERN = re.compile(r"^[A-Za-z0-9._:-]+$")


def configure_standard_streams() -> None:
    input_reconfigure = getattr(sys.stdin, "reconfigure", None)
    if callable(input_reconfigure):
        input_reconfigure(encoding="utf-8-sig", errors="replace")

    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


def resolve_claude_command() -> list[str]:
    executable = shutil.which("claude")
    if executable is None:
        raise RuntimeError("Claude Code CLI was not found on PATH")

    path = Path(executable)
    if path.suffix.lower() == ".ps1":
        powershell = shutil.which("pwsh") or shutil.which("powershell")
        if powershell is None:
            raise RuntimeError("Claude resolves to a PowerShell script, but no PowerShell executable was found")
        return [powershell, "-NoProfile", "-File", str(path)]

    return [str(path)]


def parse_claude_result(raw_output: str) -> dict[str, Any]:
    try:
        payload = json.loads(raw_output)
    except json.JSONDecodeError as error:
        raise ValueError(f"Claude returned invalid JSON: {error}") from error
    if not isinstance(payload, dict):
        raise ValueError("Claude returned JSON that is not an object")
    return payload


def claude_error_details(payload: dict[str, Any]) -> str | None:
    subtype = payload.get("subtype")
    has_error_subtype = isinstance(subtype, str) and subtype.startswith("error")
    if payload.get("is_error") is not True and not has_error_subtype:
        return None

    errors = payload.get("errors")
    if isinstance(errors, list):
        messages = [message for message in errors if isinstance(message, str)]
        if messages:
            return "; ".join(messages)

    for key in ("result", "terminal_reason", "subtype"):
        value = payload.get(key)
        if isinstance(value, str) and value:
            return value
    return "Claude reported an unspecified error"


def session_mode(args: argparse.Namespace) -> str:
    if args.fresh:
        return "fresh"
    if args.resume:
        return "resume"
    if args.continue_session:
        return "continue"
    if args.persistent or args.session_persistence_default:
        return "persistent"
    return "fresh"


def build_command(args: argparse.Namespace, claude_command: list[str]) -> list[str]:
    command = [
        *claude_command,
        "-p",
        "--model",
        args.model,
        "--effort",
        args.effort,
        "--output-format",
        "json",
        "--permission-mode",
        "dontAsk",
        "--tools",
        READ_ONLY_TOOLS,
        "--allowed-tools",
        READ_ONLY_TOOLS,
        "--max-budget-usd",
        format(args.max_budget_usd, "g"),
    ]

    mode = session_mode(args)
    if mode == "fresh":
        command.append("--no-session-persistence")
    elif mode == "resume":
        command.extend(["--resume", args.resume])
    elif mode == "continue":
        command.append("--continue")
    elif args.session_name:
        command.extend(["--name", args.session_name])

    if not args.customizations_enabled:
        command.append("--safe-mode")

    return command
