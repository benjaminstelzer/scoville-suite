#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import os
from pathlib import Path


TOP_LEVEL_KEYS = ["plan", "work_item", "direct_dependencies", "decisions"]
ROLE_INPUT_KEYS = {
    "executor": {"context_handoff"},
    "reviewer": {"executor_result", "context_handoff"},
    "repair": {"reviewer_result", "repair_assignment", "context_handoff"},
}


class PromptError(Exception):
    def __init__(self, code: str, message: str, *, exit_code: int = 1) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.exit_code = exit_code


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise PromptError("USAGE_ERROR", message, exit_code=2)


def parser() -> argparse.ArgumentParser:
    result = JsonArgumentParser(description="Build one deterministic Scoville Workflow child prompt.")
    result.add_argument("--selector", required=True, help="Loaded Scoville Plan select_context.py path.")
    result.add_argument("--plan-root", required=True, help="Canonical Scoville Plan profile root.")
    result.add_argument("--unit", required=True, help="Exact W-NNN, W-NNN/step-N, or W-NNN/steps-N-M unit.")
    result.add_argument("--role", choices=("executor", "reviewer", "repair"), required=True)
    result.add_argument("--workspace-root", required=True, help="Exact absolute shared workflow workspace.")
    result.add_argument("--return-to-thread-id", required=True, help="Exact coordinator task ID for result delivery.")
    result.add_argument("--delivery-reference", required=True, help="Unique result-delivery reference for this child turn.")
    result.add_argument("--guard-workflow-id", required=True, help="Exact active workflow guard identity.")
    result.add_argument("--guard-generation", required=True, type=int, help="Expected coordinator generation.")
    result.add_argument("--guard-revision", required=True, type=int, help="Expected guard revision for this assignment.")
    result.add_argument("--guard-dispatch-key", required=True, help="Pending writer or read-only dispatch identity.")
    result.add_argument("--guard-task-id", help="Exact activated writer task ID; required for executor and repair.")
    output = result.add_mutually_exclusive_group()
    output.add_argument("--transport-json", action="store_true", help="Envelope for execution-memory transport; do not print to chat.")
    output.add_argument("--binding-only", action="store_true", help="Fresh input digest without prompt generation.")
    result.add_argument("--transport-target", help="Writer thread ID or project:<saved-project-id> for reviewer creation.")
    return result


def compact(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def configure_utf8() -> None:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="strict")


def diagnostic(error: PromptError) -> str:
    return compact({"schema_version": 1, "valid": None, "diagnostics": [{"code": error.code, "message": error.message}]}) + "\n"


def validate_role_input(role: str, payload: object) -> dict[str, object]:
    if not isinstance(payload, dict):
        raise PromptError("ROLE_INPUT_INVALID", "stdin must contain one JSON object")
    unknown = set(payload) - ROLE_INPUT_KEYS[role]
    if unknown:
        raise PromptError("ROLE_INPUT_KEYS_INVALID", "stdin contains keys not permitted for this role")
    if any(not isinstance(value, dict) for value in payload.values()):
        raise PromptError("ROLE_INPUT_INVALID", "every role input value must be a JSON object")
    if role == "reviewer" and "executor_result" not in payload:
        raise PromptError("EXECUTOR_RESULT_REQUIRED", "reviewer prompt requires executor_result")
    if role == "repair" and "reviewer_result" not in payload:
        raise PromptError("REVIEWER_RESULT_REQUIRED", "repair prompt requires reviewer_result")
    if role == "repair":
        assignment = payload.get("repair_assignment")
        findings = payload.get("reviewer_result", {}).get("findings", [])
        if not isinstance(assignment, dict) or set(assignment) != {"finding_indices"}:
            raise PromptError("REPAIR_ASSIGNMENT_REQUIRED", "repair prompt requires finding_indices")
        indices = assignment["finding_indices"]
        if (
            not isinstance(indices, list)
            or not indices
            or any(not isinstance(index, int) or isinstance(index, bool) for index in indices)
            or indices != sorted(set(indices))
            or any(index < 0 or index >= len(findings) for index in indices)
        ):
            raise PromptError("REPAIR_ASSIGNMENT_INVALID", "repair finding_indices must select existing unique reviewer findings")
    return payload


def read_role_input(role: str) -> dict[str, object]:
    raw = sys.stdin.read()
    if not raw.strip():
        payload: object = {}
    else:
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as error:
            raise PromptError("ROLE_INPUT_INVALID", "stdin must contain one JSON object") from error
    return validate_role_input(role, payload)


def validate_plan_context(payload: object, unit: str) -> dict[str, object]:
    if not isinstance(payload, dict) or list(payload) != TOP_LEVEL_KEYS:
        raise PromptError("SELECTOR_SHAPE_INVALID", "selector success must contain the four ordered semantic areas")
    work_item = payload.get("work_item")
    if not isinstance(work_item, dict) or work_item.get("unit") != unit:
        raise PromptError("SELECTOR_UNIT_INVALID", "selector did not return the exact requested unit")
    if "evidence" in {str(key).lower() for key in work_item}:
        raise PromptError("SELECTOR_EVIDENCE_FORBIDDEN", "dispatch unit must not contain Work Item Evidence")
    if not isinstance(payload.get("decisions"), list):
        raise PromptError("SELECTOR_DECISIONS_INVALID", "selector decisions must be a list")
    return payload


def validate_prompt_arguments(
    role: str,
    workspace_root: str,
    return_to_thread_id: str,
    delivery_reference: str,
    guard_workflow_id: str,
    guard_generation: int,
    guard_revision: int,
    guard_dispatch_key: str,
    guard_task_id: str | None,
) -> None:
    if role not in ROLE_INPUT_KEYS:
        raise PromptError("ROLE_INVALID", "prompt role is unsupported", exit_code=2)
    if not Path(workspace_root).is_absolute():
        raise PromptError("WORKSPACE_ROOT_INVALID", "--workspace-root must be absolute", exit_code=2)
    checks = (
        (return_to_thread_id, 128, "RETURN_THREAD_ID_INVALID", "--return-to-thread-id has an invalid shape"),
        (delivery_reference, 128, "DELIVERY_REFERENCE_INVALID", "--delivery-reference has an invalid shape"),
        (guard_workflow_id, 160, "GUARD_WORKFLOW_ID_INVALID", "--guard-workflow-id has an invalid shape"),
        (guard_dispatch_key, 160, "GUARD_DISPATCH_KEY_INVALID", "--guard-dispatch-key has an invalid shape"),
    )
    for value, maximum, code, message in checks:
        if not isinstance(value, str) or not re.fullmatch(rf"[A-Za-z0-9._:-]{{1,{maximum}}}", value):
            raise PromptError(code, message, exit_code=2)
    if type(guard_generation) is not int or guard_generation < 0:
        raise PromptError("GUARD_GENERATION_INVALID", "--guard-generation must be non-negative", exit_code=2)
    if type(guard_revision) is not int or guard_revision < 0:
        raise PromptError("GUARD_REVISION_INVALID", "--guard-revision must be non-negative", exit_code=2)
    if role in {"executor", "repair"}:
        if not isinstance(guard_task_id, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,160}", guard_task_id):
            raise PromptError("GUARD_TASK_ID_INVALID", "--guard-task-id is required for executor and repair", exit_code=2)
    elif guard_task_id is not None:
        raise PromptError("GUARD_TASK_ID_INVALID", "--guard-task-id is not permitted for reviewer", exit_code=2)


def select_unit(selector_value: str, plan_root: str, unit: str) -> dict[str, object]:
    selector = Path(selector_value)
    if not selector.is_file():
        raise PromptError("SELECTOR_MISSING", "--selector must name an existing regular file", exit_code=2)
    environment = dict(os.environ)
    environment["PYTHONUTF8"] = "1"
    environment["PYTHONIOENCODING"] = "utf-8"
    completed = subprocess.run(
        [
            sys.executable,
            "-B",
            str(selector),
            "--root",
            plan_root,
            "--unit",
            unit,
            "--format",
            "json",
        ],
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=False,
        env=environment,
    )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        raise PromptError("SELECTOR_OUTPUT_INVALID", "selector did not return one JSON object") from error
    if completed.returncode != 0:
        raise PromptError("SELECTOR_FAILED", compact(payload))
    return validate_plan_context(payload, unit)


def result_contract(role: str) -> list[str]:
    if role == "reviewer":
        return [
            "Return one compact JSON object only with exactly status, summary, findings.",
            "Allowed status values: pass, changes_requested, blocked, needs_user_decision, context_handoff.",
            "For pass, findings must be empty. Summary is at most 800 characters; findings contains at most eight strings of at most 400 characters each; combined prose is at most 4000 characters.",
            "For context_handoff, summary names completed effects, changed paths, decisive checks, unverified behavior, remaining work, and unresolved state. Findings contain only unresolved defects with location, mechanism, impact, and smallest fix. Do not copy Plan Evidence or a work log.",
            "Before delivery, parse the finished JSON and verify that it is one complete object with exactly the required keys, allowed status, field types, and limits above; correct any failure before sending.",
        ]
    return [
        "Return one compact JSON object only with exactly status, summary, review, findings.",
        "Allowed status values: completed, blocked, needs_user_decision, context_handoff.",
        'For completed, review has exactly code_changed and critical_docs_changed; each value is the JSON string "yes" or "no". Otherwise review is null.',
        'Set code_changed to "yes" for changes to source, tests, executable scripts, build, deployment, runtime, configuration, or generated-code artifacts; otherwise set it to "no".',
        'Set critical_docs_changed to "yes" when changed documentation materially governs security, permissions, data handling, migrations, deployment, operations, public behavior, or required acceptance or lifecycle behavior; otherwise set it to "no".',
        "Inspect the actual final changed result before setting either value; never infer it from the unit title, Step wording, activity name, or route class.",
        "For completed, summary names completed effects, changed paths, decisive checks, and any unverified behavior. State none explicitly when there is no changed path or unverified behavior.",
        "Summary is at most 800 characters; findings contains at most eight strings of at most 400 characters each; combined prose is at most 4000 characters.",
        "For context_handoff, summary names completed effects, changed paths, decisive checks, unverified behavior, remaining work, and unresolved state. Findings contain only unresolved defects with location, mechanism, impact, and smallest fix. Do not copy Plan Evidence or a work log.",
        "Before delivery, parse the finished JSON and verify that it is one complete object with exactly the required keys, allowed status, field types, and limits above; correct any failure before sending.",
    ]


def context_safety_contract(
    inspector: str,
    role: str,
    delivery_reference: str,
    return_to_thread_id: str,
) -> list[str]:
    return [
        "First run the read-only gate below, before project access. Repeat it after host compaction. Use the shell tool for this command. Section 6 restricts only final delivery, not gate or work tool calls.",
        f"Run `python {json.dumps(inspector)} --role {role} --delivery-reference {delivery_reference} --return-to-thread-id {return_to_thread_id}`. It selects only the active rollout bound to your exact CODEX_THREAD_ID; never inspect another task or select by recency.",
        "IF its action is continue_role, continue this unchanged role. IF its action is deliver_then_return, deliver result_text once under the current reference and return the identical result_text. IF its action is return_only, return result_text without another delivery. IF it returns return_blocked or cannot run, perform no project action and return a schema-valid blocked result naming only this gate failure.",
        "A supplied context_handoff is inherited continuation input. It is never your own terminal result and never satisfies this gate.",
        f'At a natural internal boundary with material work remaining, run `python "{Path(__file__).with_name("check_context_checkpoint.py").resolve()}" --role {role}` once. It reads only your exact native rollout and calculates the role threshold; do not search rollout files or calculate occupancy yourself.',
        "The helper reads assets/workflow.toml context.worker_percent from its installed Skill on each call. If action is context_handoff, return context_handoff in the normal role schema. If action is continue, continue this unit. If action is blocked, return a schema-valid blocked result with its configuration diagnostic; do not substitute a threshold. Unavailable telemetry or an unavailable helper alone does not block work or create a successor; continue unless an independently observed host failure blocks progress. Do not poll this helper. This checkpoint does not replace the post-compaction terminal gate above.",
    ]


def result_delivery_contract(return_to_thread_id: str, delivery_reference: str) -> list[str]:
    return [
        f"return_to_thread_id={return_to_thread_id}",
        f"delivery_reference={delivery_reference}",
        "Apply this section only after work ends or the gate requests delivery. Until then, use the tools needed for the gate and authorized work. Do not deliver merely because the gate has not yet been run.",
        f"After constructing your final role JSON, call send_message_to_thread exactly once through functions.exec. Its complete JavaScript must have this exact shape with no other code: `const r=await tools.mcp__codex_app__send_message_to_thread({{\"threadId\":\"{return_to_thread_id}\",\"prompt\":\"...\"}});for(const c of(r.content??[])){{if(c.type===\"text\")text(c.text);}}`. Replace only the JSON prompt string. The object contains only threadId and prompt; both are inline JSON strings, never variables, concatenation, or templates. Put `workflow_result_delivery={delivery_reference}` on the first decoded prompt line and the exact JSON bytes on the second line. This delivery is the only authorized message to another task. The only exception is a native-context action of return_only, whose single delivery attempt already settled successfully or with a definite failure.",
        "After the delivery call, perform no project, Plan, Decision, Git, write, delegation, review, publication, selector, or raw-Plan action. If the call succeeds, return the identical JSON bytes as your own final response. If it definitively fails or is rejected, do not retry; still return the identical JSON bytes so the coordinator's exact-child wait can recover them. If the call remains waitingOnApproval, wait for that same call to resolve before returning.",
    ]


def build_prompt(
    role: str,
    unit: str,
    workspace_root: str,
    return_to_thread_id: str,
    delivery_reference: str,
    native_context_inspector: str,
    guard_workflow_id: str,
    guard_generation: int,
    guard_revision: int,
    guard_dispatch_key: str,
    guard_task_id: str | None,
    plan_context: dict[str, object],
    role_input: dict[str, object],
) -> str:
    lines = [
        f"scoville_role={role}",
        "dispatch_contract=scoville-workflow-v1",
        f"unit={unit}",
        f"workspace_root={workspace_root}",
        "guard_path=.scoville-workflow/guard.json",
        f"guard_workflow_id={guard_workflow_id}",
        f"guard_generation={guard_generation}",
        f"guard_revision={guard_revision}",
        f"guard_dispatch_key={guard_dispatch_key}",
        f"guard_task_id={guard_task_id if guard_task_id is not None else 'read_only'}",
        f"guard_helper={Path(__file__).with_name('manage_workflow_guard.py').resolve()}",
        "[1 Native context gate]",
    ]
    lines.extend(context_safety_contract(
        native_context_inspector,
        role,
        delivery_reference,
        return_to_thread_id,
    ))
    lines.extend([
        "[2 Role and authority]",
        "Verify that the exact current working directory equals workspace_root before project access; on mismatch return needs_user_decision and use no other workspace.",
        "Do not load or use Scoville Plan, the Scoville Workflow Codex launcher Skill, or Scoville Handoff. Do not run select_context.py or build_dispatch_prompt.py and do not read or edit canonical Plan or Decision files; plan_context below is the complete planning input.",
        "Follow repository instructions and applicable Skills under their normal trigger rules. Do not delegate or split the unit by activity.",
        "Never stage, commit, push, or rewrite Git history.",
        "Never reset, stash, discard, or revert unrelated or user work. Preserve every existing change and commit.",
    ])
    if role == "reviewer":
        lines.append("Remain read-only. Run guard_helper with `verify --workspace workspace_root --workflow-id guard_workflow_id --expected-revision guard_revision --expected-generation guard_generation --role reviewer --capability read_only`; require a successful read_only result, then review only the exact unit result against plan_context, executor_result, the scoped workspace diff, and directly relevant validation evidence.")
    else:
        lines.append("This assignment is the activation message. Require your exact runtime CODEX_THREAD_ID to equal guard_task_id. Before every project write, run guard_helper with `verify --workspace workspace_root --workflow-id guard_workflow_id --expected-revision guard_revision --expected-generation guard_generation --role <executor|repair> --capability source --unit unit --dispatch-key guard_dispatch_key`; proceed only when the response is successful and authorized is true. Pending, missing, unreadable, stale, or mismatched state blocks writes.")
        lines.append("Plan and Decision records remain read-only; external publication requires explicit authorization in plan_context.")
    lines.append("[3 Continuation inputs]")
    if "context_handoff" in role_input:
        lines.extend([
            "The supplied context_handoff is predecessor continuation input, never your own terminal result. Continue the remaining role work before returning any result.",
            "If you later return context_handoff, its summary must contain `progress_after_dispatch=<newly completed unit action>; evidence=<new observation>` for work performed after this dispatch. Copied, reworded, re-identified, or own-final-message-only predecessor content is not progress; return blocked or needs_user_decision when no new progress is possible.",
        ])
    if role == "repair":
        lines.append("Correct only the reviewer findings selected by repair_assignment.finding_indices. Preserve the complete reviewer_result as review context; do not repeat accepted unit effects or attempt coordinator-owned Plan corrections.")
    lines.append("[4 Work]")
    lines.append("Perform the authorized role work now. Do not infer omitted work from prior Steps or chat history. If the host denies required project, tool, or network access, stop and return a schema-valid blocked result that names the denied operation and observed error.")
    lines.append("[5 Result]")
    lines.extend(result_contract(role))
    lines.append("[6 Delivery]")
    lines.extend(result_delivery_contract(return_to_thread_id, delivery_reference))
    lines.append("[Inputs]")
    lines.append("plan_context=" + compact(plan_context))
    for key in ("executor_result", "reviewer_result", "repair_assignment", "context_handoff"):
        if key in role_input:
            lines.append(key + "=" + compact(role_input[key]))
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    configure_utf8()
    try:
        args = parser().parse_args(argv)
        workspace_root = Path(args.workspace_root)
        validate_prompt_arguments(
            args.role, str(workspace_root), args.return_to_thread_id,
            args.delivery_reference, args.guard_workflow_id,
            args.guard_generation, args.guard_revision,
            args.guard_dispatch_key, args.guard_task_id,
        )
        role_input = read_role_input(args.role)
        plan_context = select_unit(args.selector, args.plan_root, args.unit)
        binding_input = {key: value for key, value in vars(args).items()
                         if key not in {"transport_json", "binding_only", "transport_target"}}
        binding_input.update(plan_context=plan_context, role_input=role_input,
                             builder_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                             selector_sha256=hashlib.sha256(Path(args.selector).read_bytes()).hexdigest())
        binding = hashlib.sha256(compact(binding_input).encode("utf-8")).hexdigest()
        if args.binding_only:
            sys.stdout.write(compact({"binding": binding}) + "\n")
            return 0
        if args.transport_json:
            expected_target = args.guard_task_id if args.role != "reviewer" else args.transport_target
            if not expected_target or args.transport_target != expected_target or (
                args.role == "reviewer" and not expected_target.startswith("project:")
            ):
                raise PromptError("TRANSPORT_TARGET_INVALID", "use the exact writer ID or project:<saved-project-id>", exit_code=2)
        prompt = build_prompt(
            args.role,
            args.unit,
            str(workspace_root),
            args.return_to_thread_id,
            args.delivery_reference,
            str(Path(__file__).with_name("inspect_native_context.py").resolve()),
            args.guard_workflow_id,
            args.guard_generation,
            args.guard_revision,
            args.guard_dispatch_key,
            args.guard_task_id,
            plan_context,
            role_input,
        )
    except PromptError as error:
        sys.stdout.write(diagnostic(error))
        return error.exit_code
    except Exception as error:  # pragma: no cover - final containment boundary
        internal = PromptError("PROMPT_BUILDER_INTERNAL_ERROR", f"prompt builder failed unexpectedly ({type(error).__name__})", exit_code=3)
        sys.stdout.write(diagnostic(internal))
        return 3
    if args.transport_json:
        sys.stdout.write(compact({
            "prompt": prompt, "binding": binding,
            "guard": {"workflow_id": args.guard_workflow_id, "generation": args.guard_generation,
                      "revision": args.guard_revision, "unit": args.unit,
                      "dispatch_key": args.guard_dispatch_key},
            "receipt": {"target": args.transport_target, "role": args.role,
                        "reference": args.delivery_reference,
                        "characters": len(prompt), "bytes": len(prompt.encode("utf-8")),
                        "sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest()},
        }) + "\n")
    else:
        sys.stdout.write(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
