---
format_version: 1
id: ADR-0013
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/result-contract
---

# Encode review classifications as strings

## Decision

Require new executor and repair results to encode `code_changed` and `critical_docs_changed` as exact `yes` or `no` strings. Accept the former boolean object only for a child that was already dispatched under that legacy contract.

## Problem

Native wait-result projection can remove Boolean values embedded in an otherwise valid JSON assistant message and make every completed executor result appear malformed.

## Drivers

- Keep the normal completed-result path on `wait_threads` without an additional chat read.
- Preserve explicit independent classifications for code and critical documentation changes.
- Retain one bounded compatibility path for work already running under the former schema.
- Leave identity-bound recovery available for other projection corruption.

## Considered alternatives

- Keep booleans and recover every executor result: Preserves the old schema but adds a large exceptional read to the normal path.
- Encode changed classes as a label list: Avoids booleans but makes the absence of each required classification implicit.
- Encode both required classifications as `yes` or `no` strings: Preserves both explicit keys and avoids the observed Boolean-loss path.

## Consequences

- Every new executor and repair prompt uses the two-string object.
- The coordinator treats either `yes` value as requiring review and verifies two `no` values against the scoped result before skipping review.
- One already-dispatched legacy child may return its requested boolean object without being reformatted.
- A future projection defect still follows ADR-0012's identity-bound recovery gate.

## Confirmation

1. Run the focused workflow contract suite and verify every new prompt definition uses only `yes` or `no` strings.
2. Observe the next new executor result through `wait_threads` and confirm both classifications remain intact.
3. Confirm an in-flight legacy result remains recoverable without changing its original task output.

## Revisit when

Reconsider when native wait results expose typed role fields or preserve embedded JSON values byte-for-byte.
