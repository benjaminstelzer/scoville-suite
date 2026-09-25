#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from typing import Any


MAGIC = "SCOVILLE_RESULT_V1"
ROLES = {"executor", "reviewer", "repair"}
STATUSES = {
    "executor": {"completed", "blocked", "needs_user_decision", "context_handoff"},
    "repair": {"completed", "blocked", "needs_user_decision", "context_handoff"},
    "reviewer": {"pass", "changes_requested", "blocked", "needs_user_decision", "context_handoff"},
}


class RoleResultError(ValueError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


def configure_utf8() -> None:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="strict")


def compact(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def validate_semantics(value: dict[str, Any], role: str) -> dict[str, Any]:
    status = value.get("status")
    if status not in STATUSES[role]:
        raise RoleResultError("STATUS_INVALID", "status is not allowed for this role")
    summary = value.get("summary")
    if not isinstance(summary, str) or not summary or len(summary) > 800:
        raise RoleResultError("SUMMARY_INVALID", "summary must contain 1 to 800 characters")
    findings = value.get("findings")
    if (
        not isinstance(findings, list)
        or len(findings) > 8
        or any(not isinstance(item, str) or not item or len(item) > 400 for item in findings)
    ):
        raise RoleResultError("FINDINGS_INVALID", "findings must contain at most eight non-empty strings of at most 400 characters")
    if len(summary) + sum(len(item) for item in findings) > 4000:
        raise RoleResultError("PROSE_LIMIT_EXCEEDED", "summary and findings exceed 4000 characters")
    if role == "reviewer" and status == "pass" and findings:
        raise RoleResultError("PASS_WITH_FINDINGS", "a passing review cannot contain findings")
    if role in {"executor", "repair"}:
        review = value.get("review")
        if status == "completed":
            if not isinstance(review, dict) or list(review) != ["code_changed", "critical_docs_changed"]:
                raise RoleResultError("REVIEW_FIELDS_INVALID", "a completed result requires both ordered review fields")
            if any(item not in {"yes", "no"} for item in review.values()):
                raise RoleResultError("REVIEW_VALUE_INVALID", "review values must be yes or no")
        elif review is not None:
            raise RoleResultError("REVIEW_NOT_ALLOWED", "review fields are allowed only for completed results")
    return value


def parse_line_result(raw: str, role: str) -> dict[str, Any]:
    if not isinstance(raw, str) or not raw:
        raise RoleResultError("RESULT_EMPTY", "result is empty")
    if "\x00" in raw or "\r" in raw.replace("\r\n", ""):
        raise RoleResultError("LINE_ENDING_INVALID", "result contains an invalid line ending or NUL byte")
    if raw.endswith("\r\n"):
        raw = raw[:-2]
    elif raw.endswith("\n"):
        raw = raw[:-1]
    lines = raw.replace("\r\n", "\n").split("\n")
    if not lines or lines[0] != MAGIC:
        raise RoleResultError("MAGIC_INVALID", f"first line must be exactly {MAGIC}")
    if any(not line for line in lines[1:]):
        raise RoleResultError("EMPTY_LINE", "result contains an empty or trailing line")

    fields: list[tuple[str, str]] = []
    for line in lines[1:]:
        if "=" not in line:
            raise RoleResultError("FIELD_INVALID", "every field line must use key=value")
        key, value = line.split("=", 1)
        if not key or not value or value != value.strip():
            raise RoleResultError("FIELD_INVALID", "field keys and values must be non-empty and unpadded")
        if key not in {"role", "status", "code_changed", "critical_docs_changed", "summary", "finding"}:
            raise RoleResultError("FIELD_UNKNOWN", f"unknown field: {key}")
        fields.append((key, value))

    if len(fields) < 3:
        raise RoleResultError("FIELDS_MISSING", "required result fields are missing")
    actual_role = fields[0] if fields else None
    if actual_role != ("role", role):
        raise RoleResultError("ROLE_INVALID", "role field is missing, misplaced, or does not match the assignment")
    if fields[1][0] != "status":
        raise RoleResultError("FIELD_ORDER_INVALID", "status must follow role")
    status = fields[1][1]

    if role in {"executor", "repair"} and status == "completed":
        expected_prefix = ["role", "status", "code_changed", "critical_docs_changed", "summary"]
    else:
        expected_prefix = ["role", "status", "summary"]
    keys = [key for key, _value in fields]
    if keys[:len(expected_prefix)] != expected_prefix or any(key != "finding" for key in keys[len(expected_prefix):]):
        raise RoleResultError("FIELD_ORDER_INVALID", "fields are missing, duplicated, or out of order")

    mapped = dict(fields[:len(expected_prefix)])
    findings = [value for key, value in fields[len(expected_prefix):] if key == "finding"]
    result: dict[str, Any] = {"status": status, "summary": mapped["summary"]}
    if role in {"executor", "repair"}:
        result["review"] = None
        if status == "completed":
            result["review"] = {
                "code_changed": mapped["code_changed"],
                "critical_docs_changed": mapped["critical_docs_changed"],
            }
    result["findings"] = findings
    return validate_semantics(result, role)


def parse_role_result(raw: str, role: str) -> dict[str, Any]:
    if role not in ROLES:
        raise RoleResultError("ROLE_INVALID", "unsupported role")
    return parse_line_result(raw, role)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Validate one Scoville Workflow role result from stdin.")
    result.add_argument("--role", choices=sorted(ROLES), required=True)
    return result


def main(argv: list[str] | None = None) -> int:
    configure_utf8()
    args = parser().parse_args(argv)
    try:
        raw = sys.stdin.buffer.read().decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        sys.stdout.write(compact({
            "schema_version": 1,
            "valid": False,
            "diagnostics": [{"code": "UTF8_INVALID", "message": "result is not valid UTF-8"}],
        }) + "\n")
        return 1
    try:
        parsed = parse_role_result(raw, args.role)
    except RoleResultError as error:
        sys.stdout.write(compact({
            "schema_version": 1,
            "valid": False,
            "diagnostics": [{"code": error.code, "message": error.message}],
        }) + "\n")
        return 1
    sys.stdout.write(compact({"schema_version": 1, "valid": True, "result": parsed}) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
