from pathlib import Path
import hashlib
import html
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[2]
# Exercise the actual package, including bundled shared helpers and defaults.
SUITE_ROOT = ROOT.parents[1]
_build_spec = importlib.util.spec_from_file_location("workflow_test_build", SUITE_ROOT / "development/build_suite.py")
_builder = importlib.util.module_from_spec(_build_spec)
_build_spec.loader.exec_module(_builder)
_test_package = tempfile.TemporaryDirectory(prefix="workflow-tests-", ignore_cleanup_errors=True)
PACKAGE = Path(_test_package.name) / "scoville-workflow-for-codex"
_config = _builder.load(SUITE_ROOT, 'codex')
_member = next(m for m in _config['members'] if m['name'] == PACKAGE.name)
for _name, _data in _builder.payload(SUITE_ROOT, _member, _config).items():
    _target = Path(_test_package.name) / _name
    _target.parent.mkdir(parents=True, exist_ok=True)
    _target.write_bytes(_data)
SKILL = PACKAGE / "SKILL.md"
OPERATIONS = PACKAGE / "references" / "operations.md"
NATIVE_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "native-rollout-cases.json"
PROMPT_BUILDER = PACKAGE / "scripts" / "build_dispatch_prompt.py"
MODEL_RESOLVER = PACKAGE / "scripts" / "resolve_model_pair.py"
DISPATCH_PREFLIGHT = PACKAGE / "scripts" / "inspect_dispatch_preflight.py"
NATIVE_INSPECTOR = PACKAGE / "scripts" / "inspect_native_context.py"
ROLE_RESULT_PARSER = PACKAGE / "scripts" / "parse_role_result.py"
ROLLOVER_READINESS = ROOT.parents[1].parent / "shared" / "runtime" / "rollover_readiness.md"
AGENTS_CONTRACT = PACKAGE / "references" / "agents-contract.md"
AGENTS_HELPER = PACKAGE / "scripts" / "manage_agents_contract.py"
GUARD_HELPER = PACKAGE / "scripts" / "manage_workflow_guard.py"
ROUTE_CLASSES = {"ultra_low", "low", "medium", "high", "ultra_high"}
SUPPORTED_MODELS = {"gpt-6-luna", "gpt-6-sol", "gpt-6-astra"}
SUPPORTED_EFFORTS = {"low", "medium", "high", "xhigh"}

_resolver_spec = importlib.util.spec_from_file_location("workflow_model_resolver", MODEL_RESOLVER)
model_resolver = importlib.util.module_from_spec(_resolver_spec)
_resolver_spec.loader.exec_module(model_resolver)
_preflight_spec = importlib.util.spec_from_file_location("workflow_dispatch_preflight", DISPATCH_PREFLIGHT)
dispatch_preflight = importlib.util.module_from_spec(_preflight_spec)
_preflight_spec.loader.exec_module(dispatch_preflight)
_result_spec = importlib.util.spec_from_file_location("workflow_role_result", ROLE_RESULT_PARSER)
role_result_parser = importlib.util.module_from_spec(_result_spec)
_result_spec.loader.exec_module(role_result_parser)


def contract_text(path: Path) -> str:
    if path == OPERATIONS:
        return path.read_text(encoding="utf-8") + "\n" + "\n".join(
            part.read_text(encoding="utf-8") for part in sorted(path.parent.glob("operations-*.md")))
    return path.read_text(encoding="utf-8")


def flat(path: Path) -> str:
    return " ".join(contract_text(path).split())


def markdown_table(path: Path, heading: str) -> dict[str, tuple[str, ...]]:
    lines = contract_text(path).splitlines()
    start = lines.index(heading) + 1
    rows = {}
    for line in lines[start:]:
        if line.startswith("#"):
            break
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells[0] in {"Route", "Scenario", "State", "Transition", "Inspected interval", "Event while child is active"} or set(cells[0]) == {"-"}:
            continue
        rows[cells[0]] = tuple(cells[1:])
    return rows


def level_two_headings(path: Path) -> list[str]:
    return [
        line[3:]
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("## ")
    ]


def model_create_call(config, role, route=None, override=None, launched=None, repair_number=1):
    if role == "coordinator":
        selected = config["coordinator"]
        return {
            "title": selected["title"],
            "model": selected["model"],
            "thinking": selected["reasoning"],
        }
    if role == "rollover":
        if launched is None:
            raise ValueError("launched pair required")
        return {"model": launched["model"], "thinking": launched["thinking"]}
    pair = model_resolver.resolve(
        config, role, route,
        override_model=(override or {}).get("model"),
        override_reasoning=(override or {}).get("reasoning"),
        original_model=(launched or {}).get("model"),
        original_reasoning=(launched or {}).get("thinking"),
        repair_number=repair_number if role == "repair" else None,
    )
    if pair["model"] not in SUPPORTED_MODELS:
        raise ValueError("unsupported pair")
    return {"model": pair["model"], "thinking": pair["thinking"]}


def validate_event_stream(fixture):
    if fixture.get("fixture_kind") != "sanitized_minimal_native_projection":
        raise ValueError("unknown fixture shape")
    if fixture.get("rollout_count") != 1:
        raise ValueError("wrong rollout count")
    events = fixture.get("events")
    if not isinstance(events, list) or not events:
        raise ValueError("missing events")
    ordinals = [event.get("ordinal") for event in events]
    if any(not isinstance(ordinal, int) for ordinal in ordinals):
        raise ValueError("invalid ordinal")
    if ordinals != sorted(ordinals) or len(ordinals) != len(set(ordinals)):
        raise ValueError("duplicate or unordered ordinal")
    session_meta = [event for event in events if event.get("record_type") == "session_meta"]
    if len(session_meta) != 1 or session_meta[0].get("session_id") != fixture.get("session_id"):
        raise ValueError("wrong session metadata")
    if any(
        event.get("thread_id") not in {None, fixture["session_id"]}
        for event in events
    ):
        raise ValueError("contradictory event session")
    active_turn = None
    for event in events:
        payload_type = event.get("payload_type")
        if payload_type == "task_started":
            turn_id = event.get("turn_id")
            if active_turn is not None or not isinstance(turn_id, str) or not turn_id:
                raise ValueError("overlapping or unidentified turn")
            active_turn = turn_id
        elif payload_type in {"task_complete", "task_failed", "task_aborted"}:
            if active_turn is None or event.get("turn_id") != active_turn:
                raise ValueError("contradictory turn termination")
            active_turn = None
    return events


def parse_role_payload(raw, role):
    return role_result_parser.parse_role_result(raw, role)


def recover_completed_api_payload(case, role="executor"):
    wait = case["wait"]
    read = case["read"]
    if wait.get("status") != "completed":
        raise ValueError("wait result is not completed")
    try:
        return "wait", parse_role_payload(wait["message"], role)
    except (TypeError, ValueError):
        pass
    identity_keys = ("task_id", "host_id", "turn_id")
    if any(wait.get(key) != read.get(key) for key in identity_keys):
        raise ValueError("read result identity mismatch")
    if wait.get("message_id") is not None and read.get("message_id") != wait["message_id"]:
        raise ValueError("read result message mismatch")
    return "read", parse_role_payload(read["message"], role)


def classify_projection_recovery_fixture(case, role="reviewer"):
    """Model only the written recovery contract for deterministic test fixtures.

    This does not invoke or stand in for a production recovery helper.
    """
    wait = case["wait"]
    read = case["read"]
    delivery = case["delivery"]
    expected_identity = case["expected_identity"]
    if wait.get("status") != "completed" or delivery.get("authenticated") is not True:
        raise ValueError("recovery authority is not established")
    identity_keys = ("task_id", "host_id", "turn_id", "message_id")
    for key in identity_keys:
        expected = expected_identity.get(key)
        if not isinstance(expected, str) or not expected:
            raise ValueError("expected completed identity is missing")
        if wait.get(key) != expected or read.get(key) != expected:
            raise ValueError("read result identity mismatch")
    if delivery.get("source_task_id") != expected_identity["task_id"]:
        raise ValueError("delivery source mismatch")
    for key in ("delivery_reference", "dispatch_key"):
        expected = expected_identity.get(key)
        if not isinstance(expected, str) or not expected:
            raise ValueError("expected dispatch identity is missing")
        if delivery.get(key) != expected:
            raise ValueError("dispatch identity mismatch")
    if wait.get("truncated") is True or read.get("truncated") is True or delivery.get("truncated") is True:
        raise ValueError("truncated result")
    if wait.get("message") == delivery.get("message"):
        return {
            "action": "accept_wait",
            "source": "wait",
            "payload": parse_role_payload(wait["message"], role),
            "recovery_reads": 0,
        }
    if read.get("message") != delivery.get("message"):
        raise ValueError("source-delivery conflict")
    return {
        "action": "recover_source",
        "source": "delivery",
        "payload": parse_role_payload(read["message"], role),
        "recovery_reads": 1,
    }


def classify_post_compaction(case, role="executor"):
    try:
        events = validate_event_stream(case)
    except ValueError:
        return "unavailable", None
    turn_id = case["turn_id"]
    starts = [
        event
        for event in events
        if event.get("record_type") == "event_msg"
        and event.get("payload_type") == "task_started"
        and event.get("turn_id") == turn_id
    ]
    if len(starts) != 1:
        return "unavailable", None
    compacted_events = [event for event in events if event.get("record_type") == "compacted"]
    if len(compacted_events) != 1:
        return "unavailable", None
    compacted = compacted_events[0]
    prior_contexts = [
        event
        for event in events
        if event.get("record_type") == "turn_context"
        and event.get("turn_id") == turn_id
        and event["ordinal"] < compacted["ordinal"]
    ]
    post_contexts = [
        event
        for event in events
        if event.get("record_type") == "turn_context"
        and event.get("turn_id") == turn_id
        and event["ordinal"] > compacted["ordinal"]
    ]
    if not prior_contexts or len(post_contexts) != 1:
        return "unavailable", None
    prior_context = max(prior_contexts, key=lambda event: event["ordinal"])
    post_context = post_contexts[0]
    if not starts[0]["ordinal"] < prior_context["ordinal"] < compacted["ordinal"] < post_context["ordinal"]:
        return "unavailable", None
    complete_bound = [
        event for event in events
        if starts[0]["ordinal"] <= event["ordinal"] <= post_context["ordinal"]
    ]
    if any(
        (
            event.get("payload_type") == "task_started"
            and event["ordinal"] != starts[0]["ordinal"]
        )
        or event.get("payload_type") in {"task_failed", "task_aborted", "task_complete"}
        or (
            event.get("record_type") == "turn_context"
            and event.get("turn_id") != turn_id
        )
        or (
            event.get("turn_id") is not None
            and event.get("turn_id") != turn_id
        )
        for event in complete_bound
    ):
        return "unavailable", None
    interval = [
        event for event in complete_bound
        if prior_context["ordinal"] < event["ordinal"] < compacted["ordinal"]
    ]
    message_bound = [
        event for event in complete_bound
        if prior_context["ordinal"] < event["ordinal"] < post_context["ordinal"]
    ]
    all_finals = [
        event
        for event in complete_bound
        if event.get("record_type") == "response_item"
        and event.get("payload_type") == "message"
        and event.get("phase") == "final_answer"
    ]
    finals = [
        event
        for event in interval
        if event.get("record_type") == "response_item"
        and event.get("payload_type") == "message"
        and event.get("phase") == "final_answer"
    ]
    if len(all_finals) != len(finals) or len(finals) > 1:
        return "unavailable", None
    all_mirrors = [
        event
        for event in complete_bound
        if event.get("record_type") == "event_msg"
        and event.get("payload_type") == "item_completed"
        and event.get("item_type") == "AgentMessage"
    ]
    mirrors = [
        event
        for event in message_bound
        if event.get("record_type") == "event_msg"
        and event.get("payload_type") == "item_completed"
        and event.get("item_type") == "AgentMessage"
    ]
    replacement_id = compacted.get("replacement_message_id")
    if (
        len(all_mirrors) != len(mirrors)
        or len(mirrors) > 1
        or (not finals and (mirrors or replacement_id is not None))
    ):
        return "unavailable", None
    if not finals:
        return "no_handoff", None
    final = finals[0]
    if (
        not isinstance(final.get("message_id"), str)
        or not final["message_id"]
        or final.get("role") != "assistant"
        or final.get("embedded_turn_id", turn_id) != turn_id
    ):
        return "unavailable", None
    if mirrors:
        mirror = mirrors[0]
        if (
            mirror.get("turn_id") != turn_id
            or mirror.get("thread_id") != case["session_id"]
            or mirror.get("phase") != "final_answer"
            or mirror.get("item_id") != final.get("message_id")
        ):
            return "unavailable", None
    if replacement_id is not None and replacement_id != final.get("message_id"):
        return "unavailable", None
    try:
        payload = parse_role_payload(final["bytes"], role)
    except (json.JSONDecodeError, TypeError, ValueError):
        return "unavailable", None
    if payload["status"] != "context_handoff":
        return "no_handoff", None
    return "terminal_handoff", final["bytes"]


def recover_exact_rollout_turn(expected_session_id, fixture, turn, role="executor"):
    if fixture.get("session_id") != expected_session_id:
        raise ValueError("wrong or duplicate rollout")
    events = validate_event_stream(fixture)
    if turn["wait_status"] != "completed" or turn["wait_message"] is not None or turn["read_message"] is not None:
        raise ValueError("rollout recovery not eligible")
    turn_id = turn["turn_id"]
    starts = [
        event for event in events
        if event.get("record_type") == "event_msg"
        and event.get("payload_type") == "task_started"
        and event.get("turn_id") == turn_id
    ]
    completions = [
        event for event in events
        if event.get("record_type") == "event_msg"
        and event.get("payload_type") == "task_complete"
        and event.get("turn_id") == turn_id
    ]
    if len(starts) != 1 or len(completions) != 1:
        raise ValueError("ambiguous or failed turn bounds")
    start = starts[0]["ordinal"]
    completion = completions[0]["ordinal"]
    if start >= completion:
        raise ValueError("invalid turn ordering")
    bound = [event for event in events if start <= event["ordinal"] <= completion]
    if any(
        (
            event.get("payload_type") == "task_started"
            and event["ordinal"] != start
        )
        or event.get("payload_type") in {"task_failed", "task_aborted"}
        or (
            event.get("record_type") == "turn_context"
            and event.get("turn_id") != turn_id
        )
        for event in bound
    ):
        raise ValueError("contradictory turn activity")
    contexts = [
        event for event in bound
        if event.get("record_type") == "turn_context"
        and event.get("turn_id") == turn_id
        and start < event["ordinal"] < completion
    ]
    mirrors = [
        event for event in bound
        if event.get("record_type") == "event_msg"
        and event.get("payload_type") == "item_completed"
        and event.get("item_type") == "AgentMessage"
    ]
    finals = [
        event for event in bound
        if event.get("record_type") == "response_item"
        and event.get("payload_type") == "message"
        and event.get("phase") == "final_answer"
    ]
    if not contexts or len(mirrors) != 1 or len(finals) != 1:
        raise ValueError("ambiguous turn payload")
    latest_context = max(contexts, key=lambda event: event["ordinal"])
    mirror = mirrors[0]
    final = finals[0]
    if (
        mirror.get("thread_id") != expected_session_id
        or mirror.get("turn_id") != turn_id
        or mirror.get("phase") != "final_answer"
        or final.get("role") != "assistant"
        or final.get("embedded_turn_id", turn_id) != turn_id
        or mirror.get("item_id") != final.get("message_id")
        or not latest_context["ordinal"] < mirror["ordinal"] < final["ordinal"] < completion
    ):
        raise ValueError("ambiguous message identity")
    replacement_ids = {
        event.get("message_id")
        for event in bound
        if event.get("record_type") == "replacement_message"
    }
    if replacement_ids - {final["message_id"]}:
        raise ValueError("conflicting replacement message")
    parse_role_payload(final["bytes"], role)
    newer_activity = any(event["ordinal"] > completion for event in events)
    return {
        "session_id": expected_session_id,
        "turn_id": turn_id,
        "message_id": final["message_id"],
        "requires_reconcile": newer_activity,
    }


class NativeWorkflowContractTests(unittest.TestCase):
    def test_package_has_no_cli_runtime(self):
        self.assertEqual(
            [
                "build_dispatch_prompt.py",
                "check_context_checkpoint.py",
                "coordinator_contract.py",
                "dispatch_transport.js",
                "inspect_dispatch_preflight.py",
                "inspect_native_context.py",
                "manage_agents_contract.py",
                "manage_workflow_guard.py",
                "parse_role_result.py",
                "resolve_model_pair.py",
                "resolve_prompt_profile.py",
                "rollover_readiness.md",
                "task_lifecycle.md",
                "task_lifecycle.py",
            ],
            sorted(path.name for path in (PACKAGE / "scripts").iterdir() if path.is_file()),
        )
        self.assertIn("native Codex project tasks", flat(SKILL))
        self.assertIn("There is no coordinator CLI runner", flat(OPERATIONS))

    def run_prompt_builder(self, context, unit, role="executor", role_input=None, reference=None):
        with tempfile.TemporaryDirectory(prefix="workflow-prompt-") as directory:
            selector = Path(directory) / "selector.py"
            selector.write_text(
                "import json, os\nprint(os.environ['FAKE_PLAN_CONTEXT'])\n",
                encoding="utf-8",
                newline="\n",
            )
            environment = dict(os.environ)
            environment["FAKE_PLAN_CONTEXT"] = json.dumps(context, ensure_ascii=False, separators=(",", ":"))
            return subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(PROMPT_BUILDER),
                    "--recipient-model", "gpt-6-sol",
                    "--selector",
                    str(selector),
                    "--plan-root",
                    str(ROOT),
                    "--unit",
                    unit,
                    "--role",
                    role,
                    "--workspace-root",
                    str(ROOT),
                    "--return-to-thread-id",
                    "coordinator-test-id",
                    "--delivery-reference",
                    reference or f"delivery-{role}-{unit.replace('/', '-')}",
                    "--guard-workflow-id",
                    "workflow-test-id",
                    "--guard-generation",
                    "0",
                    "--guard-revision",
                    "7",
                    "--guard-dispatch-key",
                    f"dispatch-{role}-{unit.replace('/', '-')}",
                    *(["--guard-task-id", f"{role}-test-id"] if role in {"executor", "repair"} else []),
                ],
                input=json.dumps(role_input or {}, ensure_ascii=False),
                text=True,
                encoding="utf-8",
                capture_output=True,
                check=False,
                env=environment,
            )

    def run_native_inspector(self, events, role="executor", reference="delivery-test"):
        with tempfile.TemporaryDirectory(prefix="workflow-native-") as directory:
            rollout = Path(directory) / "rollout-test-thread.jsonl"
            rollout.write_text(
                "".join(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n" for event in events),
                encoding="utf-8",
                newline="\n",
            )
            return subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(NATIVE_INSPECTOR),
                    "--thread-id",
                    "test-thread",
                    "--role",
                    role,
                    "--delivery-reference",
                    reference,
                    "--return-to-thread-id",
                    "coordinator-test-id",
                    "--rollout",
                    str(rollout),
                ],
                text=True,
                encoding="utf-8",
                capture_output=True,
                check=False,
            )

    @staticmethod
    def run_result_parser(raw, role="executor"):
        return subprocess.run(
            [sys.executable, "-B", str(ROLE_RESULT_PARSER), "--role", role],
            input=raw,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )

    @staticmethod
    def run_result_parser_bytes(raw, role="executor"):
        return subprocess.run(
            [sys.executable, "-B", str(ROLE_RESULT_PARSER), "--role", role],
            input=raw,
            capture_output=True,
            check=False,
        )

    @staticmethod
    def run_guard(workspace, actor, *arguments):
        environment = dict(os.environ)
        environment["CODEX_THREAD_ID"] = actor
        from native_startup_fixture import supply_native_startup
        environment["CODEX_HOME"] = str(supply_native_startup(PACKAGE, workspace, actor, arguments))
        return subprocess.run(
            [sys.executable, "-B", str(GUARD_HELPER), *arguments, "--workspace", str(workspace)],
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
            env=environment,
        )

    def test_agents_contract_setup_is_exact_bounded_and_terminal(self):
        source = AGENTS_CONTRACT.read_bytes()
        self.assertLessEqual(len(source.split()), 110)
        self.assertLessEqual(len(source), 900)
        contract = source.decode("utf-8")
        self.assertIn("while the guard exists", contract)
        self.assertIn("its own required write authorization is pending or mismatched", contract)
        self.assertIn("except for an identity-checked guard transition", contract)
        with tempfile.TemporaryDirectory(prefix="workflow-agents-") as directory:
            workspace = Path(directory)
            missing = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "check", "--workspace", str(workspace)],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(1, missing.returncode)
            self.assertEqual("absent", json.loads(missing.stdout)["reason"])
            refused = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(workspace)],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(1, refused.returncode)
            self.assertFalse((workspace / "AGENTS.md").exists())
            installed = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(workspace), "--approved"],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(0, installed.returncode, installed.stdout)
            payload = json.loads(installed.stdout)
            self.assertTrue(payload["installed"])
            self.assertEqual(source, (workspace / "AGENTS.md").read_bytes())
            checked = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "check", "--workspace", str(workspace)],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual("valid", json.loads(checked.stdout)["reason"])

        with tempfile.TemporaryDirectory(prefix="workflow-agents-missing-root-") as directory:
            missing_workspace = Path(directory) / "does-not-exist"
            invalid_root = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(missing_workspace), "--approved"],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(1, invalid_root.returncode)
            self.assertEqual("workspace_invalid", json.loads(invalid_root.stdout)["reason"])
            self.assertFalse(missing_workspace.exists())

        setup = flat(PACKAGE / "references" / "agents-setup.md")
        skill = SKILL.read_text(encoding="utf-8")
        gate_lines = [line for line in skill.splitlines() if "manage_agents_contract.py check" in line or "installed: false" in line]
        self.assertEqual(2, len(gate_lines))
        self.assertIn("end this invocation even when verification succeeds", setup)
        self.assertIn("active workflow never installs or updates", setup)

    def test_agents_contract_preserves_unrelated_bytes_and_rejects_unsafe_markers(self):
        source = AGENTS_CONTRACT.read_bytes()
        with tempfile.TemporaryDirectory(prefix="workflow-agents-preserve-") as directory:
            workspace = Path(directory)
            unrelated = b"# Existing\r\n\r\nKeep  two spaces.\r\n"
            target = workspace / "AGENTS.md"
            target.write_bytes(unrelated)
            installed = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(workspace), "--approved"],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(0, installed.returncode, installed.stdout)
            self.assertEqual(source + b"\n" + unrelated, target.read_bytes())
            target.write_bytes(unrelated + source)
            moved = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(workspace), "--approved"],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(0, moved.returncode, moved.stdout)
            self.assertTrue(target.read_bytes().startswith(source))
            self.assertIn(unrelated, target.read_bytes())
            target.write_bytes(source + source)
            duplicated = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(workspace), "--approved"],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(1, duplicated.returncode)
            self.assertEqual("duplicated", json.loads(duplicated.stdout)["reason"])
            target.write_bytes(source + b"<!-- scoville-workflow-contract:v1:start --\n")
            malformed_extra = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "check", "--workspace", str(workspace)],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(1, malformed_extra.returncode)
            self.assertEqual("malformed_markers", json.loads(malformed_extra.stdout)["reason"])
            target.write_bytes(b"<!-- scoville-workflow-contract:vX:start -->\n")
            malformed_only = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(workspace), "--approved"],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(1, malformed_only.returncode)
            self.assertEqual("malformed_markers", json.loads(malformed_only.stdout)["reason"])

    def test_agents_contract_accepts_bom_and_crlf_and_upgrades_recognized_old_version(self):
        source = AGENTS_CONTRACT.read_bytes()
        with tempfile.TemporaryDirectory(prefix="workflow-agents-variants-") as directory:
            workspace = Path(directory)
            target = workspace / "AGENTS.md"
            target.write_bytes(b"\xef\xbb\xbf" + source.replace(b"\n", b"\r\n") + b"# Existing\r\n")
            checked = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "check", "--workspace", str(workspace)],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(0, checked.returncode, checked.stdout)
            self.assertTrue(json.loads(checked.stdout)["installed"])
            legacy = (
                b"<!-- scoville-workflow-contract:v0:start -->\n"
                b"While Scoville Workflow is active, only its coordinator and assigned worker may write.\n"
                b"<!-- scoville-workflow-contract:v0:end -->\n"
            )
            unrelated = b"# Preserve exactly\r\n"
            target.write_bytes(legacy + unrelated)
            old = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "check", "--workspace", str(workspace)],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual("recognized_old", json.loads(old.stdout)["reason"])
            upgraded = subprocess.run(
                [sys.executable, "-B", str(AGENTS_HELPER), "install", "--workspace", str(workspace), "--approved"],
                text=True, encoding="utf-8", capture_output=True, check=False,
            )
            self.assertEqual(0, upgraded.returncode, upgraded.stdout)
            self.assertEqual(source + b"\n" + unrelated, target.read_bytes())

    def test_guard_writer_authorization_is_pending_until_exact_activation(self):
        with tempfile.TemporaryDirectory(prefix="workflow-guard-") as directory:
            workspace = Path(directory)
            acquired = self.run_guard(workspace, "launcher-1", "acquire", "--workflow-id", "launcher-1")
            self.assertEqual(0, acquired.returncode, acquired.stdout)
            wrong_workflow_claim = self.run_guard(
                workspace, "coordinator-1", "claim", "--workflow-id", "other-workflow",
                "--expected-revision", "0", "--expected-generation", "0",
            )
            self.assertEqual(1, wrong_workflow_claim.returncode)
            self.assertEqual("workflow_mismatch", json.loads(wrong_workflow_claim.stdout)["reason"])
            reconciled_coordinator = self.run_guard(
                workspace, "launcher-1", "reconcile-coordinator", "--workflow-id", "launcher-1",
                "--expected-revision", "0", "--expected-generation", "0", "--task-id", "coordinator-1",
            )
            self.assertEqual(0, reconciled_coordinator.returncode, reconciled_coordinator.stdout)
            claimed = self.run_guard(
                workspace, "coordinator-1", "claim", "--workflow-id", "launcher-1",
                "--expected-revision", "1", "--expected-generation", "0",
            )
            self.assertEqual(0, claimed.returncode, claimed.stdout)
            stale_generation = self.run_guard(
                workspace, "coordinator-1", "verify", "--workflow-id", "launcher-1",
                "--expected-revision", "2", "--expected-generation", "1",
                "--role", "coordinator", "--capability", "plan",
            )
            self.assertEqual(1, stale_generation.returncode)
            self.assertEqual("generation_mismatch", json.loads(stale_generation.stdout)["reason"])
            authorized = self.run_guard(
                workspace, "coordinator-1", "authorize-writer", "--workflow-id", "launcher-1",
                "--expected-revision", "2", "--expected-generation", "0",
                "--role", "executor", "--unit", "W-001/step-1", "--dispatch-key", "dispatch-1", "--title", "W-001 executor 1",
            )
            self.assertEqual(0, authorized.returncode, authorized.stdout)
            pending = self.run_guard(
                workspace, "executor-1", "verify", "--workflow-id", "launcher-1", "--expected-revision", "3",
                "--expected-generation", "0", "--role", "executor", "--capability", "source",
                "--unit", "W-001/step-1", "--dispatch-key", "dispatch-1",
            )
            self.assertFalse(json.loads(pending.stdout)["authorized"])
            coordinator_plan = self.run_guard(
                workspace, "coordinator-1", "verify", "--workflow-id", "launcher-1", "--expected-revision", "3",
                "--expected-generation", "0", "--role", "coordinator", "--capability", "plan",
            )
            self.assertTrue(json.loads(coordinator_plan.stdout)["authorized"])
            coordinator_commit = self.run_guard(
                workspace, "coordinator-1", "verify", "--workflow-id", "launcher-1", "--expected-revision", "3",
                "--expected-generation", "0", "--role", "coordinator", "--capability", "stage_commit",
            )
            self.assertFalse(json.loads(coordinator_commit.stdout)["authorized"])
            reconciled = self.run_guard(
                workspace, "coordinator-1", "reconcile-writer", "--workflow-id", "launcher-1",
                "--expected-revision", "3", "--expected-generation", "0",
                "--dispatch-key", "dispatch-1", "--task-id", "executor-1",
            )
            self.assertEqual(0, reconciled.returncode, reconciled.stdout)
            still_pending = self.run_guard(
                workspace, "executor-1", "verify", "--workflow-id", "launcher-1", "--expected-revision", "4",
                "--expected-generation", "0", "--role", "executor", "--capability", "source",
                "--unit", "W-001/step-1", "--dispatch-key", "dispatch-1",
            )
            self.assertFalse(json.loads(still_pending.stdout)["authorized"])
            missing_id = self.run_guard(
                workspace, "coordinator-1", "activate-writer", "--workflow-id", "launcher-1",
                "--expected-revision", "4", "--expected-generation", "0", "--dispatch-key", "dispatch-1",
            )
            self.assertEqual("invalid_argument", json.loads(missing_id.stdout)["reason"])
            active = self.run_guard(
                workspace, "coordinator-1", "activate-writer", "--workflow-id", "launcher-1",
                "--expected-revision", "4", "--expected-generation", "0",
                "--dispatch-key", "dispatch-1", "--task-id", "executor-1",
            )
            self.assertEqual(0, active.returncode, active.stdout)
            verified = self.run_guard(
                workspace, "executor-1", "verify", "--workflow-id", "launcher-1", "--expected-revision", "5",
                "--expected-generation", "0", "--role", "executor", "--capability", "source",
                "--unit", "W-001/step-1", "--dispatch-key", "dispatch-1",
            )
            self.assertTrue(json.loads(verified.stdout)["authorized"])
            wrong_workflow = self.run_guard(
                workspace, "executor-1", "verify", "--workflow-id", "other-workflow", "--expected-revision", "5",
                "--expected-generation", "0", "--role", "executor", "--capability", "source",
                "--unit", "W-001/step-1", "--dispatch-key", "dispatch-1",
            )
            self.assertEqual("workflow_mismatch", json.loads(wrong_workflow.stdout)["reason"])
            stale = self.run_guard(
                workspace, "coordinator-1", "clear-writer", "--workflow-id", "launcher-1",
                "--expected-revision", "4", "--expected-generation", "0", "--dispatch-key", "dispatch-1",
            )
            self.assertEqual(1, stale.returncode)
            self.assertEqual("revision_mismatch", json.loads(stale.stdout)["reason"])

    def test_guard_accepts_step_ranges_for_writer_and_rollover_units(self):
        with tempfile.TemporaryDirectory(prefix="workflow-unit-ranges-") as directory:
            workspace = Path(directory)
            self.assertEqual(0, self.run_guard(workspace, "launcher-1", "acquire", "--workflow-id", "launcher-1").returncode)
            self.assertEqual(0, self.run_guard(workspace, "launcher-1", "reconcile-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "0", "--expected-generation", "0", "--task-id", "coordinator-1").returncode)
            self.assertEqual(0, self.run_guard(workspace, "coordinator-1", "claim", "--workflow-id", "launcher-1", "--expected-revision", "1", "--expected-generation", "0").returncode)
            for invalid_unit in ("W-001/steps-2-1", "W-001/steps-1-1"):
                invalid = self.run_guard(
                    workspace, "coordinator-1", "authorize-writer", "--workflow-id", "launcher-1",
                    "--expected-revision", "2", "--expected-generation", "0", "--role", "repair",
                    "--unit", invalid_unit, "--dispatch-key", "dispatch-invalid", "--title", "Invalid range",
                )
                self.assertEqual(1, invalid.returncode)
                self.assertEqual("invalid_argument", json.loads(invalid.stdout)["reason"])
            writer = self.run_guard(
                workspace, "coordinator-1", "authorize-writer", "--workflow-id", "launcher-1",
                "--expected-revision", "2", "--expected-generation", "0", "--role", "repair",
                "--unit", "W-001/steps-1-2", "--dispatch-key", "dispatch-range", "--title", "Range repair",
            )
            self.assertEqual(0, writer.returncode, writer.stdout)
            cleared = self.run_guard(
                workspace, "coordinator-1", "clear-writer", "--workflow-id", "launcher-1",
                "--expected-revision", "3", "--expected-generation", "0", "--dispatch-key", "dispatch-range",
            )
            self.assertEqual(0, cleared.returncode, cleared.stdout)
            rollover = self.run_guard(
                workspace, "coordinator-1", "begin-rollover", "--workflow-id", "launcher-1",
                "--expected-revision", "4", "--expected-generation", "0", "--transition-key", "range-rollover",
                "--accepted-unit", "W-001/steps-1-2", "--title", "Range rollover",
            )
            self.assertEqual(0, rollover.returncode, rollover.stdout)

    def test_guard_rollover_transfers_before_successor_activation(self):
        with tempfile.TemporaryDirectory(prefix="workflow-rollover-") as directory:
            workspace = Path(directory)
            self.assertEqual(0, self.run_guard(workspace, "launcher-1", "acquire", "--workflow-id", "launcher-1").returncode)
            self.assertEqual(0, self.run_guard(workspace, "launcher-1", "reconcile-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "0", "--expected-generation", "0", "--task-id", "coordinator-1").returncode)
            self.assertEqual(0, self.run_guard(workspace, "coordinator-1", "claim", "--workflow-id", "launcher-1", "--expected-revision", "1", "--expected-generation", "0").returncode)
            begin = self.run_guard(
                workspace, "coordinator-1", "begin-rollover", "--workflow-id", "launcher-1", "--expected-revision", "2", "--expected-generation", "0",
                "--transition-key", "rollover-W-001", "--accepted-unit", "W-001/step-1", "--title", "Coordinator rollover 1",
            )
            self.assertEqual(0, begin.returncode, begin.stdout)
            ready = self.run_guard(
                workspace, "coordinator-1", "reconcile-successor", "--workflow-id", "launcher-1", "--expected-revision", "3", "--expected-generation", "0",
                "--transition-key", "rollover-W-001", "--task-id", "coordinator-2",
            )
            self.assertEqual(0, ready.returncode, ready.stdout)
            wrong_validation_key = self.run_guard(workspace, "coordinator-2", "validate-successor", "--workflow-id", "launcher-1", "--expected-revision", "4", "--expected-generation", "0", "--transition-key", "wrong-key")
            self.assertEqual(1, wrong_validation_key.returncode)
            self.assertEqual("successor_mismatch", json.loads(wrong_validation_key.stdout)["reason"])
            validated = self.run_guard(workspace, "coordinator-2", "validate-successor", "--workflow-id", "launcher-1", "--expected-revision", "4", "--expected-generation", "0", "--transition-key", "rollover-W-001")
            self.assertEqual(0, validated.returncode, validated.stdout)
            wrong_transfer_key = self.run_guard(
                workspace, "coordinator-1", "transfer-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "5", "--expected-generation", "0", "--transition-key", "wrong-key",
            )
            self.assertEqual(1, wrong_transfer_key.returncode)
            self.assertEqual("rollover_mismatch", json.loads(wrong_transfer_key.stdout)["reason"])
            transferred = self.run_guard(
                workspace, "coordinator-1", "transfer-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "5", "--expected-generation", "0", "--transition-key", "rollover-W-001",
            )
            self.assertEqual("coordinator_pending_activation", json.loads(transferred.stdout)["state"])
            old_owner = self.run_guard(workspace, "coordinator-1", "verify", "--workflow-id", "launcher-1", "--expected-revision", "6", "--expected-generation", "1", "--role", "coordinator", "--capability", "plan")
            new_owner = self.run_guard(workspace, "coordinator-2", "verify", "--workflow-id", "launcher-1", "--expected-revision", "6", "--expected-generation", "1", "--role", "coordinator", "--capability", "plan")
            self.assertFalse(json.loads(old_owner.stdout)["authorized"])
            self.assertFalse(json.loads(new_owner.stdout)["authorized"])
            wrong_activation_key = self.run_guard(workspace, "coordinator-2", "activate-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "6", "--expected-generation", "1", "--transition-key", "wrong-key")
            self.assertEqual(1, wrong_activation_key.returncode)
            self.assertEqual("successor_mismatch", json.loads(wrong_activation_key.stdout)["reason"])
            activated = self.run_guard(workspace, "coordinator-2", "activate-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "6", "--expected-generation", "1", "--transition-key", "rollover-W-001")
            self.assertEqual(0, activated.returncode, activated.stdout)
            self.assertTrue(json.loads(self.run_guard(workspace, "coordinator-2", "verify", "--workflow-id", "launcher-1", "--expected-revision", "7", "--expected-generation", "1", "--role", "coordinator", "--capability", "plan").stdout)["authorized"])
            released = self.run_guard(workspace, "coordinator-2", "release", "--workflow-id", "launcher-1", "--expected-revision", "7", "--expected-generation", "1")
            self.assertEqual(0, released.returncode, released.stdout)
            self.assertFalse((workspace / ".scoville-workflow" / "guard.json").exists())

    def test_guard_concurrent_acquire_has_one_winner_and_direct_edits_fail_closed(self):
        with tempfile.TemporaryDirectory(prefix="workflow-guard-race-") as directory:
            workspace = Path(directory)
            environment_a = dict(os.environ, CODEX_THREAD_ID="launcher-a")
            environment_b = dict(os.environ, CODEX_THREAD_ID="launcher-b")
            command_a = [sys.executable, "-B", str(GUARD_HELPER), "acquire", "--workflow-id", "launcher-a", "--workspace", str(workspace)]
            command_b = [sys.executable, "-B", str(GUARD_HELPER), "acquire", "--workflow-id", "launcher-b", "--workspace", str(workspace)]
            first = subprocess.Popen(command_a, text=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment_a)
            second = subprocess.Popen(command_b, text=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment_b)
            first_out, first_err = first.communicate(timeout=10)
            second_out, second_err = second.communicate(timeout=10)
            self.assertEqual(1, [first.returncode, second.returncode].count(0), (first_out, first_err, second_out, second_err))
            loser = json.loads(second_out if second.returncode else first_out)
            self.assertIn(loser["reason"], {"guard_exists", "transition_busy"})
            guard_path = workspace / ".scoville-workflow" / "guard.json"
            guard_path.write_bytes(guard_path.read_bytes() + b" \n")
            actor = "launcher-a" if first.returncode == 0 else "launcher-b"
            drift = self.run_guard(workspace, actor, "verify", "--workflow-id", actor, "--expected-revision", "0", "--expected-generation", "0", "--role", "other", "--capability", "read_only")
            self.assertEqual(1, drift.returncode)
            self.assertEqual("guard_noncanonical", json.loads(drift.stdout)["reason"])
            value = json.loads(guard_path.read_text(encoding="utf-8"))
            guard_path.write_text(
                json.dumps(
                    {**value, "plan": "changed-directly"},
                    ensure_ascii=False,
                    separators=(",", ":"),
                    sort_keys=True,
                ) + "\n",
                encoding="utf-8",
            )
            integrity_drift = self.run_guard(workspace, actor, "verify", "--workflow-id", actor, "--expected-revision", "0", "--expected-generation", "0", "--role", "other", "--capability", "read_only")
            self.assertEqual(1, integrity_drift.returncode)
            self.assertEqual("guard_integrity_mismatch", json.loads(integrity_drift.stdout)["reason"])

    def test_guard_rejects_internally_inconsistent_but_resealed_state(self):
        with tempfile.TemporaryDirectory(prefix="workflow-guard-shape-") as directory:
            workspace = Path(directory)
            self.assertEqual(0, self.run_guard(workspace, "launcher-1", "acquire", "--workflow-id", "launcher-1").returncode)
            self.assertEqual(0, self.run_guard(workspace, "launcher-1", "reconcile-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "0", "--expected-generation", "0", "--task-id", "coordinator-1").returncode)
            path = workspace / ".scoville-workflow" / "guard.json"
            value = json.loads(path.read_text(encoding="utf-8"))
            value["state"] = "writer_active"
            value["writer"] = {
                "dispatch_key": "dispatch-1",
                "unit": "W-001/step-1",
                "role": "executor",
                "title": "Executor",
                "task_id": "executor-1",
                "active": False,
            }
            unsigned = {key: item for key, item in value.items() if key != "integrity"}
            canonical = json.dumps(unsigned, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
            value["integrity"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            path.write_text(
                json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n",
                encoding="utf-8",
            )
            rejected = self.run_guard(
                workspace, "coordinator-1", "verify", "--workflow-id", "launcher-1",
                "--expected-revision", "1", "--expected-generation", "0",
                "--role", "coordinator", "--capability", "plan",
            )
            self.assertEqual(1, rejected.returncode)
            payload = json.loads(rejected.stdout)
            self.assertEqual("guard_invalid", payload["reason"])
            self.assertFalse(payload["ok"])

    def test_guard_every_response_is_complete_valid_json(self):
        with tempfile.TemporaryDirectory(prefix="workflow-guard-json-") as directory:
            workspace = Path(directory)
            outputs = [
                self.run_guard(workspace, "launcher-1", "acquire", "--workflow-id", "launcher-1"),
                self.run_guard(workspace, "launcher-1", "reconcile-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "99", "--expected-generation", "0", "--task-id", "coordinator-1"),
                self.run_guard(workspace, "launcher-1", "reconcile-coordinator", "--workflow-id", "launcher-1", "--expected-revision", "0", "--expected-generation", "0", "--task-id", "coordinator-1"),
                self.run_guard(workspace, "other-1", "verify", "--workflow-id", "launcher-1", "--expected-revision", "1", "--expected-generation", "0", "--role", "other", "--capability", "read_only"),
            ]
            required = {
                "ok", "action", "reason", "diagnostic", "path", "authorized", "state",
                "workflow_id", "generation", "revision", "coordinator_id", "writer", "rollover",
            }
            for completed in outputs:
                payload = json.loads(completed.stdout)
                self.assertEqual(required, set(payload))
                self.assertEqual(
                    completed.stdout.strip(),
                    json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
                )

    def test_mutating_guard_instructions_require_revision_and_generation(self):
        skill = flat(SKILL)
        operations = flat(OPERATIONS)
        builder = PROMPT_BUILDER.read_text(encoding="utf-8")
        self.assertIn("exact workflow ID, revision and generation", skill)
        self.assertIn(
            "Every later guard transition supplies the current workflow ID, revision and generation",
            operations,
        )
        self.assertIn("expected guard revision and generation", operations)
        self.assertIn("same successor identity, transition key, revision, generation", operations)
        self.assertIn("guard_workflow_id --expected-revision guard_revision", builder)
        self.assertIn("--expected-generation guard_generation", builder)

    def test_role_results_self_validate_before_delivery_and_guard_is_never_staged(self):
        operations = flat(OPERATIONS)
        self.assertIn("Before its final response, the child checks the header", operations)
        self.assertIn("scripts/parse_role_result.py", operations)
        self.assertIn("Models never compose result JSON", operations)
        self.assertIn("It sends no callback message", operations)
        self.assertIn("The coordinator still performs independent", operations)
        self.assertIn("Never stage `.scoville-workflow/guard.json`", operations)

    def test_role_result_helper_accepts_only_ordered_line_protocol(self):
        valid = {
            "executor": (
                "SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\n"
                "code_changed=yes\ncritical_docs_changed=no\nsummary=Implemented.\n"
                "finding=One issue remains."
            ),
            "repair": (
                "SCOVILLE_RESULT_V1\nrole=repair\nstatus=completed\n"
                "code_changed=no\ncritical_docs_changed=yes\nsummary=Documentation corrected."
            ),
            "reviewer": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=Review passed.",
        }
        for role, raw in valid.items():
            with self.subTest(role=role):
                completed = self.run_result_parser(raw, role)
                self.assertEqual(0, completed.returncode, completed.stdout)
                payload = json.loads(completed.stdout)
                self.assertTrue(payload["valid"])
                self.assertEqual(role_result_parser.parse_role_result(raw, role), payload["result"])
        self.assertEqual(
            "pass",
            role_result_parser.parse_role_result(
                "SCOVILLE_RESULT_V1\r\nrole=reviewer\r\nstatus=pass\r\nsummary=Review passed.\r\n",
                "reviewer",
            )["status"],
        )
        eight_findings = (
            "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\nsummary=One\n"
            + "\n".join("finding=x" for _ in range(8))
        )
        self.assertEqual(0, self.run_result_parser(eight_findings, "reviewer").returncode)

        invalid = {
            "json": '{"status":"pass","summary":"Review passed.","findings":[]}',
            "fence": "```text\nSCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=Review passed.\n```",
            "missing": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass",
            "duplicate": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\nsummary=Two",
            "unknown": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\nnote=Two",
            "unordered": "SCOVILLE_RESULT_V1\nstatus=pass\nrole=reviewer\nsummary=One",
            "wrong_role": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=pass\nsummary=One",
            "bad_status": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=completed\nsummary=One",
            "pass_finding": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\nfinding=Two",
            "empty": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=blocked\nsummary=",
            "multiline": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=blocked\nsummary=First\nsecond line",
            "trailing_blank": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=One\n\n",
            "nine_findings": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\nsummary=One\n" + "\n".join("finding=x" for _ in range(9)),
            "long_summary": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=blocked\nsummary=" + "x" * 801,
            "long_finding": "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\nsummary=One\nfinding=" + "x" * 401,
            "completion_fields_missing": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\nsummary=One",
            "completion_fields_on_block": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=blocked\ncode_changed=no\ncritical_docs_changed=no\nsummary=One",
        }
        for name, raw in invalid.items():
            with self.subTest(name=name):
                completed = self.run_result_parser(raw, "reviewer" if name not in {"completion_fields_missing", "completion_fields_on_block"} else "executor")
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertFalse(json.loads(completed.stdout)["valid"])
        with self.assertRaises(role_result_parser.RoleResultError):
            role_result_parser.parse_role_result(
                "SCOVILLE_RESULT_V1\rrole=reviewer\nstatus=pass\nsummary=One", "reviewer"
            )
        bare_cr = self.run_result_parser_bytes(
            b"SCOVILLE_RESULT_V1\rrole=reviewer\nstatus=pass\nsummary=One", "reviewer"
        )
        self.assertEqual(1, bare_cr.returncode, bare_cr.stdout)
        self.assertEqual("LINE_ENDING_INVALID", json.loads(bare_cr.stdout)["diagnostics"][0]["code"])

    @staticmethod
    def compacted_rollout(*, delivery=None, final=None, delivery_failed=False, delivery_unknown=False):
        events = [
            {"ordinal": 0, "type": "session_meta", "payload": {"session_id": "test-thread"}},
            {"ordinal": 1, "type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1"}},
            {"ordinal": 2, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
        ]
        ordinal = 3
        if delivery is not None:
            delivery_prompt = "workflow_result_delivery=delivery-test\n" + delivery
            arguments = json.dumps(
                {"threadId": "coordinator-test-id", "prompt": delivery_prompt},
                ensure_ascii=False,
                separators=(",", ":"),
            )
            events.append(
                {
                    "ordinal": ordinal,
                    "type": "response_item",
                    "payload": {
                        "type": "custom_tool_call",
                        "id": "delivery-call",
                        "call_id": "delivery-call-id",
                        "name": "exec",
                        "status": "completed",
                        "input": "const r=await tools.mcp__codex_app__send_message_to_thread(" + arguments + ");for(const c of(r.content??[])){if(c.type===\"text\")text(c.text);}",
                    },
                }
            )
            if delivery_failed:
                events.append({
                    "ordinal": ordinal + 1,
                    "type": "event_msg",
                    "payload": {
                        "type": "item_completed",
                        "thread_id": "test-thread",
                        "turn_id": "turn-1",
                        "item": {
                            "type": "McpToolCall",
                            "id": "delivery-exec",
                            "server": "codex_app",
                            "tool": "send_message_to_thread",
                            "status": "failed",
                            "arguments": {"threadId": "coordinator-test-id", "prompt": delivery_prompt},
                        },
                    },
                })
                ordinal += 2
            elif delivery_unknown:
                ordinal += 1
            else:
                events.extend([{
                    "ordinal": ordinal + 1,
                    "type": "event_msg",
                    "payload": {
                        "type": "item_completed",
                        "thread_id": "test-thread",
                        "turn_id": "turn-1",
                        "item": {"type": "McpToolCall", "id": "delivery-exec", "status": "completed"},
                    },
                }, {
                    "ordinal": ordinal + 2,
                    "type": "response_item",
                    "payload": {
                        "type": "custom_tool_call_output",
                        "id": "delivery-output",
                        "call_id": "delivery-call-id",
                        "output": [
                            {"type": "input_text", "text": "Script completed\nWall time 0.1 seconds\nOutput:\n"},
                            {"type": "input_text", "text": '{"threadId":"coordinator-test-id"}'},
                        ],
                    },
                }])
                ordinal += 3
        if final is not None:
            events.extend([
                {
                    "ordinal": ordinal,
                    "type": "event_msg",
                    "payload": {
                        "type": "item_completed",
                        "thread_id": "test-thread",
                        "turn_id": "turn-1",
                        "item": {"type": "AgentMessage", "id": "final-message", "phase": "final_answer"},
                    },
                },
                {
                    "ordinal": ordinal + 1,
                    "type": "response_item",
                    "payload": {
                        "type": "message",
                        "id": "final-message",
                        "role": "assistant",
                        "phase": "final_answer",
                        "content": [{"type": "output_text", "text": final}],
                    },
                },
            ])
            ordinal += 2
        events.extend([
            {"ordinal": ordinal, "type": "compacted", "payload": {"replacement_history": []}},
            {"ordinal": ordinal + 1, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
        ])
        return events

    @staticmethod
    def dispatch_context(unit, steps):
        work_item = {
            "unit": unit,
            "header": "### W-003 Exact unit",
            "status": "Status: in_progress",
            "depends_on": "Depends on: [W-002]",
            "blocked_by": "Blocked by: []",
            "decisions": "Decisions: [ADR-0001]",
            "outcome": "Outcome: Exact behavior.",
            "acceptance": "Acceptance: Focused proof passes.",
            "steps": steps,
            "source_text": "\n".join(steps) + "\n" if steps else "### W-003 Exact unit\nEvidence: []\nNext action: Perform the selected unit.\n",
        }
        if not steps:
            work_item["next_action"] = "Next action: Perform the selected unit."
        return {
            "plan": {
                "frontmatter": "---\nformat_version: 1\nid: PLAN-0001\nstatus: active\ncurrent_item: W-003\n---\n",
                "goal": "## Goal\n\nShip the exact unit.",
                "non_goals": "## Non-goals\n\n- Do not publish.",
            },
            "work_item": work_item,
            "direct_dependencies": [{"id": "W-002", "status_line": "Status: done"}],
            "decisions": ["---\nid: ADR-0001\n---\n# Keep compatibility\n"],
        }

    def test_prompt_builder_supports_exact_step_and_whole_item_units(self):
        step_unit = "W-003/step-2"
        step_context = self.dispatch_context(step_unit, ["2. Change only the selected behavior."])
        executor = self.run_prompt_builder(step_context, step_unit)
        self.assertEqual(0, executor.returncode, executor.stdout)
        self.assertTrue(executor.stdout.startswith("scoville_role=executor\n"))
        self.assertIn("unit=W-003/step-2", executor.stdout)
        self.assertIn("Change only the selected behavior", executor.stdout)
        self.assertIn("ADR-0001", executor.stdout)
        self.assertNotIn("Evidence:", executor.stdout)
        self.assertIn("return_to_thread_id=coordinator-test-id", executor.stdout)
        self.assertIn("Do not call send_message_to_thread", executor.stdout)
        self.assertIn("guard_revision=7", executor.stdout)
        self.assertIn("guard_task_id=executor-test-id", executor.stdout)
        self.assertIn("--capability source", executor.stdout)
        self.assertIn("Use at most eight finding lines", executor.stdout)

        whole_unit = "W-003"
        whole_context = self.dispatch_context(whole_unit, [])
        whole = self.run_prompt_builder(whole_context, whole_unit)
        self.assertEqual(0, whole.returncode, whole.stdout)
        self.assertIn("unit=W-003", whole.stdout)
        self.assertIn('"steps":[]', whole.stdout)
        self.assertIn("Evidence:", whole.stdout)

    def test_reviewer_prompt_contains_only_same_unit_plus_executor_result(self):
        unit = "W-003/step-2"
        context = self.dispatch_context(unit, ["2. Change only the selected behavior."])
        result = parse_role_payload(
            "SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\n"
            "code_changed=yes\ncritical_docs_changed=no\n"
            "summary=Changed the selected behavior.",
            "executor",
        )
        reviewer = self.run_prompt_builder(
            context,
            unit,
            role="reviewer",
            role_input={"executor_result": result},
        )
        self.assertEqual(0, reviewer.returncode, reviewer.stdout)
        self.assertTrue(reviewer.stdout.startswith("scoville_role=reviewer\n"))
        self.assertIn("executor_result=" + json.dumps(result, separators=(",", ":")), reviewer.stdout)
        self.assertIn("Remain read-only", reviewer.stdout)
        self.assertIn("SCOVILLE_RESULT_V1\nrole=reviewer", reviewer.stdout)
        self.assertIn("Use at most eight finding lines", reviewer.stdout)
        self.assertNotIn("Return one JSON object", reviewer.stdout)
        self.assertNotIn("Evidence:", reviewer.stdout)

    def test_rollover_prompt_treats_inherited_handoff_as_continuation(self):
        unit = "W-003/step-2"
        context = self.dispatch_context(unit, ["2. Change only the selected behavior."])
        inherited = {
            "status": "context_handoff",
            "summary": "Continue the remaining review.",
            "findings": [],
        }
        reviewer_result = parse_role_payload(
            "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\n"
            "summary=One correction remains.\nfinding=Correct the selected behavior.",
            "reviewer",
        )
        rollover = self.run_prompt_builder(
            context,
            unit,
            role="repair",
            role_input={
                "reviewer_result": reviewer_result,
                "repair_assignment": {"finding_indices": [0]},
                "context_handoff": inherited,
            },
        )
        self.assertEqual(0, rollover.returncode, rollover.stdout)
        self.assertIn("progress_after_dispatch=<newly completed unit action>", rollover.stdout)
        self.assertIn("context_handoff=" + json.dumps(inherited, separators=(",", ":")), rollover.stdout)
        self.assertIn("reviewer_result=" + json.dumps(reviewer_result, separators=(",", ":")), rollover.stdout)

    def test_result_delivery_is_single_use_and_byte_identical(self):
        unit = "W-003/step-2"
        context = self.dispatch_context(unit, ["2. Change only the selected behavior."])
        completed = self.run_prompt_builder(context, unit)
        self.assertEqual(0, completed.returncode, completed.stdout)
        self.assertIn("delivery_reference=delivery-executor-W-003-step-2", completed.stdout)
        self.assertNotIn("tools.mcp__codex_app__send_message_to_thread(", completed.stdout)
        self.assertNotIn("workflow_result_delivery=", completed.stdout)

        invalid = subprocess.run(
            [
                sys.executable,
                "-B",
                str(PROMPT_BUILDER),
                    "--recipient-model", "gpt-6-sol",
                "--selector",
                str(PROMPT_BUILDER),
                    "--recipient-model", "gpt-6-sol",
                "--plan-root",
                str(ROOT),
                "--unit",
                unit,
                "--role",
                "executor",
                "--workspace-root",
                str(ROOT),
                "--return-to-thread-id",
                "bad reference with spaces",
                "--delivery-reference",
                "delivery-valid",
                "--guard-workflow-id",
                "workflow-test-id",
                    "--guard-generation",
                    "0",
                    "--guard-revision",
                    "0",
                    "--guard-dispatch-key",
                    "dispatch-test-id",
                    "--guard-task-id",
                    "executor-test-id",
            ],
            input="{}",
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )
        self.assertEqual(2, invalid.returncode)
        self.assertEqual("RETURN_THREAD_ID_INVALID", json.loads(invalid.stdout)["diagnostics"][0]["code"])

    def test_every_child_prompt_contains_executable_context_safety_rules(self):
        unit = "W-003/step-2"
        context = self.dispatch_context(unit, ["2. Change only the selected behavior."])
        role_inputs = {
            "executor": {},
            "reviewer": {
                "executor_result": {
                    "status": "completed",
                    "summary": "done",
                    "review": {"code_changed": "yes", "critical_docs_changed": "no"},
                    "findings": [],
                }
            },
            "repair": {
                "reviewer_result": {
                    "status": "changes_requested",
                    "summary": "repair",
                    "findings": ["fix"],
                },
                "repair_assignment": {"finding_indices": [0]},
            },
        }
        prompts = {}
        for role, role_input in role_inputs.items():
            completed = self.run_prompt_builder(context, unit, role=role, role_input=role_input)
            self.assertEqual(0, completed.returncode, completed.stdout)
            prompts[role] = completed.stdout
            self.assertTrue(completed.stdout.startswith(f"scoville_role={role}\ndispatch_contract=SCOVILLE_DISPATCH_V1\n"))
            for field in ("unit=W-003/step-2", "workspace_root=", "guard_workflow_id=workflow-test-id",
                          "guard_generation=0", "guard_revision=7", f"guard_dispatch_key=dispatch-{role}-W-003-step-2"):
                self.assertIn(field, completed.stdout)
            self.assertIn("guard_task_id=" + ("read_only" if role == "reviewer" else role + "-test-id"), completed.stdout)
            self.assertIn("inspect_native_context.py", completed.stdout)
            self.assertIn("--return-to-thread-id coordinator-test-id", completed.stdout)
            self.assertNotIn("tools.mcp__codex_app__send_message_to_thread(", completed.stdout)
            self.assertIn("check_context_checkpoint.py", completed.stdout)
            self.assertIn("--role " + role, completed.stdout)
            headings = [completed.stdout.index(f"[{number} {name}]") for number, name in (
                (1, "Native context gate"), (2, "Role and authority"), (3, "Continuation inputs"),
                (4, "Work"), (5, "Result"), (6, "Delivery"))]
            self.assertEqual(sorted(headings), headings)
            self.assertIn("plan_context=" + json.dumps(context, ensure_ascii=False, separators=(",", ":")), completed.stdout)
            self.assertNotIn("expected_approval_policy", completed.stdout)
            self.assertNotIn("permission_inheritance_mismatch", completed.stdout)
            for key, value in role_input.items():
                self.assertIn(key + "=" + json.dumps(value, ensure_ascii=False, separators=(",", ":")), completed.stdout)
        self.assertIn("--capability read_only", prompts["reviewer"])
        self.assertIn("--capability source --unit unit --dispatch-key guard_dispatch_key", prompts["executor"])
        self.assertIn("--capability source --unit unit --dispatch-key guard_dispatch_key", prompts["repair"])

    def test_native_gate_rejects_abbreviated_agent_assignment_before_project_access(self):
        def assignment_events(prompt):
            return [
                {
                    "ordinal": 0,
                    "type": "session_meta",
                    "payload": {
                        "session_id": "test-thread",
                        "source": "vscode",
                        "thread_source": "agent_created_thread",
                    },
                },
                {"ordinal": 1, "type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1"}},
                {"ordinal": 2, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
                {
                    "ordinal": 3,
                    "type": "response_item",
                    "payload": {
                        "type": "function_call_output",
                        "name": "create_thread" if prompt.startswith("scoville_role=reviewer\n") else "send_message_to_thread",
                        "output": (
                            "<codex_delegation>\n"
                            "  <source_thread_id>coordinator-test-id</source_thread_id>\n"
                            "  <input>" + prompt + "</input>\n"
                            "</codex_delegation>"
                        ),
                    },
                },
                {"ordinal": 4, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
            ]

        abbreviated = assignment_events("Autorisierte Ausführung. Verändere keine Plan-Datei.")
        rejected = self.run_native_inspector(abbreviated)
        self.assertEqual(1, rejected.returncode)
        self.assertEqual("return_blocked", json.loads(rejected.stdout)["action"])
        self.assertIn("assignment", json.loads(rejected.stdout)["diagnostic"])

        unit = "W-003/step-2"
        context = self.dispatch_context(unit, ["2. Change only the selected behavior."])
        context["plan"]["goal"] += "\nLiteral envelope example: <input>inside</input>. Unicode separator: \u2028."
        role_inputs = {
            "executor": {},
            "reviewer": {
                "executor_result": {
                    "status": "completed",
                    "summary": "done",
                    "review": {"code_changed": "yes", "critical_docs_changed": "no"},
                    "findings": [],
                }
            },
            "repair": {
                "reviewer_result": {
                    "status": "changes_requested",
                    "summary": "repair",
                    "findings": ["fix"],
                },
                "repair_assignment": {"finding_indices": [0]},
            },
        }
        for role, role_input in role_inputs.items():
            prompt = self.run_prompt_builder(context, unit, role=role, role_input=role_input)
            self.assertEqual(0, prompt.returncode, prompt.stdout)
            reference = f"delivery-{role}-{unit.replace('/', '-')}"
            continued = self.run_native_inspector(
                assignment_events(prompt.stdout), role=role, reference=reference
            )
            self.assertEqual(0, continued.returncode, continued.stdout)
            self.assertEqual("continue_role", json.loads(continued.stdout)["action"])

            if role in {"executor", "repair"}:
                header = dict(line.split("=", 1) for line in prompt.stdout.splitlines()[:10])
                parking = (
                    f"scoville_role={role}\n"
                    f"unit={unit}\n"
                    f"workspace_root={header['workspace_root']}\n"
                    f"workflow_id={header['guard_workflow_id']}\n"
                    f"dispatch_key={header['guard_dispatch_key']}\n"
                    "Perform no project read or write and await the actual assignment."
                )
                same_turn = assignment_events(prompt.stdout)
                same_turn[3]["ordinal"] = 4
                same_turn[4]["ordinal"] = 5
                parked = dict(same_turn[3])
                parked["ordinal"] = 3
                parked["payload"] = dict(same_turn[3]["payload"])
                parked["payload"]["name"] = "create_thread"
                parked["payload"]["output"] = parked["payload"]["output"].replace(
                    prompt.stdout, parking
                )
                same_turn.insert(3, parked)
                accepted = self.run_native_inspector(
                    same_turn, role=role, reference=reference
                )
                self.assertEqual(0, accepted.returncode, accepted.stdout)
                self.assertEqual("continue_role", json.loads(accepted.stdout)["action"])
                duplicate = [dict(event) for event in same_turn]
                duplicate.insert(5, dict(same_turn[4]))
                for ordinal, event in enumerate(duplicate):
                    event["ordinal"] = ordinal
                rejected = self.run_native_inspector(
                    duplicate, role=role, reference=reference
                )
                self.assertEqual(1, rejected.returncode)
                self.assertIn("no unique native assignment", json.loads(rejected.stdout)["diagnostic"])
                same_turn[3]["payload"]["output"] = same_turn[3]["payload"]["output"].replace(
                    parking, parking + " Extra work."
                )
                rejected = self.run_native_inspector(
                    same_turn, role=role, reference=reference
                )
                self.assertEqual(1, rejected.returncode)
                self.assertIn("conflicting parking", json.loads(rejected.stdout)["diagnostic"])

            for transported in (
                html.escape(prompt.stdout, quote=False),
                prompt.stdout.removesuffix("\n"),
                html.escape(prompt.stdout, quote=False).removesuffix("\n"),
            ):
                accepted = self.run_native_inspector(
                    assignment_events(transported), role=role, reference=reference
                )
                self.assertEqual(0, accepted.returncode, accepted.stdout)
                self.assertEqual("continue_role", json.loads(accepted.stdout)["action"])

            if role in {"executor", "repair"}:
                noncanonical_entity = html.escape(prompt.stdout, quote=False).replace(
                    "&lt;executor|repair&gt;", "&#60;executor|repair&gt;", 1
                )
                blocked = self.run_native_inspector(
                    assignment_events(noncanonical_entity), role=role, reference=reference
                )
                self.assertEqual(1, blocked.returncode)
                self.assertEqual("return_blocked", json.loads(blocked.stdout)["action"])

            wrong_role = "reviewer" if role != "reviewer" else "executor"
            blocked = self.run_native_inspector(
                assignment_events(prompt.stdout), role=wrong_role, reference=reference
            )
            self.assertEqual(1, blocked.returncode)
            self.assertIn("conflicting role", json.loads(blocked.stdout)["diagnostic"])

            for missing in (
                "dispatch_contract=SCOVILLE_DISPATCH_V1\n",
                "Do not load Scoville Plan, Workflow or Handoff",
                "Perform this role now.",
            ):
                incomplete = assignment_events(prompt.stdout.replace(missing, "", 1))
                blocked = self.run_native_inspector(
                    incomplete, role=role, reference=reference
                )
                self.assertEqual(1, blocked.returncode)
                self.assertEqual("return_blocked", json.loads(blocked.stdout)["action"])
                self.assertIn("assignment", json.loads(blocked.stdout)["diagnostic"])

            wrong_identity = assignment_events(
                prompt.stdout.replace(reference, reference + "-WRONG")
            )
            blocked = self.run_native_inspector(
                wrong_identity, role=role, reference=reference
            )
            self.assertEqual(1, blocked.returncode)
            self.assertEqual("return_blocked", json.loads(blocked.stdout)["action"])

            if role in {"reviewer", "repair"}:
                required_input = "executor_result=" if role == "reviewer" else "repair_assignment="
                incomplete_prompt = "\n".join(
                    line for line in prompt.stdout.split("\n")
                    if not line.startswith(required_input)
                )
                blocked = self.run_native_inspector(
                    assignment_events(incomplete_prompt), role=role, reference=reference
                )
                self.assertEqual(1, blocked.returncode)
                self.assertEqual("return_blocked", json.loads(blocked.stdout)["action"])

            if role == "repair":
                invalid_assignment = prompt.stdout.replace(
                    'repair_assignment={"finding_indices":[0]}',
                    'repair_assignment={"finding_indices":[99]}',
                )
                blocked = self.run_native_inspector(
                    assignment_events(invalid_assignment), role=role, reference=reference
                )
                self.assertEqual(1, blocked.returncode)
                self.assertEqual("return_blocked", json.loads(blocked.stdout)["action"])

        malformed = assignment_events(prompt.stdout)
        malformed[3]["payload"]["output"] = "<input>" + prompt.stdout + "</input>"
        blocked = self.run_native_inspector(
            malformed, role="repair", reference="delivery-repair-W-003-step-2"
        )
        self.assertEqual(1, blocked.returncode)
        self.assertIn("envelope is malformed", json.loads(blocked.stdout)["diagnostic"])

        direct = assignment_events("handwritten direct prompt")
        direct[0]["payload"].pop("thread_source")
        continued = self.run_native_inspector(direct)
        self.assertEqual(0, continued.returncode, continued.stdout)
        self.assertEqual("continue_role", json.loads(continued.stdout)["action"])

    def test_same_task_user_decision_continuation_uses_complete_dispatch(self):
        unit = "W-003/step-2"
        context = self.dispatch_context(unit, ["2. Continue only after the user's decision."])
        initial_inputs = {
            "executor": {},
            "reviewer": {
                "executor_result": {
                    "status": "completed",
                    "summary": "done",
                    "review": {"code_changed": "yes", "critical_docs_changed": "no"},
                    "findings": [],
                }
            },
            "repair": {
                "reviewer_result": {
                    "status": "changes_requested",
                    "summary": "repair",
                    "findings": ["fix"],
                },
                "repair_assignment": {"finding_indices": [0]},
            },
        }

        def delegated(ordinal, turn_id, prompt, call):
            return {
                "ordinal": ordinal,
                "type": "response_item",
                "payload": {
                    "type": "function_call_output",
                    "name": call,
                    "output": (
                        "<codex_delegation>\n"
                        "  <source_thread_id>coordinator-test-id</source_thread_id>\n"
                        "  <input>" + prompt + "</input>\n"
                        "</codex_delegation>"
                    ),
                    "internal_chat_message_metadata_passthrough": {"turn_id": turn_id},
                },
            }

        for role, initial_input in initial_inputs.items():
            with self.subTest(role=role):
                initial = self.run_prompt_builder(
                    context, unit, role=role, role_input=initial_input,
                )
                self.assertEqual(0, initial.returncode, initial.stdout)
                followup_reference = f"delivery-{role}-followup"
                followup_input = json.loads(json.dumps(initial_input))
                followup_input["supplemental_context"] = {
                    "user_decision": "Use option A.",
                    "continuation": "continue_same_task",
                }
                followup = self.run_prompt_builder(
                    context,
                    unit,
                    role=role,
                    role_input=followup_input,
                    reference=followup_reference,
                )
                self.assertEqual(0, followup.returncode, followup.stdout)
                events = [
                    {"ordinal": 0, "type": "session_meta", "payload": {
                        "session_id": "test-thread", "thread_source": "agent_created_thread"}},
                    {"ordinal": 1, "type": "event_msg", "payload": {
                        "type": "task_started", "turn_id": "prior-turn"}},
                    {"ordinal": 2, "type": "turn_context", "payload": {"turn_id": "prior-turn"}},
                    delegated(
                        3,
                        "prior-turn",
                        initial.stdout,
                        "create_thread" if role == "reviewer" else "send_message_to_thread",
                    ),
                    {"ordinal": 4, "type": "event_msg", "payload": {
                        "type": "task_complete", "turn_id": "prior-turn"}},
                    {"ordinal": 5, "type": "event_msg", "payload": {
                        "type": "task_started", "turn_id": "followup-turn"}},
                    {"ordinal": 6, "type": "turn_context", "payload": {"turn_id": "followup-turn"}},
                    delegated(7, "followup-turn", followup.stdout, "send_message_to_thread"),
                    {"ordinal": 8, "type": "turn_context", "payload": {"turn_id": "followup-turn"}},
                ]
                continued = self.run_native_inspector(
                    events, role=role, reference=followup_reference,
                )
                self.assertEqual(0, continued.returncode, continued.stdout)
                self.assertEqual("continue_role", json.loads(continued.stdout)["action"])

                after_compaction = [
                    json.loads(json.dumps(event)) for event in events
                ] + [
                    {"ordinal": 9, "type": "compacted", "payload": {
                        "replacement_history": []}},
                    {"ordinal": 10, "type": "turn_context", "payload": {
                        "turn_id": "followup-turn"}},
                ]
                continued = self.run_native_inspector(
                    after_compaction, role=role, reference=followup_reference,
                )
                self.assertEqual(0, continued.returncode, continued.stdout)
                self.assertEqual("continue_role", json.loads(continued.stdout)["action"])

                wrong_transport = [json.loads(json.dumps(event)) for event in events]
                wrong_transport[7]["payload"]["name"] = "create_thread"
                blocked = self.run_native_inspector(
                    wrong_transport, role=role, reference=followup_reference,
                )
                self.assertEqual(1, blocked.returncode)
                self.assertIn("assignment order", json.loads(blocked.stdout)["diagnostic"])

                compact = [json.loads(json.dumps(event)) for event in events]
                compact[7] = delegated(
                    7,
                    "followup-turn",
                    "unit=W-003/step-2\nanswer=Use option A.\ncontinue_same_task\n",
                    "send_message_to_thread",
                )
                blocked = self.run_native_inspector(
                    compact, role=role, reference=followup_reference,
                )
                self.assertEqual(1, blocked.returncode)
                self.assertIn("assignment", json.loads(blocked.stdout)["diagnostic"])

                if role == "reviewer":
                    unbound = self.run_prompt_builder(
                        context,
                        unit,
                        role=role,
                        role_input=initial_input,
                        reference=followup_reference,
                    )
                    self.assertEqual(0, unbound.returncode, unbound.stdout)
                    unbound_events = [json.loads(json.dumps(event)) for event in events]
                    unbound_events[7] = delegated(
                        7, "followup-turn", unbound.stdout, "send_message_to_thread",
                    )
                    blocked = self.run_native_inspector(
                        unbound_events, role=role, reference=followup_reference,
                    )
                    self.assertEqual(1, blocked.returncode)
                    self.assertIn("assignment order", json.loads(blocked.stdout)["diagnostic"])


    def test_native_context_inspector_freezes_after_delivery_or_final(self):
        result = "SCOVILLE_RESULT_V1\nrole=executor\nstatus=context_handoff\nsummary=completed effects; remaining work"

        delivered = self.run_native_inspector(self.compacted_rollout(delivery=result))
        self.assertEqual(0, delivered.returncode, delivered.stdout)
        self.assertEqual("return_only", json.loads(delivered.stdout)["action"])
        self.assertEqual(result, json.loads(delivered.stdout)["result_text"])

        final_only = self.run_native_inspector(self.compacted_rollout(final=result))
        self.assertEqual(0, final_only.returncode, final_only.stdout)
        self.assertEqual("return_only", json.loads(final_only.stdout)["action"])

        both = self.run_native_inspector(self.compacted_rollout(delivery=result, final=result))
        self.assertEqual(0, both.returncode, both.stdout)
        self.assertEqual("return_only", json.loads(both.stdout)["action"])

        failed_delivery = self.run_native_inspector(
            self.compacted_rollout(delivery=result, final=result, delivery_failed=True)
        )
        self.assertEqual(0, failed_delivery.returncode, failed_delivery.stdout)
        self.assertEqual("return_only", json.loads(failed_delivery.stdout)["action"])

        failed_before_final = self.run_native_inspector(
            self.compacted_rollout(delivery=result, delivery_failed=True)
        )
        self.assertEqual(0, failed_before_final.returncode, failed_before_final.stdout)
        self.assertEqual("return_only", json.loads(failed_before_final.stdout)["action"])
        self.assertEqual(result, json.loads(failed_before_final.stdout)["result_text"])

        unknown_delivery = self.run_native_inspector(
            self.compacted_rollout(delivery=result, delivery_unknown=True)
        )
        self.assertEqual(1, unknown_delivery.returncode)
        self.assertEqual("return_blocked", json.loads(unknown_delivery.stdout)["action"])

        no_result = self.run_native_inspector(self.compacted_rollout())
        self.assertEqual(0, no_result.returncode, no_result.stdout)
        self.assertEqual("continue_role", json.loads(no_result.stdout)["action"])

        mismatch = self.run_native_inspector(
            self.compacted_rollout(
                delivery=result,
                final="SCOVILLE_RESULT_V1\nrole=executor\nstatus=blocked\nsummary=different",
            )
        )
        self.assertEqual(1, mismatch.returncode)
        self.assertEqual("return_blocked", json.loads(mismatch.stdout)["action"])

        unauthenticated = self.compacted_rollout(delivery=result)
        next(
            event for event in unauthenticated
            if event.get("type") == "response_item"
            and event.get("payload", {}).get("type") == "custom_tool_call_output"
        )["payload"]["output"][-1]["text"] = '{"threadId":"different-coordinator"}'
        failed = self.run_native_inspector(unauthenticated)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        unexpected = self.compacted_rollout(delivery=result)
        call = next(
            event for event in unexpected
            if event.get("type") == "response_item"
            and event.get("payload", {}).get("type") == "custom_tool_call"
        )
        call["payload"]["input"] = call["payload"]["input"].replace(
            "workflow_result_delivery=delivery-test",
            "ordinary message",
        )
        failed = self.run_native_inspector(unexpected)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        for delivered_result, expected_action in ((None, "return_only"), (result, "return_only")):
            repeated = self.compacted_rollout(delivery=delivered_result, final=result)
            latest = repeated[-1]["ordinal"]
            repeated.extend([
                {"ordinal": latest + 1, "type": "compacted", "payload": {"replacement_history": []}},
                {"ordinal": latest + 2, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
            ])
            replay = self.run_native_inspector(repeated)
            self.assertEqual(0, replay.returncode, replay.stdout)
            self.assertEqual(expected_action, json.loads(replay.stdout)["action"])

        delayed_final = self.compacted_rollout()
        latest = delayed_final[-1]["ordinal"]
        delayed_final.extend([
            {
                "ordinal": latest + 1,
                "type": "event_msg",
                "payload": {
                    "type": "item_completed",
                    "thread_id": "test-thread",
                    "turn_id": "turn-1",
                    "item": {"type": "AgentMessage", "id": "delayed-final", "phase": "final_answer"},
                },
            },
            {
                "ordinal": latest + 2,
                "type": "response_item",
                "payload": {
                    "type": "message",
                    "id": "delayed-final",
                    "role": "assistant",
                    "phase": "final_answer",
                    "content": [{"type": "output_text", "text": result}],
                },
            },
            {"ordinal": latest + 3, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
        ])
        replay = self.run_native_inspector(delayed_final)
        self.assertEqual(0, replay.returncode, replay.stdout)
        self.assertEqual("return_only", json.loads(replay.stdout)["action"])

        wrong_thread = self.compacted_rollout(final=result)
        next(
            event for event in wrong_thread
            if event.get("type") == "event_msg"
            and event.get("payload", {}).get("item", {}).get("type") == "AgentMessage"
        )["payload"]["thread_id"] = "wrong-thread"
        failed = self.run_native_inspector(wrong_thread)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        wrong_replacement = self.compacted_rollout(final=result)
        next(event for event in wrong_replacement if event.get("type") == "compacted")["payload"][
            "replacement_message_id"
        ] = "different-final"
        failed = self.run_native_inspector(wrong_replacement)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        gap_final = self.compacted_rollout()
        compaction = next(event for event in gap_final if event.get("type") == "compacted")
        resumed = gap_final[-1]
        resumed["ordinal"] += 2
        gap_final.extend([
            {
                "ordinal": compaction["ordinal"] + 1,
                "type": "event_msg",
                "payload": {
                    "type": "item_completed",
                    "thread_id": "test-thread",
                    "turn_id": "turn-1",
                    "item": {"type": "AgentMessage", "id": "gap-final", "phase": "final_answer"},
                },
            },
            {
                "ordinal": compaction["ordinal"] + 2,
                "type": "response_item",
                "payload": {
                    "type": "message",
                    "id": "gap-final",
                    "role": "assistant",
                    "phase": "final_answer",
                    "content": [{"type": "output_text", "text": result}],
                },
            },
        ])
        gap_final.sort(key=lambda event: event["ordinal"])
        failed = self.run_native_inspector(gap_final)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        metadata_only = [
            {"ordinal": 0, "type": "session_meta", "payload": {"session_id": "test-thread"}},
            {"ordinal": 1, "type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1"}},
        ]
        failed = self.run_native_inspector(metadata_only)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        missing_prior_context = [
            {"ordinal": 0, "type": "session_meta", "payload": {"session_id": "test-thread"}},
            {"ordinal": 1, "type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1"}},
            {"ordinal": 2, "type": "compacted", "payload": {"replacement_history": []}},
            {"ordinal": 3, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
        ]
        failed = self.run_native_inspector(missing_prior_context)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        fresh = [
            {"ordinal": 0, "type": "session_meta", "payload": {"session_id": "test-thread"}},
            {"ordinal": 1, "type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1"}},
            {"ordinal": 2, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
        ]
        continued = self.run_native_inspector(fresh)
        self.assertEqual(0, continued.returncode, continued.stdout)
        self.assertEqual("continue_role", json.loads(continued.stdout)["action"])

        wrong_native_final = self.compacted_rollout(final=result)
        next(
            event for event in wrong_native_final
            if event.get("type") == "response_item"
            and event.get("payload", {}).get("type") == "message"
        )["payload"]["internal_chat_message_metadata_passthrough"] = {"turn_id": "wrong-turn"}
        failed = self.run_native_inspector(wrong_native_final)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        wrong_native_delivery = self.compacted_rollout(delivery=result)
        next(
            event for event in wrong_native_delivery
            if event.get("type") == "response_item"
            and event.get("payload", {}).get("type") == "custom_tool_call_output"
        )["payload"]["internal_chat_message_metadata_passthrough"] = {"turn_id": "wrong-turn"}
        failed = self.run_native_inspector(wrong_native_delivery)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("return_blocked", json.loads(failed.stdout)["action"])

        prior_result = "SCOVILLE_RESULT_V1\nrole=executor\nstatus=needs_user_decision\nsummary=choose"
        prior_history = [
            {"ordinal": 0, "type": "session_meta", "payload": {"session_id": "test-thread"}},
            {"ordinal": 1, "type": "event_msg", "payload": {"type": "task_started", "turn_id": "prior-turn"}},
            {"ordinal": 2, "type": "turn_context", "payload": {"turn_id": "prior-turn"}},
            {
                "ordinal": 3,
                "type": "event_msg",
                "payload": {
                    "type": "item_completed",
                    "thread_id": "test-thread",
                    "turn_id": "prior-turn",
                    "item": {"type": "AgentMessage", "id": "prior-final", "phase": "final_answer"},
                },
            },
            {
                "ordinal": 4,
                "type": "response_item",
                "payload": {
                    "type": "message",
                    "id": "prior-final",
                    "role": "assistant",
                    "phase": "final_answer",
                    "content": [{"type": "output_text", "text": prior_result}],
                    "internal_chat_message_metadata_passthrough": {"turn_id": "prior-turn"},
                },
            },
            {"ordinal": 5, "type": "event_msg", "payload": {"type": "task_complete", "turn_id": "prior-turn"}},
            {"ordinal": 6, "type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1"}},
            {"ordinal": 7, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
            {
                "ordinal": 8,
                "type": "compacted",
                "payload": {
                    "replacement_history": [{
                        "type": "message",
                        "id": "prior-final",
                        "role": "assistant",
                        "phase": "final_answer",
                        "content": [{"type": "output_text", "text": prior_result}],
                        "internal_chat_message_metadata_passthrough": {"turn_id": "prior-turn"},
                    }],
                },
            },
            {"ordinal": 9, "type": "turn_context", "payload": {"turn_id": "turn-1"}},
        ]
        continued = self.run_native_inspector(prior_history)
        self.assertEqual(0, continued.returncode, continued.stdout)
        self.assertEqual("continue_role", json.loads(continued.stdout)["action"])

    def test_prompt_builder_is_utf8_safe_and_repair_assignment_is_exact(self):
        unit = "W-003/step-2"
        context = self.dispatch_context(unit, ["2. Prüfe 日本語 paths."])
        valid_repair = {
            "reviewer_result": {
                "status": "changes_requested",
                "summary": "Ändere nur den Befund.",
                "findings": ["Korrigiere 日本語."],
            },
            "repair_assignment": {"finding_indices": [0]},
        }
        completed = self.run_prompt_builder(context, unit, role="repair", role_input=valid_repair)
        self.assertEqual(0, completed.returncode, completed.stdout)
        self.assertIn("日本語", completed.stdout)

        missing = self.run_prompt_builder(
            context,
            unit,
            role="repair",
            role_input={"reviewer_result": valid_repair["reviewer_result"]},
        )
        self.assertEqual(1, missing.returncode)
        self.assertEqual("REPAIR_ASSIGNMENT_REQUIRED", json.loads(missing.stdout)["diagnostics"][0]["code"])

    def test_entrypoint_is_small_and_has_one_runtime_owner(self):
        skill_source = SKILL.read_text(encoding="utf-8")
        skill = flat(SKILL)
        self.assertEqual(
            [
                "First operation: role gate",
                "Prompt writing",
                "Complete coordinator startup",
                "Coordinator boundary",
                "Dispatch routing",
                "Coordinator runtime reference",
            ],
            level_two_headings(SKILL),
        )
        self.assertLess(len((ROOT / "scoville-workflow-for-codex/SKILL.md").read_bytes()), 18_000)
        self.assertIn("from its canonical source files", skill)
        for duplicated_contract in (
            "last_token_usage.input_tokens",
            "`changes_requested`",
            "`wait_threads`",
            "`send_message_to_thread`",
            "`git diff --no-index`",
            "complete the item, Plan, and `PROJECT_INDEX.md` together",
        ):
            self.assertNotIn(duplicated_contract, skill)

    def test_explicit_launcher_and_native_local_tasks(self):
        skill = SKILL.read_text(encoding="utf-8")
        launcher = (PACKAGE / "references" / "launcher.md").read_text(encoding="utf-8")
        operations = flat(OPERATIONS)
        metadata = (PACKAGE / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: false", metadata)
        for trigger in ("$scoville-workflow-for-codex", "Scoville Workflow Codex", "scoflow codex", "$scw"):
            self.assertIn(trigger, skill)
        self.assertIn("before commentary, project\nreads, Skill selection or another tool call", skill)
        self.assertIn("[launcher.md](references/launcher.md)", skill)
        self.assertIn("scripts/task_lifecycle.md", launcher)
        self.assertIn("scripts/manage_workflow_guard.py acquire", launcher)
        self.assertNotIn("coordinator_task_id=", launcher.split("## Activate", 1)[0])
        parking_fields = ["scoville_role=coordinator", "coordinator_start=initial_parking",
                          "workflow_id=<exact launcher CODEX_THREAD_ID>", "workspace_root=<exact workflow workspace>",
                          "workspace_mode=shared_local OR workspace_mode=isolated_worktree",
                          "saved_project_id=<exact saved project ID>", "Perform no project or Plan access"]
        parking_positions = [launcher.index(field) for field in parking_fields]
        self.assertEqual(sorted(parking_positions), parking_positions)
        activation_fields = ["scoville_role=coordinator", "coordinator_start=initial_claim",
                             "coordinator_task_id=<reconciled ready threadId>",
                             "guard_revision=<revision returned by reconcile-coordinator>",
                             "coordinator_generation=0", "project_root=<absolute project path>",
                             "workspace_root=<exact workflow workspace>", "saved_project_id=<exact saved project ID>",
                             "requested_scope=whole_active_plan", "continuation_intent=resume_active_plan",
                             "plan=<canonical Plan reference> OR objective=<task substance only>"]
        activation = launcher.split("## Activate", 1)[1]
        activation_positions = [activation.index(field) for field in activation_fields]
        self.assertEqual(sorted(activation_positions), activation_positions)
        self.assertIn('environment: { type: "local" }', launcher)
        self.assertIn("`projectId` is invalid outside `target`", launcher)
        self.assertIn("`rollover_validation` never consume `continuation_intent`", operations)

    def test_all_tasks_reuse_one_disclosed_workspace(self):
        skill = flat(SKILL)
        launcher = (PACKAGE / "references" / "launcher.md").read_text(encoding="utf-8")
        operations = flat(OPERATIONS)
        self.assertIn('`SCW <unit> WORK|REVIEW|REPAIR RUN [#<N>]`', operations)
        for text in (launcher, operations):
            self.assertIn('environment: { type: "local" }', text)
        self.assertIn("exact `workspace_root`", operations)
        for field in ("workspace_mode=shared_local OR workspace_mode=isolated_worktree",
                      "workspace_root=<exact workflow workspace>",
                      "workspace_return=none OR workspace_return=<authorized reintegration method>",
                      "workspace_non_inherited=none OR workspace_non_inherited=<state not guaranteed to transfer>"):
            self.assertIn(field, launcher)
        self.assertIn("Never fork a prior task, select a new worktree or reconstruct shared workspace state", operations)
        self.assertIn("uncommitted changes", operations.lower())
        self.assertIn("uses that same workspace and saved project", operations)
        self.assertIn(
            "same unit, role, launched model, launched reasoning, authorization, remaining work, logical attempt, `workspace_mode`, and exact `workspace_root`",
            operations,
        )

    def test_routes_are_complete_and_supported(self):
        config_path = PACKAGE / "assets" / "workflow.toml"
        with config_path.open("rb") as stream:
            config = tomllib.load(stream)
        self.assertEqual(set(config), {"schema_version", "coordinator", "execute", "review", "context", "prompting"})
        self.assertEqual(config["schema_version"], 1)
        self.assertEqual(set(config["execute"]), ROUTE_CLASSES)
        self.assertEqual(set(config["review"]), ROUTE_CLASSES)
        for table in ("execute", "review"):
            for pair in config[table].values():
                self.assertEqual(set(pair), {"model", "reasoning"})
                self.assertIn(pair["model"], SUPPORTED_MODELS)
                self.assertIn(pair["reasoning"], SUPPORTED_EFFORTS)
        self.assertEqual(
            config["coordinator"],
            {
                "model": "gpt-6-sol",
                "reasoning": "medium",
                "title": "SCW COORD",
            },
        )
        config_text = config_path.read_text(encoding="utf-8")
        for retired in ("[limits]", "max_repairs_per_unit", "handoff_target_chars", "handoff_hard_chars"):
            self.assertNotIn(retired, config_text)
        operations = flat(OPERATIONS)
        self.assertIn("Summary contains 1 to 800 characters", operations)
        self.assertIn("Each finding contains 1 to 400 characters", operations)
        self.assertIn("Combined summary and findings target 2,000 and must not exceed 4,000 characters", operations)

    def test_workflow_toml_drives_modeled_call_construction(self):
        with (PACKAGE / "assets" / "workflow.toml").open("rb") as stream:
            config = tomllib.load(stream)
        changed = {
            "schema_version": config["schema_version"],
            "coordinator": {"title": "Changed Coordinator", "model": "gpt-6-astra", "reasoning": "high"},
            "execute": {route: dict(pair) for route, pair in config["execute"].items()},
            "review": {route: dict(pair) for route, pair in config["review"].items()},
        }
        cycle_models = ["gpt-6-luna", "gpt-6-sol", "gpt-6-sol", "gpt-6-astra", "gpt-6-luna"]
        cycle_efforts = ["low", "medium", "high", "low", "high"]
        for index, route in enumerate(sorted(ROUTE_CLASSES)):
            changed["execute"][route] = {"model": cycle_models[index], "reasoning": cycle_efforts[index]}
            changed["review"][route] = {"model": cycle_models[-index - 1], "reasoning": cycle_efforts[-index - 1]}

        self.assertEqual(
            model_create_call(changed, "coordinator"),
            {"title": "Changed Coordinator", "model": "gpt-6-astra", "thinking": "high"},
        )
        for route in ROUTE_CLASSES:
            self.assertEqual(model_create_call(changed, "executor", route)["model"], changed["execute"][route]["model"])
            self.assertEqual(model_create_call(changed, "reviewer", route)["thinking"], changed["review"][route]["reasoning"])

        default = model_create_call(changed, "executor", "medium")
        model_only = model_create_call(changed, "executor", "medium", {"model": "gpt-6-astra"})
        reasoning_only = model_create_call(changed, "executor", "medium", {"reasoning": "high"})
        both = model_create_call(changed, "executor", "medium", {"model": "gpt-6-luna", "reasoning": "low"})
        self.assertEqual(model_only, {"model": "gpt-6-astra", "thinking": default["thinking"]})
        self.assertEqual(reasoning_only, {"model": default["model"], "thinking": "high"})
        self.assertEqual(both, {"model": "gpt-6-luna", "thinking": "low"})
        self.assertEqual(model_create_call(changed, "reviewer", "medium"), {"model": changed["review"]["medium"]["model"], "thinking": changed["review"]["medium"]["reasoning"]})
        self.assertEqual(model_create_call(changed, "repair", launched=both), both)
        self.assertEqual(model_create_call(changed, "rollover", launched=both), both)
        with self.assertRaises(ValueError):
            model_create_call(changed, "executor", "medium", {"model": "unsupported"})

    def test_model_resolver_escalates_new_repairs_without_changing_review(self):
        config = model_resolver.load_config(PACKAGE / "assets" / "workflow.toml")
        routes = model_resolver.ROUTES
        for base_index, route in enumerate(routes):
            original = model_create_call(config, "executor", route)
            reviewer = model_create_call(config, "reviewer", route)
            for repair_number in (1, 2, 3):
                with self.subTest(route=route, repair_number=repair_number):
                    target = routes[min(base_index + repair_number - 1, len(routes) - 1)]
                    expected = original if repair_number == 1 else model_create_call(config, "executor", target)
                    self.assertEqual(
                        model_create_call(config, "repair", launched=original, repair_number=repair_number),
                        expected,
                    )
                    self.assertEqual(model_create_call(config, "reviewer", route), reviewer)

        custom = {**config, "execute": {key: dict(value) for key, value in config["execute"].items()}}
        custom["execute"]["ultra_high"] = {"model": "gpt-6-astra", "reasoning": "xhigh"}
        medium = model_create_call(custom, "executor", "medium")
        self.assertEqual(
            model_create_call(custom, "repair", launched=medium, repair_number=3),
            {"model": "gpt-6-astra", "thinking": "xhigh"},
        )
        override = model_create_call(config, "executor", "medium", {"model": "gpt-6-astra", "reasoning": "low"})
        self.assertEqual(model_create_call(config, "repair", launched=override), override)
        with self.assertRaisesRegex(ValueError, "outside the WORK route table"):
            model_create_call(config, "repair", launched=override, repair_number=2)
        with self.assertRaisesRegex(ValueError, "invalid original pair or repair number"):
            model_create_call(config, "repair", launched=medium, repair_number=4)

    def test_model_resolver_rejects_malformed_user_config(self):
        source = (PACKAGE / "assets" / "workflow.toml").read_text(encoding="utf-8")
        for altered, diagnostic in (
            (source.replace('schema_version = 1', 'schema_version = true', 1), "schema_version"),
            (source.replace('reasoning = "low"', 'reasoning = []', 1), "invalid execute.ultra_low values"),
            (source.replace('reasoning = "low"', 'reasoning = { bad = true }', 1), "invalid execute.ultra_low values"),
        ):
            with self.subTest(diagnostic=diagnostic), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "workflow.toml"
                path.write_text(altered, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, diagnostic):
                    model_resolver.load_config(path)

    def test_dispatch_preflight_rechecks_guard_after_bounded_selection(self):
        contract = {"installed": True}
        guard = {"ok": True, "authorized": True, "workflow_id": "wf", "revision": 7, "generation": 2}
        selection = {"plan": {}, "work_item": {}, "direct_dependencies": [], "decisions": []}
        calls = []

        def runner(command):
            calls.append(command)
            return [contract, guard, selection, guard][len(calls) - 1]

        result = dispatch_preflight.inspect(Path("workspace"), Path("plan"), Path("selector.py"),
                                             "wf", 7, 2, "W-001", runner)
        self.assertTrue(result["valid"])
        self.assertEqual(result["selection"], selection)
        self.assertEqual([Path(call[1]).name for call in calls],
                         ["manage_agents_contract.py", "manage_workflow_guard.py",
                          "selector.py", "manage_workflow_guard.py"])
        self.assertEqual(calls[2][-2:], ["--work-item", "W-001"])

        calls.clear()

        def changed_runner(command):
            calls.append(command)
            return [contract, guard, selection, {**guard, "revision": 8}][len(calls) - 1]

        with self.assertRaisesRegex(ValueError, "not authorized at the expected revision"):
            dispatch_preflight.inspect(Path("workspace"), Path("plan"), Path("selector.py"),
                                       "wf", 7, 2, runner=changed_runner)

        calls.clear()

        def malformed_runner(command):
            calls.append(command)
            return [contract, guard, {"plan": {}}][len(calls) - 1]

        with self.assertRaisesRegex(ValueError, "four required semantic areas"):
            dispatch_preflight.inspect(Path("workspace"), Path("plan"), Path("selector.py"),
                                       "wf", 7, 2, runner=malformed_runner)
        self.assertEqual(len(calls), 3)

        calls.clear()

        def missing_contract(command):
            calls.append(command)
            return {"installed": False}

        with self.assertRaisesRegex(ValueError, "project contract is not installed"):
            dispatch_preflight.inspect(Path("workspace"), Path("plan"), Path("selector.py"),
                                       "wf", 7, 2, runner=missing_contract)
        self.assertEqual(len(calls), 1)

    def test_dispatch_preflight_preserves_real_selector_diagnostic(self):
        selector = ROOT.parent / "scoville-plan" / "scoville-plan" / "scripts" / "select_context.py"
        with tempfile.TemporaryDirectory(prefix="workflow-preflight-selector-") as directory:
            missing = Path(directory) / "missing-plan"
            with self.assertRaises(dispatch_preflight.HelperFailure) as failure:
                dispatch_preflight.call_json([
                    sys.executable, str(selector), "--root", str(missing), "--format", "json",
                ])
        self.assertEqual(failure.exception.payload["diagnostics"][0]["code"], "ROOT_MISSING")
        self.assertEqual(failure.exception.payload["diagnostics"][0]["message"],
                         "root must be an existing directory")

    def test_explicit_resume_intent_skips_only_the_initial_choice(self):
        operations = flat(OPERATIONS)
        self.assertIn("continuation_intent=resume_active_plan", operations)
        self.assertIn("continue the active Plan immediately", operations)
        self.assertIn("directly to the same coordinator to continue or resume", operations)
        self.assertIn("continuation_intent=unspecified", operations)
        self.assertIn("genuine unresolved scope, authorization, blocker, or lifecycle decision", operations)

    def test_point_execution_overrides_preserve_risk_and_reviewer_routing(self):
        skill = flat(OPERATIONS)
        operations = flat(OPERATIONS)
        self.assertIn("treat that class as the planned minimum", skill)
        self.assertIn("Check the classes from `ultra_high` down to `ultra_low`", skill)
        self.assertIn("raise the effective dispatch route when the annotation was too low or incomplete", skill)
        self.assertIn("never dispatch below it", skill)
        self.assertIn("Do not reclassify a repair or context-rollover continuation", skill)
        self.assertIn("no diagnosis across component or test-harness boundaries", skill)
        self.assertIn("nontrivial local implementation judgment or verification", skill)
        self.assertIn("Use `ultra_low` only when none of `medium`, `high`, or `ultra_high` applies", skill)
        self.assertIn("helper or mock availability across a harness boundary", skill)
        self.assertIn("unresolved helper contract or required local diagnostic discovery", skill)
        self.assertIn("`low` is allowed only when every low criterion is positively established", skill)
        self.assertIn("If any one of these facts is false or unknown, use at least `medium`", skill)
        self.assertIn("preserve a contract across languages or components", skill)
        self.assertIn("A simple verb such as add, rename, comment, document, or test is not evidence for `low`", skill)
        self.assertIn("Route class, model, and reasoning level are separate decisions", skill)
        self.assertIn("even when no fact changed after planning", operations)
        self.assertIn("every low criterion is positively established", operations)
        self.assertIn("If any one of these facts is false or unknown, use at least `medium`", operations)
        self.assertIn("Keep classification transient", operations)
        self.assertIn("consequential changes to state, authorization, or integration contracts", operations)
        self.assertIn("Many files, generated metadata, or a known large test suite alone do not raise the route", operations)
        self.assertIn("selected Step's strict `[execute: ...]` annotation", skill)
        self.assertIn("overrides the matching route-default property", skill)
        self.assertIn("block the unit rather than substitute", skill)
        self.assertIn("point overrides never affect coordinator or reviewer routing", skill)
        self.assertIn("property-wise", operations)
        self.assertIn("malformed or unsupported effective pair blocks that unit", operations)

        # The README links to configuration rather than duplicating its table.
        config = tomllib.loads((PACKAGE / "assets/workflow.toml").read_text(encoding="utf-8"))
        expected = {
            "ultra_low": (("gpt-6-sol", "low"), ("gpt-6-sol", "medium")),
            "low": (("gpt-6-sol", "medium"), ("gpt-6-sol", "high")),
            "medium": (("gpt-6-sol", "high"), ("gpt-6-sol", "xhigh")),
            "high": (("gpt-6-sol", "xhigh"), ("gpt-6-astra", "high")),
            "ultra_high": (("gpt-6-astra", "high"), ("gpt-6-astra", "xhigh")),
        }
        self.assertEqual(("gpt-6-sol", "medium"),
                         (config["coordinator"]["model"], config["coordinator"]["reasoning"]))
        for route, pairs in expected.items():
            for role, pair in zip(("execute", "review"), pairs):
                self.assertEqual(pair, (config[role][route]["model"], config[role][route]["reasoning"]))

    def test_plan_selection_is_exact_and_never_falls_back(self):
        operations = flat(OPERATIONS)
        self.assertIn(
            "python <plan-skill-directory>/scripts/select_context.py --root <plan_root> [--work-item W-001] --format json",
            operations,
        )
        for field in ("`plan`", "`work_item`", "`direct_dependencies`", "`decisions`"):
            self.assertIn(field, operations)
        self.assertIn("exactly these four top-level semantic areas", operations)
        self.assertIn("It never embeds this recovery object in a child prompt", operations)
        self.assertIn("--unit <exact-unit> --format json", operations)
        self.assertIn("range form is valid only when `M > N`", operations)
        self.assertIn("Reject a same-number or reversed range before dispatch", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Dispatch-unit identifier scenarios"),
            {
                "`W-001`": ("Valid Step-less Work Item unit",),
                "`W-001/step-2`": ("Valid single-Step unit",),
                "`W-001/steps-2-3`": ("Valid forward range containing at least two Steps",),
                "`W-001/steps-2-2`": ("Reject before dispatch",),
                "`W-001/steps-3-2`": ("Reject before dispatch",),
            },
        )
        self.assertIn("For Step units it contains no Work Item Evidence, unselected Step, or Work Item-wide `Next action`", operations)
        self.assertIn("A whole-item unit without Steps retains `Next action`", operations)
        self.assertIn("coordinator never filters Decisions", operations)
        self.assertIn("Send the retained reviewer prompt unchanged at creation", operations)
        self.assertIn("predicted next guard revision", operations)
        self.assertIn("send it unchanged only after activation returns that exact revision", operations)
        self.assertIn("unassigned-parking case", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Writer activation scenarios"),
            {
                "Reconciled writer is pending and no failure occurred": (
                    "Build the complete prompt for the predicted next revision; do not archive or activate yet",
                ),
                "Prompt construction definitely failed before activation": (
                    "Archive and verify the exact unassigned parked task, clear its pending authorization, then record the blocker",
                ),
                "Activation definitely failed and the guard remains pending": (
                    "Use the same unassigned-parking cleanup",
                ),
                "Activation outcome is unknown": (
                    "Send nothing, archive nothing, clear nothing, and reconcile the exact guard state",
                ),
                "Activation returned the exact predicted revision": (
                    "Announce the phase and send the already-built prompt unchanged",
                ),
                "Pending child acted before activation": (
                    "Record a blocker and never grant write authority",
                ),
            },
        )
        self.assertIn("never use a raw-file fallback", operations)
        self.assertIn("becomes one coordinator-owned Plan blocker", operations)
        self.assertNotIn("Get-Content -Raw", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Plan context scenarios"),
            {
                "Coordinator current or named Work Item": (
                    "Selector success",
                    "Exactly the four semantic areas for unit formation",
                ),
                "Work Item without Steps": (
                    "Prompt-helper success for `W-NNN`",
                    "Complete unchanged whole-item source_text including Evidence and all referenced Decisions",
                ),
                "Work Item with Steps": (
                    "Prompt-helper success for exact Step or adjacent range",
                    "Only selected Step text all referenced Decisions and no Evidence",
                ),
                "Reviewer or repair": (
                    "Prompt-helper success plus validated role input",
                    "Same exact unit plus only the required prior result object",
                ),
                "Unrelated proposed Decision": (
                    "Separate Decision-frontmatter inventory",
                    "Keep ID/status discoverable; read contents only if relevant or during a full audit",
                ),
                "Relevant dependency Evidence": (
                    "Separate complete dependency block",
                    "Use only for that preflight",
                ),
                "Queued successor": (
                    "Separate bounded graph and title view",
                    "Resolve authored order without Work Item bodies",
                ),
                "Paused return target": (
                    "Separate complete named blocks",
                    "Preserve the recorded return state",
                ),
                "One-MiB Plan with small selected item": (
                    "Selector success",
                    "Same selected facts without unrelated bodies",
                ),
                "Missing helper malformed boundary or budget overflow": (
                    "Structured selector diagnostic or invocation diagnostic",
                    "Record one blocker with no raw fallback",
                ),
            },
        )

    def test_adjacent_steps_bundle_only_at_one_behavior_boundary(self):
        operations = flat(OPERATIONS)
        self.assertIn("`Steps` is optional: absence means the complete Work Item is one unit", operations)
        self.assertIn("presence requires a non-empty consecutive numbered block", operations)
        self.assertIn("named-unit selector then independently rejects", operations)
        self.assertIn(
            "(outcome, owner, authorization, route, effective executor pair, workspace, Acceptance boundary)",
            operations,
        )
        self.assertIn("maximal authored-order prefix of adjacent unperformed Steps", operations)
        self.assertIn("only when a referenced accepted Decision explicitly authorizes compatible-Step bundling", operations)
        self.assertIn("Never bundle across Work Items", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Step-bundle scenarios"),
            {
                "Five adjacent Steps share all seven compatibility facts": (
                    "One executor for the five-Step range",
                    "At most one initial reviewer",
                ),
                "Adjacent Step changes route or material risk": (
                    "Split before that Step",
                    "Each resulting behavior boundary",
                ),
                "Adjacent Step changes effective executor model or reasoning": (
                    "Split before that Step",
                    "Reviewer still follows each unit's route class",
                ),
                "Adjacent Step changes Decision or authorization": (
                    "Split before that Step",
                    "Each resulting behavior boundary",
                ),
                "Adjacent Step starts a separately authorized external effect": (
                    "Split before that Step",
                    "External-effect result stays isolated",
                ),
                "Adjacent Step has an independently resumable result": (
                    "Split before that Step",
                    "Independent Acceptance ownership",
                ),
                "Adjacent Step changes owner or workspace": (
                    "Split before that Step",
                    "Each owner or workspace boundary",
                ),
                "Work Item has no Steps": (
                    "One executor for the complete Work Item",
                    "One behavior boundary",
                ),
            },
        )

    def test_scope_continues_without_per_unit_confirmation(self):
        operations = flat(OPERATIONS)
        self.assertIn("`whole_active_plan` includes every nonterminal item", operations)
        self.assertIn("without another confirmation", operations)
        self.assertIn("continues the next eligible unit", operations)
        self.assertIn("remaining dispatch units in the current Work Item", operations)
        self.assertIn("only for `needs_user_decision`", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Continuation scenarios"),
            {
                "W-001 point A accepted while point B remains and scope is W-001": (
                    "Dispatch W-001 point B",
                    "No",
                    "Yes",
                ),
                "W-001 terminal and W-002 is eligible in whole-Plan scope": (
                    "Dispatch W-002 first unit",
                    "No",
                    "Yes",
                ),
                "Explicit boundary through W-003 is accepted": (
                    "Emit boundary completion",
                    "Completion only",
                    "Yes",
                ),
                "W-001 unit blocked while independent W-002 is eligible": (
                    "Record W-001 blocker and dispatch W-002",
                    "No",
                    "Yes",
                ),
                "W-001 is blocked after a HEAD-bound backup and source edit while W-002 is otherwise eligible": (
                    "Preserve the interval and ask before W-002 dispatch or commit",
                    "User decision",
                    "Yes",
                ),
                "W-001 required pair unavailable while independent W-002 is eligible": (
                    "Record W-001 blocker and dispatch W-002 with its configured pair",
                    "No",
                    "Yes",
                ),
                "Blocker leaves no eligible in-scope unit": (
                    "Ask exact disposition decision",
                    "User decision",
                    "Yes",
                ),
                "User explicitly says stop": (
                    "Forward Stop and reconcile Plan",
                    "User cancellation",
                    "Yes",
                ),
            },
        )

    def test_prompt_helper_embeds_exact_unit_without_coordinator_prose(self):
        operations = flat(OPERATIONS)
        self.assertIn("`scripts/build_dispatch_prompt.py` helper", operations)
        self.assertIn("its envelope contains the same byte-for-byte native task prompt", operations)
        self.assertIn("capture only that process's stdout", operations)
        self.assertIn("Never combine it with configuration reads, diagnostics, shell transcripts", operations)
        self.assertIn("Immediately before sending any helper-built prompt", operations)
        self.assertIn("Apply this at reviewer creation, at executor or repair assignment", operations)
        self.assertIn("and at every same-task continuation", operations)
        self.assertIn("same-task reviewer continuation, or to lifecycle `create` for a new reviewer", operations)
        self.assertIn("Routing configuration selects the native task call and never appears in the child prompt", operations)
        self.assertIn("Add no summary, handoff prose, rationale, restatement", operations)
        self.assertIn("The executor must not run the Plan selector or prompt builder", operations)
        self.assertIn("Apply no prompt character target or hard limit", operations)
        self.assertIn("a reviewer receives `executor_result`", operations)
        self.assertIn("a repair receives `reviewer_result`", operations)
        self.assertIn("no Work Item Evidence, unselected Step, or Work Item-wide `Next action`", operations)
        self.assertNotIn("The Plan path and unit ID are sufficient", operations)
        self.assertNotIn("8,000-character hard limit", operations)
        self.assertNotIn("supplies only missing turn-specific facts", operations)

    def test_results_waits_and_decisions_are_compact(self):
        operations = flat(OPERATIONS)
        self.assertIn("never stage, commit, push, or rewrite history", operations)
        self.assertIn("The first line is exactly `SCOVILLE_RESULT_V1`", operations)
        self.assertIn("Remaining lines use `key=value`", operations)
        self.assertIn("The helper is the only result parser", operations)
        self.assertIn("`code_changed` is `yes` for changes to source, tests, executable scripts", operations)
        self.assertIn("`critical_docs_changed` is `yes` when changed documentation materially governs", operations)
        self.assertIn("inspect the actual final changed result", operations)
        self.assertIn("Every executor and repair prompt includes these definitions", operations)
        self.assertIn("A second invalid result is a blocker", operations)
        self.assertIn("call `wait_threads` for exactly that child with a timeout", operations)
        self.assertIn("targets: [{threadId: exact_child_id, hostId: exact_host_id,", operations)
        self.assertIn("afterCursor: latest_cursor", operations)
        self.assertIn("timeoutMs: 60000", operations)
        self.assertIn("Omit `afterCursor` only before the first cursor exists", operations)
        self.assertIn("Never use `read_thread` as this wait loop", operations)
        self.assertIn("Do not read an active child conversation", operations)
        self.assertIn("send_message_to_thread", operations)
        self.assertIn("same task ID", operations)
        self.assertIn("Archive every terminal task immediately", operations)

    def test_completed_result_payload_recovery_is_identity_bound(self):
        operations = flat(OPERATIONS)
        self.assertIn("Treat the assistant-message text from `wait_threads` as the candidate payload", operations)
        self.assertIn("exactly one `read_thread` call", operations)
        self.assertIn("`turnLimit: 1`, `includeOutputs: false`, and `maxOutputCharsPerItem: 6000`", operations)
        self.assertIn("Select exactly one active or archived rollout whose session identity equals the recorded child task ID", operations)
        self.assertIn("Require exactly one `session_meta` whose session ID equals the recorded child task ID", operations)
        self.assertIn("events need only carry the exact wait-turn ID and inherit the verified file session", operations)
        self.assertIn("then bind its item ID to exactly one assistant `response_item`", operations)
        self.assertIn("The `response_item` itself need not carry a top-level turn ID", operations)
        self.assertIn("Ignore tool output, commentary, reasoning, user text, and results quoted only", operations)
        self.assertIn("Keep the wait cursor and native state authoritative", operations)
        self.assertIn("Never use this read for an already matching valid candidate, an active or nonterminal child", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Result payload recovery scenarios"),
            {
                "Valid `wait_threads` payload": (
                    "None",
                    "Validate the wait payload normally",
                ),
                "Completed projection differs from authenticated delivery": (
                    "Read the exact completed turn once",
                    "Automatically use unchanged source bytes only if they exactly equal delivery and all identity/protocol checks pass; otherwise retain the conflict",
                ),
                "Invalid completed payload with matching valid source message": (
                    "Read the newest completed turn once",
                    "Validate the recovered message text and retain wait state and cursor",
                ),
                "Both task APIs omit one exact completed result and the exact rollout has one matching final message": (
                    "Read the exact native rollout once",
                    "Validate only its message bytes and retain wait state and cursor",
                ),
                "Exact candidate exists but its bytes are malformed": (
                    "One API read and if needed one exact-rollout read",
                    "Send one same-task formatting correction",
                ),
                "Identity ordering absence ambiguity or truncation remains": (
                    "One API read and if eligible one exact-rollout read",
                    "Archive as terminal failure and record a blocker without success transitions",
                ),
                "Active or nonterminal child": (
                    "None",
                    "Return to the same exact-child wait loop with the saved cursor",
                ),
            },
        )

    def test_retained_divi_rollouts_recover_only_the_exact_completed_turns(self):
        fixture = json.loads(NATIVE_FIXTURES.read_text(encoding="utf-8"))["divi_omitted_results"]
        self.assertEqual(fixture["fixture_kind"], "sanitized_minimal_native_projection")
        self.assertEqual(
            [event["session_id"] for event in fixture["events"] if event["record_type"] == "session_meta"],
            [fixture["session_id"]],
        )
        self.assertTrue(all(
            "thread_id" not in event
            for event in fixture["events"]
            if event.get("payload_type") in {"task_started", "task_complete"}
        ))
        recovered = [recover_exact_rollout_turn(fixture["session_id"], fixture, turn) for turn in fixture["turns"]]
        self.assertEqual([item["turn_id"] for item in recovered], [turn["turn_id"] for turn in fixture["turns"]])
        self.assertEqual(len({item["message_id"] for item in recovered}), 2)
        self.assertEqual([item["requires_reconcile"] for item in recovered], [True, False])

        mirrored = json.loads(json.dumps(fixture))
        mirrored["events"].append({
            "ordinal": 229,
            "record_type": "replacement_message",
            "message_id": recovered[0]["message_id"],
        })
        mirrored["events"].sort(key=lambda event: event["ordinal"])
        self.assertEqual(
            recover_exact_rollout_turn(fixture["session_id"], mirrored, fixture["turns"][0])["message_id"],
            recovered[0]["message_id"],
        )

        latest_context = json.loads(json.dumps(fixture))
        latest_context["events"].append({
            "ordinal": 200,
            "record_type": "turn_context",
            "turn_id": fixture["turns"][0]["turn_id"],
        })
        latest_context["events"].sort(key=lambda event: event["ordinal"])
        self.assertEqual(
            recover_exact_rollout_turn(fixture["session_id"], latest_context, fixture["turns"][0])["message_id"],
            recovered[0]["message_id"],
        )

        reviewer = json.loads(json.dumps(fixture))
        reviewer_final = next(
            event for event in reviewer["events"]
            if event.get("record_type") == "response_item" and event.get("message_id", "").endswith("b4583")
        )
        reviewer_final["bytes"] = "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=pass\nsummary=review passed"
        self.assertEqual(
            recover_exact_rollout_turn(
                fixture["session_id"], reviewer, fixture["turns"][1], role="reviewer"
            )["message_id"],
            recovered[1]["message_id"],
        )

        later_commentary = json.loads(json.dumps(fixture))
        later_commentary["events"].append({
            "ordinal": 243,
            "record_type": "response_item",
            "payload_type": "message",
            "message_id": "later-commentary",
            "role": "assistant",
            "phase": "commentary",
            "bytes": "later",
        })
        self.assertTrue(
            recover_exact_rollout_turn(
                fixture["session_id"], later_commentary, fixture["turns"][1]
            )["requires_reconcile"]
        )

        mutations = (
            "wrong_session",
            "wrong_session_meta",
            "duplicate_rollout",
            "duplicate_ordinal",
            "malformed_json",
            "quoted_json",
            "malformed_role",
            "nonassistant",
            "wrong_embedded_turn",
            "missing_completion",
            "failed_turn",
            "pre_context_output",
            "intervening_turn",
            "conflicting_mirror",
            "wrong_mirror_session",
        )
        for mutation in mutations:
            invalid = json.loads(json.dumps(fixture))
            expected_session = fixture["session_id"]
            if mutation == "wrong_session":
                expected_session = "wrong-session"
            elif mutation == "wrong_session_meta":
                invalid["events"][0]["session_id"] = "wrong-session"
            elif mutation == "duplicate_rollout":
                invalid["rollout_count"] = 2
            elif mutation == "duplicate_ordinal":
                invalid["events"].append(dict(invalid["events"][1]))
            elif mutation in {"malformed_json", "quoted_json", "malformed_role", "nonassistant", "wrong_embedded_turn"}:
                final = next(
                    event for event in invalid["events"]
                    if event.get("record_type") == "response_item" and event.get("message_id", "").endswith("a8cd5")
                )
                if mutation == "malformed_json":
                    final["bytes"] = "not json"
                elif mutation == "quoted_json":
                    final["bytes"] = json.dumps(final["bytes"])
                elif mutation == "malformed_role":
                    final["bytes"] = "{}"
                elif mutation == "nonassistant":
                    final["role"] = "user"
                else:
                    final["embedded_turn_id"] = "wrong-turn"
            elif mutation == "missing_completion":
                invalid["events"] = [event for event in invalid["events"] if event["ordinal"] != 230]
            elif mutation == "failed_turn":
                invalid["events"].append({
                    "ordinal": 229,
                    "record_type": "event_msg",
                    "payload_type": "task_failed",
                    "turn_id": fixture["turns"][0]["turn_id"],
                })
            elif mutation == "pre_context_output":
                next(
                    event for event in invalid["events"]
                    if event.get("record_type") == "turn_context" and event.get("turn_id") == fixture["turns"][0]["turn_id"]
                )["ordinal"] = 229
            elif mutation == "intervening_turn":
                invalid["events"].append({
                    "ordinal": 235,
                    "record_type": "event_msg",
                    "payload_type": "task_started",
                    "turn_id": "intervening-turn",
                })
            elif mutation == "conflicting_mirror":
                invalid["events"].append({
                    "ordinal": 225,
                    "record_type": "event_msg",
                    "payload_type": "item_completed",
                    "thread_id": fixture["session_id"],
                    "turn_id": fixture["turns"][0]["turn_id"],
                    "item_type": "AgentMessage",
                    "item_id": "different",
                    "phase": "final_answer",
                })
            else:
                next(
                    event for event in invalid["events"]
                    if event.get("item_type") == "AgentMessage" and event.get("turn_id") == fixture["turns"][0]["turn_id"]
                )["thread_id"] = "wrong-session"
            invalid["events"].sort(key=lambda event: event["ordinal"])
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                recover_exact_rollout_turn(expected_session, invalid, fixture["turns"][0])

    def test_projection_mismatch_recovery_preserves_source_and_authority(self):
        source_result = (
            "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=changes_requested\n"
            "summary=Keep the responsive class findings.\n"
            "finding=Use md:w-1/2 for the half-width breakpoint.\n"
            "finding=Keep md:grid w-1/2 for the grid variant."
        )
        projected_result = source_result.replace("md:w-1/2", "md/2").replace(
            "md:grid w-1/2", "md w-1/2"
        )
        fixture = {
            "fixture_kind": "instruction_contract_projection_recovery",
            "expected_identity": {
                "task_id": "review-task",
                "host_id": "local",
                "turn_id": "review-turn",
                "message_id": "review-message",
                "delivery_reference": "delivery-review-1",
                "dispatch_key": "dispatch-review-1",
            },
            "wait": {
                "status": "completed",
                "task_id": "review-task",
                "host_id": "local",
                "turn_id": "review-turn",
                "message_id": "review-message",
                "message": projected_result,
            },
            "read": {
                "task_id": "review-task",
                "host_id": "local",
                "turn_id": "review-turn",
                "message_id": "review-message",
                "message": source_result,
            },
            "delivery": {
                "authenticated": True,
                "source_task_id": "review-task",
                "delivery_reference": "delivery-review-1",
                "dispatch_key": "dispatch-review-1",
                "message": source_result,
            },
        }

        recovered = classify_projection_recovery_fixture(fixture)
        self.assertEqual(recovered["action"], "recover_source")
        self.assertEqual(recovered["source"], "delivery")
        self.assertEqual(recovered["recovery_reads"], 1)
        self.assertEqual(recovered["payload"]["status"], "changes_requested")
        self.assertEqual(
            recovered["payload"]["findings"],
            [
                "Use md:w-1/2 for the half-width breakpoint.",
                "Keep md:grid w-1/2 for the grid variant.",
            ],
        )

        for key in ("task_id", "host_id", "turn_id", "message_id"):
            invalid = json.loads(json.dumps(fixture))
            invalid["read"][key] = "wrong-" + key
            with self.subTest(mismatch=key), self.assertRaises(ValueError):
                classify_projection_recovery_fixture(invalid)

        for key in ("delivery_reference", "dispatch_key"):
            invalid = json.loads(json.dumps(fixture))
            invalid["delivery"][key] = "wrong-" + key
            with self.subTest(contradiction=key), self.assertRaises(ValueError):
                classify_projection_recovery_fixture(invalid)

        wrong_source = json.loads(json.dumps(fixture))
        wrong_source["delivery"]["source_task_id"] = "wrong-review-task"
        with self.assertRaises(ValueError):
            classify_projection_recovery_fixture(wrong_source)

        missing_identity = json.loads(json.dumps(fixture))
        missing_identity["expected_identity"]["message_id"] = ""
        with self.assertRaises(ValueError):
            classify_projection_recovery_fixture(missing_identity)

        nonterminal = json.loads(json.dumps(fixture))
        nonterminal["wait"]["status"] = "running"
        with self.assertRaises(ValueError):
            classify_projection_recovery_fixture(nonterminal)

        truncated = json.loads(json.dumps(fixture))
        truncated["read"]["truncated"] = True
        with self.assertRaises(ValueError):
            classify_projection_recovery_fixture(truncated)

        conflicting = json.loads(json.dumps(fixture))
        conflicting["read"]["message"] = source_result.replace(
            "Keep the responsive class findings.", "Different source result."
        )
        with self.assertRaises(ValueError):
            classify_projection_recovery_fixture(conflicting)

        operations = flat(OPERATIONS)
        self.assertIn("This mismatch route grants no additional rollout lookup or reread", operations)
        self.assertIn("ask for a new review, or request user approval for this proven recovery", operations)

    def test_context_checkpoint_is_fail_soft_and_exact_when_fresh(self):
        operations = flat(OPERATIONS)
        self.assertIn("Unavailable telemetry alone creates neither a blocker nor a successor", operations)
        self.assertIn("`last_token_usage.input_tokens / model_context_window * 100`", operations)
        self.assertIn("context.worker_percent", operations)
        self.assertIn("This transition is neither a repair nor a review", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Context checkpoint scenarios"),
            {
                "Exact rollout or metric unavailable": (
                    "Continue bounded work",
                    "No telemetry-only blocker or successor",
                ),
                "Ordering stale or contradictory": (
                    "Continue bounded work",
                    "No telemetry-only blocker or successor",
                ),
                "Fresh occupancy at or below the configured worker percentage": (
                    "Continue same task",
                    "No handoff",
                ),
                "Fresh occupancy strictly above the configured worker percentage with material work remaining": (
                    "Return `context_handoff`",
                    "One same-role successor",
                ),
                "Fresh post-compaction sample follows the compacted event": (
                    "Evaluate its exact occupancy",
                    "Apply the same strict threshold",
                ),
                "Compaction follows an emitted final `context_handoff`": (
                    "Run the terminal gate and repeat the same bytes",
                    "No same-task project work; reconcile one predecessor-keyed successor after completion",
                ),
                "Work completed before another natural boundary": (
                    "Return normal role result",
                    "No checkpoint or successor",
                ),
                "Host failure independently prevents progress": (
                    "Return ordinary blocked result",
                    "Block on the observed failure not missing telemetry",
                ),
            },
        )

    def test_retained_empco_compaction_trace_is_terminal(self):
        fixture = json.loads(NATIVE_FIXTURES.read_text(encoding="utf-8"))["empco_post_handoff"]
        self.assertEqual(fixture["fixture_kind"], "sanitized_minimal_native_projection")
        start = next(event for event in fixture["events"] if event.get("payload_type") == "task_started")
        self.assertEqual(start["ordinal"], 1)
        self.assertNotIn("thread_id", start)
        final = next(event for event in fixture["events"] if event.get("record_type") == "response_item")
        self.assertNotIn("turn_id", final)
        state, payload = classify_post_compaction(fixture)
        self.assertEqual(state, "terminal_handoff")
        self.assertEqual(parse_role_payload(payload, "executor")["status"], "context_handoff")

        reviewer = json.loads(json.dumps(fixture))
        next(event for event in reviewer["events"] if event.get("record_type") == "response_item")["bytes"] = (
            "SCOVILLE_RESULT_V1\nrole=reviewer\nstatus=context_handoff\nsummary=retained reviewer fixture"
        )
        self.assertEqual(classify_post_compaction(reviewer, role="reviewer")[0], "terminal_handoff")

        no_handoff = json.loads(json.dumps(fixture))
        no_handoff["events"] = [event for event in no_handoff["events"] if event.get("record_type") != "response_item"]
        next(event for event in no_handoff["events"] if event.get("record_type") == "compacted").pop("replacement_message_id")
        self.assertEqual(classify_post_compaction(no_handoff), ("no_handoff", None))

        for mutation in (
            "duplicate_final",
            "malformed_json",
            "quoted_json",
            "wrong_embedded_turn",
            "wrong_session_meta",
            "late_start",
            "conflicting_mirror",
            "failed_turn",
            "resumed_gap_start",
            "duplicate_ordinal",
            "wrong_replacement",
            "gap_wrong_turn_final",
            "gap_different_final",
            "gap_wrong_mirror",
            "gap_malformed_final",
            "gap_wrong_token_turn",
            "missing_final_identity",
            "wrong_review_container",
        ):
            invalid = json.loads(json.dumps(fixture))
            if mutation == "duplicate_final":
                invalid["events"].append({
                    "ordinal": 799,
                    "record_type": "response_item",
                    "payload_type": "message",
                    "message_id": "different",
                    "role": "assistant",
                    "phase": "final_answer",
                    "bytes": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=context_handoff\nsummary=duplicate",
                })
            elif mutation in {"malformed_json", "quoted_json", "wrong_embedded_turn"}:
                mutated_final = next(
                    event for event in invalid["events"] if event.get("record_type") == "response_item"
                )
                if mutation == "malformed_json":
                    mutated_final["bytes"] = "not json"
                elif mutation == "quoted_json":
                    mutated_final["bytes"] = json.dumps(mutated_final["bytes"])
                else:
                    mutated_final["embedded_turn_id"] = "wrong-turn"
            elif mutation == "wrong_session_meta":
                invalid["events"][0]["session_id"] = "wrong-session"
            elif mutation == "late_start":
                next(event for event in invalid["events"] if event.get("payload_type") == "task_started")["ordinal"] = 900
            elif mutation == "conflicting_mirror":
                invalid["events"].append({
                    "ordinal": 799,
                    "record_type": "event_msg",
                    "payload_type": "item_completed",
                    "thread_id": "wrong-session",
                    "turn_id": "wrong-turn",
                    "item_type": "AgentMessage",
                    "item_id": "different",
                    "phase": "final_answer",
                })
            elif mutation == "failed_turn":
                invalid["events"].append({
                    "ordinal": 800,
                    "record_type": "event_msg",
                    "payload_type": "task_failed",
                    "turn_id": fixture["turn_id"],
                })
            elif mutation == "resumed_gap_start":
                invalid["events"].append({
                    "ordinal": 802,
                    "record_type": "event_msg",
                    "payload_type": "task_started",
                    "turn_id": fixture["turn_id"],
                })
            elif mutation == "duplicate_ordinal":
                invalid["events"].append(dict(invalid["events"][1]))
            elif mutation == "wrong_replacement":
                next(event for event in invalid["events"] if event.get("record_type") == "compacted")["replacement_message_id"] = "different"
            elif mutation in {"gap_wrong_turn_final", "gap_different_final", "gap_malformed_final"}:
                gap_final = {
                    "ordinal": 802,
                    "record_type": "response_item",
                    "payload_type": "message",
                    "message_id": "conflicting-gap-final",
                    "role": "assistant",
                    "phase": "final_answer",
                    "bytes": "SCOVILLE_RESULT_V1\nrole=executor\nstatus=context_handoff\nsummary=gap",
                }
                if mutation == "gap_wrong_turn_final":
                    gap_final["embedded_turn_id"] = "wrong-turn"
                elif mutation == "gap_different_final":
                    gap_final["embedded_turn_id"] = fixture["turn_id"]
                else:
                    gap_final["bytes"] = "{}"
                invalid["events"].append(gap_final)
            elif mutation == "gap_wrong_mirror":
                invalid["events"].append({
                    "ordinal": 802,
                    "record_type": "event_msg",
                    "payload_type": "item_completed",
                    "thread_id": fixture["session_id"],
                    "turn_id": "wrong-turn",
                    "item_type": "AgentMessage",
                    "item_id": "different-gap-message",
                    "phase": "final_answer",
                })
            elif mutation == "gap_wrong_token_turn":
                invalid["events"].append({
                    "ordinal": 802,
                    "record_type": "event_msg",
                    "payload_type": "token_count",
                    "turn_id": "wrong-turn",
                })
            elif mutation == "missing_final_identity":
                next(event for event in invalid["events"] if event.get("record_type") == "response_item").pop("message_id")
                next(event for event in invalid["events"] if event.get("record_type") == "compacted").pop("replacement_message_id")
            else:
                next(event for event in invalid["events"] if event.get("record_type") == "response_item")["bytes"] = (
                    "SCOVILLE_RESULT_V1\nrole=executor\nstatus=completed\ncode_changed=maybe\ncritical_docs_changed=no\nsummary=bad values"
                )
            invalid["events"].sort(key=lambda event: event["ordinal"])
            with self.subTest(mutation=mutation):
                self.assertEqual(classify_post_compaction(invalid), ("unavailable", None))
        self.assertEqual(
            markdown_table(OPERATIONS, "### Post-compaction scenarios"),
            {
                "Exact own result delivered before compaction but final response absent": (
                    "Return the delivered result bytes without a second delivery",
                    "Accept only after exact turn completion and byte recovery",
                ),
                "Exact own final result before compaction but delivery absent": (
                    "Return the same result bytes without a callback or further work",
                    "Accept only after exact turn completion and byte recovery",
                ),
                "Complete interval with no own terminal result": (
                    "Continue the unchanged role",
                    "Normal result handling",
                ),
                "Missing duplicate malformed or contradictory evidence": (
                    "Return `blocked` without project action",
                    "Archive exact failure and record a blocker",
                ),
                "Same predecessor is delivered twice": (
                    "Repeat the same terminal result",
                    "Reconcile the existing successor; create no duplicate",
                ),
                "Fresh successor receives inherited handoff and has no local compaction": (
                    "Treat it only as continuation input and perform remaining role work",
                    "No terminal transition from inherited content",
                ),
                "Successor copies or paraphrases inherited handoff without new action and evidence": (
                    "Return no accepted rollover progress",
                    "Archive it add `WORKFLOW-NOPROGRESS` and create no grandchild",
                ),
                "A successor later rolls over after new action and evidence": (
                    "Use its distinct predecessor key",
                    "Create at most one next-generation successor",
                ),
            },
        )

        operations = flat(OPERATIONS)
        self.assertIn("copied or reworded predecessor content are not progress", operations)
        self.assertIn("one successor and no grandchild", operations)
        self.assertIn("preserve the unit and logical attempt", operations)

    def test_coordinator_stays_visible_and_waits_for_exact_child(self):
        operations = flat(OPERATIONS)
        self.assertIn("at least one coordinator task must remain unarchived and visible", operations)
        self.assertIn("A coordinator must not finish its turn merely because a child is running", operations)
        self.assertIn("timeout no greater than 60 seconds", operations)
        self.assertIn("On an unchanged timeout, emit no commentary", operations)
        self.assertIn("An unchanged timeout remains in the silent cursor-bound loop", operations)
        self.assertIn("single-use delivery reference", operations)
        self.assertIn("`waitingOnApproval`", operations)
        self.assertIn("Treat that exact call as pending delivery", operations)
        self.assertIn("Do not retry, relay, recreate either task, poll, or send progress narration", operations)
        self.assertIn("When delivery succeeded, require the recovered candidate bytes to equal the delivered result byte-for-byte", operations)
        self.assertIn("When delivery failed or never arrived", operations)
        self.assertIn("already-dispatched callback settled successfully or with a definite failure", operations)
        self.assertIn("A real `wait_threads` tool error stops the workflow visibly", operations)
        self.assertIn("`needs_user_decision` retains the exact child open", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Coordinator wake scenarios"),
            {
                "Exact child remains active through a wait timeout": (
                    "No state change",
                    "Wait again with the updated cursor and no commentary or project inspection",
                ),
                "Exact child completes with one final role result": (
                    "One completion result",
                    "Recover validate and when present compare delivered bytes",
                ),
                "Exact child completes with `needs_user_decision`": (
                    "One decision result",
                    "Confirm the completed turn then ask only the exact decision",
                ),
                "User requests status": (
                    "One user wake",
                    "Report one exact-child wait snapshot then resume the same wait loop",
                ),
                "Identical retry of one pending or settled delivery": (
                    "One reconciliation wake",
                    "Reuse the same transition state; do not wait or transition twice",
                ),
                "Unknown source or conflicting delivery reuse": (
                    "One rejected wake",
                    "Fail closed with no project or Plan action",
                ),
                "Completed wait projection differs from authenticated delivery": (
                    "One recovery read",
                    "Apply the exact-source recovery rule below; no transition before it passes",
                ),
                "Result delivery arrives before native completion": (
                    "Expected race",
                    "Continue the same exact-child wait loop until authoritative completion",
                ),
                "`wait_threads` returns a tool error": (
                    "Visible blocker",
                    "Preserve coordinator child and guard; perform no workflow transition",
                ),
            },
        )

    def test_persistent_codex_goals_cannot_drive_the_coordinator(self):
        operations = flat(OPERATIONS)
        self.assertIn(
            "The canonical Plan is the workflow's only durable progress owner",
            operations,
        )
        self.assertIn("never call `create_goal` for the workflow objective", operations)
        self.assertIn(
            "as requested scope and continuation intent inside this operations loop",
            operations,
        )
        self.assertIn(
            "A persistent goal would create a second continuation owner beside the coordinator's exact-child wait loop",
            operations,
        )
        self.assertIn("call `update_goal` with `status=paused`", operations)
        self.assertIn(
            "Pausing that Codex goal does not pause the canonical Plan or cancel an already active child",
            operations,
        )
        self.assertIn(
            "An automatic persistent-goal continuation is not a meaningful coordinator state change",
            operations,
        )
        self.assertIn(
            "never authorizes project inspection or an \"I am waiting\" message",
            operations,
        )

    def test_review_threshold_and_repairs_use_the_changed_result(self):
        operations = flat(OPERATIONS)
        self.assertIn("Use the executor report as the primary classification", operations)
        self.assertIn("Never classify from the unit title, Step wording, or route class", operations)
        self.assertIn("Either `yes` requires review", operations)
        self.assertIn("A conflict or unclear classification requires review", operations)
        self.assertIn("Do not repeat project inspection, tests, acceptance work, or a review", operations)
        self.assertIn("first attempt plus at most three repair executors", operations)
        self.assertIn("after the third repair executor, create no fourth repair", operations)
        self.assertIn("repair 2 moves one WORK row above", operations)
        self.assertIn("repair 3 moves two rows above", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Review correction scenarios"),
            {
                "Initial code or critical documentation change": (
                    "None",
                    "None",
                    "Reviewer required",
                ),
                "Initial consistent non-qualifying result": (
                    "None",
                    "None",
                    "Reviewer skipped",
                ),
                "Initial conflict explicit requirement or ambiguity": (
                    "None",
                    "None",
                    "Reviewer required",
                ),
                "Exact non-material Plan-only finding": (
                    "Coordinator",
                    "None",
                    "Follow-up skipped after bounded comparison",
                ),
                "Material explicit or ambiguous Plan-only finding": (
                    "Coordinator",
                    "None",
                    "Follow-up required",
                ),
                "Routine non-critical project-documentation finding": (
                    "None",
                    "Project correction",
                    "Follow-up skipped when report and result agree",
                ),
                "Code critical-documentation or material-risk project finding": (
                    "None",
                    "Project correction",
                    "Follow-up required",
                ),
                "Mixed Plan and project findings": (
                    "Coordinator handles Plan part",
                    "Project correction only",
                    "Decide from all corrections and require follow-up when qualifying or unclear",
                ),
            },
        )

        call_trace = ["initial"]
        for repair_number in range(1, 5):
            if repair_number > 3:
                break
            call_trace.append(f"repair-{repair_number}")
        self.assertEqual(call_trace, ["initial", "repair-1", "repair-2", "repair-3"])
        self.assertNotIn("repair-4", call_trace)

    def test_coordinator_announces_real_phase_transitions_in_retained_language(self):
        operations = flat(OPERATIONS)
        self.assertIn(
            "Consume `requested_scope`, `continuation_intent` and `language` exactly as the Core supplied them",
            operations,
        )
        self.assertIn(
            "Announce each real workflow phase transition once in the retained `language`",
            operations,
        )
        self.assertEqual(
            markdown_table(OPERATIONS, "### Required phase announcements"),
            {
                "Initial execution": (
                    "Immediately before sending the activated executor its complete assignment, after parking-task identity reconciliation, unit formation, preflight, routing, prompt construction, and guard activation succeed",
                    "Identify the exact unit and selected Plan work; say that the execution assignment will now be sent",
                ),
                "Required review": (
                    "Immediately before creating each required reviewer, after the review decision is final",
                    "Identify the exact unit and completed or corrected result under review; say that the review request will now be sent",
                ),
                "Assigned repair": (
                    "Immediately before sending the activated repair its complete assignment, after parking-task identity reconciliation, prompt construction, and guard activation and after correction ownership and finding indices are final",
                    "Identify the exact unit and assigned findings; say that the repair assignment will now be sent",
                ),
                "Accepted completion transition": (
                    "After the applicable review gate is satisfied and immediately before Plan mutation, structural validation, staging, or commit",
                    "Identify the exact unit; say that the completion phase begins and whether it is closing the unit, an explicit requested boundary, or the whole Plan when that target is already known",
                ),
            },
        )
        self.assertIn(
            "The completion-phase announcement reports a transition, not successful completion",
            operations,
        )
        self.assertIn(
            "These announcements do not authorize polling, periodic progress chatter, or messages while a child is active",
            operations,
        )
        self.assertIn("send the required review-phase announcement", operations)
        self.assertIn("Send the required repair-phase announcement", operations)
        self.assertIn("send the required completion-phase announcement", operations)
        self.assertIn("send the required initial-execution announcement", operations)

    def test_accepted_transition_batches_safe_deterministic_operations(self):
        operations = flat(OPERATIONS)
        self.assertIn("use one coordinator transition pass", operations)
        self.assertIn("fresh selector output", operations)
        self.assertIn("run complete structural validation", operations)
        self.assertIn("inspect the staged diff", operations)
        self.assertIn("capture status evidence", operations)
        self.assertIn("Never parallelize dependent writes", operations)
        self.assertIn("A failed gate stops the remaining transition steps", operations)

    def test_terminal_child_archival_requires_verified_exact_state(self):
        operations = flat(OPERATIONS)
        self.assertIn("before any Plan mutation, successor, reviewer, or repair creation, or next dispatch", operations)
        self.assertIn("A tool-call wrapper reporting `completed`", operations)
        self.assertIn("general active or archived task listing is not archival-state proof", operations)
        self.assertIn("perform one bounded reconciliation for the same exact ID", operations)
        self.assertIn("reconcile every retained terminal child from the interrupted unit", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Archival verification scenarios"),
            {
                "Archive response returns the exact child ID and `archived: true`": (
                    "Verified",
                    "Continue the guarded transition",
                ),
                "Archive call reports `completed` but no explicit archival state": (
                    "Unverified",
                    "Reconcile the same exact ID once",
                ),
                "General task lists omit or include the child": (
                    "Unverified",
                    "Do not infer archival state from list membership",
                ),
                "Retained terminal child is still visible after resume": (
                    "Unverified until exact-state confirmation",
                    "Re-archive the same ID once and verify before transition",
                ),
                "Exact state remains false mismatched or unavailable after reconciliation": (
                    "Failed",
                    "Ask the user and perform no Plan mutation or child creation",
                ),
            },
        )

    def test_unit_commit_defers_plan_checkpoints_and_preserves_backup_order(self):
        operations = flat(OPERATIONS)
        self.assertIn("keep every coordinator-owned Plan change for the unit uncommitted", operations)
        self.assertIn("Never create a standalone Plan checkpoint commit after dispatch", operations)
        self.assertIn("the next accepted unit commit contains its accepted project changes", operations)
        self.assertIn("No commit may occur before observed Acceptance and the satisfied review gate", operations)
        self.assertIn("No Plan-only or other intermediate commit may advance `HEAD`", operations)
        self.assertIn("preserve every commit and working-tree change", operations)
        self.assertIn("before another unit is dispatched or allowed to advance the same `HEAD`", operations)
        self.assertIn("The authorized executor creates and verifies the project-compliant backup before its first source edit", operations)
        self.assertIn("the coordinator only checks its returned named result", operations)
        self.assertIn("Retained terminal blocker state from an earlier unit may enter the next accepted unit commit", operations)
        self.assertIn("unaccepted project changes from that earlier unit never do", operations)
        self.assertIn("Never split canonical planning records into unit-local staged hunks", operations)
        self.assertIn("verify their staged bytes equal the validated working bytes", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Unit commit scenarios"),
            {
                "Active unit before Acceptance or required review": (
                    "No commit",
                    "Keep project and Plan changes uncommitted",
                ),
                "Valid backup followed by an accepted reviewed source unit": (
                    "One unit commit",
                    "Stage accepted project changes and all accumulated unit Plan changes together",
                ),
                "Plan checkpoint commit advanced `HEAD` after the backup while source is unchanged and whole Work Item dispatches": (
                    "No source commit yet",
                    "Put backup creation in projected Next action before executor source edits",
                ),
                "Same stale backup with a started Step that lacks projected backup authority": (
                    "No dispatch or source edit",
                    "Ask the exact recovery decision; do not rewrite the Step or rely on excluded Next action",
                ),
                "Blocked unit retains source changes after a HEAD-bound backup": (
                    "No other same-workspace unit dispatch or commit",
                    "Preserve the interval and ask for disposition",
                ),
                "Earlier unit has retained terminal blocker state but no protected source interval": (
                    "Next accepted independent unit may commit",
                    "Stage the complete valid accumulated Plan profile but none of the earlier unit's project changes",
                ),
                "Candidate independent transition cannot stage a complete valid Plan profile": (
                    "No dispatch",
                    "Ask for disposition before creating another child",
                ),
                "Source changes exist but no valid pre-change backup remains": (
                    "No commit or destructive recovery",
                    "Preserve all work and ask for the project-authorized recovery",
                ),
                "Commit hook fails": (
                    "No bypass or completion report",
                    "Retain the complete diagnostic and every change for correction",
                ),
            },
        )

    def test_plan_commit_visible_completion_and_stop_remain_gated(self):
        operations = flat(OPERATIONS)
        self.assertIn("complete the item, Plan, and `PROJECT_INDEX.md` together", operations)
        self.assertIn("Zero diagnostics are required before staging", operations)
        self.assertIn("Stage only accepted project paths or separable project hunks", operations)
        self.assertIn("plus each complete changed canonical Plan, Decision, and index file", operations)
        self.assertIn("one concise completion report as the final workflow action", operations)
        self.assertIn("Keep the final coordinator unarchived after the report", operations)
        self.assertIn(
            "Only a transferred rollover predecessor is archived by its activated successor",
            operations,
        )
        self.assertIn("send the exact instruction to the active child", operations)
        self.assertIn("Stopping the coordinator does not imply that a child stopped", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Post-commit scenarios"),
            {
                "Active Plan retains eligible in-scope work": (
                    "Run the coordinator checkpoint first",
                    "Continue permits selection; rollover requires transfer first; blocked requires configuration correction",
                ),
                "Explicit boundary is accepted while out-of-scope work remains": (
                    "Do not run selector",
                    "Report boundary completion",
                ),
                "Final Work Item completes the Plan and index becomes idle": (
                    "Do not run selector",
                    "Report whole-Plan completion",
                ),
            },
        )

    def test_coordinator_rollover_is_exact_at_accepted_units(self):
        operations = flat(OPERATIONS)
        readiness = flat(ROLLOVER_READINESS)
        self.assertIn("input_tokens * 100 >= model_context_window * coordinator_percent", operations)
        self.assertIn("one Step, one authorized compatible Step bundle, or one Step-less Work Item", operations)
        self.assertIn("Missing, stale, malformed, or contradictory telemetry is never estimated and continues in the same coordinator", operations)
        self.assertIn("expected Git HEAD or `not_applicable_non_git`", operations)
        self.assertIn("reconcile-successor", operations)
        self.assertIn("validate-successor", operations)
        self.assertIn("transfer-coordinator", operations)
        self.assertIn("activate-coordinator", operations)
        self.assertIn("returns its validation receipt as its final response", operations)
        self.assertIn("explicit activation message naming", operations)
        self.assertIn("exact predecessor task ID", operations)
        self.assertIn("The successor sends no activation acknowledgement", operations)
        self.assertIn("performs no further action", operations)
        self.assertIn("without moving the successor between sidebar sections", operations)
        self.assertIn("exact ID/host in `listing.threads` OR `exact_successor.status:active`", readiness)
        self.assertIn("Both paths require complete placement lists", readiness)
        self.assertIn("no successor pin or section entry", readiness)
        self.assertIn("Missing or non-active exact status cannot replace a missing list entry", readiness)
        self.assertIn("wait for the exact predecessor activation turn", operations)
        self.assertIn("calls of at most 60 seconds", operations)
        self.assertIn("the predecessor remains in that same turn", operations)
        self.assertIn("does the successor call `set_thread_archived` for the exact predecessor task ID", operations)
        self.assertIn("same predecessor ID has `archived: true`", operations)
        self.assertIn("The predecessor never calls archival on itself", operations)
        self.assertIn("A nonterminal `needs-attention` state preserves the exact child", operations)
        self.assertIn("A ready or validated ID alone never permits archival", operations)
        self.assertEqual(
            markdown_table(OPERATIONS, "### Coordinator rollover scenarios"),
            {
                "Fresh occupancy below the configured coordinator percentage": ("Continue in the same coordinator",),
                "Fresh occupancy at the configured coordinator percentage": ("Run one rollover after the accepted unit",),
                "Telemetry missing, stale, malformed, or contradictory": ("Continue in the same coordinator",),
                "Mid-unit phase or failed transition": ("Do not roll over",),
                "Provisional or unknown successor creation": ("Reconcile; do not recreate or archive",),
                "Ready successor not yet validated or transferred": ("Both remain read-only for handoff; predecessor stays visible",),
                "Ready successor completed validation checks": (
                    "Successor returns its validation receipt; predecessor confirms its exact completed turn and reconciles the same validated guard",
                ),
                "Guard is `rollover_validated` and predecessor is awake": (
                    "Predecessor transfers the guard and sends same-key activation; it never self-archives",
                ),
                "Activated successor is listed or exact-read active and sees predecessor turn completion": (
                    "After the helper permits archival, successor alone archives that exact predecessor and requires same-ID `archived: true` before selection or dispatch",
                ),
                "Transfer succeeded but activation delivery failed": (
                    "Keep both tasks unarchived; predecessor visibly reports the blocker without Plan or project writes and reconciles only the same-key activation",
                ),
                "Successor is neither listed nor exact-read active but reachability and predecessor completion are proven under the active guard": (
                    "Continue guarded selection; retain predecessor open; create no replacement coordinator",
                ),
                "Successor exact reachability or predecessor completion is unproven": (
                    "Archive neither task; preserve the guard and report the exact blocker",
                ),
                "Scope complete, Plan complete, or Stop": ("Create no successor",),
            },
        )


if __name__ == "__main__":
    unittest.main()
