#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from build_dispatch_prompt import (
    PromptError, build_prompt, validate_plan_context, validate_prompt_arguments,
    validate_role_input,
)


class InspectionError(Exception):
    pass


def configure_utf8() -> None:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="strict")


def compact(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect one exact Codex rollout after compaction.")
    parser.add_argument("--thread-id", default=os.environ.get("CODEX_THREAD_ID"))
    parser.add_argument("--role", choices=("executor", "reviewer", "repair"), required=True)
    parser.add_argument("--delivery-reference", required=True)
    parser.add_argument("--return-to-thread-id", required=True)
    parser.add_argument("--rollout", help="Exact rollout JSONL path; intended for deterministic verification.")
    parser.add_argument("--sessions-root", help="Active Codex sessions root. Defaults to the local Codex sessions directory.")
    return parser.parse_args(argv)


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


def payload_type(event: dict[str, Any]) -> str | None:
    return event_payload(event).get("type")


def message_text(payload: dict[str, Any]) -> str | None:
    content = payload.get("content")
    if not isinstance(content, list):
        return None
    parts: list[str] = []
    for item in content:
        if not isinstance(item, dict):
            return None
        text = item.get("text")
        if not isinstance(text, str):
            return None
        parts.append(text)
    return "".join(parts)


def delegated_input(event: dict[str, Any]) -> str | None:
    payload = event_payload(event)
    if (
        event.get("type") != "response_item"
        or payload.get("type") != "function_call_output"
        or payload.get("name") not in {"create_thread", "send_message_to_thread"}
    ):
        return None
    output = payload.get("output")
    if not isinstance(output, str):
        raise InspectionError("the native assignment envelope is not text")
    match = re.fullmatch(
        r"<codex_delegation>\s*"
        r"<source_thread_id>[^<>]+</source_thread_id>\s*"
        r"<input>(.*)</input>\s*"
        r"</codex_delegation>",
        output,
        flags=re.DOTALL,
    )
    if match is None:
        raise InspectionError("the native assignment envelope is malformed")
    return match.group(1)


def parse_builder_assignment(assignment: str) -> dict[str, Any]:
    if not assignment.endswith("\n"):
        raise InspectionError("the builder assignment has no terminal newline")
    lines = assignment[:-1].split("\n")
    fixed_names = (
        "scoville_role",
        "dispatch_contract",
        "unit",
        "workspace_root",
        "guard_path",
        "guard_workflow_id",
        "guard_generation",
        "guard_revision",
        "guard_dispatch_key",
        "guard_task_id",
        "guard_helper",
    )
    if len(lines) < len(fixed_names) or any(
        not lines[index].startswith(name + "=")
        for index, name in enumerate(fixed_names)
    ):
        raise InspectionError("the builder assignment header is malformed")
    fields = {
        name: lines[index].split("=", 1)[1]
        for index, name in enumerate(fixed_names)
    }
    try:
        inputs_index = len(lines) - 1 - lines[::-1].index("[Inputs]")
    except ValueError as error:
        raise InspectionError("the builder assignment inputs are missing") from error
    input_lines = lines[inputs_index + 1:]
    if not input_lines or any("=" not in line for line in input_lines):
        raise InspectionError("the builder assignment inputs are malformed")
    inputs: dict[str, object] = {}
    for line in input_lines:
        name, raw = line.split("=", 1)
        if name in inputs:
            raise InspectionError("the builder assignment has duplicate inputs")
        try:
            inputs[name] = json.loads(raw)
        except json.JSONDecodeError as error:
            raise InspectionError("the builder assignment input is not JSON") from error
    plan_context = inputs.pop("plan_context", None)
    try:
        generation = int(fields["guard_generation"])
        revision = int(fields["guard_revision"])
    except ValueError as error:
        raise InspectionError("the builder assignment guard version is invalid") from error
    task_id = fields["guard_task_id"]
    parsed = {
        "role": fields["scoville_role"],
        "unit": fields["unit"],
        "workspace_root": fields["workspace_root"],
        "return_to_thread_id": "",
        "delivery_reference": "",
        "guard_workflow_id": fields["guard_workflow_id"],
        "guard_generation": generation,
        "guard_revision": revision,
        "guard_dispatch_key": fields["guard_dispatch_key"],
        "guard_task_id": None if task_id == "read_only" else task_id,
        "plan_context": plan_context,
        "role_input": inputs,
    }
    try:
        validate_prompt_arguments(
            parsed["role"], parsed["workspace_root"], "placeholder",
            "placeholder", parsed["guard_workflow_id"],
            parsed["guard_generation"], parsed["guard_revision"],
            parsed["guard_dispatch_key"], parsed["guard_task_id"],
        )
        parsed["plan_context"] = validate_plan_context(plan_context, parsed["unit"])
        parsed["role_input"] = validate_role_input(parsed["role"], inputs)
    except PromptError as error:
        raise InspectionError(error.message) from error
    return parsed


def require_builder_assignment(
    events: list[dict[str, Any]],
    start_ordinal: int,
    current_ordinal: int,
    role: str,
    reference: str,
    return_to_thread_id: str,
) -> None:
    assignments = [
        value
        for event in events
        if start_ordinal < event["ordinal"] < current_ordinal
        for value in [delegated_input(event)]
        if value is not None
    ]
    if len(assignments) != 1:
        raise InspectionError("the current turn has no unique native assignment")
    native_assignment = assignments[0]
    candidates = [native_assignment]
    decoded = html.unescape(native_assignment)
    if decoded != native_assignment and html.escape(decoded, quote=False) == native_assignment:
        candidates.append(decoded)
    for candidate in candidates:
        assignment = candidate if candidate.endswith("\n") else candidate + "\n"
        try:
            parsed = parse_builder_assignment(assignment)
        except InspectionError:
            continue
        if parsed["role"] != role:
            raise InspectionError("the current assignment has a conflicting role")
        parsed["return_to_thread_id"] = return_to_thread_id
        parsed["delivery_reference"] = reference
        expected = build_prompt(
            native_context_inspector=str(Path(__file__).resolve()),
            **parsed,
        )
        if assignment == expected:
            return
    raise InspectionError("the current assignment is not a complete builder dispatch")


def native_turn_id(payload: dict[str, Any]) -> str | None:
    if "internal_chat_message_metadata_passthrough" not in payload:
        return None
    metadata = payload.get("internal_chat_message_metadata_passthrough")
    if not isinstance(metadata, dict):
        raise InspectionError("native turn metadata is malformed")
    turn_id = metadata.get("turn_id")
    if turn_id is None:
        return None
    if not isinstance(turn_id, str) or not turn_id:
        raise InspectionError("native turn metadata is malformed")
    return turn_id


def require_native_turn(payload: dict[str, Any], expected_turn_id: str) -> None:
    embedded = native_turn_id(payload)
    if embedded is not None and embedded != expected_turn_id:
        raise InspectionError("native response metadata has a conflicting turn identity")


def final_message_catalog(events: list[dict[str, Any]]) -> dict[str, tuple[str, str]]:
    active_turn: str | None = None
    catalog: dict[str, tuple[str, str]] = {}
    for event in events:
        payload = event_payload(event)
        kind = payload.get("type")
        if event.get("type") == "event_msg" and kind == "task_started":
            candidate = payload.get("turn_id")
            active_turn = candidate if isinstance(candidate, str) and candidate else None
            continue
        if is_final_message(event):
            message_id = payload.get("id")
            text = message_text(payload)
            embedded = native_turn_id(payload)
            source_turn = embedded or active_turn
            if (
                not isinstance(message_id, str)
                or not message_id
                or text is None
                or not isinstance(source_turn, str)
                or not source_turn
                or (embedded is not None and active_turn is not None and embedded != active_turn)
            ):
                continue
            value = (source_turn, text)
            if message_id in catalog and catalog[message_id] != value:
                raise InspectionError("a final message identity has conflicting source records")
            catalog[message_id] = value
        if event.get("type") == "event_msg" and kind in {"task_complete", "task_failed", "task_aborted"}:
            active_turn = None
    return catalog


def validate_role_result(raw: str, role: str) -> dict[str, Any]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as error:
        raise InspectionError("the terminal result is not valid JSON") from error
    if not isinstance(value, dict):
        raise InspectionError("the terminal result is not an object")
    expected = {"status", "summary", "findings"}
    statuses = {"pass", "changes_requested", "blocked", "needs_user_decision", "context_handoff"}
    if role in {"executor", "repair"}:
        expected.add("review")
        statuses = {"completed", "blocked", "needs_user_decision", "context_handoff"}
    if set(value) != expected or value.get("status") not in statuses:
        raise InspectionError("the terminal result does not match its role schema")
    if not isinstance(value.get("summary"), str) or len(value["summary"]) > 800:
        raise InspectionError("the terminal summary is invalid")
    findings = value.get("findings")
    if not isinstance(findings, list) or len(findings) > 8 or any(
        not isinstance(item, str) or len(item) > 400 for item in findings
    ):
        raise InspectionError("the terminal findings are invalid")
    if len(value["summary"]) + sum(len(item) for item in findings) > 4000:
        raise InspectionError("the terminal result exceeds the prose limit")
    if role == "reviewer" and value["status"] == "pass" and findings:
        raise InspectionError("a passing review contains findings")
    if role in {"executor", "repair"}:
        review = value.get("review")
        if value["status"] == "completed":
            if not isinstance(review, dict) or set(review) != {"code_changed", "critical_docs_changed"}:
                raise InspectionError("the completed result has an invalid review object")
            if any(item not in {"yes", "no"} for item in review.values()):
                raise InspectionError("the completed result has an invalid review value")
        elif review is not None:
            raise InspectionError("a non-completed result has a review object")
    return value


def extract_delivery_prompt(prompt: object, reference: str) -> str | None:
    if not isinstance(prompt, str):
        raise InspectionError("the delivery prompt is not text")
    marker = f"workflow_result_delivery={reference}\n"
    if not prompt.startswith(marker):
        return None
    result = prompt[len(marker):]
    if not result or result != result.strip():
        raise InspectionError("the delivered result bytes are empty or padded")
    return result


def extract_json_call(source: object) -> dict[str, Any] | None:
    if not isinstance(source, str):
        return None
    stripped = source.strip()
    token = "tools.mcp__codex_app__send_message_to_thread("
    if token not in stripped:
        return None
    prefix = "const r=await " + token
    suffix = ');for(const c of(r.content??[])){if(c.type==="text")text(c.text);}'
    if stripped.count(token) != 1 or not stripped.startswith(prefix) or not stripped.endswith(suffix):
        raise InspectionError("the delivery wrapper does not match the canonical call shape")
    encoded = stripped[len(prefix):-len(suffix)]
    try:
        arguments = json.loads(encoded)
    except json.JSONDecodeError as error:
        raise InspectionError("the delivery wrapper must use one inline JSON object") from error
    if not isinstance(arguments, dict) or set(arguments) != {"threadId", "prompt"}:
        raise InspectionError("the delivery wrapper has unexpected arguments")
    return arguments


def text_blocks(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [text for item in value for text in text_blocks(item)]
    if isinstance(value, dict):
        if value.get("type") in {"text", "input_text", "output_text"} and isinstance(value.get("text"), str):
            return [value["text"]]
        return [text for key in ("content", "output") if key in value for text in text_blocks(value[key])]
    return []


def successful_delivery_output(output: object, return_to_thread_id: str) -> bool:
    matches: list[dict[str, Any]] = []
    for text in text_blocks(output):
        try:
            value = json.loads(text.strip())
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and "threadId" in value:
            matches.append(value)
    return len(matches) == 1 and matches[0] == {"threadId": return_to_thread_id}


def is_delivery_call(event: dict[str, Any]) -> bool:
    payload = event_payload(event)
    return (
        event.get("type") == "response_item"
        and payload.get("type") == "custom_tool_call"
        and payload.get("name") == "exec"
        and isinstance(payload.get("input"), str)
        and "tools.mcp__codex_app__send_message_to_thread(" in payload["input"]
    )


def is_final_message(event: dict[str, Any]) -> bool:
    payload = event_payload(event)
    return (
        event.get("type") == "response_item"
        and payload.get("type") == "message"
        and payload.get("role") == "assistant"
        and payload.get("phase") == "final_answer"
    )


def is_final_mirror(event: dict[str, Any]) -> bool:
    payload = event_payload(event)
    item = payload.get("item")
    return (
        event.get("type") == "event_msg"
        and payload.get("type") == "item_completed"
        and isinstance(item, dict)
        and item.get("type") == "AgentMessage"
        and item.get("phase") == "final_answer"
    )


def delivered_results(
    events: list[dict[str, Any]],
    lower: int,
    upper: int,
    reference: str,
    return_to_thread_id: str,
    turn_id: str,
) -> tuple[list[str], list[str]]:
    bounded = [event for event in events if lower < event["ordinal"] < upper]
    outputs: dict[str, list[dict[str, Any]]] = {}
    for event in bounded:
        payload = event_payload(event)
        if event.get("type") == "response_item" and payload.get("type") == "custom_tool_call_output":
            call_id = payload.get("call_id")
            if isinstance(call_id, str) and call_id:
                outputs.setdefault(call_id, []).append(event)

    deliveries: list[str] = []
    failed_attempts: list[str] = []
    attempted_reference = False
    seen_call_ids: set[str] = set()
    for event in bounded:
        payload = event_payload(event)
        if not is_delivery_call(event):
            continue
        require_native_turn(payload, turn_id)
        arguments = extract_json_call(payload.get("input"))
        if arguments is None:
            continue
        delivered = extract_delivery_prompt(arguments.get("prompt"), reference)
        if delivered is None:
            raise InspectionError("the resumed interval contains an unexpected send call")
        attempted_reference = True
        if arguments.get("threadId") != return_to_thread_id:
            raise InspectionError("the delivered result targets a different coordinator")
        call_id = payload.get("call_id")
        if not isinstance(call_id, str) or not call_id or call_id in seen_call_ids:
            raise InspectionError("the delivery wrapper call identity is missing or duplicated")
        seen_call_ids.add(call_id)
        matching_outputs = outputs.get(call_id, [])
        succeeded = False
        if payload.get("status") == "completed" and len(matching_outputs) == 1:
            succeeded = (
                matching_outputs[0]["ordinal"] > event["ordinal"]
                and successful_delivery_output(
                    event_payload(matching_outputs[0]).get("output"), return_to_thread_id
                )
            )
        if succeeded:
            require_native_turn(event_payload(matching_outputs[0]), turn_id)
            deliveries.append(delivered)
            continue

        failed_events = []
        for candidate in bounded:
            candidate_payload = event_payload(candidate)
            item = candidate_payload.get("item")
            if (
                candidate.get("type") == "event_msg"
                and candidate_payload.get("type") == "item_completed"
                and isinstance(item, dict)
                and item.get("type") == "McpToolCall"
                and item.get("server") == "codex_app"
                and item.get("tool") == "send_message_to_thread"
                and item.get("status") == "failed"
                and item.get("arguments") == arguments
                and candidate["ordinal"] > event["ordinal"]
            ):
                require_native_turn(candidate_payload, turn_id)
                failed_events.append(candidate)
        if payload.get("status") == "failed" or len(failed_events) == 1:
            failed_attempts.append(delivered)
            continue
        raise InspectionError("the delivery attempt outcome is unknown")
    if attempted_reference and len(deliveries) + len(failed_attempts) != 1:
        raise InspectionError("the delivery attempt is missing or duplicated")
    return deliveries, failed_attempts


def inspect(
    events: list[dict[str, Any]],
    thread_id: str,
    role: str,
    reference: str,
    return_to_thread_id: str,
) -> dict[str, Any]:
    session_meta = [event for event in events if event.get("type") == "session_meta"]
    if len(session_meta) != 1 or event_payload(session_meta[0]).get("session_id") != thread_id:
        raise InspectionError("session metadata does not bind exactly one matching task")
    contexts = [event for event in events if event.get("type") == "turn_context"]
    if not contexts:
        raise InspectionError("the current turn context is unavailable")
    current = contexts[-1]
    turn_id = event_payload(current).get("turn_id")
    if not isinstance(turn_id, str) or not turn_id:
        raise InspectionError("the current turn context has no identity")
    starts = [
        event for event in events
        if event.get("type") == "event_msg"
        and payload_type(event) == "task_started"
        and event_payload(event).get("turn_id") == turn_id
        and event["ordinal"] < current["ordinal"]
    ]
    if len(starts) != 1:
        raise InspectionError("the current turn has no unique task start")
    start = starts[0]
    if event_payload(session_meta[0]).get("thread_source") == "agent_created_thread":
        require_builder_assignment(
            events,
            start["ordinal"],
            events[-1]["ordinal"] + 1,
            role,
            reference,
            return_to_thread_id,
        )
    turn_contexts = [
        event for event in contexts
        if event_payload(event).get("turn_id") == turn_id
        and start["ordinal"] < event["ordinal"] < current["ordinal"]
    ]
    compactions = [
        event for event in events
        if event.get("type") == "compacted"
        and start["ordinal"] < event["ordinal"] < current["ordinal"]
    ]
    if not compactions:
        return {"schema_version": 1, "state": "not_applicable", "action": "continue_role"}
    if not turn_contexts:
        raise InspectionError("the compaction has no preceding turn context")
    bound = [event for event in events if start["ordinal"] <= event["ordinal"] <= current["ordinal"]]
    for event in bound:
        kind = payload_type(event)
        if kind == "task_started" and event["ordinal"] != start["ordinal"]:
            raise InspectionError("the resumed interval contains another task start")
        if kind in {"task_complete", "task_failed", "task_aborted"}:
            raise InspectionError("the resumed interval contains a terminal task event")
        event_turn = event_payload(event).get("turn_id")
        if event_turn is not None and event_turn != turn_id:
            raise InspectionError("the resumed interval contains a conflicting turn identity")
        event_thread = event_payload(event).get("thread_id")
        if event_thread is not None and event_thread != thread_id:
            raise InspectionError("the resumed interval contains a conflicting task identity")

    intervals: list[tuple[int, int]] = []
    lower = turn_contexts[0]["ordinal"]
    for compaction in compactions:
        prior_contexts = [event for event in contexts if lower <= event["ordinal"] < compaction["ordinal"]]
        following_contexts = [
            event for event in contexts
            if compaction["ordinal"] < event["ordinal"] <= current["ordinal"]
        ]
        if not prior_contexts or not following_contexts:
            raise InspectionError("the compaction has no complete context boundary")
        resumed = following_contexts[0]
        if any(
            other["ordinal"] != compaction["ordinal"]
            and compaction["ordinal"] < other["ordinal"] < resumed["ordinal"]
            for other in compactions
        ):
            raise InspectionError("the resumed interval has adjacent compactions")
        gap = [event for event in bound if compaction["ordinal"] < event["ordinal"] < resumed["ordinal"]]
        if any(is_final_message(event) or is_final_mirror(event) or is_delivery_call(event) for event in gap):
            raise InspectionError("the compaction-to-resume gap contains terminal activity")
        intervals.append((lower, compaction["ordinal"]))
        lower = resumed["ordinal"]
    if lower < current["ordinal"]:
        intervals.append((lower, current["ordinal"]))

    def inside_interval(event: dict[str, Any]) -> bool:
        return any(lower_bound < event["ordinal"] < upper_bound for lower_bound, upper_bound in intervals)

    result_events = [event for event in bound if inside_interval(event) and is_final_message(event)]
    final_ids: list[str] = []
    final_texts: list[str] = []
    for event in result_events:
        payload = event_payload(event)
        require_native_turn(payload, turn_id)
        message_id = payload.get("id")
        text = message_text(payload)
        if not isinstance(message_id, str) or not message_id or text is None:
            raise InspectionError("the final result identity or bytes are missing")
        if message_id in final_ids:
            raise InspectionError("the final result identity is duplicated")
        final_ids.append(message_id)
        final_texts.append(text)

    mirrors = [
        event_payload(event).get("item", {})
        for event in bound
        if inside_interval(event) and is_final_mirror(event)
    ]
    mirror_ids = [item.get("id") for item in mirrors]
    if any(not isinstance(item, str) or not item for item in mirror_ids):
        raise InspectionError("the final-message mirror identity is missing")
    if len(mirror_ids) != len(set(mirror_ids)) or any(item not in final_ids for item in mirror_ids):
        raise InspectionError("the final-message mirror is ambiguous")

    catalog = final_message_catalog([event for event in events if event["ordinal"] < current["ordinal"]])
    observed_final_ids: set[str] = set()
    for compaction in compactions:
        observed_final_ids.update(
            event_payload(event).get("id")
            for event in result_events
            if event["ordinal"] < compaction["ordinal"]
        )
        payload = event_payload(compaction)
        replacement_id = payload.get("replacement_message_id")
        if replacement_id is not None and replacement_id not in observed_final_ids:
            raise InspectionError("the compaction replacement identity conflicts with final output")
        history = payload.get("replacement_history", [])
        if not isinstance(history, list):
            raise InspectionError("the compaction replacement history is malformed")
        for item in history:
            if not isinstance(item, dict):
                raise InspectionError("the compaction replacement history is malformed")
            if item.get("role") == "assistant" and item.get("phase") == "final_answer":
                history_id = item.get("id")
                source = catalog.get(history_id) if isinstance(history_id, str) else None
                if source is None:
                    raise InspectionError("replacement history contains an unauthenticated final result")
                copied = message_text(item)
                if copied is not None and copied != source[1]:
                    raise InspectionError("replacement history changes the final result bytes")
                embedded = native_turn_id(item)
                if embedded is not None and embedded != source[0]:
                    raise InspectionError("replacement history changes the final result turn")
                if source[0] == turn_id and history_id not in observed_final_ids:
                    raise InspectionError("replacement history contains unbounded current-turn final output")

    delivery_states = [
        state
        for lower_bound, upper_bound in intervals
        for state in [delivered_results(
            events,
            lower_bound,
            upper_bound,
            reference,
            return_to_thread_id,
            turn_id,
        )]
    ]
    delivery_texts = [result for delivered, _failed in delivery_states for result in delivered]
    failed_delivery_texts = [result for _delivered, failed in delivery_states for result in failed]
    terminal_values = set(final_texts + delivery_texts + failed_delivery_texts)
    if len(terminal_values) > 1:
        raise InspectionError("the delivered and final result bytes differ")
    terminal = next(iter(terminal_values), None)
    if terminal is None:
        return {"schema_version": 1, "state": "continue", "action": "continue_role"}
    validate_role_result(terminal, role)
    action = "return_only" if delivery_texts or failed_delivery_texts else "deliver_then_return"
    return {
        "schema_version": 1,
        "state": "replay",
        "action": action,
        "result_text": terminal,
    }


def main(argv: list[str] | None = None) -> int:
    configure_utf8()
    try:
        args = parse_args(argv)
        if not re.fullmatch(r"[A-Za-z0-9._:-]{1,128}", args.delivery_reference):
            raise InspectionError("the delivery reference is invalid")
        if not re.fullmatch(r"[A-Za-z0-9._:-]{1,128}", args.return_to_thread_id):
            raise InspectionError("the return task identity is invalid")
        rollout = resolve_rollout(args)
        result = inspect(
            load_events(rollout),
            args.thread_id,
            args.role,
            args.delivery_reference,
            args.return_to_thread_id,
        )
    except InspectionError as error:
        result = {
            "schema_version": 1,
            "state": "blocked",
            "action": "return_blocked",
            "diagnostic": str(error),
        }
        sys.stdout.write(compact(result) + "\n")
        return 1
    except Exception as error:  # pragma: no cover - final containment boundary
        result = {
            "schema_version": 1,
            "state": "blocked",
            "action": "return_blocked",
            "diagnostic": f"native context inspection failed unexpectedly ({type(error).__name__})",
        }
        sys.stdout.write(compact(result) + "\n")
        return 2
    sys.stdout.write(compact(result) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
