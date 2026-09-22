---
format_version: 1
id: ADR-0019
status: superseded
created: 2026-09-19
accepted: 2026-09-19
scope: project/execution-routing
superseded_by: ADR-0021
---

# Allow explicit point-level execution overrides

## Decision

Allow an explicitly user-selected executor model or reasoning effort on one Work Item or unperformed Step. Resolve each property independently with precedence Step override, Work Item override, then the selected Workflow route default. Validate the final pair against current host support, block rather than substitute when unavailable, preserve reviewer routing, and separate bundles whose effective executor pairs differ.

## Problem

The native Plan currently forbids model names while Workflow always maps route classes through defaults, so an explicit point-scoped user choice has no canonical representation or deterministic dispatch precedence.

## Drivers

- The selected model and reasoning must be visible in the exact Plan point they govern.
- Defaults remain authoritative when no explicit point override exists.
- A point override must not lower route risk, suppress review, or affect coordinator and reviewer assignments.
- Started history and already launched children must retain their actual pair.

## Considered alternatives

- Put model choices in Goal or prose: Recreates global history growth and leaves precedence ambiguous.
- Create one Decision per execution choice: Adds durable architecture records for ordinary point-scoped runtime choices.
- Add strict Work Item and Step annotations: Gives the dispatcher one visible, validated source while retaining route defaults.

## Consequences

- A Work Item may use `Execution override: model=ID; reasoning=LEVEL`; a Step may use `[execute: model=ID; reasoning=LEVEL]` after its optional route annotation. Either property may appear alone in canonical key order.
- Work Item overrides change only while `todo`; after start, only an explicitly named unperformed Step's execution annotation may change, without altering its action prose or any completed or running dispatch.
- Executor repair and rollover successors inherit the launched effective pair. Reviewer and coordinator pairs continue to come from Workflow configuration.
- Malformed or unsupported overrides block the selected unit and never silently fall back.

## Confirmation

1. Validate complete, partial, duplicate, unknown, malformed, unsupported, inherited, and no-override cases.
2. Verify property-wise resolution and bundle separation for different effective executor pairs.
3. Verify reviewer isolation, repair and rollover inheritance, and unchanged default routing when no override exists.

## Revisit when

Reconsider if Codex exposes a typed native per-task execution policy that the Plan and Workflow can reference without duplicating ownership.
