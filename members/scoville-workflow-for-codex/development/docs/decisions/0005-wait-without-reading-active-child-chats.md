---
format_version: 1
id: ADR-0005
status: superseded
created: 2026-09-19
accepted: 2026-09-19
scope: project/coordination
superseded_by: ADR-0012
---

# Wait without reading active child chats

## Decision

During normal execution, the coordinator waits through native task-result events and does not read an active child conversation. Only an explicit user request to inspect or read one named child conversation permits one bounded chat read. A general status request uses the bounded native wait snapshot instead.

## Problem

Repeatedly reading a running child conversation duplicates work in coordinator context and spends tokens without advancing a workflow transition.

## Drivers

- Keep the coordinator focused on result transitions rather than worker narration.
- Preserve the validated child result as the workflow handoff.
- Let the user request targeted inspection when the conversation itself matters.

## Considered alternatives

- Read active child chats during every wait: exposes progress detail but repeatedly consumes coordinator context.
- Never allow chat reads: minimizes tokens but prevents a user-requested inspection.
- Wait by default and allow one bounded user-requested read: preserves the efficient path and a deliberate inspection escape hatch.

## Consequences

- Normal coordination uses `wait_threads` with its cursor and does not call `read_thread`.
- A generic status request uses an immediate or bounded wait snapshot without opening the child conversation.
- A user-requested chat read is scoped to the named child and does not become result or completion evidence.

## Confirmation

1. Inspect the Skill and operations reference for the same default and exception.
2. Run focused contract tests covering normal waiting generic status and explicit chat inspection.
3. Confirm Astra Low reports no remaining contract conflict before local installation or push.

## Revisit when

Native wait events no longer expose enough state to distinguish completion user decisions blockers and timeouts without reading the child conversation.
