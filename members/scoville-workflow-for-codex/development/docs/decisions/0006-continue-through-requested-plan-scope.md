---
format_version: 1
id: ADR-0006
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/coordination
---

# Continue through the requested Plan scope

## Decision

Treat the entire active Plan as the coordinator's scope unless the user explicitly names one or more Work Items or an end boundary. After each accepted unit the coordinator continues with the next eligible in-scope item without asking again. It returns control only for an exact user decision or after reaching the explicit boundary or completing the Plan.

## Problem

The coordinator interpreted a general implementation request as permission to complete only the current Work Item and stopped even though the active Plan still contained eligible work.

## Drivers

- The active Plan is the durable owner of remaining work.
- Singular request wording does not define a Work Item boundary.
- Explicit Work Item IDs ranges and end points must remain valid scope limits.
- A blocked unit should not prevent independent eligible work from continuing.

## Considered alternatives

- Default to one Work Item: minimizes each run but stops an intended Plan loop prematurely.
- Require an explicit scope on every invocation: removes ambiguity but adds an unnecessary user decision for the common whole-Plan case.
- Default to the active Plan with explicit boundaries: continues useful work while preserving deliberate limits.

## Consequences

- The launcher records whether the user supplied an explicit Plan boundary without reading the Plan.
- The coordinator rereads canonical Plan state and advances through eligible in-scope items after every accepted unit.
- If a blocker leaves no eligible in-scope work the coordinator asks for the exact disposition decision and remains open.
- Successful completion and self-archival occur only at the explicit boundary or complete Plan.

## Confirmation

1. Inspect the Skill and operations reference for matching default-scope and continuation rules.
2. Run focused tests for an unbounded active Plan an explicit boundary and a blocked unit with independent eligible work.
3. Obtain the requested Astra Low review before local installation.

## Revisit when

Native Plan lifecycle behavior can express an equivalent explicit execution scope without launcher metadata.
