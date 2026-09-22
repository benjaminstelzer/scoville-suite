---
format_version: 1
id: ADR-0026
status: accepted
created: 2026-09-20
accepted: 2026-09-20
scope: project/coordinator-waiting
---

# Keep the coordinator idle while a child runs

## Decision

After dispatch, the coordinator remains dormant until an authoritative child completion, `needs_user_decision`, or new user input wakes it. Transport timeouts must not create recurring coordinator reasoning, project inspection, commentary, or live correction. If the host cannot provide that wake behavior, qualification stays open instead of describing periodic polling as idle.

## Problem

The DIVI coordinator repeatedly re-entered the model while its child was active, consuming millions of mostly cached input tokens and making live supervision an accidental safety mechanism.

## Drivers

- The worker owns its complete bounded unit until it returns a role result.
- Worker isolation and terminal-result validation must remain safe without live coordinator supervision.
- Waiting must not repeatedly reload the coordinator context when no decision or transition is available.
- The current `wait_threads` call is capped at 120 seconds and therefore cannot by itself prove event-driven coordinator idle behavior.

## Considered alternatives

- Keep the current nested polling loop: It can reveal live misbehavior but repeatedly activates the coordinator and couples correctness to supervision.
- Poll less often or align the outer yield with 120 seconds: It reduces token use but still wakes the model without a result and is not idle behavior.
- Resume only from authoritative child or user events: This removes monitoring work and keeps correctness in the child boundary and post-result gates, but depends on host support for an event-driven wake path.

## Consequences

- The coordinator performs no Plan, Decision, Git, project, or child-chat reads while a child remains active.
- Worker terminal isolation and post-result validation cannot rely on a coordinator noticing intermediate actions.
- A host without an event-driven wake path leaves the waiting optimization unqualified rather than silently falling back to periodic model turns.

## Confirmation

1. Run a native child longer than 120 seconds and count coordinator model responses and project actions between dispatch and terminal or decision state.
2. Confirm completion and `needs_user_decision` each wake the coordinator once with authoritative task identity and state.
3. Confirm user input interrupts the dormant wait without reading the active child conversation or project state.

## Revisit when

Reconsider when Codex changes native child-completion notifications, the `wait_threads` ceiling, or deferred tool-cell wake behavior.
