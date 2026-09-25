# Release preflight

## Current candidate

The suite now contains Code, Handoff, Plan, UI, Workflow and WordPress UI.
Standalone and general projections contain the five portable members. The Codex
projection also contains Workflow.

Use only `E:/Dropbox/AI Projects/skills/temp/release/` for staging. Its
`standalone`, `general` and `codex` directories hold development projections.
Final committed exports belong under `exports/general` and `exports/codex` in
the same root. Wait for current readers before refreshing any staging directory.

The post-removal builds have passed package checks, but their receipts record a
dirty source tree. They are development artifacts, not release evidence. Older
aggregate model runs covered a different member inventory and do not approve the
current candidate.

## Retained evidence and open gates

- Native profile validation reported zero errors and zero warnings after the
  membership and Plan cleanup.
- Five suite build tests passed after rebuilding the six retained members.
- Forty-four shared tests passed. The separate Ask repository still holds an
  older shared snapshot, so its portable-source comparison remains outside this
  cleanup and must not be repaired through pre-emptive Ask work.
- `selected-cases.json` owns the current 45-case comprehension selection. No
  complete result exists for the final package bytes.
- Existing targeted reports prove only the exact historical package and runtime
  named in each report.

Before W-010, create clean scoped commits, rebuild all affected projections and
run the checks changed by those commits. Then complete the required Astra review
of the final non-Ask state using the review session designated by PLAN-0002.
Record exact revisions, receipts, model identity and unresolved limits. Do not
carry an earlier pass across changed package bytes.

W-010 publishes the general suite and Plan under its existing authorization.
W-011 publishes the Codex suite and verifies the public profile entry. Stop
afterward before PLAN-0002/W-001. W-001 and W-002 remain todo and require a new
explicit instruction.
