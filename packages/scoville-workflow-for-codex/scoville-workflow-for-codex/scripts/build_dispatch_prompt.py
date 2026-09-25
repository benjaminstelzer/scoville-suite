#!/usr/bin/env python3
"""Build a complete single-unit assignment without transport receipts."""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from parse_role_result import validate_semantics


def select_unit(selector: Path, root: Path, unit: str) -> dict:
    if not re.fullmatch(r"W-[0-9]{3}(?:/step-[1-9][0-9]*)?", unit):
        raise ValueError("select one Work Item or one Step; Step ranges are not dispatch units")
    result = subprocess.run([sys.executable, "-B", str(selector), "--root", str(root),
                             "--unit", unit, "--format", "json"],
                            capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise ValueError("Plan selection failed: " + result.stdout + result.stderr)
    data = json.loads(result.stdout)
    if not isinstance(data, dict) or set(data) != {"plan", "work_item", "direct_dependencies", "decisions"}:
        raise ValueError("Plan selector returned an unsupported projection")
    item = data.get("work_item")
    if not isinstance(item, dict) or item.get("unit") != unit:
        raise ValueError("Plan selector returned another unit")
    if not isinstance(item.get("source_text"), str) or not item["source_text"]:
        raise ValueError("SELECTOR_INCOMPATIBLE: Plan must provide source_text")
    return data


def result_contract(role: str) -> list[str]:
    if role == "reviewer":
        return [
            "Return only this line format, without Markdown fences or extra lines:\nSCOVILLE_RESULT_V1\nrole=reviewer\nstatus=<value>\nsummary=<one line>\nfinding=<one line>",
            "Omit finding when there is none. Repeat only finding, after summary, for additional findings. Use at most eight finding lines.",
            "Status is pass, changes_requested, blocked, needs_user_decision, or context_handoff. Pass has no finding lines.",
            "Summary is 1 to 800 characters. Each finding is 1 to 400 characters. Combined summary and findings are at most 4000 characters. Keep every value on one line.",
            "For context_handoff, summary states completed effects, changed paths, decisive checks, unverified behavior, remaining work, and unresolved state. Findings contain only unresolved defects with location, mechanism, impact, and smallest fix. Include no Plan Evidence or work log.",
            "Before returning, check the header, role, field order, status, counts, and limits.",
        ]
    return [
        f"For completed, return only this line format, without Markdown fences or extra lines:\nSCOVILLE_RESULT_V1\nrole={role}\nstatus=completed\ncode_changed=<yes or no>\ncritical_docs_changed=<yes or no>\nsummary=<one line>\nfinding=<one line>",
        f"For blocked, needs_user_decision, or context_handoff, use:\nSCOVILLE_RESULT_V1\nrole={role}\nstatus=<value>\nsummary=<one line>\nfinding=<one line>",
        "Omit finding when there is none. Repeat only finding, after summary, for additional findings. Use at most eight finding lines.",
        'Set code_changed to "yes" only when the final result changes source, tests, executable scripts, build, deployment, runtime, configuration, or generated code.',
        'Set critical_docs_changed to "yes" only when changed documentation materially governs security, permissions, data handling, migrations, deployment, operations, public behavior, acceptance, or lifecycle behavior.',
        "Inspect the final result before setting review values. Do not infer them from labels, wording, activity, or route.",
        "For completed and context_handoff, summary states completed effects, changed paths, decisive checks, and unverified behavior. For completed, state none when no path changed or nothing remains unverified.",
        "Summary is 1 to 800 characters. Each finding is 1 to 400 characters. Combined summary and findings are at most 4000 characters. Keep every value on one line.",
        "For context_handoff, summary also states remaining work and unresolved state. Findings contain only unresolved defects with location, mechanism, impact, and smallest fix. Include no Plan Evidence or work log.",
        "Before returning, check the header, role, field order, status, counts, and limits.",
    ]



def build_prompt(role: str, workspace: Path, coordinator: str, reference: str,
                 context: dict, role_input: dict) -> str:
    allowed = {"context_handoff", "supplemental_context"}
    if role == "reviewer":
        allowed.add("executor_result")
        result = validate_semantics(role_input.get("executor_result", {}), "executor")
        if result["status"] != "completed":
            raise ValueError("review requires a completed executor or repair result")
    if role == "repair":
        allowed.update({"reviewer_result", "repair_assignment"})
        result = validate_semantics(role_input.get("reviewer_result", {}), "reviewer")
        if result["status"] != "changes_requested":
            raise ValueError("repair requires unresolved reviewer findings")
        assignment = role_input.get("repair_assignment", {}).get("finding_indices")
        if (not isinstance(assignment, list) or not assignment
                or any(type(i) is not int or i < 0 or i >= len(result["findings"]) for i in assignment)
                or assignment != sorted(set(assignment))):
            raise ValueError("repair_assignment must select existing unique finding_indices")
    if set(role_input) - allowed:
        raise ValueError("unknown role input")
    checkpoint = Path(__file__).with_name("check_context_checkpoint.py")
    lines = [f"scoville_role={role}", "dispatch_contract=SCOVILLE_DISPATCH_V1",
             f"workspace_root={workspace}", f"return_to_thread_id={coordinator}",
             f"delivery_reference={reference}",
             "Work only in the named workspace on this assigned unit. The coordinator owns Plan, Decision and index edits, staging and commits. Do not create tasks, change settings or dispatch other work.",
             ("Stay read-only. Review the actual scoped diff, assignment and named evidence." if role == "reviewer" else
              "Implement only the assigned work and its proportionate checks. Preserve unrelated changes. Follow repository instructions, including required backups."),
             "For repair, correct only repair_assignment findings. For inherited context_handoff, continue its unfinished work and preserve completed effects, unit, role and logical repair attempt.",
             "At natural boundaries while your own assigned work remains unfinished, run the bundled context checkpoint below. When your work and checks are complete, return the normal result for your role without another checkpoint: completed for executor/repair, pass or changes_requested for reviewer. The coordinator's later review and acceptance are not your unfinished work.",
             f'"{sys.executable}" "{checkpoint}" --role {role} --project-root "{workspace}"',
             "On context_handoff, save completed effects, current files, checks, unresolved facts and the next concrete action in the result. For executor or repair only, if needed, save the longer factual handoff as Markdown under .scoville/handoffs/<your-task-id>.md and name it in summary. Then end this task. The coordinator creates the successor after observing your completion. Do not continue writing.",
             "On unavailable telemetry, continue without inventing occupancy or claiming rollover. Invalid configuration or a failed helper stops the affected operation and returns blocked with the diagnostic.",
             "After compaction, recover this assignment and compare the actual files and retained checks with completed effects before continuing. Do not repeat completed work or treat compaction as a task handoff.",
             "Treat a user stop as immediate: make no further change, return the exact retained state and stop. A missing material choice returns needs_user_decision.",
             "Return the role result as your final answer. The coordinator collects that exact task's completion; do not send another delivery message.",
             "plan_context=" + json.dumps(context, ensure_ascii=False, separators=(",", ":")),
             "role_input=" + json.dumps(role_input, ensure_ascii=False, separators=(",", ":")),
             *result_contract(role)]
    return "\n".join(lines) + "\n"


def main() -> int:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selector", type=Path, required=True)
    parser.add_argument("--plan-root", type=Path, required=True)
    parser.add_argument("--unit", required=True)
    parser.add_argument("--role", choices=("executor", "reviewer", "repair"), required=True)
    parser.add_argument("--workspace-root", type=Path, required=True)
    parser.add_argument("--return-to-thread-id", required=True)
    parser.add_argument("--delivery-reference", required=True)
    args = parser.parse_args()
    try:
        if not args.workspace_root.is_absolute() or not args.workspace_root.is_dir():
            raise ValueError("workspace-root must be an existing absolute directory")
        if any(not value.strip() or "\n" in value or "\r" in value for value in
               (args.return_to_thread_id, args.delivery_reference)):
            raise ValueError("coordinator and reference must be nonempty single-line values")
        raw = sys.stdin.read()
        role_input = json.loads(raw) if raw.strip() else {}
        if not isinstance(role_input, dict):
            raise ValueError("stdin must contain a role-input object")
        context = select_unit(args.selector, args.plan_root, args.unit)
        sys.stdout.write(build_prompt(args.role, args.workspace_root, args.return_to_thread_id,
                                      args.delivery_reference, context, role_input))
        return 0
    except (OSError, ValueError, TypeError, AttributeError) as error:
        print(json.dumps({"valid": False, "diagnostic": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
