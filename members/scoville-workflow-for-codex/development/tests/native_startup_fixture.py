"""Native host records for guard integration tests; no production bypass flags."""
import importlib.util
import json


def contract_module(package):
    spec = importlib.util.spec_from_file_location("tested_coordinator_contract", package / "scripts/coordinator_contract.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_native(home, identity, prompt, parent="launcher-1", source="agent_created_thread"):
    path = home / "sessions" / ("rollout-" + identity + ".jsonl")
    path.parent.mkdir(parents=True, exist_ok=True)
    events = [
        {"ordinal": 0, "type": "session_meta", "payload": {"session_id": identity, "thread_source": source}},
        {"ordinal": 1, "type": "response_item", "payload": {
            "type": "function_call_output", "name": "create_thread", "namespace": "codex_app",
            "output": "<codex_delegation>\n<source_thread_id>" + parent + "</source_thread_id>\n<input>"
                      + prompt + "</input>\n</codex_delegation>"}},
    ]
    path.write_text("\n".join(json.dumps(event) for event in events) + "\n", encoding="utf-8")
    return path


def supply_native_startup(package, workspace, actor, arguments):
    home = workspace / ".test-host"
    path = home / "sessions" / ("rollout-" + actor + ".jsonl")
    guard_path = workspace / ".scoville-workflow/guard.json"
    guard = json.loads(guard_path.read_text()) if guard_path.exists() else None
    if actor.startswith("coordinator-") and not path.exists():
        prompt = ("scoville_role=coordinator\ncoordinator_start=initial_parking\n"
                  "workspace_root=" + str(workspace) + "\nworkflow_id=" + guard["workflow_id"] + "\n")
        write_native(home, actor, contract_module(package).build_prompt(prompt, package))
    if arguments[0] == "reconcile-writer" and guard and guard.get("writer"):
        identity = arguments[arguments.index("--task-id") + 1]
        writer = guard["writer"]
        prompt = ("scoville_role=" + writer["role"] + "\nunit=" + writer["unit"]
                  + "\nworkspace_root=" + str(workspace) + "\nworkflow_id=" + guard["workflow_id"]
                  + "\ndispatch_key=" + writer["dispatch_key"] + "\n")
        write_native(home, identity, prompt, actor)
    return home
