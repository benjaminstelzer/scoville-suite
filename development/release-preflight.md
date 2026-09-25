# Release preflight

## Current candidate

The general suite contains Code, Handoff, Plan and UI. WordPress backend UI
is a local adapter inside UI. The Codex suite also contains Workflow and ASK.
ASK additionally has its Codex-only standalone package and a catalog entry in
the general README; that entry does not add a general runtime member.

Use only `E:/Dropbox/AI Projects/skills/temp/release/` for staging. Its
`standalone`, `general` and `codex` directories hold development projections.
Final committed exports belong under `exports/general` and `exports/codex` in
the same root. Wait for current readers before refreshing any staging directory.

The UI merge is tracked in PLAN-0006. Its builds under `ui-merge/yaml-fix/` have dirty
source receipts and are development artifacts, not release evidence. Astra has
approved their instructions and package contents for delegated SOL High tests.
Five focused build tests, all three package checks and isolated export/rebuild
passed under SOL High. After the earlier CLI comparison was blocked, a visible
SOL High task implemented and checked Greenfield and existing UI changes in
22 minutes, including keyboard paths and i18n preparation. Its evidence is in
`development/ui-visible-sol-results.md`. There is no controlled relative-effect
comparison or release approval. PLAN-0006 is closed under the final user scope.

## Retained evidence and open gates

- Native profile validation reported zero errors and zero warnings after the
  membership and Plan cleanup.
- Five suite build tests passed historically for the six-member inventory,
  before the UI merge. They do not verify the current inventory.
- The subsequent ASK update passed 17 member tests and 46 shared tests, with
  three projections and real provider follow-ups recorded in
  `members/scoville-ask-for-codex/development/test-evidence.md`.
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
W-011 publishes the Codex suite and verifies the public profile entry. ASK
implementation was independently authorized and is already complete. Its old
source cleanup is tracked by PLAN-0011/W-013. The current review-fix Plan and
its proposals are separate from this closure; they are not release evidence.
