#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Iterator

from coordinator_contract import ContractError, verify_coordinator, verify_writer


SCHEMA_VERSION = 1
ID_PATTERN = re.compile(r"[A-Za-z0-9._:-]{1,160}\Z")
UNIT_PATTERN = re.compile(
    r"W-[0-9]{3}(?:/step-[1-9][0-9]*|/steps-(?P<first>[1-9][0-9]*)-(?P<last>[1-9][0-9]*))?\Z"
)
WRITER_ROLES = {"executor", "repair"}


class GuardError(Exception):
    def __init__(self, reason: str, diagnostic: str) -> None:
        super().__init__(diagnostic)
        self.reason = reason
        self.diagnostic = diagnostic


def compact(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def guard_integrity(value: dict[str, object]) -> str:
    unsigned = {key: item for key, item in value.items() if key != "integrity"}
    return hashlib.sha256(compact(unsigned).encode("utf-8")).hexdigest()


def seal_guard(value: dict[str, object]) -> dict[str, object]:
    value["integrity"] = guard_integrity(value)
    return value


def actor_id() -> str:
    value = os.environ.get("CODEX_THREAD_ID", "")
    if not ID_PATTERN.fullmatch(value):
        raise GuardError("actor_identity_missing", "CODEX_THREAD_ID is missing or invalid")
    return value


def validate_id(value: str | None, field: str, *, reason: str = "invalid_argument") -> str:
    if not isinstance(value, str) or not ID_PATTERN.fullmatch(value):
        raise GuardError(reason, f"{field} is missing or invalid")
    return value


def validate_title(value: str | None, *, reason: str = "invalid_argument") -> str:
    if not isinstance(value, str) or not value or len(value) > 160 or "\n" in value or "\r" in value:
        raise GuardError(reason, "title is missing or invalid")
    return value


def validate_unit(value: str | None, field: str, *, reason: str = "invalid_argument") -> str:
    match = UNIT_PATTERN.fullmatch(value) if isinstance(value, str) else None
    if match is None:
        raise GuardError(reason, f"{field} is missing or invalid")
    if match.group("first") is not None and int(match.group("first")) >= int(match.group("last")):
        raise GuardError(reason, f"{field} Step range must increase and contain at least two Steps")
    return value


def paths(workspace: Path) -> tuple[Path, Path]:
    root = workspace.resolve()
    if not root.is_dir():
        raise GuardError("workspace_invalid", "workspace must be an existing directory")
    guard = root / ".scoville-workflow" / "guard.json"
    key = hashlib.sha256(str(root).casefold().encode("utf-8")).hexdigest()
    lock_root = Path(tempfile.gettempdir()) / "scoville-workflow-locks"
    lock_root.mkdir(parents=True, exist_ok=True)
    return guard, lock_root / f"{key}.lock"


@contextlib.contextmanager
def process_lock(lock_path: Path) -> Iterator[None]:
    try:
        stream = lock_path.open("a+b")
        stream.seek(0)
        if stream.read(1) != b"0":
            stream.seek(0)
            stream.write(b"0")
            stream.flush()
        stream.seek(0)
    except OSError as error:
        raise GuardError("transition_busy", "another guard transition holds the workspace lock") from error
    locked = False
    try:
        if os.name == "nt":
            import msvcrt

            try:
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError as error:
                raise GuardError("transition_busy", "another guard transition holds the workspace lock") from error
        else:
            import fcntl

            try:
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as error:
                raise GuardError("transition_busy", "another guard transition holds the workspace lock") from error
        locked = True
        yield
    finally:
        try:
            if locked:
                stream.seek(0)
                if os.name == "nt":
                    import msvcrt

                    msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl

                    fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
        finally:
            stream.close()


def guard_shape(value: object, workspace: Path) -> dict[str, object]:
    if not isinstance(value, dict):
        raise GuardError("guard_invalid", "guard root is not an object")
    required = {
        "schema_version",
        "workflow_id",
        "workspace_root",
        "plan",
        "generation",
        "revision",
        "state",
        "launcher_id",
        "coordinator_id",
        "writer",
        "rollover",
        "integrity",
    }
    if set(value) != required:
        raise GuardError("guard_invalid", "guard fields do not match schema version 1")
    if not isinstance(value["schema_version"], int) or isinstance(value["schema_version"], bool) or value["schema_version"] != SCHEMA_VERSION:
        raise GuardError("guard_invalid", "guard schema version is unsupported")
    if not isinstance(value["integrity"], str) or not re.fullmatch(r"[0-9a-f]{64}", value["integrity"]):
        raise GuardError("guard_invalid", "guard integrity field is invalid")
    if value["integrity"] != guard_integrity(value):
        raise GuardError("guard_integrity_mismatch", "guard content changed outside a valid helper transition")
    if value["workspace_root"] != str(workspace.resolve()):
        raise GuardError("guard_workspace_mismatch", "guard workspace does not match the requested workspace")
    if not isinstance(value["plan"], str) or not value["plan"] or len(value["plan"]) > 1000:
        raise GuardError("guard_invalid", "guard Plan reference is invalid")
    if not isinstance(value["generation"], int) or isinstance(value["generation"], bool) or value["generation"] < 0:
        raise GuardError("guard_invalid", "guard generation is invalid")
    if not isinstance(value["revision"], int) or isinstance(value["revision"], bool) or value["revision"] < 0:
        raise GuardError("guard_invalid", "guard revision is invalid")
    validate_id(value["workflow_id"], "workflow_id", reason="guard_invalid")
    validate_id(value["launcher_id"], "launcher_id", reason="guard_invalid")
    if value["launcher_id"] != value["workflow_id"]:
        raise GuardError("guard_invalid", "guard launcher and workflow identities differ")
    if value["coordinator_id"] is not None:
        validate_id(value["coordinator_id"], "coordinator_id", reason="guard_invalid")
    if not isinstance(value["state"], str) or value["state"] not in {
        "initializing",
        "coordinator_ready",
        "coordinator_active",
        "writer_pending",
        "writer_active",
        "rollover_pending",
        "rollover_ready",
        "rollover_validated",
        "coordinator_pending_activation",
    }:
        raise GuardError("guard_invalid", "guard state is invalid")
    writer = value["writer"]
    rollover = value["rollover"]
    state = value["state"]
    if writer is not None:
        if not isinstance(writer, dict) or set(writer) != {"dispatch_key", "unit", "role", "title", "task_id", "active"}:
            raise GuardError("guard_invalid", "writer authorization fields are invalid")
        validate_id(writer["dispatch_key"], "writer.dispatch_key", reason="guard_invalid")
        validate_unit(writer["unit"], "writer.unit", reason="guard_invalid")
        if not isinstance(writer["role"], str) or writer["role"] not in WRITER_ROLES:
            raise GuardError("guard_invalid", "writer role is invalid")
        validate_title(writer["title"], reason="guard_invalid")
        if writer["task_id"] is not None:
            validate_id(writer["task_id"], "writer.task_id", reason="guard_invalid")
        if not isinstance(writer["active"], bool):
            raise GuardError("guard_invalid", "writer active flag is invalid")
    if rollover is not None:
        if not isinstance(rollover, dict) or set(rollover) != {"transition_key", "accepted_unit", "title", "successor_id", "validated"}:
            raise GuardError("guard_invalid", "rollover authorization fields are invalid")
        validate_id(rollover["transition_key"], "rollover.transition_key", reason="guard_invalid")
        validate_unit(rollover["accepted_unit"], "rollover.accepted_unit", reason="guard_invalid")
        validate_title(rollover["title"], reason="guard_invalid")
        if rollover["successor_id"] is not None:
            validate_id(rollover["successor_id"], "rollover.successor_id", reason="guard_invalid")
        if not isinstance(rollover["validated"], bool):
            raise GuardError("guard_invalid", "rollover validated flag is invalid")

    coordinator_required = state != "initializing"
    if coordinator_required != (value["coordinator_id"] is not None):
        raise GuardError("guard_invalid", "coordinator identity does not match guard state")
    if state in {"initializing", "coordinator_ready", "coordinator_active"}:
        if writer is not None or rollover is not None:
            raise GuardError("guard_invalid", "inactive guard state contains an authorization")
    elif state == "writer_pending":
        if writer is None or writer["active"] is not False or rollover is not None:
            raise GuardError("guard_invalid", "pending writer state is inconsistent")
    elif state == "writer_active":
        if writer is None or writer["active"] is not True or writer["task_id"] is None or rollover is not None:
            raise GuardError("guard_invalid", "active writer state is inconsistent")
    elif state == "rollover_pending":
        if writer is not None or rollover is None or rollover["successor_id"] is not None or rollover["validated"] is not False:
            raise GuardError("guard_invalid", "pending rollover state is inconsistent")
    elif state == "rollover_ready":
        if writer is not None or rollover is None or rollover["successor_id"] is None or rollover["validated"] is not False:
            raise GuardError("guard_invalid", "ready rollover state is inconsistent")
    elif state == "rollover_validated":
        if writer is not None or rollover is None or rollover["successor_id"] is None or rollover["validated"] is not True:
            raise GuardError("guard_invalid", "validated rollover state is inconsistent")
    elif state == "coordinator_pending_activation":
        if (
            writer is not None
            or rollover is None
            or rollover["successor_id"] != value["coordinator_id"]
            or rollover["validated"] is not True
        ):
            raise GuardError("guard_invalid", "pending coordinator activation state is inconsistent")
    return value


def read_guard(path: Path, workspace: Path) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise GuardError("guard_missing", "guard is missing or is not a regular file")
    try:
        raw = path.read_text(encoding="utf-8")
        value = json.loads(raw)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise GuardError("guard_unreadable", "guard cannot be read as valid UTF-8 JSON") from error
    if raw != compact(value) + "\n":
        raise GuardError("guard_noncanonical", "guard JSON is not in canonical helper format")
    return guard_shape(value, workspace)


def atomic_write(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    seal_guard(value)
    guard_shape(value, path.parent.parent)
    encoded = (compact(value) + "\n").encode("utf-8")
    handle, temporary = tempfile.mkstemp(prefix=".guard-", dir=str(path.parent))
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def require_revision(guard: dict[str, object], expected: int | None, expected_generation: int | None) -> None:
    if expected is None or expected != guard["revision"]:
        raise GuardError("revision_mismatch", "expected revision does not match the current guard")
    if expected_generation is None or expected_generation != guard["generation"]:
        raise GuardError("generation_mismatch", "expected generation does not match the current guard")


def require_workflow(guard: dict[str, object], expected: str | None) -> None:
    workflow_id = validate_id(expected, "workflow_id")
    if workflow_id != guard["workflow_id"]:
        raise GuardError("workflow_mismatch", "expected workflow does not match the current guard")


def require_coordinator(guard: dict[str, object], actor: str, states: set[str]) -> None:
    if guard["coordinator_id"] != actor:
        raise GuardError("coordinator_mismatch", "runtime task is not the current coordinator")
    if guard["state"] not in states:
        raise GuardError("state_mismatch", "guard state does not permit this coordinator transition")


def increment(guard: dict[str, object]) -> dict[str, object]:
    guard["revision"] = int(guard["revision"]) + 1
    return guard


def response(path: Path, guard: dict[str, object] | None, *, ok: bool, action: str, reason: str, diagnostic: str | None = None, authorized: bool | None = None) -> dict[str, object]:
    value: dict[str, object] = {
        "ok": ok,
        "action": action,
        "reason": reason,
        "diagnostic": diagnostic,
        "path": str(path.resolve()),
        "authorized": authorized,
        "state": guard.get("state") if guard else None,
        "workflow_id": guard.get("workflow_id") if guard else None,
        "generation": guard.get("generation") if guard else None,
        "revision": guard.get("revision") if guard else None,
        "coordinator_id": guard.get("coordinator_id") if guard else None,
        "writer": guard.get("writer") if guard else None,
        "rollover": guard.get("rollover") if guard else None,
    }
    json.loads(compact(value))
    return value


def acquire(args: argparse.Namespace, path: Path, workspace: Path, actor: str) -> dict[str, object]:
    if path.exists():
        raise GuardError("guard_exists", "an existing guard must be reconciled or released")
    workflow_id = validate_id(args.workflow_id, "workflow_id")
    if workflow_id != actor:
        raise GuardError("workflow_mismatch", "workflow_id must equal the launcher's runtime task identity")
    guard: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "workflow_id": workflow_id,
        "workspace_root": str(workspace.resolve()),
        "plan": args.plan,
        "generation": 0,
        "revision": 0,
        "state": "initializing",
        "launcher_id": actor,
        "coordinator_id": None,
        "writer": None,
        "rollover": None,
    }
    atomic_write(path, guard)
    return guard


def transition(args: argparse.Namespace, guard: dict[str, object], actor: str) -> tuple[dict[str, object] | None, bool | None]:
    action = args.command
    require_workflow(guard, args.workflow_id)
    # Enforce supplied native instructions at the existing authority boundary.
    # Read-only inspection and stop cleanup remain available to legacy sessions.
    bootstrap_action = action in {"claim", "validate-successor", "activate-coordinator"}
    coordinator_action = actor == guard["coordinator_id"] and action not in {
        "release", "clear-writer", "verify",
    }
    coordinator_write = action == "verify" and args.role == "coordinator" and actor == guard["coordinator_id"]
    if bootstrap_action or coordinator_action or coordinator_write:
        try:
            verify_coordinator(actor, str(guard["workflow_id"]), Path(str(guard["workspace_root"])))
        except (ContractError, OSError, ValueError) as error:
            raise GuardError("coordinator_contract_invalid", str(error)) from error
    if action == "verify":
        require_revision(guard, args.expected_revision, args.expected_generation)
        authorized = False
        role = args.role
        if role == "coordinator":
            if args.capability == "plan":
                authorized = guard["coordinator_id"] == actor and guard["state"] in {"coordinator_active", "writer_pending"}
            elif args.capability == "stage_commit":
                authorized = guard["coordinator_id"] == actor and guard["state"] == "coordinator_active"
            else:
                raise GuardError("invalid_argument", "coordinator verify requires plan or stage_commit capability")
        elif role in WRITER_ROLES:
            if args.capability != "source":
                raise GuardError("invalid_argument", "writer verify requires source capability")
            writer = guard["writer"] if isinstance(guard["writer"], dict) else {}
            authorized = (
                guard["state"] == "writer_active"
                and writer.get("active") is True
                and writer.get("task_id") == actor
                and writer.get("role") == role
                and writer.get("unit") == args.unit
                and writer.get("dispatch_key") == args.dispatch_key
            )
        elif role in {"reviewer", "audit", "consultation", "other"}:
            if args.capability != "read_only":
                raise GuardError("invalid_argument", "read-only role verify requires read_only capability")
            authorized = False
        else:
            raise GuardError("invalid_argument", "verify requires a known role")
        return guard, authorized

    require_revision(guard, args.expected_revision, args.expected_generation)
    if action == "cancel-initializing":
        if guard["state"] != "initializing" or guard["launcher_id"] != actor or guard["coordinator_id"] is not None:
            raise GuardError("state_mismatch", "only the exact launcher can cancel its unclaimed guard")
        return None, None
    if action == "reconcile-coordinator":
        if guard["state"] != "initializing" or guard["launcher_id"] != actor or guard["coordinator_id"] is not None:
            raise GuardError("state_mismatch", "only the exact launcher can reconcile its initializing coordinator")
        guard["coordinator_id"] = validate_id(args.task_id, "task_id")
        guard["state"] = "coordinator_ready"
    elif action == "claim":
        if guard["state"] != "coordinator_ready" or guard["coordinator_id"] != actor:
            raise GuardError("coordinator_mismatch", "runtime task is not the launcher-reconciled coordinator")
        guard["state"] = "coordinator_active"
    elif action == "authorize-writer":
        require_coordinator(guard, actor, {"coordinator_active"})
        role = validate_id(args.role, "role")
        if role not in WRITER_ROLES:
            raise GuardError("invalid_argument", "writer role must be executor or repair")
        guard["writer"] = {
            "dispatch_key": validate_id(args.dispatch_key, "dispatch_key"),
            "unit": validate_unit(args.unit, "unit"),
            "role": role,
            "title": validate_title(args.title),
            "task_id": None,
            "active": False,
        }
        guard["state"] = "writer_pending"
    elif action == "reconcile-writer":
        require_coordinator(guard, actor, {"writer_pending"})
        writer = guard["writer"]
        if not isinstance(writer, dict) or writer.get("dispatch_key") != args.dispatch_key or writer.get("task_id") is not None:
            raise GuardError("writer_mismatch", "pending writer does not match the reconciliation request")
        try:
            verify_writer(args.task_id, actor, str(guard["workflow_id"]),
                          Path(str(guard["workspace_root"])), str(writer["role"]),
                          str(writer["unit"]), str(writer["dispatch_key"]))
        except (ContractError, OSError, ValueError) as error:
            raise GuardError("writer_transport_invalid", str(error)) from error
        writer["task_id"] = validate_id(args.task_id, "task_id")
    elif action == "activate-writer":
        require_coordinator(guard, actor, {"writer_pending"})
        writer = guard["writer"]
        task_id = validate_id(args.task_id, "task_id")
        if not isinstance(writer, dict) or writer.get("dispatch_key") != args.dispatch_key or writer.get("task_id") != task_id:
            raise GuardError("writer_mismatch", "reconciled writer does not match the activation request")
        writer["active"] = True
        guard["state"] = "writer_active"
    elif action == "clear-writer":
        require_coordinator(guard, actor, {"writer_pending", "writer_active"})
        writer = guard["writer"]
        if not isinstance(writer, dict) or writer.get("dispatch_key") != args.dispatch_key:
            raise GuardError("writer_mismatch", "writer does not match the clear request")
        guard["writer"] = None
        guard["state"] = "coordinator_active"
    elif action == "begin-rollover":
        require_coordinator(guard, actor, {"coordinator_active"})
        if guard["writer"] is not None:
            raise GuardError("writer_active", "coordinator rollover requires no writer authorization")
        guard["rollover"] = {
            "transition_key": validate_id(args.transition_key, "transition_key"),
            "accepted_unit": validate_unit(args.accepted_unit, "accepted_unit"),
            "title": validate_title(args.title),
            "successor_id": None,
            "validated": False,
        }
        guard["state"] = "rollover_pending"
    elif action == "reconcile-successor":
        require_coordinator(guard, actor, {"rollover_pending"})
        rollover = guard["rollover"]
        if not isinstance(rollover, dict) or rollover.get("transition_key") != args.transition_key or rollover.get("successor_id") is not None:
            raise GuardError("rollover_mismatch", "pending rollover does not match the reconciliation request")
        rollover["successor_id"] = validate_id(args.task_id, "task_id")
        guard["state"] = "rollover_ready"
    elif action == "validate-successor":
        if (
            guard["state"] != "rollover_ready"
            or not isinstance(guard["rollover"], dict)
            or guard["rollover"].get("successor_id") != actor
            or guard["rollover"].get("transition_key") != args.transition_key
        ):
            raise GuardError("successor_mismatch", "runtime task is not the ready successor")
        guard["rollover"]["validated"] = True
        guard["state"] = "rollover_validated"
    elif action == "transfer-coordinator":
        require_coordinator(guard, actor, {"rollover_validated"})
        rollover = guard["rollover"]
        if not isinstance(rollover, dict) or rollover.get("transition_key") != args.transition_key or rollover.get("validated") is not True:
            raise GuardError("rollover_mismatch", "validated rollover does not match the transfer request")
        guard["coordinator_id"] = rollover["successor_id"]
        guard["generation"] = int(guard["generation"]) + 1
        guard["state"] = "coordinator_pending_activation"
    elif action == "activate-coordinator":
        if (
            guard["state"] != "coordinator_pending_activation"
            or guard["coordinator_id"] != actor
            or not isinstance(guard["rollover"], dict)
            or guard["rollover"].get("transition_key") != args.transition_key
        ):
            raise GuardError("successor_mismatch", "runtime task is not the transferred successor")
        guard["rollover"] = None
        guard["state"] = "coordinator_active"
    elif action == "release":
        require_coordinator(guard, actor, {"coordinator_active"})
        if guard["writer"] is not None or guard["rollover"] is not None:
            raise GuardError("active_authorization", "guard cannot be released with an active authorization")
        return None, None
    else:
        raise GuardError("invalid_argument", "unknown transition")
    return increment(guard), None


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description="Manage the transient Scoville Workflow write guard.")
    value.add_argument("command", choices=(
        "acquire", "verify", "cancel-initializing", "reconcile-coordinator", "claim", "authorize-writer", "reconcile-writer",
        "activate-writer", "clear-writer", "begin-rollover", "reconcile-successor",
        "validate-successor", "transfer-coordinator", "activate-coordinator", "release",
    ))
    value.add_argument("--workspace", required=True)
    value.add_argument("--expected-revision", type=int)
    value.add_argument("--expected-generation", type=int)
    value.add_argument("--workflow-id")
    value.add_argument("--plan", default="unresolved")
    value.add_argument("--role")
    value.add_argument("--capability", choices=("plan", "stage_commit", "source", "read_only"))
    value.add_argument("--unit")
    value.add_argument("--dispatch-key")
    value.add_argument("--task-id")
    value.add_argument("--title")
    value.add_argument("--transition-key")
    value.add_argument("--accepted-unit")
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    workspace = Path(args.workspace).resolve()
    path: Path | None = None
    guard: dict[str, object] | None = None
    try:
        path, lock_path = paths(workspace)
        actor = actor_id()
        with process_lock(lock_path):
            if args.command == "acquire":
                guard = acquire(args, path, workspace, actor)
                payload = response(path, guard, ok=True, action="acquire", reason="ok")
            else:
                guard = read_guard(path, workspace)
                changed, authorized = transition(args, guard, actor)
                if args.command == "verify":
                    payload = response(path, guard, ok=True, action="verify", reason="authorized" if authorized else "read_only", authorized=authorized)
                elif changed is None:
                    path.unlink()
                    payload = response(path, guard, ok=True, action=args.command, reason="ok")
                else:
                    atomic_write(path, changed)
                    reread = read_guard(path, workspace)
                    if reread != changed:
                        raise GuardError("verification_failed", "guard changed after atomic transition")
                    guard = reread
                    payload = response(path, guard, ok=True, action=args.command, reason="ok")
    except (GuardError, OSError, UnicodeError, json.JSONDecodeError) as error:
        reason = error.reason if isinstance(error, GuardError) else "helper_failure"
        diagnostic = error.diagnostic if isinstance(error, GuardError) else f"{type(error).__name__}: {error}"
        if path is None:
            path = workspace / ".scoville-workflow" / "guard.json"
        payload = response(path, guard, ok=False, action=args.command, reason=reason, diagnostic=diagnostic)
    except Exception as error:  # pragma: no cover - final containment boundary
        if path is None:
            path = workspace / ".scoville-workflow" / "guard.json"
        payload = response(
            path,
            guard,
            ok=False,
            action=args.command,
            reason="helper_failure",
            diagnostic=f"{type(error).__name__}: {error}",
        )
    encoded = compact(payload)
    json.loads(encoded)
    sys.stdout.write(encoded + "\n")
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
