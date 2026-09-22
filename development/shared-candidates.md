# Shared candidates audit

Status: complete candidate audit. Recommendations only, no candidate
implementation authorized. This is not a behavioral certification of the Skills.

## Scope and evidence

The manifests list nine Scoville members and five Ask variants from three
bases: single, paired and Claude-only. An exact-paragraph scan covered 102
distinct exported Markdown, Python and JavaScript source files. This scan
identifies duplication, not semantic equivalence or complete audit coverage.
Development histories and unreferenced imported README snapshots are excluded.

Existing shared owners include `shared/runtime/task_lifecycle.py`, its operation
contracts, `shared/build/build_suite.py` and `shared/readme/`. Ask already shares
variant bases. New candidates must not duplicate those owners.

## Initial candidates

| Priority | Candidate and consumers | Proposed owner and integration | Benefit and risk |
| --- | --- | --- | --- |
| 1 | Identical independence paragraph in all eight core Scoville SKILL.md files | `shared/text/skill-independence.md`, build include expanded into each package | Removes eight maintained copies. Preserve applicability and opt-out scope. Do not automatically apply it to Workflow orchestration. |
| 1 | Five route boundaries in Plan SKILL.md and planning-granularity.md, Workflow SKILL.md and operations.md | `shared/text/dispatch-route-criteria.md`, shared criteria plus local owner-specific wrappers | Prevents classification drift. Plan shapes steps but does not assign routes. Workflow selects the effective route and owns repair/rollover exceptions. |
| 2 | Claude timeout contract in Ask paired and Claude-only SKILL.md | `shared/text/claude-deadline.md`, expanded at build time | Preserves identical disabled-default, exit-124 and no-retry rules. Must not change the native adviser deadline. |
| 2 | Claude JSON parsing, finite budget/timeout validation and session-mode selection in paired and Claude-only scripts | `shared/runtime/claude_contract.py`, bundled in both packages | Inputs: raw JSON, numeric CLI values, parsed session flags. Outputs: validated payload/value or explicit error, selected session mode. Preserve config precedence and provider-specific command resolution in local adapters. |
| 3 | Native creation payload repeated in Ask single and paired | Reuse `shared/runtime/task_lifecycle.py` rather than add a launcher | Inputs: resolved project, adviser, title, prompt and model settings. Output: host arguments and retained handle. Check existing create coverage before recommending any extension. Avoid silently changing parallel-pair coordination. |

All proposed paths above are recommendations, not existing implementations.
Runtime helpers must be copied into each package by manifest mapping. Text must
be expanded into standalone files, with missing includes failing the build.

## Risk schemes must remain distinct

Plan and Workflow share `ultra_low`, `low`, `medium`, `high`, `ultra_high`
boundaries. Both distinguish known local work from unresolved helpers,
cross-component diagnosis and consequential state or authorization changes.
Workflow additionally requires positive evidence for every low-eligibility
fact and maps the chosen route to model and reasoning settings. Plan does not
perform that mapping. Share criteria, not dispatch authority.

Code uses `Normal`, `Structural`, `High` to select engineering proof and scope.
It is not a model-routing scale. A matching word such as `High` does not justify
one common enum, automatic conversion or a merged decision helper.

## Member coverage

Coverage combines the manifest-wide source/duplicate scan with targeted semantic
inspection of the contracts named below. It does not claim a line-by-line
correctness audit of every specialist module.

| Member or source base | Shared candidates or retained boundary |
| --- | --- |
| Brainstorm | Independence paragraph and Research composition. Keep generator isolation and originality judgment local. |
| Research | Independence and combined landscape contract. Keep evidence routes, private-query checks and research stopping local. |
| Code | Independence only. Its engineering risk scale and validation authority are not Workflow routing. |
| Design | Independence and Design/UI exchange. Keep specialist source, rights, typography and visual judgment contracts local. |
| UI | Independence and Design/UI exchange. Keep framework, measurement, sight and interaction gates local. |
| Scribe | Independence. Keep source-exact, localization and claim-preservation contracts distinct from Research retrieval and Design evidence registries. |
| Plan | Independence, dispatch criteria and low-level file identity functions. Keep native lifecycle and record ownership local. |
| Handoff | Independence. Keep the fixed continuation template and named-source/no-command restrictions local. |
| Workflow | Dispatch criteria. Reuse existing task lifecycle and rollover helpers, not generic Handoff or Ask archival policy. |
| Ask single: Astra and SOL | Existing shared single base, lifecycle helper and native-role text candidate. Preserve adviser-specific defaults and exclusions. |
| Ask paired: Claude+Astra and Claude+SOL | Existing paired base, native-role text and Claude pure functions/deadline. Preserve pair independence and provider-specific failure behavior. |
| Ask Claude-only | Claude pure functions/deadline. No native task lifecycle requirement. |

## Native Ask role contract

Single and paired `references/native-second-opinion.md` repeat read-only scope,
untrusted-input treatment, exact return-task delivery, the 6000-character bound,
explicit archive consent and same-task follow-up. Recommend
`shared/text/native-adviser-role.md` with small local scope introductions.
Expand it into both reference files during the build, preserving standalone use.
The single version explicitly forbids delegation and distinguishes requested
model settings from actual host metadata. Preserve those boundaries when
consolidating, and retain a format suitable for non-review questions.
Do not use this text for Workflow workers: they may implement changes and have
a different archival authorization contract.

## Recommended order and verification

1. Share the exact independence paragraph, dispatch criteria and combined
   Research/Brainstorm contract. Check expanded packages for preserved gates,
   owner distinctions and no unresolved includes.
2. Share native Ask role/deadline text and pure Claude functions. Run all existing
   isolated Ask package tests against every variant, especially config precedence,
   timeout, process failure and follow-up behavior.
3. Normalize the Design/UI exchange only with bidirectional contract cases.
   Extract Plan stat primitives only if the reduced maintenance offsets the new
   dependency. Test Windows identity semantics and each caller's error contract.

No token reduction is measured here. Shared source reduces authoring drift,
but embedded copies still consume context when loaded. Shorter runtime loading
requires separate comprehension and routing evidence. Do not remove necessary
rules merely to reduce a word count.

## Adapter and file-safety findings

Both Ask `members/paired/scripts/ask_claude.py` and
`members/claude/scripts/ask_claude.py` were compared, including callers.
Extractable functions include `positive_timeout`, `positive_amount`,
`parse_claude_result`, `claude_error_details` and `session_mode`. Inputs and
outputs are ordinary values, JSON dictionaries or parsed argument attributes.
Keep exact exception and error meanings at the adapter boundary.

Do not merge the complete adapters. Paired configuration nests Claude and the
native provider, supports an explicit command path and normalizes process
failure. Claude-only configuration is flat, resolves Claude from PATH and
preserves the subprocess exit code. Their decoding and error reporting also
differ. A common runner would silently change behavior unless separately
specified and tested. A shared pure-function module is the narrower candidate.

Plan's `scripts/select_context.py` and `scripts/compute_decision_batch.py`
share `is_redirect`, `snapshot` and `same_opened_file`. A possible
`shared/runtime/file_identity.py` would accept stat results and return a
redirect flag, immutable snapshot or identity comparison. Bundle it in Plan's
scripts directory through the manifest. It would reduce repeated Windows
ctime handling, but it would not eliminate either caller's safety checks.

Do not merge their complete readers. The selector returns decoded text and
structured diagnostic codes, and separately checks directory enumeration.
The batch helper streams a hash and associates failures with a Decision ID.
Both compare path and open-descriptor identity and detect changes during the
read. A replacement must preserve pre-open, post-open and final path checks,
Windows reparse rejection and each caller's error contract. With only one
Skill consuming them, this is lower priority than cross-Skill text drift.

## Composition and evidence findings

Brainstorm `references/research-composition.md` and Research
`references/brainstorm-composition.md` describe the same explicitly combined
run. Candidate owner: `shared/text/research-brainstorm-composition.md`, included
into both packages. Preserve one Research landscape lane, frozen generator
inputs, no early cross-visibility, bounded originality and the solo fallback.
Research's version explicitly reserves topology/isolation reporting to the
host or evaluator. Any consolidation must retain that stronger ownership rule,
not select the shorter copy and lose it. Keep each entrypoint's activation gate.

Design `references/coordination-with-sibling-skills.md` and UI's core workflow
share a design-decision exchange schema. Candidate owner:
`shared/text/design-ui-exchange.md`. Inputs are the concern, canonical owner,
version, decision, protected dimensions, allowed variation and validation
target. Output is an exchange record with observed evidence and unresolved
conflicts. Prefer a shared text contract, not an automatic approver. Design's
visual judgment, UI's framework/interaction proof and wording ownership remain
separate. Field names currently vary, including exception/compensation/falsifier
versus deliberate exception and compensation. Normalize only after checking
consumers, not by string replacement.

Do not generalize Handoff's `assets/continuation-prompt.md` into that exchange.
Handoff is an explicitly requested session snapshot with fixed receiver rules
and a no-task-command boundary. The design/UI exchange is an in-task contract,
and Workflow rollover additionally requires live guard and task identities.
Similar fields do not make these interchangeable.

Design's `references/source-verification-and-evidence.md` and UI's
`references/validation.md` both limit claims to inspected evidence, but prove
different things. Design tracks claim-source relations, origin and currentness.
UI distinguishes source, measurement, viewed render and interaction. Code's
validation likewise ties proof to changed behavior. Reject a universal evidence
validator or common pass label: structural completeness cannot establish any
of those semantic judgments. A tiny shared principle would save little and
could hide the operation-specific requirements, so retain the local contracts.
