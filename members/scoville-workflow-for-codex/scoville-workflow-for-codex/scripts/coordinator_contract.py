#!/usr/bin/env python3
"""Supply and verify the complete normal coordinator contract at native startup."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
MARKER = "\n[Coordinator runtime contract]\n"
PHASES = ("scope", "selection", "dispatch", "activation", "wait", "results", "review", "accepted", "stop")
STARTS = {"initial_parking", "initial_claim", "rollover_parking", "rollover_validation", "rollover_activation"}


class ContractError(ValueError):
    pass


def without_scenarios(source: str) -> str:
    """Omit only explicitly labelled example tables, never procedural sections."""
    return re.sub(r"^### [^\n]*scenarios\n.*?(?=^#{1,3} |\Z)", "", source,
                  flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)


def absolute_links(source: str, owner: Path) -> str:
    def replace(match: re.Match) -> str:
        target = match[1]
        if "://" in target or target.startswith("#"):
            return match[0]
        path, sep, anchor = target.partition("#")
        return "](" + (owner.parent / path).resolve().as_posix() + (sep + anchor if sep else "") + ")"
    return re.sub(r"\]\(([^)]+)\)", replace, source)


def runtime_contract(package: Path = PACKAGE) -> str:
    """One generated projection; the phase sources remain the sole rule owners."""
    package = package.resolve()
    skill = (package / "SKILL.md").read_text(encoding="utf-8")
    startup = skill.split("## Complete coordinator startup\n", 1)[1].split("## First operation: role gate\n", 1)[0]
    boundary = skill.split("## Coordinator boundary\n", 1)[1].split("## Dispatch routing\n", 1)[0]
    core = (package / "references/operations.md").read_text(encoding="utf-8")
    core = core.split("## Coordinator delivery\n", 1)[0]
    parts = ["# Coordinator contract\n\n"
             "This is the complete normal workflow, supplied by the package helper. "
             "Read it before project access. Parking still permits no project action. "
             "Use native create_thread project tasks, never collaboration.spawn_agent, "
             "followup_task or a fork as a workflow transport.\n",
             absolute_links("## Complete coordinator startup\n" + startup, package / "SKILL.md"),
             absolute_links("## Coordinator boundary\n" + boundary, package / "SKILL.md"),
             absolute_links(core, package / "references/operations.md")]
    for phase in PHASES:
        path = package / "references" / f"operations-{phase}.md"
        source = path.read_text(encoding="utf-8")
        # The opening cross-reference paragraph only routed the former partial reads.
        source = source[source.index("\n## ") + 1:]
        parts.append(absolute_links(without_scenarios(source), path))
    lifecycle = package / "scripts/task_lifecycle.md"
    parts.append(absolute_links(lifecycle.read_text(encoding="utf-8"), lifecycle))
    rollover = package / "references/operations-rollover.md"
    source = rollover.read_text(encoding="utf-8")
    checkpoint = source.split("Perform this sequence once:", 1)[0]
    parts.append(absolute_links(checkpoint, rollover))
    parts.append("## Conditional recovery\n\n"
                 "For an actual coordinator rollover, read " + rollover.as_posix() + " completely.\n"
                 "For a worker context_handoff or post-compaction recovery, read "
                 + (package / "references/operations-compaction.md").as_posix() + " and "
                 + (package / "references/operations-checkpoint.md").as_posix() + ".\n"
                 "After compaction or context loss, run `python \"" +
                 (package / "scripts/coordinator_contract.py").as_posix() +
                 "\" show` and read its complete output before resuming. "
                 "A receipt or remembered hash does not restore missing instructions.\n")
    return "\n\n".join(part.strip() for part in parts) + "\n"


def fields(prompt: str) -> dict[str, str]:
    values = {}
    for line in prompt.splitlines():
        match = re.fullmatch(r"([a-z_][a-z_0-9]*)=(.*)", line)
        if match:
            if match[1] in values:
                raise ContractError("duplicate coordinator field: " + match[1])
            values[match[1]] = match[2]
    return values


def build_prompt(prompt: str, package: Path = PACKAGE) -> str:
    if not prompt.startswith("scoville_role=coordinator\n") or MARKER in prompt:
        raise ContractError("supply one unwrapped coordinator prompt with its leading role marker")
    values = fields(prompt)
    if values.get("coordinator_start") not in STARTS:
        raise ContractError("unknown coordinator start")
    for key in ("workspace_root", "workflow_id"):
        if not values.get(key):
            raise ContractError("missing coordinator field: " + key)
    contract = runtime_contract(package)
    prompt = re.sub(r"^skill_path=.*\n?", "", prompt, flags=re.MULTILINE).rstrip()
    return (prompt + "\nskill_path=" + (package.resolve() / "SKILL.md").as_posix()
            + "\ncoordinator_contract_sha256=" + hashlib.sha256(contract.encode()).hexdigest()
            + MARKER + contract)


def native_events(thread_id: str, sessions_root: Path | None = None) -> list[dict]:
    if not re.fullmatch(r"[A-Za-z0-9._:-]{1,160}", thread_id):
        raise ContractError("invalid native task identity")
    root = sessions_root or Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "sessions"
    paths = list(root.rglob("*" + thread_id + ".jsonl"))
    if len(paths) != 1:
        raise ContractError("exact active native task evidence is missing or ambiguous")
    events = [json.loads(line) for line in paths[0].read_text(encoding="utf-8").splitlines() if line.strip()]
    if any(not isinstance(event, dict) for event in events):
        raise ContractError("native task evidence contains a non-object event")
    ordinals = [event.get("ordinal") for event in events]
    if (any(type(value) is not int for value in ordinals)
            or ordinals != sorted(ordinals) or len(set(ordinals)) != len(ordinals)):
        raise ContractError("native task evidence has missing, duplicate or unordered ordinals")
    meta = [e.get("payload", {}) for e in events if e.get("type") == "session_meta"]
    if len(meta) != 1 or meta[0].get("session_id") != thread_id:
        raise ContractError("native session identity mismatch")
    if meta[0].get("thread_source") != "agent_created_thread":
        raise ContractError("workflow roles require create_thread, not a subagent or fork")
    return events


def native_inputs(events: list[dict], tool: str | None = None):
    for event in events:
        p = event.get("payload", {})
        if (event.get("type") != "response_item" or p.get("type") != "function_call_output"
                or p.get("name") not in ({tool} if tool else {"create_thread", "send_message_to_thread"})
                or p.get("namespace") != "codex_app"):
            continue
        output = p.get("output")
        if not isinstance(output, str):
            continue
        match = re.fullmatch(r"<codex_delegation>\s*<source_thread_id>([^<>]+)</source_thread_id>\s*"
                             r"<input>(.*)</input>\s*</codex_delegation>", output, re.DOTALL)
        if match:
            yield match[1], match[2]


def output_contains(value, contract: str) -> bool:
    """Recognize complete tool-delivered text, including native JSON wrappers."""
    if isinstance(value, str):
        # Native Windows shell output may translate LF to CRLF.
        if contract in value.replace("\r\n", "\n"):
            return True
        try:
            decoded = json.loads(value)
        except (ValueError, RecursionError):
            return False
        return decoded != value and output_contains(decoded, contract)
    if isinstance(value, list):
        return any(output_contains(item, contract) for item in value)
    if isinstance(value, dict):
        return any(output_contains(item, contract) for item in value.values())
    return False


def verify_coordinator(thread_id: str, workflow_id: str, workspace: Path,
                       package: Path = PACKAGE, sessions_root: Path | None = None) -> None:
    events = native_events(thread_id, sessions_root)
    creations = list(native_inputs(events, "create_thread"))
    if len(creations) != 1:
        raise ContractError("one native coordinator creation envelope is required")
    prompt = creations[0][1]
    if prompt.count(MARKER) != 1:
        raise ContractError("coordinator was created without its complete runtime contract")
    header, observed = prompt.split(MARKER)
    values = fields(header)
    expected = runtime_contract(package)
    if (values.get("scoville_role") != "coordinator"
            or values.get("coordinator_start") not in {"initial_parking", "rollover_parking"}
            or values.get("workflow_id") != workflow_id
            or Path(values.get("workspace_root", "")).resolve() != workspace.resolve()
            or values.get("skill_path") != (package.resolve() / "SKILL.md").as_posix()
            or values.get("coordinator_contract_sha256") != hashlib.sha256(expected.encode()).hexdigest()
            or observed != expected):
        raise ContractError("coordinator startup contract is stale, incomplete or bound to another workflow")
    compactions = [index for index, event in enumerate(events) if event.get("type") == "compacted"]
    if compactions:
        restored = False
        for event in events[compactions[-1] + 1:]:
            payload = event.get("payload", {})
            if (event.get("type") == "response_item"
                    and payload.get("type") in {"function_call_output", "custom_tool_call_output"}
                    and output_contains(payload.get("output"), expected)):
                restored = True
                break
        if not restored:
            raise ContractError("coordinator contract must be shown completely again after compaction")


def verify_writer(thread_id: str, coordinator_id: str, workflow_id: str, workspace: Path,
                  role: str, unit: str, dispatch_key: str, sessions_root: Path | None = None) -> None:
    creations = list(native_inputs(native_events(thread_id, sessions_root), "create_thread"))
    if len(creations) != 1 or creations[0][0] != coordinator_id:
        raise ContractError("writer was not created by its exact native coordinator")
    values = fields(creations[0][1])
    expected = {"scoville_role": role, "unit": unit, "workflow_id": workflow_id,
                "dispatch_key": dispatch_key}
    if any(values.get(k) != v for k, v in expected.items()) or Path(values.get("workspace_root", "")).resolve() != workspace.resolve():
        raise ContractError("native writer parking envelope does not match its guard assignment")


def main() -> int:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("build", "show"))
    args = parser.parse_args()
    try:
        if args.operation == "show":
            sys.stdout.write(runtime_contract())
        else:
            request = json.load(sys.stdin)
            if not isinstance(request, dict) or set(request) != {"prompt"} or not isinstance(request["prompt"], str):
                raise ContractError("build requires exactly one prompt string")
            print(json.dumps({"prompt": build_prompt(request["prompt"])}, ensure_ascii=False))
        return 0
    except (ValueError, OSError, IndexError, KeyError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
