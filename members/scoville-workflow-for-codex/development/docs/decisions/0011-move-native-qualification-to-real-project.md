---
format_version: 1
id: ADR-0011
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/qualification
---

# Move native qualification to the real-project run

## Decision

Treat W-012 and W-013 source checks as implementation evidence only; assign native recovery and bundle task-count qualification to W-017's explicitly authorized real-project run.

## Problem

W-013 is terminal while its Acceptance's native executor and reviewer count evidence remains explicitly pending W-017.

## Drivers

- Preserve W-012 and W-013 terminal history.
- Do not claim native lifecycle behavior from source-contract fixtures.
- Use the already authorized real-project observation instead of a synthetic lifecycle fixture or fixed token target.

## Considered alternatives

- Reopen or rewrite W-013: Would violate immutable terminal Work Item history.
- Treat the source checks as native qualification: Would overstate the observed evidence.
- Qualify the behavior in W-017: Preserves history and puts observation in the real-project run that already owns token and task accounting.

## Consequences

- W-012 and W-013 retain implementation evidence without claiming native execution.
- W-017 must observe a compatible five-Step range using one executor and at most one initial reviewer, with mixed-route and user-decision boundaries remaining separate.
- If the real project cannot exercise both bundle and boundary cases, qualification is inconclusive and W-017 remains nonterminal.
- No synthetic lifecycle fixture or fixed token-improvement target is introduced.

## Confirmation

1. Run W-017 on an explicitly authorized real project and capture the exact executor and reviewer task IDs for one compatible five-Step range.
2. Confirm that the compatible range uses one executor and at most one initial reviewer.
3. Confirm that mixed-route and user-decision boundaries remain separate, or record the qualification as inconclusive and keep W-017 nonterminal.

## Revisit when

Reconsider if a later native workflow run supplies stronger directly comparable lifecycle evidence without synthetic fixtures.
