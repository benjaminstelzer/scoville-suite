# Codex CLI Luna results

Current baseline: `codex-cli-inputs-r13.json`; ADR-0008 selects Code20 plus44
non-Code cases. `selected-cases.json` owns the IDs. Results below retain their
actual package revision; old denominators and native/Gemini runs are historical,
not final acceptance or release approval.

## Historical R2 results

| Case | SOL | Author | Evidence |
| --- | --- | --- | --- |
| code-01 | pass | confirmed | workspace temp/2026-09-21-suite-luna-evaluation/code-r2-01-cli-pilot/ |
| code-02–05 | pass | confirmed | workspace temp/2026-09-21-suite-luna-evaluation/code-r2-02-cli/ through code-r2-05-cli/ |
| code-06–07 | pass | confirmed | workspace temp/2026-09-21-suite-luna-evaluation/code-r2-06-v2-cli/ and code-r2-07-v2-cli/ |
| code-08 | pass | confirmed | workspace temp/2026-09-21-suite-luna-evaluation/code-r2-08-reusable-cli/ |
| code-09–12 | pass | confirmed | workspace temp/2026-09-21-suite-luna-evaluation/code-r2-09-reusable-cli/ through code-r2-12-reusable-cli/ |

12/300 accepted on r2 before the repair. Changed-core cases require r3 evidence.
The author checked exact discovery input and answer, all five
CLI events and the exact-thread native metadata: thread
`01a0c499-8425-7b40-b640-c7918b690556`, `gpt-5.6-luna`, `medium`.
No tool/permission events; one completed turn, exit 0, empty stderr, stopped
process tree. The known pre-turn Code Mode fail-closed diagnostic is retained,
not treated as a result. Correctly rejects a conceptual binary-search question.

The case's `cli-manifest.json` records catalog, CLI, package and test hashes.
Usage: 9,682 input tokens (1,792 cached), 19 output, 0 reasoning output.
Do not add cached input again or infer monetary cost from these counts.

Cases 02–05: author checked each prompt, complete event stream, answer and
exact-thread native Luna/medium metadata. All exit 0, no tools or permissions,
stopped trees. Patch review, implementation and Plan-only work activate;
explicit opt-out does not. Prompt and pinned catalog hashes match manifests.

Cases 06–07: author verified the supplied built core, requested reference text,
complete event streams and exact native thread/model/effort. Case 06 is
Core-only; 07 requested Change and Validation and resumed the same thread.
Both preserve diagnosis/classification limits. SOL's manual fixed-key grade
for 07 is PASS: the pilot's substring grader missed the valid no-edit wording.
Keep its original automated FAIL as grader-defect evidence; no model retry.

Case 08 qualifies the reusable runner on a real two-turn reference exchange.
Author independently checked full events, frozen prompt, exact requested texts
and native Luna/medium identity. Develop/Normal and Change+Validation match
the fixed key; no work is falsely claimed. Both turns exit zero with empty
stderr and no stream, timeout or cleanup failure. Thread:
`01a0c4b2-8b9e-70d0-8a45-df1047c22abe`.

Cases 09–12: SOL and author agree on Structural serialization, High migration
audit, Develop despite a temporary edit prohibition, and Normal central-comment
classification respectively. Author checked exact prompts, complete events,
delivered references and native model/effort. Case 12 stays Core-only; no
unperformed project action is claimed.

## Code r3 repair in progress

Code 13–14 passed SOL review; author confirmation is pending. Code 15 is a
confirmed routing failure, despite protocol PASS: it selected Validation and
interpreted failed-test evidence without requesting `references/validation.md`.
Original evidence: workspace
`temp/2026-09-21-suite-luna-evaluation/code-r2-15-reusable-cli/`.
Cases 16–25 were not run.

The source now requires reading selected references before advice-only
judgments and states that naming a route is not a read. No key, route predicate
or model setting changed. Only Code's core differs in the new public build;
the 13-package verifier passes. Core SHA256:
`8349d6c4d51f9f5834f5dd1d19cca16d2c63d89da5047fcc10214141f3383e49`.
The original core and receipt remain under workspace temp
`2026-09-21-suite-luna-evaluation/public-r2-before-code-fix/`.
R3 case 15 passes SOL and author review: it requests exactly Validation before
judging the failure. Exact prompt, delivered reference, complete events and
native Luna/medium identity were verified. Evidence: workspace temp
`2026-09-21-suite-luna-evaluation/code-r3-15-reusable-cli/`; thread
`01a0c4be-1567-79f2-b7fa-74e80344c159`. Core-only cases 06/12 and Validation-only
case 13 also pass SOL and author review. Cases 06/12 load no references; 13
loads only Validation. Author checked complete streams, exact prompts/texts
and native identities. R3 cases 07–10 also pass SOL and author review: exact
prompts, full event streams, served texts and native contexts verified. They
preserve diagnosis-only authority, Normal internal rewrite, Structural consumer
representation change and High migration-audit classification respectively.

Current r3 core evidence: cases 06–10/12/13/15 accepted (8 selected cases).
The author compared current frontmatter with accepted discovery inputs 01–05:
the exact supplied metadata is unchanged, so those five passes carry forward
without claiming that they exercised the revised core. Current gate: 13/113
accepted; remaining Code cases and other sets are incomplete.

## Reference-read harness ambiguity

R3 case 16 has correct substantive content and protocol PASS but requests no
references despite naming Change and Validation. SOL and author reclassified
the initial routing FAIL as inconclusive: the v2 wrapper can exempt evaluator
reads, while the core requires them before a substantive judgment. It is not
an accepted pass or a clean Skill-defect reproduction. The same ambiguity
limits the earlier case-15 causal diagnosis; preserve its original evidence.

`codex-transport-v4.md` removes that ambiguity without changing cases, keys or
package bytes. Qualify case 16 and the listed regressions before continuing.
The earlier 13 accepted cases remain recorded under their actual wrapper;
affected read-selection evidence must be rechecked before final acceptance.
R3 cases 11/14 have SOL PASS but still await author confirmation; 17+ unrun.

## R4 risk-to-route clarification

The v4-wrapper R3 case16 is protocol PASS but semantic FAIL: it reads Validation
and preserves the assertion, yet labels the case High while omitting Change.
SOL's first PASS was corrected after auditing the explicit route rule; the
author agrees. This is distinct from the prior wrapper ambiguity.

R4 puts the existing Structural/High-to-Change rule before route selection,
explicitly including read-only audits and evidence judgments. Its duplicated
table clause is removed; cases, keys and required behavior are unchanged.
Only Code core differs in the public build; 13-package verification passes.
Core SHA256: `9f8376327a0e677a92ad6b94bb42bafaa209b3206074bd33ddbbbb264329c05b`.
Receipt SHA256: `b3cb4dddab51681bc9475cb2c0bed6e49fdd09d84b828eeb4ec9f07ea4312cd3`.
R3 originals remain in workspace temp `public-r3-before-risk-fix/` beneath
`2026-09-21-suite-luna-evaluation/`. R4/v4 case16 is the first pending check;
earlier-core counts are historical, not final R4 acceptance.

R4/v4 case16 passes SOL and author review. It requests Change and Validation,
classifies High and preserves the authorization assertion. Exact prompt,
delivered references, complete events and native Luna/medium identity verified;
two clean turns, thread `01a0c4d6-7fb7-78f3-bd80-a12e05297764`. Evidence:
workspace temp `2026-09-21-suite-luna-evaluation/code-r4-v4-16-reusable-cli/`.
The remaining core cases require current R4/v4 evidence; no aggregate final
gate is claimed from earlier-core results.

R4/v4 regressions 06/12/13/15 pass SOL and author review. Cases 06/12 remain
Core-only; 13/15 read only Validation and preserve the evidence limits. Exact
prompts, reference delivery, complete events and native identities were checked.
Current R4 core passes: 06/12/13/15/16. Discovery 01–05 uses unchanged supplied
metadata; its earlier accepted evidence carries forward on that limited basis.
Current gate: 10/113 accepted; other current-core cases remain incomplete.

## R5 operation-boundary clarification

R4/v4 case08 stopped the batch: Change-only, with a focused check described as
later work. The independent contract audit found conflicting scope cues:
current-operation-only routing versus Develop delivery with focused proof.
Retain the initial routing FAIL as an inconclusive contract finding, not a
clean model failure or accepted pass. R4 case07 passed SOL; author confirmation
was not completed before the build changed.

R5 routes an authorized operation through its acceptance boundary: unblocked
Develop includes its focused proof, while materially blocked/future work does
not activate later routes and pure classification remains Core-only. No key,
case, v4 wrapper or model setting changed. Only Code core changed; all 13 public
packages verify. Core `9553fcfd3f65847f3f37dc403e975f5e9f41238dc3e815c470afa23ae516cc65`;
receipt `f1a51a40f5e354a4d06be60612cbf94757264869d8f41ac07c7c3e30002f7f1b`.
First check is R5/v4 case08, followed by 06/11/12/13/16/25 regressions.
Earlier-core counts remain historical; final R5 coverage is not yet proven.

R5/v4 case08 passes SOL and author review. It reads Change and Validation,
classifies Develop/Normal and limits proof to the changed behavior. The author
verified the exact prompt/core, delivered reference bytes/hashes, complete
events and both native Luna/medium contexts. Two clean turns; thread
`01a0c4e3-e81e-7d80-ab35-1617ecb09039`. Evidence: workspace temp
`2026-09-21-suite-luna-evaluation/code-r5-v4-08-reusable-cli/`.
Boundary cases 06/11/12/13/16/25 are authorized next, sequentially under SOL
Medium with stop on first failure. They are not yet accepted.

The R5 boundary batch stopped at case11. Protocol and fixed-key substance pass,
but full routing fails: Luna reads Change for blocked future implementation,
without current inspection or a Structural/High trigger. SOL and author agree;
no retry or key change. Thread `01a0c4eb-09aa-7a73-a5da-92f87241a2f9`, evidence
`code-r5-v4-11-reusable-cli/` under the same temp root. Cases06/12 pass SOL and
author review as Core-only; exact inputs/events/native identity were checked.
Case12 finished before the case11 routing audit stopped dispatch; 13/16/25
were not started. Next: clarify mode versus currently authorized operations,
then rebuild and requalify case11 before resuming the boundary group.

## R6 mode/route separation

The routing opening now excludes blocked/deferred operations before selecting
references. A pre-inspection clarification uses the core; independently
authorized current work and Structural/High routing remain intact. SOL reviewed
this contract against 06/08/11/12/13/16/25; no case or key changed.
Only Code core differs from R5. All 13 public packages/188 files verify.
Core SHA256: `0d06a96c259464f758371d3f6cf6aa5289a10737cf478388bfd8632d071546e7`.
Receipt SHA256: `2dd2edd64989b4ec5b4cd9345e4bbde90793fb9798574d20a961c8bc297f9b2c`.
The generic `quick_validate.py` rejects the unchanged `compatibility` field;
it did not pass and establishes no behavioral result. R5 bytes remain in
workspace temp `public-r5-before-mode-route-fix/`. R6 Code11 alone is authorized
as the next pilot; prior-core results do not prove final R6 coverage.

R6/v4 case11 passes SOL and author review: Develop, no reference reads, no
edits before the pending decision. Exact events, input prompt and native
Luna/medium identity match; one clean turn, thread
`01a0c4f1-b470-7af3-b955-02852f266bd1`. Evidence: workspace temp
`2026-09-21-suite-luna-evaluation/code-r6-v4-11-reusable-cli/`.
All 206 files across the public packages and private Workflow match R6's frozen
manifest; its 24 corpus/key files are unchanged. Next authorized sequence:
06/08/12/13/16/25, then remaining Code cases if SOL's full review passes.
Stop on first failure; author acceptance remains separate.

R6 cases06/08/12/13 pass SOL and author review. Actual reads are none for
06/12, Change+Validation for08, and Validation for13. Exact prompts, complete
events, served reference bytes/hashes and native Luna/medium identity match.
Together with11, five current-core cases are accepted; no final gate claimed.
All 88 selected non-Code prompts also match current built core/frontmatter and
unchanged case text; this is input preparation, not behavioral acceptance.

## User-reduced coverage

ADR-0008 replaces the 113-case requirement with Code20 plus44 non-Code cases.
`selected-cases.json` owns exact IDs; `codex-cli-inputs-r6-reduced.json` freezes
that selection and the unchanged R6 packages/keys. No omitted Code case had
started in R6 when the limit arrived; running case25 remains selected.
Earlier attempts remain evidence, not additional required cases. Do not run
excluded prompts merely because they were already prepared.

R6 case25 stops the batch: protocol passes, but full routing fails. Luna calls
the current risk High yet reads only Planning and Validation, treating the
no-implementation boundary as a veto on reading Change. Its final limitations
also call worktree state unknown despite the supplied dirty-worktree fact.
Thread `01a0c4f8-89a7-7e73-90db-9f5fdeaafb5c`; raw evidence remains in
`code-r6-v4-25-reusable-cli/` under the evaluation temp root. No retry accepted.
Reinspect routing precedence and distinguish reading guidance from authority
to execute its operations before another correction.

## R7 ordered reference routing

The contract audit identified conflated reference selection and action
authority. Routing now excludes deferred work, combines current-operation
routes, applies the Structural/High override last, then reads references while
retaining action limits. This replaces prose routing with one ordered rule;
cases, keys, wrapper and reduced64 selection are unchanged. Only Code core
changed; 13 public packages/188 files verify. Prior bytes are retained in
`public-r6-before-route-order-fix/` under evaluation temp.
Core: `d9e73101a4246509f28302ce313af5a7ec4e995011c1d81ff71690a997d53034`.
Receipt: `54cf85dff4c54c2fb6081943861cc507850ea747e7f31b5412a8da3f099989b5`.
Case25 is the only authorized R7 pilot; no final R7 coverage is claimed.

R7 case25 passes author protocol and semantic review: Planning+Change+Validation
were actually read, Advise/High is separated from later Develop, dirty-worktree
facts and no-action limits are preserved. Prompt, delivered reference bytes,
full events and native Luna/medium identity verified; two clean turns, thread
`01a0c4fe-a51b-7e01-a862-9fc980cec338`. SOL's independent grade gates continuing
the remaining 14 selected core cases. Discovery01–05 may carry forward only
after exact supplied metadata comparison; no excluded cases are authorized.

SOL independently confirms R7 case25 PASS. The remaining selected Code cases
are running sequentially with stop-on-first-failure; their acceptance is open.

R7 case06 passes SOL and author review: Core-only/Normal classification,
no unauthorized action or result claims; exact events, prompt and native
Luna/medium identity verified. Discovery01–05 carries forward from accepted
R2 evidence: SOL and author compared supplied frontmatter and original case
text against current inputs and reconfirmed the five answers. This carries
only discovery proof, not prior-core behavior. Current accepted selection:7/64
(discovery01–05 and R7 core06/25); all other cases remain open.

Author review passes R7 cases07–10: diagnosis-only authority07, Normal internal
rewrite08, Structural consumer contract09, High read-only migration audit10.
All read Change+Validation and preserve scoped evidence limits. Complete events,
native Luna/medium contexts, exact prompts and delivered references verified.
Cases08/09 required three turns to request both references;10 used two. Raw
`code-r7-v4-NN-reusable-cli/` directories retain per-turn usage. SOL confirmation
is tracked separately; these author checks alone do not advance the gate count.

SOL confirms07–10; SOL and author also accept11–13 on R7. Cases11/12 read no
references and preserve blocked/classification boundaries;13 reads Validation
and does not treat a stub as external compatibility proof. Author verified
complete events, exact inputs/delivered files and native identities. Current
accepted selection:14/64 (Code01–13 and25). Remaining Code IDs15/16/20/21/23/24
and all44 non-Code cases are not yet accepted.

R7 cases15/16/20/21 pass SOL and author review. They preserve change-caused
failure attribution, authorization assertions, repeated-failure stopping and
the infrastructure-recovery limit. Case16's hypothetical remedy is advice,
not executed or claimed edit authority. Exact events, prompts, served files
and native identities verified. Current accepted selection:18/64; only23/24
remain for Code, followed by44 non-Code cases.

## Code gate complete

All20 selected Code cases pass SOL and author review on the R7 baseline:
discovery01–05 carries forward on exact inputs;06–13/15/16/20/21/23/24/25 have
fresh R7 evidence. Final23/24 reject responsibility-splitting cycles and require
durable write before success with failure-path evidence. Both final runs have
verified prompts, complete events, served references and native Luna/medium
identity. This is theoretical comprehension proof, not executed project work.
Current accepted selection:20/64. Handoff06 asset pilot is next; no other
non-Code test is accepted. No publication or full-suite completion is claimed.

## Non-Code selected cases

Handoff06 passes SOL and author review, qualifying packaged asset delivery:
Luna requested `assets/continuation-prompt.md` naturally; exact bytes/hash were
served in the same thread. Complete events/native Luna-medium identity and
the fixed Receiver Instructions, all H2s, fence, not_started and unknown facts
were verified. Thread `01a0c50f-9749-7e23-9eaa-9a5209fabcb6`; evidence under
evaluation temp `handoff-r7-06-reusable-cli/`. Current accepted selection:21/64.
Remaining43 selected non-Code cases are authorized sequentially with stop on
first failure; independent author review remains required.

Author checks Handoff01/09 pass: ordinary summary does not activate Handoff;
truncated input requires cursor recovery while preserving known partial facts.
Complete events, native identities, prompts and case09's actual template
delivery verified. Await SOL batch confirmation before counting these two.

## R8 Handoff status fidelity

Handoff15 on R7 stops the batch: protocol PASS, semantic FAIL by SOL and author.
Secret redaction is correct, but `Status: not_started` is unsupported by the
fixture. Other unknown/none-known fields are not the decisive failure. No25
or later set was dispatched. Preserve `handoff-r7-15-reusable-cli/` evidence.
R8 requires a source-confirmed not-started status; absent status is unknown.
Only Handoff core changed; Code20 remains accepted without reruns. The earlier
Handoff core pilot must be rechecked; current accepted gate is20/64 pending
discovery carryover confirmation. R8 case15 alone is authorized first.
Core: `1dbc3d8208f839a76fde5a55ece750d6c80628829381da0fdc51046f4e7fa89d`.
Receipt: `5c824bb9030d92c24a2ff06d9dec63c978a2f8a08b58615bd275d6aae0d0d4c5`.
All13 public packages/188 files verify. Original R7 Handoff bytes remain in
evaluation temp `public-r7-before-handoff-status-fix/`. No live install changed.

R8 Handoff15 passes SOL and author review. Status stays unknown; no variable
name or secret value is invented, fixed template/Receiver Instructions remain
intact. Objective describes the requested transfer artifact, not a fabricated
underlying project. Exact prompt, delivered asset bytes, full events and native
Luna/medium identity verified; thread `01a0c517-5c9a-76a2-aee4-154f59bc267b`.
Code20 remains valid; current accepted gate21/64 before discovery carryover.
Next: Handoff06/09/25 on R8, then remaining selected sets; no Code reruns.

R8 Handoff06 passes SOL; author review remains pending. Handoff09 stops the
batch: protocol PASS, semantic FAIL. Its fenced artifact defers available
cursor recovery to the receiver instead of finishing READ before RENDER.
Author inspected the complete answer and agrees; no25 or later case started.
The source READ gate now explicitly forbids rendering while permitted recovery
remains available. Build and targeted09 validation remain pending; R8 package
bytes are still installed only in public test staging, not live Skills.

## Supporting completion audit (not model-test passes)

Shared lifecycle unit checks:9/9 pass. The isolated-build test hit WinError32
during temporary-directory cleanup; no behavioral assertion failed before it.
One alternate run retained its temporary directories (Python TemporaryDirectory
delete=False, test-process only): both build tests pass, exercising all six
consumers, isolated helper calls and deliberate drift detection. Cleanup is
not proven by that run; retained test output is under workspace temp
`2026-09-21-suite-completion-audit/`. No cleanup or global settings changed.

## R9 Handoff read gate

The explicit read-before-render gate is built; only Handoff core differs from
R8. Public13/188 verification passes; Code20 evidence remains valid. R8 bytes
are retained in evaluation temp `public-r8-before-read-gate-fix/`.
Core: `94ac912157aa8a3ca9a0cb0ab32f004701092881b42c0983d41b079d13f71c9b`.
Receipt: `3837d9d52314d4f037f2ac77c0151ce125ad275449e959d94c63965701d6147c`.
Only R9 Handoff09 is authorized as a pilot; no R9 Handoff acceptance yet.

R9 Handoff09 passes SOL and author review. It holds at READ, requires cursor
recovery, preserves usable facts and emits no premature artifact. Exact prompt,
asset bytes, events and native Luna/medium identity verified; thread
`01a0c51d-ba61-76b1-b6e2-fad1625fd5fe`. Handoff06/15/25 are next on R9,
then remaining39 selected non-Code cases. Code20 is unchanged and accepted.

Completion-audit check: all8 `test_rollover_readiness.py` tests pass against
the current shared owner. Coverage includes exact-ID continuation without a
list entry, title-independent visibility, fresh guard/generation checks,
completed predecessor proof, deferred archive verification and linked
multi-generation recovery. This verifies helper behavior with fixtures, not
live host visibility or actual archival; no running task was mutated.

Handoff selected set passes SOL and author review on R9:01 carries forward on
unchanged discovery metadata;06/09/15/25 have fresh evidence. Source-confirmed
not_started, unknown status, read-before-render and size-conflict handling are
preserved. Exact prompts, full events, template delivery and native identities
verified. Case25 explains the hypothetical recovery limits and specifies only
a size-conflict response, not a falsely complete handoff. Current accepted
selection:25/64 (Code20 + Handoff5). Remaining39 selected cases are running.

## Brainstorm scenario ambiguity

Brainstorm01 passes author protocol and semantic review: known-root correction
does not activate Brainstorm. Exact discovery input, full events and native
Luna/medium identity verified; SOL confirmation is tracked separately.

R9 Brainstorm06 is protocol PASS but semantically inconclusive. SOL initially
graded FAIL because dispatch NO contradicted the assumed active scenario.
SOL and author then found that the prompt omitted that application context.
Luna's conditional Standard answer is correct, but neither a full pass nor a
proven Skill defect. Preserve `brainstorm-r9-06-reusable-cli/`, thread
`01a0c523-0fbd-7681-8a57-7f0f63c6a74c`. Events, exact prompt and native identity
were independently verified. No later case was dispatched.

`codex-brainstorm-transport-v5.md` clarifies only the hypothetical application
context. Core, cases, keys, runner and package revision remain unchanged.
Qualify06 before12/18/25; do not repeat Code or Handoff.

Brainstorm01 is now confirmed PASS by SOL and author. R9/v5 case06 also passes
both reviews: Standard without complexity escalation, correct process and
authority boundary. Full events, exact prompt and native Luna/medium identity
verified; thread `01a0c52a-35ec-7e50-8174-77f9fd72c457`. The v5 supplement freezes
the four revised application prompts; all206 package files and24 corpus/key
files still match R9. Current accepted selection:27/64. Selected12/18/25 are
authorized next; other sets retain their own existing wrapper.

Completion-audit checks: five current shared title tests pass, covering WORK,
REVIEW, REPAIR, coordinator generation, ASK advisers, rejected malformed inputs,
create/handle title equality and same-attempt predecessor exclusion. The focused
Workflow child-prompt test passes for executor/reviewer/repair: gate precedes
work and final-delivery restrictions do not block gate/work calls. These are
helper/generated-prompt checks, not live dispatch or archival proof.

Additional current-source audit: two Ask variant tests pass for all four native
variants' exact names, source ownership, model/xhigh defaults and missing-value
failure. Four README tests pass for shared descriptions, Workflow first and
suite-only/Codex-only notice, one monorepo install link, shared license and
preserved installation safeguards. The added-member fixture propagates the new
family member to every full list in manifest order while keeping intentional
neighbor subsets unchanged. Its temporary copy is retained under completion-
audit temp to avoid the previously observed Windows cleanup lock; no cleanup
success is claimed. These checks make no provider call or live installation.

R9/v5 Brainstorm12 passes SOL and author review; exact prompt, complete events
and native identity verified. Case18 stops the batch: protocol PASS, semantic
FAIL. It merges the candidates correctly but labels the mechanism Established
solely because those candidates match, while acknowledging absent landscape
evidence. Candidate equivalence does not prove relation to existing approaches.
Thread `01a0c52c-3f15-7fe1-8fd8-3ba7d1466112`; keep its full failed answer.
Case25 finished before this full-answer review stopped dispatch; it is retained
but not accepted. No later set started.

The canonical Brainstorm core now distinguishes comparison with existing
approaches from duplicate candidates and requires Unresolved when comparison
evidence is insufficient. It adds no web-search requirement. Build and targeted
case18 validation are pending; existing public packages still contain R9 bytes.

## R10 Brainstorm comparison evidence

Only Brainstorm core changes in the public build; all13 packages/188 files
verify, and all206 frozen package files plus24 corpus/key files match R10.
Core: `6cd779099c71d9f8ffe07e0efca50e2360302aae327d0b4e7c68d6b1c3e5eac5`.
Receipt: `2e2b669b1b0e4126ce3067d3f018dcd900daf58db6e0db78def26cfbe57f8106`.
Prior bytes remain in evaluation temp `public-r9-before-brainstorm-label-fix/`.
The generic Skill validator again rejects unchanged `compatibility`; no pass
is claimed. Only18 is authorized as pilot, then06/12/25 need current-core
proof. Discovery01 is unchanged; Code20 and Handoff5 remain valid. No installed
Skill, live task, key or case changed. The v5 supplement freezes exact prompts.

R10/v5 Brainstorm18 passes SOL and author review: one merged mechanism with
Unresolved, no prior-art inference from duplication and no invented search or
project action. Exact prompt, complete events and native Luna/medium identity
verified; thread `01a0c530-b8f7-70d0-b968-4a634d92fca6`. Remaining06/12/25 are
authorized sequentially; discovery01 requires exact-input carryover. No broader
final coverage or release approval is claimed.

Completion audit: five context-helper tests pass against the current owner.
They cover configurable coordinator/worker thresholds, coordinator rollover at
33 percent, strict worker cutoff above66, cumulative-token exclusion and
rejection of stale, wrong-identity or invalid telemetry. Three GitHub build
checks pass: suite-only Workflow target/path, private exclusion from public
staging, dirty-source release rejection, changed/extra files and development
exclusion. The source Skill routes generated members through the suite contract,
replacing redundant sibling-copy checks while retaining publication authority,
visibility, history and remote-byte verification. No remote operation ran.

Brainstorm selected set passes SOL and author review on R10. Discovery01
retains exact current metadata/case;06/12/18/25 have fresh R10/v5 evidence.
Author checked full events, exact inputs and native Luna/medium identity for
each. Case25 preserves revised source, failed evidence and the open branch,
stops for reconciliation and claims neither completion nor independence.
Current acceptance:30/64 (Code20, Handoff5, Brainstorm5). Next: the six selected
Design cases; no Code/Handoff reruns and no additional case IDs.

History-retention audit: all13 bundles under workspace
`state/suite-migration-2026-09-21/` pass `git bundle verify` against their
retained original repositories under
`Z:/Projekts/AI/state/suite-source-archives-2026-09-21/`. This verifies the
bundles, not a new claim that all later working-tree edits match the import.

Design09/12 pass SOL and author review on unchanged R10 Design bytes. Core-only
exploration and real-content fit before repetition are correct. Case12's
Critique label is defensible for its observed-state wording; the hidden Generate
category does not supply missing scenario authority. Full events, exact inputs
and native identities checked. This proves the key's sequencing behavior, not
an explicit Generate-mode choice. Current accepted selection:32/64.

Design04 stops with protocol FAIL `invalid_request_path`: Luna requested
`scoville-design-anti-ai-slop/SKILL.md` instead of returning a discovery answer.
No file was served; native identity/events/input are verified, semantics remain
unassessed. The prompt mixes metadata-only selection with full application and
READ directions. `codex-discovery-transport-v6.md` separates these scopes without
changing metadata, cases, keys, core or runner. Preserve the failed attempt,
thread `01a0c537-44d5-73a3-a53d-153b57f429bc`;24/06/25 were not run.

SOL independently confirms the wrapper diagnosis. The runner stopped before
its native-metadata step; the author separately located the sole rollout by
that exact thread ID and verified session_meta plus its one Luna/medium turn.
`codex-cli-inputs-r10-discovery-v6.json` freezes the corrected04 prompt.
Only that pilot is authorized; no Skill change or package rebuild is needed.

Design04-v6 passes SOL and author review: correct visual-critique owner,
read-only boundary, missing poster/viewing evidence unknown, no file requests.
Exact prompt, full events and native Luna/medium identity verified; thread
`01a0c53b-0113-70a2-9c6e-bf2b50b5c009`. Acceptance:33/64. Design24/06/25 are
next with unchanged application wrappers. Subsequent discovery01 prompts for
Plan/Research/Scribe/UI/Workflow use v6 and are frozen in the following-cases
supplement; preparation alone is neither dispatch nor acceptance.

Design24 passes SOL and author review after correcting SOL's initial grading
error: “Routing: Nein” answers the explicit question whether the chart label
alone decides routing. The following sentence correctly selects Information
for the contradicted encoding relation. No contradictory route remains in
context, and no retry or Skill change was needed. Full events, prompt and
native identity checked; thread `01a0c53c-738f-79d1-a243-f2ef7466105b`.
Current acceptance:34/64; Design06/25 remain.

Design06 passes SOL and author review: scoped alignment repair, protected
wording/settled decisions and explicit missing visual proof; complete events,
exact input and native identity verified. Design25 stops the group. SOL's
initial PASS was corrected after author review: no active UI partner is supplied,
yet Luna reads partner-only Coordination and requires that partner's work.
Core, index and Coordination all require an actual active-applicable partner.
Exception, rights and evidence limits were otherwise correct. Preserve thread
`01a0c53f-1427-7b12-a5cb-cae7b18f6f27`, its exact served references and answer;
protocol PASS does not cure this unsupported dependency.

The source Core now requires confirmed current-task partner availability before
loading Coordination. A framework conflict/name alone does not establish it;
unknown availability retains direct authorised work under the same ownership
floors. Only this gate changes. Build and case25 requalification are pending.

## R11 Design confirmed-partner gate

Only Design core changes; public13/188 verification passes and all206 frozen
files plus24 corpus/key files match R11. Prior package bytes remain in
evaluation temp `public-r10-before-design-partner-fix/`.
Core: `681c6ecdd2c8aa48057da662afee0a280d6138e0ee382a4a13ebb8c9117a48ef`.
Receipt: `529f9afe7c0f0eb3e5b1b87069c66680da2bd74815bdc20feca6c675167f548d`.
Generic Skill validation still rejects unchanged `compatibility`; not a pass.
Only25 is authorized first. The R11 Design supplement freezes five application
prompts, with unchanged wrapper/cases. Discovery04 can carry on identical input.
Code20, Handoff5 and Brainstorm5 remain accepted without reruns. Live installed
Skills and tasks are untouched; no release approval is implied.

R11 Design25 passes SOL and author review. It loads only the direct index,
critique/validation and rights; no active UI partner or Coordination dependency
is invented. Disputed evidence, unresolved rights and framework ownership remain
open, without a final pass. Exact prompt, served bytes, complete event streams,
native Luna/medium identity and clean exits verified; thread
`01a0c543-e99a-7db0-ad22-261c6a92d62e`. Evidence: evaluation temp
`design-r11-25-reusable-cli/`. Selected09/12/24/06 require current-core proof;
discovery04 may carry only unchanged input. Code20/Handoff5/Brainstorm5 retain
acceptance; no extra case IDs or unaffected-package reruns are authorized.

All six selected Design cases pass SOL and author review on R11. Fresh
09/12/24/06 preserve exploration timing, fit before repetition, encoding-driven
Information routing and narrow alignment repair. Case12 retains its documented
mode-selection limitation. Exact events, prompts, served files and native
Luna/medium identity verified. Discovery04 carries on exact current frontmatter
and identical accepted v6 prompt. Current acceptance:36/64.
Plan01/07/13/19/25 are next; their exact existing prompts are frozen in
`codex-cli-inputs-r11-plan.json`. No source, key or package changed.

Plan01/07/13/19/25 pass SOL and author review against R11. They preserve
non-activation, partial-profile protection, exact Step execution annotation,
explicit successor priority and incomplete/proposal-dependent state with an
independent deferred queue. Complete events, exact prompts/references, clean
exits and native Luna/medium identities verified in `plan-r11-NN-reusable-cli/`.
Current acceptance:41/64. Research01/07/10/15/25 are authorized next.
Research, Scribe/UI and private Workflow prompt supplements freeze checked
existing input bytes; preparation is not dispatch or acceptance.

Research01/07/10/15 pass SOL and author review on R11: correct exclusion,
mixed domain routing, snippet limits and abstract-only evidence. Exact prompts,
events, references and native Luna/medium identity verified. Research25 fails
semantically despite clean protocol: it prohibits completion whenever a
material contradiction remains. Core permits explicitly unresolved findings
after the stop checks; job/cleanup obligations still gate completion. Preserve
thread `01a0c556-5c6a-7d01-8b6e-3011ba062a65` and its full failed answer.

## R12 Research bounded completion

Only `references/deep-research.md` changes: unresolved findings are distinct
from unmet required checks/access/job obligations. No core, case, key or prompt
changed. Public13/188 verification and all206 manifest files plus24 corpus/key
files pass. Receipt:
`4111f0747b9544c0f821fb49770e2d706a42626f7efa81008af1a72cbfacc6a2`.
Changed reference:
`6c172169931abd3df41525d7c0e10562890d6b11a88d931429cdfe612c90d7e2`.
Prior bytes remain in `public-r11-before-research-stop-fix/` under evaluation
temp. Generic Skill validation rejects unchanged `compatibility`; not a pass.
Only Research25 is requalified;01/07/10/15 did not consume the changed reference.
Current accepted selection:45/64. All earlier accepted sets remain unchanged.
Scribe and later sets have not started; no release or live installation.

R12 Research25 fixes completion but fails overall: it omits Academic despite
scholarly evidence materially limiting the survey. SOL and author agree after
full-answer review against Core routing. Complete events, exact prompt,
delivered references and native identity verified; preserve thread
`01a0c55a-5ad9-7971-b466-4e4aaad387ad`. This routing omission also occurred
on R11; neither run is an accepted full pass.

## R13 Research mixed evidence routing

Core now selects domains by material evidence rather than the task label.
Relevant scholarly evidence adds Academic even when abstract-only; a passing
paper mention does not. Deep replaces no domain. Only Research core and receipt
changed; all206 package files and24 corpus/key files verify, public13/188 passes.
Core: `49e444523dcf32e2958a08971cee2db3a36f6e5622488e71841eaea2bb6369ca`.
Receipt: `1b9da874dad9fa63d3adb89bf61c628360e8f124c09068c934c95613f53e7c61`.
Prior bytes remain in `public-r12-before-research-routing-fix/`.
Generic Skill validator rejects unchanged `compatibility`; no pass claimed.
Research25 is the sole pilot;07/10/15 need current-core proof afterward.
Discovery01 may carry exact metadata. Other41 accepted cases remain unchanged.

R13 Research25 passes SOL and author review: Development, Academic and Deep
are actually read; abstract limits, unresolved findings, targeted stopping and
job/cleanup gates are preserved. Exact prompt, full events, served references
and native Luna/medium identity verified; thread
`01a0c55e-5a53-7cd0-91b9-e469fe64e107`. Selected07/10/15 now run on R13;
discovery01 requires exact-input carryover. No other set is rerun.

All five selected Research cases pass SOL and author review on R13. Fresh
07/10/15 preserve mixed routing, snippet-only discovery and abstract evidence
limits. Their exact prompts, full events, native identity and served reference
bytes are verified. Discovery01 carries on identical current frontmatter and
accepted prompt. Current acceptance:46/64. Scribe01/04/07/15/25 are next;
R13 supplements retain unchanged inputs for Scribe/UI, Workflow and Ask.

Scribe01/04/07/15/25 pass SOL and author review. They preserve ordinary-update
exclusion, Plan ownership, exact-source boundaries, visible-label accessibility
and regulated/localized GUI limits. Missing source content is not fabricated.
Exact prompts, full events, native Luna/medium identity and actual Fidelity/
Interface deliveries verified in `scribe-r13-NN-reusable-cli/`.
Current acceptance:51/64. UI01/04/08/17/25 are next; no package changes.

UI01/04/08/17/25 pass SOL and author review. Backend/WordPress exclusions,
evidence-only routing, Design conflict ownership and rejection of framework
bypasses are preserved. Source/build proof is not treated as rendered or
interactive acceptance. Exact prompts, full events, native Luna/medium identity
and delivered references verified in `ui-r13-NN-reusable-cli/`.
Current acceptance:56/64. Workflow01/06/17/20/25 now use the private suite
package and its own receipt; no live Workflow operation is authorized.

Workflow preflight rejected an outer distribution folder as `--package-root`
with `invalid_receipt_file` before model dispatch. The runner resolves receipt
files from the inner Skill folder's parent; its contract and actual nested
`SKILL.md`/outer `.gitattributes` confirm the correct path. Preserve the failed
preflight; it supplies no comprehension result. Execution instructions now state
the exact private inner path. Runner and packages are unchanged.

Completion audit: a fresh fetch of `https://learn.chatgpt.com/docs/build-skills`
confirms explicit `$skill` invocation and `allow_implicit_invocation`; it supplies
no native alias contract. W-008's documented host-discovery limitation remains,
not a new unsupported alias claim. No installation or live launch was attempted.

Workflow01/06/17 pass SOL and author review. They preserve explicit activation,
setup-only termination and authoritative completion before any transition.
Exact prompts, complete events, native identity and served operations/setup
bytes verified. SOL initially flagged17 because its simulated wait omitted
host/reference text. Full-answer review corrected that literal grading:
the same exact retained-child wait changes only cursor, accepts no delivery
and authorizes no state transition. It does not discard host or consume the
reference; the shown call is pseudocode, not a claimed native API payload.
Preserve thread `01a0c572-e7ca-7852-9b66-3b4bc9e66af5`; no source fix or retry.
Selected20/25 continue on the unchanged private package.

Workflow20/25 pass SOL and author review. The worker threshold is strict:
50 continues, above50 hands off only with material work remaining; absent
telemetry or completed work does not create a successor. Paraphrased inherited
handoffs cannot create a grandchild. Stop retains the active child and guard
until authoritative terminal proof; delivery alone is not cancellation.
Full events, exact prompts, served-file bytes and native Luna/medium identity
verified in `workflow-r13-20-reusable-cli/` and `workflow-r13-25-reusable-cli/`.
Workflow5 is accepted; current acceptance:61/64. Only Ask Claude/paired/single25
remain, using the unchanged Ask packages and R13 input manifest.

Ask paired25 R13 fails SOL and author semantic review: Luna requires a new
request before recovering the truncated native answer, conflating delivery
completion with substantive follow-up and Claude timeout resume. Full protocol,
prompt, served bytes and native identity pass; original answer is retained at
`ask-paired-r13-25-reusable-cli/` (thread
`01a0c57d-72d2-7131-9964-158d45216f1f`). The paired source now distinguishes
same-reference delivery recovery without settings overrides from a new
substantive follow-up. Claude resume remains request-only. Rebuild both paired
variants and retest selected paired25 before acceptance; single25 not launched.

Ask Claude25 passes SOL and author review: retained session/requested settings
are not asserted actual model metadata; timeout yields no complete answer or
automatic resume, budget increase, or invented session. Full protocol, initial
prompt and native Luna/medium identity verified at
`ask-claude-r13-25-reusable-cli/`, thread
`01a0c57c-9776-7103-a73e-a65baf40dcb4`. Current acceptance:62/64.

R14 delivery-recovery contract check: the unchanged shared lifecycle `message`
operation accepts a ready retained handle with `delivery_state:not_sent` and
emits only threadId/hostId/prompt when model/thinking are omitted. The local
fixture generated arguments only; no host message was sent. This confirms the
paired wording's settings-preservation path needs no helper implementation change.

Independent R14 build comparison inspected all50 fresh Ask package files against
public: only the two paired nested `SKILL.md` files differ before synchronization.
Staging is `temp/2026-09-21-suite-migration/ask-r14-delivery-recovery` under the
workspace root. The historical Ask receipt and public Scoville receipt remain
separate; use the new staging receipt for R14, never overwrite the old evidence.

After R14 public synchronization, the independent package-set verifier passes
13 packages/188 files using the unchanged public Scoville receipt plus the new
Ask R14 staging receipt. This proves package-byte integrity, not comprehension;
paired25 still requires the fresh Luna result and independent acceptance.

R14 paired25 prompt independently checked: its fenced core matches the current
public paired SOL Skill; bytes outside that core span exactly preserve the R3
scenario and framing. Trailing core newlines are framing, not scenario changes.
No expected-result file changed.

Ask paired25 R14 passes SOL and author review. Missing native delivery is
requested through the retained task without a new user-request gate; only
Claude resume is conditional on request. Attribution, incomplete-result status,
no chat-read/new-task fallback and no publication are preserved. Full protocol,
prompt and native Luna/medium identity verified at
`ask-paired-r14-25-reusable-cli/`, thread
`01a0c58d-b934-7a30-91ed-40fdd094d727`. Current acceptance:63/64.
Only selected Ask single25 remains; use its unchanged prompt/core and R14 Ask
receipt. R13 paired failure remains historical evidence.

Ask single25 R14 stops at the READ transport gate, not semantic grading.
Thread `01a0c58f-e059-7d03-a87b-457ba6c36179` requests lifecycle/role texts plus
root `config.json` and `config.default.json`; the runner permits only packaged
references/assets/scripts and returns `invalid_request_path` before an answer.
The public package has no personal `config.json`; its manifested shipped default
is SOL/xhigh. Keep the runner boundary unchanged. R15 supplies the exact shipped
default and personal-config absence as neutral fixture data before testing the
unchanged scenario. No personal/global configuration is read. R14 supplies no
semantic pass or demonstrated Skill defect; acceptance remains63/64.

Final-input audit verifies206 package files against R13 plus the two exact R14
paired-core overrides, and all24 corpus/key files unchanged. No additional
comprehension cases were run for this audit.

User change: both Astra Ask variants now default to high; SOL stays xhigh.
Manifest variable `effort` owns core/config/adapter/README projections. Sources
and public packages rebuilt from `ask-astra-high`; its separate receipt is now
current. Package verification passes13 packages/188 files. Existing variant-test
expectation updated; no new test run for this user-exempted default change.
R14/R15 comprehension evidence retains its actual pre-change package provenance;
the SOL single case remains unchanged. Live installations were not replaced.

Ask single25 R15 passes SOL and author review, thread
`01a0c593-b34f-7161-b21f-c21d0de38135`, evidence
`ask-single-r15-25-reusable-cli/`. Full protocol, prompt, delivered lifecycle/role
bytes and native Luna/medium identity verified. Revision mismatch prevents
acceptance; requested settings remain distinct from unknown actual metadata.
Publication, edits and additional reviewers remain unauthorized. SOL's initial
authority concern was corrected on meaning review: requesting the originally
intended revision from the retained reviewer completes the already authorized
read-only review; a new reference is not expanded scope. No retry or Skill edit.
All64 selected cases now pass SOL and author review. This is theoretical
comprehension evidence, not live workflow proof or publication authorization.

## Selected gate closure

All64 IDs exist in the unchanged corpus and match ADR-0008: Code20;
Brainstorm/Handoff/Plan/Research/Scribe/UI/Workflow5 each; Design6; Ask3.
Acceptance owners are SOL Medium and author. Accepted revisions: Code R7,
Handoff R9, Brainstorm R10, Design/Plan R11, Research/Scribe/UI/Workflow R13,
Ask Claude R13, paired R14, single R15. Exact-input discovery carryovers and
non-semantic transport failures are identified above, not counted twice.
The later Astra high default is explicitly exempted from new tests by the user.
The reusable execution guide and per-run manifests retain actual input hashes;
raw evidence stays temporary. W-018's selected theoretical gate is complete.
