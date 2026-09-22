---
format_version: 1
id: ADR-0018
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/plan-authorship
---

# Normalize Plan Goal ownership before writing

## Decision

Treat a Plan Goal as the normalized current target, boundary, and genuinely plan-wide product constraints, never as an append-only chronology. Route operational facts to their canonical Work Item, Decision, Evidence, Next action, or repository-policy owner before writing; keep the Goal byte-identical when a message changes none of its owned semantics. Keep selector output lossless and add no size or truncation gate.

## Problem

The EMPCO Goal accumulated dated orders, priorities, task identities, versions, deployment state, and evidence even though those facts had narrower durable owners, causing every selected worker context to repeat unrelated history.

## Drivers

- Workers must receive every relevant fact without selector truncation or heuristic omission.
- Goal prose must remain structured, concise, current, and complete.
- Moving a fact is safe only when every affected future dispatch can still reach its canonical owner.
- Existing bloated Goals require a separately authorized normalization rather than silent rewriting during ordinary work.

## Considered alternatives

- Add selector size limits: Bounds tokens by blocking or omitting context but does not correct authorship and risks withholding required information.
- Keep general compactness advice only: Preserves flexibility but already failed to prevent dated append-only growth.
- Normalize ownership before every Goal write: Preserves full information while preventing operational history from entering the global projection.

## Consequences

- Every proposed Goal is audited as a complete state, not only by inspecting added lines.
- Dates, identifiers, versions, priorities, and evidence are routing signals rather than universally forbidden tokens; a genuinely plan-wide normative value may remain.
- A relocation check proves requirement reachability and creates no second durable requirement registry.
- The deterministic selector continues to emit the complete Goal and Non-goals.

## Confirmation

1. Add evaluation cases in Scoville Plan showing operational messages leave Goal bytes unchanged and genuine target changes replace the owning statement.
2. Normalize the DIVI and EMPCO Goals only after the corrected Skill is installed.
3. Validate both profiles and compare selected current and representative future contexts with the classified requirements.

## Revisit when

Reconsider if the native Plan format gains typed plan-wide constraints with an equally lossless selection contract.
