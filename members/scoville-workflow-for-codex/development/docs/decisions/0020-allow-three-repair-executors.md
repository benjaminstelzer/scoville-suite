---
format_version: 1
id: ADR-0020
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/repair-policy
---

# Allow three repair executors before user disposition

## Decision

Allow at most three repair executors after the initial executor attempt. Request user disposition only when executor-owned findings remain after the third repair.

## Problem

The two-repair default can require premature user intervention while a bounded third correction can still resolve the reviewed unit, as observed in EMPCO.

## Drivers

- The user explicitly selected three repair attempts as the default.
- Repair remains bounded and must preserve the existing review, archival, workspace, and commit gates.
- A fourth repair must not begin without a new user choice.

## Considered alternatives

- Keep two repairs: Preserves the old limit but repeats the premature EMPCO escalation.
- Allow three repairs: Adds one bounded correction opportunity before human disposition.
- Retry without a limit: Avoids early escalation but can loop without a decision boundary.

## Consequences

- The maximum executor sequence is one initial executor plus three repair executors.
- Every repair inherits the launched executor model and reasoning pair.
- Remaining findings after repair three require user disposition and block acceptance or commit.

## Confirmation

1. Assert the three-repair limit and fourth-repair prohibition in the Workflow contract tests.
2. Verify the README and runtime operations state the same default.

## Revisit when

Reconsider if observed real-project repair data supports a different bounded default.
