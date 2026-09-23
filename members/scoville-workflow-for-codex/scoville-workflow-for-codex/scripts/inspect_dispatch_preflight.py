#!/usr/bin/env python3
"""Check coordinator authority and select one bounded Work Item in one call."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


class HelperFailure(ValueError):
    def __init__(self, source: str, payload: dict) -> None:
        self.source = source
        self.payload = payload
        reason = payload.get("diagnostic") or payload.get("message") or payload.get("reason") or "nonzero exit"
        super().__init__(f"{source}: {reason}")


def call_json(command: list[str]) -> dict:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        detail = result.stderr.strip()[:300]
        suffix = f": {detail}" if detail else ""
        raise ValueError(f"{Path(command[1]).name} returned invalid JSON{suffix}") from error
    if not isinstance(payload, dict):
        raise ValueError(f"{Path(command[1]).name} returned a non-object result")
    if result.returncode != 0:
        raise HelperFailure(Path(command[1]).name, payload)
    return payload


def inspect(workspace: Path, plan_root: Path, selector: Path, workflow_id: str,
            revision: int, generation: int, work_item: str | None = None,
            runner=call_json) -> dict:
    contract_script = Path(__file__).with_name("manage_agents_contract.py")
    contract = runner([sys.executable, str(contract_script), "check", "--workspace", str(workspace)])
    if contract.get("installed") is not True:
        raise ValueError("project contract is not installed")
    guard_script = Path(__file__).with_name("manage_workflow_guard.py")
    guard_command = [sys.executable, str(guard_script), "verify", "--workspace", str(workspace),
                     "--expected-revision", str(revision), "--expected-generation", str(generation),
                     "--workflow-id", workflow_id, "--role", "coordinator", "--capability", "plan"]

    def verified_guard() -> dict:
        guard = runner(guard_command)
        if (guard.get("ok") is not True or guard.get("authorized") is not True
                or guard.get("workflow_id") != workflow_id or guard.get("revision") != revision
                or guard.get("generation") != generation):
            raise ValueError("coordinator guard is not authorized at the expected revision")
        return guard

    verified_guard()
    selection_command = [sys.executable, str(selector), "--root", str(plan_root), "--format", "json"]
    if work_item is not None:
        selection_command.extend(["--work-item", work_item])
    selection = runner(selection_command)
    if set(selection) != {"plan", "work_item", "direct_dependencies", "decisions"}:
        raise ValueError("selector did not return the four required semantic areas")
    verified_guard()
    return {"valid": True, "guard": {"workflow_id": workflow_id, "revision": revision,
                                      "generation": generation}, "selection": selection}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--plan-root", type=Path, required=True)
    parser.add_argument("--selector", type=Path, required=True)
    parser.add_argument("--workflow-id", required=True)
    parser.add_argument("--expected-revision", type=int, required=True)
    parser.add_argument("--expected-generation", type=int, required=True)
    parser.add_argument("--work-item")
    args = parser.parse_args()
    try:
        result = inspect(args.workspace, args.plan_root, args.selector, args.workflow_id,
                         args.expected_revision, args.expected_generation, args.work_item)
    except HelperFailure as error:
        print(json.dumps({"valid": False, "diagnostic": str(error), "source": error.source,
                          "source_result": error.payload}, ensure_ascii=False))
        return 1
    except (OSError, ValueError, UnicodeError, subprocess.SubprocessError) as error:
        print(json.dumps({"valid": False, "diagnostic": str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
