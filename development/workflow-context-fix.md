# Workflow context-load fix — W-021–W-023

2026-09-21. Private source and staged package only. Thresholds and polling are
unchanged. No live DIVI5 task, installed Skill, publication or Git commit changed.

## Delivered behavior

- `build_dispatch_prompt.py`: transport envelope and fresh binding-only mode.
  Binding covers selected Plan/Decisions, role inputs, target/guard arguments,
  builder and selector source. Full required child content remains unchanged.
- `dispatch_transport.js`: one preparation per key; integrity-checked memory
  payload; lifecycle-produced arguments preserve exact bytes/target. Reservation
  precedes async checking and send_unknown precedes the native call. Exceptions,
  conflicting inputs or uncertain outcomes never authorize replay.
- `references/operations.md`: mandatory invariant core plus deterministic
  routing to twelve phase owners. All 161 substantive W-021 paragraphs were
  located unchanged after the split. Four invariant paragraphs moved to core;
  explicit links cover cross-phase gates. Reuse requires complete current
  contents, never just read markers; context loss reloads required rules.

No shared lifecycle contract changed; the new adapter consumes its existing
message/create operations. Ask packages therefore need no rebuild for this fix.
The built Workflow remains standalone with bundled shared dependencies.

## Deterministic evidence

- Workflow test discovery: **61 tests, zero failures/errors**. Includes real
  builder/lifecycle boundaries, mocked writer send and reviewer creation,
  changed inputs/guard/target, byte mutation, Unicode/hash boundaries, missing
  memory, truncated helper JSON, shortened display, unknown send and concurrency.
- CLI harness: **16 tests passed**, including Terra-only medium selection and
  rejection of unqualified pairs. General Luna gate selection remains unchanged.
- Phase/link test passed against both source manifest mappings and the actual
  built package. All twelve section owners remain unique and reachable.
- Build receipt/package verification returned valid:true, no errors.
- The generic Skill Creator validator failed on the pre-existing frontmatter
  key `compatibility`, which its allowed-key list omits. This fix leaves that
  frontmatter unchanged; no generic-validator pass is claimed. Workflow tests
  and package parity are separate evidence, not a replacement schema claim.
- Codex execution-memory smoke: built prompt 10,158 Unicode characters /
  10,193 UTF-8 bytes, SHA256
  `d3976ae305b83ce459674718f636a49624db790cf626ea7fb92f79719c47b242`.
  Retained across exec calls; passed through built lifecycle helper to one
  mock sender unchanged; second attempt rejected. No payload printed.
  The first smoke preparation failed before dispatch; the later captured
  complete envelope was used for this check. No live sender/guard proof.

One legacy assertion still expected pre-W-019 recovery wording/table despite
the existing source already permitting authenticated projection recovery. It
was aligned to that contract, retaining its identity/completion restrictions.

## Context measurement, not cost

Original operations: **93,326 characters**. New core: **5,597 characters**;
wait phase: **12,013**; activation: **16,670**; selection: **6,557**.
These are Unicode character counts, not tokens. Full-phase coverage still
exists and a task crossing every phase may eventually load it all.

In the same deterministic transport scenario, builder count is one and native
send-attempt count is one; model-facing prompt-body output is zero, with compact
receipts only. The G15 baseline emitted a 16,841-character dispatch three times
plus lifecycle arguments. This fix removes that output path; it does not prove
a measured production token or monetary saving. Live counters were not retested.

## Terra Medium author evaluation

Tested only the private build:
`<workspace-root>/temp/2026-09-21-workflow-context-fix/final/scoville-suite/packages/scoville-workflow-for-codex/scoville-workflow-for-codex`.

Receipt SHA256:
`e185f88b955a003e4e704fb27faafe87ddfe02841bea24533cf95b1981ebd4e1`.

Original tasks/key were frozen before execution; key SHA256:
`21ae0889b171e02bfa401b75198899e35ea181be3b590d3b87d85d78d9af21b7`.
Three cases contain fifteen independent variants. One supplemental case checks
two omissions; its separate key was fixed before that run. No prior answers or
grading feedback were sent to the tester. All nine native turn_context records
confirm **gpt-5.6-terra / medium**; no substitute model or tool action occurred.

| Case | Exact session ID | Turns | Protocol | Author observation |
| --- | --- | --- | --- | --- |
| context-01 | 01a0c5df-bfe7-7301-9258-119b70467114 | 3 | PASS | Safe decisions; see author notes |
| context-02 | 01a0c5e0-fc1e-72a0-8d74-7ffca4ab204d | 2 | PASS | Safe decisions; see author notes |
| context-03 | 01a0c5e0-fbf6-71a1-b571-728bd57ce6a0 | 3 | PASS | Safe decisions; see author notes |
| context-04 | 01a0c5e4-425a-72e1-a3c7-e53d715f1056 | 1 | PASS | Required send-state/core details explicit |

Author notes:
- 01: stored payload reuse and all invalid-input cases handled safely; repeated
  receipt inspection causes no send. Initial answer omitted the pre-send state.
- 02: missing memory/unknown send block replay; proven matching source preserves
  changes_requested, while a remaining conflict blocks acceptance. Pre-send
  state was again not explicit.
- 03: correct phase reuse/invalidation and both equality boundaries: coordinator
  33 triggers rollover, worker 66 continues. Initial answer omitted core reload.
- 04: explicitly requires send_unknown before sender, no retry on exception,
  exact receipt fields and core/current-phase reload. The transient internal
  checking reservation is proven by the concurrency test, not model prose.
- Combined verdict: requested safety and routing behavior demonstrated. Initial
  omissions remain recorded; the first three runs alone were not a fully
  explicit answer to every key criterion.

Raw usage is retained per turn in temp summaries; no aggregate token/cost claim
is inferred from resumed counters. This is Terra comprehension, not Luna
qualification or actual native-task integration.

## Repeat and retained state

See [test procedure](luna-tests/workflow-context-execution.md).
Raw artifacts: `<workspace-root>/temp/2026-09-21-workflow-context-fix/`.
Local no-backend qualification found one Terra/medium request, no Authorization
header and no tools (field absent); the reusable preflight passes. Its initial
check incorrectly rejected an absent tools field; it now distinguishes absent
from null/nonempty without accepting either latter case.

W-021–W-023 have acceptance evidence. W-009 remains user-paused with
HOST-FLAGOWNER. No live installation is authorized by these test results.
