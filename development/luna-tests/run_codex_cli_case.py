"""Run one bounded Codex CLI Skill-comprehension case."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import queue
import re
import stat
import subprocess
import sys
import threading
import time

from process_lifetime import WorkerProcess


KNOWN_CODE_MODE_ERROR = (
    "Code Mode is unavailable because code-mode host is disabled. Code mode will fail closed; "
    "enable `features.code_mode_host` and install `codex-code-mode-host`."
)
CONTINUATION = (
    "Continue the same hypothetical case using only supplied text. Do not use\n"
    "tools or execute project actions. Request any other required packaged text\n"
    "with `READ <relative-path>` lines; otherwise provide the final case answer.\n"
)
DISABLED_FEATURES = (
    "shell_tool", "apps", "hooks", "plugins", "remote_plugin", "plugin_sharing",
    "browser_use", "browser_use_external", "browser_use_full_cdp_access",
    "computer_use", "multi_agent", "multi_agent_v2", "collaboration_modes",
    "code_mode_host", "workspace_dependencies", "image_generation",
    "in_app_browser", "tool_suggest", "skill_search",
    "skill_mcp_dependency_install", "enable_mcp_apps",
    "codex_apps_mcp_2026_07_28", "mcp_2026_07_28", "auth_elicitation",
    "tool_call_mcp_elicitation",
)
HASH_PATTERN = re.compile(r"[0-9a-fA-F]{64}\Z")
READ_PATTERN = re.compile(r"READ ([^\r\n]+)\Z")
QUALIFIED_MODEL = "gpt-5.6-luna"
SUPPORTED_TEST_MODELS = (QUALIFIED_MODEL, "gpt-5.6-terra")
QUALIFIED_EFFORT = "medium"


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
    raw_parts = relative.split("/")
    if not raw_parts or raw_parts[0] not in {"references", "assets", "scripts"}:
        raise ProtocolError("invalid_request_path")
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


def parse_read_requests(answer: str) -> list[str] | None:
    lines = answer.splitlines()
    matches = [READ_PATTERN.fullmatch(line) for line in lines]
    if lines and all(matches):
        return [match.group(1) for match in matches if match]
    if any(line.startswith("READ ") for line in lines):
        raise ProtocolError("mixed_or_malformed_read_response")
    return None


class EventValidator:
    """Validate the qualified event stream as each complete line arrives."""

    expected_types = (
        "thread.started", "item.completed", "turn.started", "item.completed", "turn.completed"
    )

    def __init__(self, expected_thread: str | None):
        self.expected_thread = expected_thread
        self.events = []

    def feed(self, line: bytes) -> None:
        try:
            event = json.loads(line)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ProtocolError("event_parse_error") from error
        if not isinstance(event, dict):
            raise ProtocolError("event_is_not_object")
        index = len(self.events)
        if index >= len(self.expected_types) or event.get("type") != self.expected_types[index]:
            raise ProtocolError("unexpected_event_order")
        if index == 0:
            thread_id = event.get("thread_id")
            if not isinstance(thread_id, str) or not thread_id or (self.expected_thread and thread_id != self.expected_thread):
                raise ProtocolError("thread_identity_mismatch")
        elif index == 1:
            item = event.get("item")
            if not isinstance(item, dict) or item.get("type") != "error" or item.get("message") != KNOWN_CODE_MODE_ERROR:
                raise ProtocolError("missing_known_fail_closed_error")
        elif index == 3:
            item = event.get("item")
            if not isinstance(item, dict) or item.get("type") != "agent_message":
                raise ProtocolError("missing_agent_response")
            if not isinstance(item.get("text"), str) or not item["text"].strip():
                raise ProtocolError("empty_agent_response")
        self.events.append(event)

    def finish(self) -> dict:
        if len(self.events) != len(self.expected_types):
            raise ProtocolError("unexpected_event_count")
        return {
            "thread_id": self.events[0]["thread_id"],
            "answer": self.events[3]["item"]["text"],
            "usage": self.events[4].get("usage"),
            "event_types": [event["type"] for event in self.events],
        }


def validate_events(stdout: bytes, expected_thread: str | None) -> dict:
    validator = EventValidator(expected_thread)
    for line in stdout.splitlines():
        validator.feed(line)
    return validator.finish()


def base_command(codex: Path, catalog: Path, model: str, effort: str) -> list[str]:
    if model not in SUPPORTED_TEST_MODELS or effort != QUALIFIED_EFFORT:
        raise ProtocolError("unqualified_model_or_effort")
    command = [
        str(codex), "--ask-for-approval", "never", "--sandbox", "read-only",
        "--model", model, "-c", f'model_reasoning_effort="{effort}"',
        "-c", f'model_catalog_json="{catalog.as_posix()}"', "-c", "mcp_servers={}",
        "-c", 'web_search="disabled"',
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
    expected_thread: str | None = None,
) -> dict:
    deadline = time.monotonic() + timeout
    worker = WorkerProcess(
        command, cwd=workspace, env=isolated_environment(), stdin=subprocess.PIPE,
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
    }


def isolated_environment() -> dict[str, str]:
    names = (
        "APPDATA", "COMSPEC", "LOCALAPPDATA", "NUMBER_OF_PROCESSORS", "PATH",
        "PATHEXT", "PROCESSOR_ARCHITECTURE", "SystemRoot", "TEMP", "TMP",
        "USERPROFILE", "WINDIR",
    )
    return {name: os.environ[name] for name in names if name in os.environ}


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
    sessions_root: Path, thread_id: str, model: str, effort: str, expected_turns: int
) -> dict:
    matches = [path for path in sessions_root.rglob(f"*{thread_id}.jsonl") if path.is_file()]
    if len(matches) != 1:
        raise ProtocolError("native_rollout_missing_or_ambiguous")
    session_ids = []
    contexts = []
    try:
        for line in matches[0].read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            payload = record.get("payload")
            if record.get("type") == "session_meta" and isinstance(payload, dict):
                session_ids.append(payload.get("id"))
            elif record.get("type") == "turn_context" and isinstance(payload, dict):
                contexts.append({"model": payload.get("model"), "effort": payload.get("effort")})
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, AttributeError) as error:
        raise ProtocolError("invalid_native_rollout") from error
    expected = {"model": model, "effort": effort}
    if session_ids != [thread_id] or len(contexts) != expected_turns or any(item != expected for item in contexts):
        raise ProtocolError("native_identity_or_context_mismatch")
    return {"rollout": str(matches[0]), "session_meta_ids": session_ids, "turn_contexts": contexts}


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("case-id", "prompt", "package-root", "receipt", "receipt-member", "catalog", "codex", "output"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--model", required=True, choices=SUPPORTED_TEST_MODELS)
    parser.add_argument("--effort", required=True, choices=(QUALIFIED_EFFORT,))
    for name in ("prompt", "receipt", "catalog", "codex"):
        parser.add_argument("--expected-" + name + "-sha256", required=True, type=expected_hash)
    parser.add_argument("--timeout-seconds", type=float, default=90)
    parser.add_argument("--max-turns", type=int, default=4)
    args = parser.parse_args(argv)
    if not 1 <= args.max_turns <= 4 or args.timeout_seconds <= 0:
        parser.error("--max-turns must be 1..4 and --timeout-seconds must be positive")
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
    manifested = load_receipt(args.receipt, args.receipt_member, args.package_root)
    initial_prompt = args.prompt.read_bytes()
    args.output.mkdir(parents=True)
    workspace = args.output / "workspace"
    workspace.mkdir()
    base = base_command(args.codex, args.catalog, args.model, args.effort)
    manifest = {
        "case_id": args.case_id, "hashes": observed, "package_root": str(args.package_root),
        "inputs": {
            "prompt": str(args.prompt), "receipt": str(args.receipt),
            "receipt_member": args.receipt_member, "catalog": str(args.catalog),
            "codex": str(args.codex), "workspace": str(workspace),
        },
        "package_file_count": len(manifested), "model": args.model, "effort": args.effort,
        "timeout_seconds": args.timeout_seconds, "max_turns": args.max_turns,
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
        result = execute_turn(command, prompt, workspace, args.timeout_seconds, thread_id)
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
            (args.output / f"{prefix}-answer.md").write_text(answer, encoding="utf-8")
            requests = parse_read_requests(answer)
            if requests is None:
                final_answer = answer
                turn["protocol_pass"] = True
                is_final = True
            else:
                if len(requests) != len(set(requests)):
                    raise ProtocolError("duplicate_request")
                blocks = []
                for relative in requests:
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
    if failure is None and thread_id:
        try:
            user_profile = Path(os.environ["USERPROFILE"])
            native = validate_native_identity(user_profile / ".codex" / "sessions", thread_id, args.model, args.effort, len(turns))
        except (KeyError, ProtocolError) as error:
            failure = str(error)
    summary = {
        "case_id": args.case_id, "thread_id": thread_id, "turn_count": len(turns),
        "served_files": supplied, "turns": turns, "final_answer": final_answer,
        "native": native, "protocol_grade": "PASS" if failure is None else "FAIL",
        "protocol_failure": failure, "semantic_grade": "pending_manual",
    }
    write_json(args.output / "summary.json", summary)
    print(json.dumps({key: summary[key] for key in ("case_id", "thread_id", "turn_count", "protocol_grade", "semantic_grade")}), flush=True)
    return 0 if failure is None else 1


if __name__ == "__main__":
    raise SystemExit(main())
