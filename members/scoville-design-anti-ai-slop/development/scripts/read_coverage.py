"""Verify complete numbered source reads without retaining the source corpus."""

import argparse
import hashlib
import json
from pathlib import Path
import re


HEADER = re.compile(r"^SOURCE=(\S+) TOTAL=(\d+) RANGE=(\d+)-(\d+)$")
LINE = re.compile(r"^(\d+): (.*)$")
TRUNCATION = re.compile(r"\b\d+\s+(?:tokens|characters)\s+truncated\b|\boutput (?:was )?truncated\b|\btruncated output\b|\[\s*\.{3}\s*truncated\s*\.{3}\s*\]", re.IGNORECASE)


def ranges(numbers):
    result = []
    for number in sorted(set(numbers)):
        if result and result[-1][1] + 1 == number:
            result[-1][1] = number
        else:
            result.append([number, number])
    return result


def observed_text(response):
    if isinstance(response, str):
        return response
    if isinstance(response, dict) and isinstance(response.get("observer_received"), str):
        return response["observer_received"]
    raise ValueError("Response must be received text or a record with string observer_received")


def verify_coverage(responses, expected_source=None, reference_bytes=None):
    if not isinstance(responses, list):
        raise ValueError("responses must be a list")
    reference_lines = None
    if reference_bytes is not None:
        reference_lines = reference_bytes.decode("utf-8").splitlines()
    total = None
    source = expected_source
    received = {}
    contradictions = []
    receipts = []
    duplicate_count = 0
    for index, response in enumerate(responses):
        text = observed_text(response)
        receipt = {"response": index, "received_text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "declared_range": None, "observed_ranges": [], "missing_in_declared_range": None, "notes": []}
        receipts.append(receipt)
        pieces = text.splitlines(keepends=True)
        headers = [(position, HEADER.fullmatch(piece.rstrip("\r\n"))) for position, piece in enumerate(pieces)]
        headers = [(position, match) for position, match in headers if match]
        if len(headers) != 1:
            receipt["notes"].append("missing-observed-header" if not headers else "multiple-observed-headers")
            if len(headers) > 1:
                contradictions.append(f"response {index}: multiple source headers")
            continue
        position, match = headers[0]
        name, count, first, last = match.groups()
        count, first, last = int(count), int(first), int(last)
        if source is None:
            source = name
        if source != name:
            contradictions.append(f"response {index}: source mismatch {name!r} != {source!r}")
            continue
        if total is None:
            total = count
        if total != count:
            contradictions.append(f"response {index}: total mismatch {count} != {total}")
            continue
        if reference_lines is not None and count != len(reference_lines):
            contradictions.append(f"response {index}: total differs from reference line count")
        if not ((count == 0 and first == last == 0) or (1 <= first <= last <= count)):
            contradictions.append(f"response {index}: range outside declared source")
            continue
        receipt["declared_range"] = [first, last]
        numbers = []
        previous = 0
        for piece in pieces[position + 1:]:
            line = LINE.fullmatch(piece.rstrip("\r\n"))
            if not line:
                continue
            if not piece.endswith("\n"):
                receipt["notes"].append("unterminated-numbered-line")
                continue
            if TRUNCATION.search(piece):
                receipt["notes"].append("numbered-line-contains-transport-truncation-marker")
                continue
            number, content = int(line[1]), line[2]
            if not first <= number <= last or number == 0:
                contradictions.append(f"response {index}: line {number} outside declared range")
                continue
            if number <= previous:
                contradictions.append(f"response {index}: nonascending or repeated line {number}")
            previous = number
            numbers.append(number)
            if number in received:
                duplicate_count += 1
                if received[number] != content:
                    contradictions.append(f"response {index}: conflicting content at line {number}")
            else:
                received[number] = content
            if reference_lines is not None:
                if number > len(reference_lines) or content != reference_lines[number - 1]:
                    contradictions.append(f"response {index}: reference content mismatch at line {number}")
        receipt["observed_ranges"] = ranges(numbers)
        expected = set(range(first, last + 1)) if count else set()
        receipt["missing_in_declared_range"] = ranges(expected - set(numbers))
    expected_count = len(reference_lines) if reference_lines is not None else total
    missing = None if expected_count is None else ranges(set(range(1, expected_count + 1)) - received.keys())
    complete = total is not None and missing == [] and not contradictions
    return {
        "status": "contradictory" if contradictions else ("complete" if complete else "unverified"),
        "complete": complete,
        "source_id": source,
        "total_lines": total,
        "reference_total_lines": len(reference_lines) if reference_lines is not None else None,
        "reference_source_sha256": hashlib.sha256(reference_bytes).hexdigest() if reference_bytes is not None else None,
        "reference_scope": "decoded source-line content; original source bytes hashed for evaluator provenance only" if reference_bytes is not None else None,
        "observed_line_count": len(received),
        "observed_ranges": ranges(received),
        "missing_ranges": missing,
        "duplicate_line_count": duplicate_count,
        "contradictions": contradictions,
        "responses": receipts,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path, help="JSON with source_id and responses")
    parser.add_argument("--reference", type=Path, help="Known source bytes for content matching")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
    reference = args.reference
    if reference is None and receipt.get("reference"):
        reference = args.receipt.parent / receipt["reference"]
    result = verify_coverage(receipt["responses"], receipt.get("source_id"), reference.read_bytes() if reference else None)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
