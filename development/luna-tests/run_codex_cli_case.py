"""Run one bounded Codex CLI Skill-comprehension case."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import posixpath
from pathlib import Path
import queue
import re
import stat
import subprocess
import sys
import threading
import time

from process_lifetime import WorkerProcess
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "instruction_tests"))
from attempts import reserve
from results import failure_class
from case_binding import verify_preparation


CONTINUATION = (
    "Continue the same hypothetical case using only supplied text. Do not use\n"
    "tools or execute project actions. Request any other required packaged text\n"
    "with `READ <relative-path>` lines; otherwise provide the final case answer.\n"
    "Use a package-root-relative path; a Markdown link target as written also works\n"
    "when it resolves uniquely from one previously supplied file. Suite-root\n"
    "paths begin with packages/<member>/<member>/.\n"
)
DISABLED_FEATURES = (
    "shell_tool", "apps", "hooks", "plugins", "remote_plugin", "plugin_sharing",
    "browser_use", "browser_use_external", "browser_use_full_cdp_access",
    "computer_use", "multi_agent", "multi_agent_v2", "collaboration_modes",
    "workspace_dependencies", "image_generation",
    "in_app_browser", "tool_suggest", "skill_search",
    "skill_mcp_dependency_install", "enable_mcp_apps",
    "codex_apps_mcp_2026_07_28", "mcp_2026_07_28", "auth_elicitation",
    "tool_call_mcp_elicitation",
    "unified_exec", "view_image", "goals", "sleep_tool", "worktrees",
)
HASH_PATTERN = re.compile(r"[0-9a-fA-F]{64}\Z")
READ_PATTERN = re.compile(r"READ ([^\r\n]+)\Z")
QUALIFIED_MODEL = "gpt-6-luna"
SUPPORTED_TEST_MODELS = (QUALIFIED_MODEL,)
QUALIFIED_EFFORT = "high"


class ProtocolError(RuntimeError):
    """A fail-closed transport or evidence failure."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def expected_hash(value: str) -> str:
    if not HASH_PATTERN.fullmatch(value):
        raise argparse.ArgumentTypeError("expected SHA-256 must be 64 hexadecimal characters")
    return value.lower()


def verify_hash(path: Path, expected: str, label: str) -> str:
    observed = sha256_file(path)
    if observed != expected:
        raise ProtocolError(f"{label}_sha256_mismatch")
    return observed


def load_receipt(receipt_path: Path, member_name: str, package_root: Path) -> dict[str, str]:
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        matches = [item for item in receipt["members"] if item["name"] == member_name]
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise ProtocolError("invalid_receipt") from error
    if len(matches) != 1:
        raise ProtocolError("receipt_member_not_unique")
    member = matches[0]
    files = member.get("files")
    if package_root.name != member_name or not isinstance(files, dict):
        raise ProtocolError("invalid_receipt_member")
    prefix = member_name + "/"
    manifested: dict[str, str] = {}
    for receipt_name, digest in files.items():
        if not isinstance(receipt_name, str) or not isinstance(digest, str) or not HASH_PATTERN.fullmatch(digest):
            raise ProtocolError("invalid_receipt_file")
        receipt_file = contained_path(package_root.parent, receipt_name, "invalid_receipt_file")
        if not receipt_file.is_file() or sha256_file(receipt_file) != digest.lower():
            raise ProtocolError(f"package_file_mismatch:{receipt_name}")
        if isinstance(receipt_name, str) and receipt_name.startswith(prefix):
            relative = receipt_name[len(prefix):]
            if not relative:
                raise ProtocolError("invalid_receipt_file")
            manifested[relative] = digest.lower()
    if "SKILL.md" not in manifested or not (package_root / "SKILL.md").is_file():
        raise ProtocolError("receipt_does_not_describe_package_root")
    return manifested


def load_package_receipt(receipt_path: Path, member_name: str, package_root: Path) -> dict[str, str]:
    """A suite root serves verified member payloads under their original paths."""
    if member_name != "@suite":
        return load_receipt(receipt_path, member_name, package_root)
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt.get("layout") != "suite" or receipt.get("suite") != package_root.name:
        raise ProtocolError("expected_suite_root_and_suite_receipt")
    manifested = {}
    names = set()
    for member in receipt["members"]:
        name = member["name"]
        if name in names or not re.fullmatch(r"[a-z0-9-]+", name):
            raise ProtocolError("invalid_or_duplicate_suite_member")
        names.add(name)
        relative = f"packages/{name}/{name}"
        root = contained_path(package_root, relative, "invalid_suite_member_root")
        for path, digest in load_receipt(receipt_path, name, root).items():
            manifested[f"{relative}/{path}"] = digest
    if not manifested:
        raise ProtocolError("empty_suite_receipt")
    return manifested


def _is_reparse(path: Path) -> bool:
    info = path.lstat()
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return path.is_symlink() or bool(getattr(info, "st_file_attributes", 0) & reparse_flag)


def contained_path(package_root: Path, relative: str, error: str) -> Path:
    if "\\" in relative or not relative or Path(relative).is_absolute() or re.match(r"^[A-Za-z]:", relative):
        raise ProtocolError(error)
    parts = relative.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise ProtocolError(error)
    try:
        root = package_root.resolve(strict=True)
        unresolved = package_root
        for part in parts:
            if _is_reparse(unresolved):
                raise ProtocolError(error)
            unresolved = unresolved / part
        if _is_reparse(unresolved):
            raise ProtocolError(error)
        resolved = unresolved.resolve(strict=True)
    except OSError as exception:
        raise ProtocolError(error) from exception
    if not resolved.is_relative_to(root):
        raise ProtocolError(error)
    return resolved


def validate_requested_file(
    relative: str, package_root: Path, manifested: dict[str, str], served: set[str]
) -> tuple[bytes, str]:
    if relative in served:
        raise ProtocolError("duplicate_request")
    if relative not in manifested:
        raise ProtocolError("unmanifested_request")
    resolved = contained_path(package_root, relative, "requested_file_or_parent_is_reparse_point")
    if not resolved.is_file():
        raise ProtocolError("requested_file_is_not_regular_file")
    raw = resolved.read_bytes()
    if sha256_bytes(raw) != manifested[relative]:
        raise ProtocolError("requested_file_hash_mismatch")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ProtocolError("requested_file_is_not_utf8") from error
    if "\0" in text or any(ord(char) < 32 and char not in "\t\n\r\f" for char in text):
        raise ProtocolError("requested_file_is_not_text")
    return text.replace("\r\n", "\n").encode("utf-8"), sha256_bytes(raw)


def resolve_read_path(request: str, manifested: dict[str, str], supplied_paths: list[str]) -> str:
    """Resolve a READ against the package or one unambiguous served Markdown file."""
    if (not request or "\\" in request or "\0" in request or request.startswith("/")
            or re.match(r"^[A-Za-z]:", request)):
        raise ProtocolError("unmanifested_request")
    if request in manifested:
        return request
    candidates = set()
    for source in supplied_paths:
        candidate = posixpath.normpath(posixpath.join(posixpath.dirname(source), request))
        if candidate in manifested and not candidate.startswith("../"):
            candidates.add(candidate)
    if len(candidates) == 1:
        return candidates.pop()
    if len(candidates) > 1:
        raise ProtocolError("ambiguous_relative_request")
    raise ProtocolError("unmanifested_request")


def parse_read_requests(answer: str) -> list[str] | None:
    # A request keeps the turn open, even when accompanied by an explanation.
    requests = [match.group(1) for line in answer.splitlines()
                if (match := READ_PATTERN.fullmatch(line.strip()))]
    return requests or None


class EventValidator:
    """Validate the qualified event stream as each complete line arrives."""

    def __init__(self, expected_thread: str | None):
        self.expected_thread = expected_thread
        self.events = []
        self.state = "start"
        self.answers = []

    def feed(self, line: bytes) -> None:
        try:
            event = json.loads(line)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ProtocolError("event_parse_error") from error
        if not isinstance(event, dict):
            raise ProtocolError("event_is_not_object")
        kind = event.get("type")
        if self.state == "start" and kind == "thread.started":
            identity = event.get("thread_id")
            if not isinstance(identity, str) or not identity or (self.expected_thread and identity != self.expected_thread):
                raise ProtocolError("thread_identity_mismatch")
            self.state = "ready"
        elif self.state == "ready" and kind == "turn.started":
            self.state = "turn"
        elif self.state == "turn" and kind == "item.started" and event.get("item", {}).get("type") not in (None, "agent_message"):
            raise ProtocolError("forbidden_model_action")
        elif self.state == "turn" and kind == "item.completed":
            item = event.get("item", {})
            if item.get("type") != "agent_message" or not isinstance(item.get("text"), str):
                raise ProtocolError("unexpected_action_or_empty_response")
            self.answers.append(item["text"])
        elif self.state == "turn" and kind == "turn.completed":
            self.state = "done"
        else:
            raise ProtocolError("unexpected_event_order")
        self.events.append(event)

    def finish(self) -> dict:
        if self.state != "done":
            raise ProtocolError("incomplete_turn")
        nonempty = [answer for answer in self.answers if answer.strip()]
        if not nonempty:
            raise ProtocolError("unexpected_action_or_empty_response")
        requests = list(dict.fromkeys(
            path for answer in self.answers for path in (parse_read_requests(answer) or [])
        ))
        return {
            "thread_id": self.events[0]["thread_id"],
            "answer": nonempty[-1],
            "read_requests": requests or None,
            "messages": self.answers,
            "usage": self.events[-1].get("usage"),
            "event_types": [event["type"] for event in self.events],
        }


def validate_events(stdout: bytes, expected_thread: str | None) -> dict:
    validator = EventValidator(expected_thread)
    for line in stdout.splitlines():
        validator.feed(line)
    return validator.finish()


def base_command(codex: Path, catalog: Path, model: str, effort: str, instructions: Path | None = None) -> list[str]:
    if model not in SUPPORTED_TEST_MODELS or effort != QUALIFIED_EFFORT:
        raise ProtocolError("unqualified_model_or_effort")
    command = [
        str(codex), "--ask-for-approval", "never", "--sandbox", "read-only",
        "--model", model, "-c", f'model_reasoning_effort="{effort}"',
        "-c", f'model_catalog_json="{catalog.as_posix()}"', "-c", "mcp_servers={}",
        # Keep the qualified ChatGPT endpoint and login, but avoid a WebSocket
        # negotiation failure before the CLI can return a usable test answer.
        "-c", 'model_provider="scoville_test_http"',
        "-c", 'model_providers.scoville_test_http={name="OpenAI HTTPS test transport",base_url="https://chatgpt.com/backend-api/codex",wire_api="responses",requires_openai_auth=true,supports_websockets=false}',
        "-c", 'sandbox_mode="read-only"',
        "-c", 'web_search="disabled"',
        "-c", 'features.code_mode.enabled=true',
        "--enable", "code_mode_host",
        "-c", 'features.code_mode.excluded_tool_namespaces=["functions","collaboration","clock","web","image_gen"]',
        "-c", 'suppress_unstable_features_warning=true',
        "-c", 'features.skip_host_skill_discovery=true',
        "-c", 'skills.include_instructions=false',
        "-c", 'project_doc_max_bytes=0',
        "-c", 'include_collaboration_mode_instructions=false',
        "-c", 'agents.enabled=false',
        "-c", 'model_instructions_file=' + json.dumps(str((instructions or Path(__file__).with_name("comprehension-instructions.md")).resolve())),
    ]
    for feature in DISABLED_FEATURES:
        command.extend(("--disable", feature))
    return command


def turn_command(base: list[str], workspace: Path, thread_id: str | None) -> list[str]:
    if thread_id is None:
        return base + [
            "exec", "--ignore-user-config", "--ignore-rules", "--strict-config",
            "--skip-git-repo-check", "--json", "-C", str(workspace), "-",
        ]
    return base + [
        "exec", "resume", "--ignore-user-config", "--ignore-rules", "--strict-config",
        "--skip-git-repo-check", "--json", thread_id, "-",
    ]


def _read_pipe(pipe, sink: list[bytes], messages: queue.Queue, name: str) -> None:
    while True:
        data = pipe.readline()
        if not data:
            break
        sink.append(data)
        messages.put((name, data))
    messages.put((name + "_eof", b""))


def _write_pipe(pipe, payload: bytes, messages: queue.Queue, errors: list[str]) -> None:
    try:
        pipe.write(payload)
    except (OSError, ValueError) as error:
        errors.append(f"stdin_write_failure:{type(error).__name__}")
        messages.put(("stdin_error", b""))
    finally:
        if not pipe.closed:
            pipe.close()


def execute_turn(
    command: list[str], prompt: bytes, workspace: Path, timeout: float,
    expected_thread: str | None = None, host_home: Path | None = None,
) -> dict:
    deadline = time.monotonic() + timeout
    worker = WorkerProcess(
        command, cwd=workspace, env=isolated_environment(host_home), stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    stdout_parts: list[bytes] = []
    stderr_parts: list[bytes] = []
    messages: queue.Queue = queue.Queue()
    readers = [
        threading.Thread(target=_read_pipe, args=(worker.process.stdout, stdout_parts, messages, "stdout"), daemon=True),
        threading.Thread(target=_read_pipe, args=(worker.process.stderr, stderr_parts, messages, "stderr"), daemon=True),
    ]
    writer_errors: list[str] = []
    payload = (b"\0" if worker.job else b"") + prompt
    writer = threading.Thread(
        target=_write_pipe, args=(worker.process.stdin, payload, messages, writer_errors), daemon=True
    )
    eof: set[str] = set()
    timed_out = False
    close_error = None
    stream_error = None
    try:
        for reader in readers:
            reader.start()
        writer.start()
        validator = EventValidator(expected_thread)
        while worker.process.poll() is None or eof != {"stdout", "stderr"}:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                timed_out = True
                break
            try:
                source, data = messages.get(timeout=min(0.1, remaining))
            except queue.Empty:
                continue
            if source.endswith("_eof"):
                eof.add(source[:-4])
            elif source == "stdout":
                try:
                    validator.feed(data)
                except ProtocolError as error:
                    stream_error = str(error)
                    break
            elif source == "stderr":
                stream_error = "stderr_not_empty"
                break
            elif source == "stdin_error":
                stream_error = writer_errors[0] if writer_errors else "stdin_write_failure"
                break
    except (OSError, ValueError) as error:
        stream_error = f"stdin_or_process_io_failure:{type(error).__name__}"
    finally:
        try:
            worker.close()
        except BaseException as error:
            close_error = f"{type(error).__name__}: {error}"
        writer.join(timeout=5)
        for reader in readers:
            reader.join(timeout=5)
        for pipe in (worker.process.stdout, worker.process.stderr):
            if pipe and not pipe.closed:
                pipe.close()
    if writer.is_alive() and close_error is None:
        close_error = "stdin_writer_did_not_stop"
    if writer_errors and stream_error is None:
        stream_error = writer_errors[0]
    return {
        "stdout": b"".join(stdout_parts), "stderr": b"".join(stderr_parts),
        "returncode": worker.returncode, "timed_out": timed_out,
        "close_error": close_error, "stream_error": stream_error, "worker_pid": worker.pid,
        "observed_thread_id": validator.events[0]['thread_id'] if validator.events else None,
    }


def isolated_environment(host_home: Path | None = None) -> dict[str, str]:
    names = (
        "APPDATA", "COMSPEC", "LOCALAPPDATA", "NUMBER_OF_PROCESSORS", "PATH",
        "PATHEXT", "PROCESSOR_ARCHITECTURE", "SystemRoot", "TEMP", "TMP",
        "USERPROFILE", "WINDIR",
    )
    environment = {name: os.environ[name] for name in names if name in os.environ}
    if host_home is not None:
        for name, relative in {
            "HOME": "", "USERPROFILE": "", "CODEX_HOME": ".codex",
            "CLAUDE_CONFIG_DIR": ".claude", "APPDATA": "AppData/Roaming",
            "LOCALAPPDATA": "AppData/Local", "XDG_CONFIG_HOME": ".config",
            "TEMP": "tmp", "TMP": "tmp",
        }.items():
            environment[name] = str(host_home / relative)
    return environment


def validate_process_result(result: dict, expected_thread: str | None) -> dict:
    if result["timed_out"]:
        raise ProtocolError("turn_timeout")
    if result["close_error"]:
        raise ProtocolError("process_tree_close_failure")
    if result.get("stream_error"):
        raise ProtocolError(result["stream_error"])
    if result["returncode"] != 0:
        raise ProtocolError("nonzero_exit")
    if result["stderr"]:
        raise ProtocolError("stderr_not_empty")
    return validate_events(result["stdout"], expected_thread)


def validate_native_identity(
    sessions_root: Path, thread_id: str, model: str, effort: str, expected_turns: int,
    turns: list[dict] | None = None,
) -> dict:
    matches = [path for path in sessions_root.rglob(f"*{thread_id}.jsonl") if path.is_file()]
    if len(matches) != 1:
        raise ProtocolError("native_rollout_missing_or_ambiguous")
    session_ids = []
    contexts = []
    native_tool_calls = []
    display_output_calls = []
    native_action_evidence = []
    ambient_project_instructions = False
    agent_instructions = False
    turn_index = 0
    try:
        for line in matches[0].read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            payload = record.get("payload")
            if record.get("type") == "session_meta" and isinstance(payload, dict):
                session_ids.append(payload.get("id"))
            elif record.get("type") == "turn_context" and isinstance(payload, dict):
                if payload.get("multi_agent_version") != "disabled":
                    raise ProtocolError("native_agents_not_disabled")
                contexts.append({"model": payload.get("model"), "effort": payload.get("effort")})
                turn_index += 1
            elif record.get("type") == "response_item" and isinstance(payload, dict) and str(payload.get('type', '')).endswith('_call'):
                literal = re.fullmatch(r'text\(("(?:\\.|[^"\\])*")\);?', str(payload.get('input', '')).strip())
                value = None
                if literal:
                    try:
                        value = json.loads(literal.group(1))
                    except json.JSONDecodeError:
                        pass
                if (payload['type'] == 'custom_tool_call' and payload.get('name') == 'exec'
                        and isinstance(value, str)
                        and 1 <= turn_index <= expected_turns):
                    display_output_calls.append({'turn': turn_index, 'text': value})
                else:
                    native_tool_calls.append({'type': payload['type'], 'name': payload.get('name')})
                    native_action_evidence.append(payload)
            elif record.get("type") == "response_item" and isinstance(payload, dict) and payload.get("type") == "message" and payload.get("role") == "developer":
                agent_instructions |= any(
                    '<multi_agent_role>' in part.get('text', '')
                    or '<multi_agent_mode>' in part.get('text', '')
                    for part in payload.get('content', [])
                )
            elif record.get("type") == "response_item" and isinstance(payload, dict) and payload.get("type") == "message" and payload.get("role") == "user":
                for part in payload.get("content", []):
                    if part.get("type") in ("input_text", "text") and part.get("text", "").lstrip().startswith("# AGENTS.md instructions for "):
                        ambient_project_instructions = True
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, AttributeError) as error:
        raise ProtocolError("invalid_native_rollout") from error
    expected = {"model": model, "effort": effort}
    if session_ids != [thread_id] or len(contexts) != expected_turns or any(item != expected for item in contexts):
        raise ProtocolError("native_identity_or_context_mismatch")
    if ambient_project_instructions:
        raise ProtocolError("native_ambient_project_instructions")
    if agent_instructions:
        raise ProtocolError("native_agent_instructions")
    return {"rollout": str(matches[0]), "session_meta_ids": session_ids, "turn_contexts": contexts,
            "native_tool_calls": native_tool_calls, "display_output_calls": display_output_calls,
            "native_action_evidence": native_action_evidence, "multi_agent_version": "disabled"}


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("case-id", "prompt", "package-root", "receipt", "receipt-member", "catalog", "codex", "output"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--model", required=True, choices=SUPPORTED_TEST_MODELS)
    parser.add_argument("--effort", required=True, choices=(QUALIFIED_EFFORT,))
    for name in ("prompt", "receipt", "catalog", "codex"):
        parser.add_argument("--expected-" + name + "-sha256", required=True, type=expected_hash)
    parser.add_argument("--timeout-seconds", type=float, default=90)
    parser.add_argument("--max-turns", type=int, default=8)
    parser.add_argument("--host-home", type=Path, required=True,
                        help="Dedicated isolated home; provision authentication separately. Never use the real user home.")
    parser.add_argument("--register", type=Path, required=True,
                        help="The existing shared attempt register; retain every attempt and obey the current approved pool limits.")
    parser.add_argument("--run-set", required=True,
                        help="Evaluation revision label. Use a new label after any candidate, prompt, model catalog, host binary or runner change.")
    parser.add_argument("--preparation", type=Path, required=True,
                        help="Private preparation.json from prepare.py; binds this run to its frozen case and generated prompt.")
    args = parser.parse_args(argv)
    if not 1 <= args.max_turns <= 8 or args.timeout_seconds <= 0:
        parser.error("--max-turns must be 1..8 and --timeout-seconds must be positive")
    for name in ("prompt", "package_root", "receipt", "catalog", "codex", "output"):
        setattr(args, name, Path(getattr(args, name)).resolve())
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.output.exists():
        raise FileExistsError(args.output)
    observed = {
        "prompt": verify_hash(args.prompt, args.expected_prompt_sha256, "prompt"),
        "receipt": verify_hash(args.receipt, args.expected_receipt_sha256, "receipt"),
        "catalog": verify_hash(args.catalog, args.expected_catalog_sha256, "catalog"),
        "codex": verify_hash(args.codex, args.expected_codex_sha256, "codex"),
    }
    host_home = args.host_home.resolve(strict=True)
    if host_home == Path.home().resolve() or (host_home / ".codex/config.toml").exists():
        raise ProtocolError("host_home_must_be_isolated_without_user_config")
    manifested = load_package_receipt(args.receipt, args.receipt_member, args.package_root)
    initial_prompt = args.prompt.read_bytes()
    receipt_identity = json.loads(args.receipt.read_text(encoding="utf-8"))
    variant = f'{receipt_identity["profile"]}-{receipt_identity["layout"]}-luna-high'
    binding = verify_preparation(args.preparation, args.case_id, variant, args.package_root, args.receipt, args.prompt)
    observed['preparation'] = sha256_file(args.preparation)
    reservation = reserve(args.register, args.case_id, args.output, variant, args.run_set)
    args.output.mkdir(parents=True)
    workspace = args.output / "workspace"
    workspace.mkdir()
    instructions = args.output / "model-instructions.md"
    instructions.write_bytes(Path(__file__).with_name("comprehension-instructions.md").read_bytes())
    base = base_command(args.codex, args.catalog, args.model, args.effort, instructions)
    manifest = {
        "case_id": args.case_id, "hashes": observed, "package_root": str(args.package_root),
        **binding,
        "attempt_id": reservation["attempt_id"], "budget_register": str(args.register.resolve()),
        "run_set": args.run_set,
        "variant": variant, "host_platform": platform.platform(),
        "inputs": {
            "prompt": str(args.prompt), "receipt": str(args.receipt),
            "receipt_member": args.receipt_member, "catalog": str(args.catalog),
            "codex": str(args.codex), "workspace": str(workspace),
        },
        "package_file_count": len(manifested), "model": args.model, "effort": args.effort,
        "timeout_seconds": args.timeout_seconds, "max_turns": args.max_turns,
        "host_home": str(host_home),
        "runner_sha256": sha256_file(Path(__file__)),
        "instructions_sha256": sha256_file(instructions),
        "process_lifetime_sha256": sha256_file(Path(__file__).with_name("process_lifetime.py")),
        "failure_policy_sha256": sha256_file(Path(__file__).resolve().parents[1] / "instruction_tests/results.py"),
        "binding_helper_sha256": sha256_file(Path(__file__).resolve().parents[1] / "instruction_tests/case_binding.py"),
        "semantic_grade": "pending_manual", "usage_note": "Per-turn values retained; no total inferred.",
    }
    write_json(args.output / "manifest.json", manifest)
    turns = []
    supplied = []
    served: set[str] = set()
    prompt = initial_prompt
    thread_id = None
    final_answer = None
    failure = None
    for number in range(1, args.max_turns + 1):
        command = turn_command(base, workspace, thread_id)
        try:
            result = execute_turn(command, prompt, workspace, args.timeout_seconds, thread_id, host_home)
        except OSError as error:
            failure = f"process_start_failure:{type(error).__name__}"
            break
        if thread_id is None:
            thread_id = result.get('observed_thread_id')
        prefix = f"turn-{number:02d}"
        (args.output / f"{prefix}-prompt.md").write_bytes(prompt)
        (args.output / f"{prefix}-events.jsonl").write_bytes(result["stdout"])
        (args.output / f"{prefix}-stderr.log").write_bytes(result["stderr"])
        turn = {
            "turn": number, "command": command, "worker_pid": result["worker_pid"],
            "returncode": result["returncode"], "timed_out": result["timed_out"],
            "close_error": result["close_error"], "stream_error": result["stream_error"],
            "stderr_length": len(result["stderr"]),
        }
        is_final = False
        try:
            event = validate_process_result(result, thread_id)
            turn.update(event)
            if thread_id is None:
                thread_id = event["thread_id"]
            answer = event["answer"]
            (args.output / f"{prefix}-answer.md").write_text(answer, encoding="utf-8", newline="\n")
            requests = event["read_requests"]
            if requests is None:
                final_answer = answer
                turn["protocol_pass"] = True
                is_final = True
            else:
                blocks = []
                for request in requests:
                    relative = resolve_read_path(request, manifested,
                                                 [item["path"] for item in supplied])
                    delivered, original_hash = validate_requested_file(relative, args.package_root, manifested, served)
                    served.add(relative)
                    supplied.append({"turn": number, "path": relative, "sha256": original_hash})
                    text = delivered.decode("utf-8")
                    blocks.append(f"Requested packaged text `{relative}` (exact text):\n```text\n{text}\n```")
                prompt = ("\n\n".join(blocks) + "\n\n" + CONTINUATION).encode("utf-8")
                turn["protocol_pass"] = True
        except (ProtocolError, OSError) as error:
            turn["protocol_pass"] = False
            failure = str(error)
        turns.append(turn)
        write_json(args.output / f"{prefix}-summary.json", turn)
        if failure or is_final:
            break
    if final_answer is None and failure is None:
        failure = "turn_limit_without_final_answer"
    native = None
    native_failure = None
    original_failure = failure
    observed_behavior_failure = failure if failure_class(failure) == 'behavior' else None
    if thread_id:
        try:
            native = validate_native_identity(host_home / ".codex" / "sessions", thread_id, args.model, args.effort, len(turns), turns)
            if native.get('native_tool_calls'):
                failure = observed_behavior_failure = 'forbidden_model_action'
        except (KeyError, ProtocolError) as error:
            native_failure = str(error)
            if failure is None or observed_behavior_failure:
                failure = native_failure
    summary = {
        "case_id": args.case_id, "thread_id": thread_id, "turn_count": len(turns),
        "served_files": supplied, "turns": turns, "final_answer": final_answer,
        "native": native, "protocol_grade": "PASS" if failure is None else "FAIL",
        "observed_behavior_failure": observed_behavior_failure,
        "original_failure": original_failure, "native_failure": native_failure,
        "protocol_failure": failure, "failure_class": failure_class(failure),
        "semantic_grade": "FAIL" if failure_class(failure) == "behavior" else "pending_group_review",
    }
    write_json(args.output / "summary.json", summary)
    print(json.dumps({key: summary[key] for key in ("case_id", "thread_id", "turn_count", "protocol_grade", "semantic_grade")}), flush=True)
    return 0 if failure is None else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, ProtocolError) as error:
        print(f"case runner failed: {error}. Use --help for required inputs; use @suite as --receipt-member for a suite root. Preserve any reserved attempt and its output.", file=sys.stderr)
        raise SystemExit(3)
