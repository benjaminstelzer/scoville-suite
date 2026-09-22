---
format_version: 1
id: ADR-0025
status: accepted
created: 2026-09-20
accepted: 2026-09-20
scope: project/dispatch
supersedes: ADR-0024
---

# Keep Work Item Next action out of Step dispatch

## Decision

Supersede ADR-0024 only for `Next action`: an exact Step or Step-range projection excludes the Work Item-wide `Next action`, because the selected Step text is the complete executable action. A whole Work Item without Steps retains `Next action`. All other exact-unit fields and exclusions from ADR-0024 remain unchanged.

## Problem

After one Step finishes, the Work Item-wide `Next action` may already name a later Step and can misdirect a worker assigned to an earlier exact unit.

## Drivers

- A child must receive only its assigned execution unit.
- Dispatch must not infer whether free-form `Next action` prose semantically belongs to a selected Step.
- Existing whole-item recovery and no-Step execution still require the live next move.
- Existing format-version-1 Plan files must remain unchanged.

## Considered alternatives

- Include `Next action` for every unit: Preserves ADR-0024 literally but can leak a later Step into an exact Step prompt.
- Parse `Next action` for Step relevance: Retains some prose but adds nondeterministic semantic filtering.
- Exclude it only for Step units: Keeps Step dispatch exact while preserving whole-item behavior.

## Consequences

- Step and Step-range prompts contain no Work Item-wide next move.
- Whole Work Items without Steps retain `Next action`.
- Step-specific prerequisites and action details must reside in Goal, Non-goals, Outcome, Acceptance, selected Step text, or a referenced Decision rather than Evidence or `Next action`.
- No Plan field, migration, or binary change is introduced.

## Confirmation

1. Generate DIVI `W-006/step-3` after its Work Item `Next action` points to Step 4 and confirm the prompt contains neither that line nor Step 4.
2. Generate an EMPCO Work Item without Steps and confirm its `Next action` remains present.
3. Confirm executor and reviewer receive the same resulting unit context.

## Revisit when

Reconsider when Steps gain independent lifecycle state and their own native next-action field.
