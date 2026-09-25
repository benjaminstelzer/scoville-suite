# Release preflight

## Current candidate

The general suite contains Code, Handoff, Plan and UI. WordPress backend UI
is a local adapter inside UI. The Codex suite also contains Workflow and Ask.
Ask additionally has its Codex-only standalone package and a catalog entry in
the general README; that entry does not add a general runtime member.

Use only `<workspace-root>/skills/temp/release/` for staging. Its
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
- The subsequent Ask update passed 17 member tests and 46 shared tests, with
  three projections and real provider follow-ups recorded in
  `members/scoville-ask-for-codex/development/test-evidence.md`.
- `selected-cases.json` owns the current 45-case comprehension selection. No
  complete result exists for the final package bytes.
- Existing targeted reports prove only the exact historical package and runtime
  named in each report.

PLAN-0012 owns the release sequence. W-011 requires a fresh read-only
gpt-6-astra/medium review of sources, all four package layouts, full exports,
public outputs, Viewer assets, checksums, inventory and planned GitHub changes.
Resolve relevant findings before W-009 publication. Record exact revisions,
receipts and evidence limits. Build success grants no publication authority.

The current preparation includes PLAN-0013. Its W-007 comparison and Workflow
run were cancelled by the user; W-008/W-009 retain the encoding, activation and
historical-priority corrections. Rebuild affected packages before review.
Earlier package evidence does not establish acceptance of changed bytes.
Viewer tests remain excluded under ADR-0078; retain existing artifact provenance
without claiming a new Viewer build or runtime test.

Final exports require inspected, committed sources and a current shared
snapshot. The authorizing task must approve any missing commit or publication
authority. W-009 also checks PLAN-0011 completion and applicable release gates;
W-010 verifies the resulting installations and links.


For this PLAN-0012 release only, ADR-0080 records the user's decision to omit a
second Astra check after the two locally verified corrections. ADR-0081 waives
the complete 45-case Luna gate for this release. Neither check is reported as
passed. All other publication and remote-verification gates remain in force.
