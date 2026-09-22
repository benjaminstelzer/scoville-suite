---
format_version: 1
id: ADR-0016
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/archival
---

# Verify terminal child archival

## Decision

Require an authoritative response for the exact terminal child ID with `archived: true` before Plan mutation or another child transition. Generic tool completion and task-list membership are not proof; an interrupted workflow performs one bounded same-ID reconciliation.

## Problem

Archive calls can be acknowledged as completed while a terminal reviewer remains visible, so advancing from the call status alone loses lifecycle cleanup assurance.

## Drivers

- Keep executor, reviewer, repair, and rollover cleanup tied to the exact recorded identity.
- Prevent duplicate successors or reviewers while a predecessor's archival state is uncertain.
- Recover terminal children left visible after interruption without guessing from title or recency.
- Never archive active or user-decision tasks or discard an unretained result.

## Considered alternatives

- Trust successful tool-call completion: Costs no extra read but did not prove that DIVI reviewers were archived.
- Trust active or archived task lists: Uses existing inventory controls but delegated children are not exposed reliably enough for proof.
- Require exact-ID state with one bounded reconciliation: Adds one recovery operation only on uncertainty and preserves identity and lifecycle gates.

## Consequences

- Ordinary verified archival adds no extra child or Plan work.
- Missing exact archival state pauses the transition for a user decision instead of silently proceeding.
- Resume first reconciles any retained terminal child whose archival was not explicitly verified.

## Confirmation

1. Run the workflow contract suite and verify the exact-state scenarios.
2. Complete one executor and reviewer lifecycle and observe the same ID with `archived: true` before Plan advancement.
3. Resume with one retained terminal child still visible and verify one same-ID reconciliation without creating another child.

## Revisit when

Reconsider when native terminal-result collection atomically archives the child and returns authoritative archival state.
