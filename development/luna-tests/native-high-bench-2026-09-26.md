# Native Luna High benchmark - 2026-09-26

Status: all 70 planned runs completed and semantically assessed; release authorized with reported limits under ADR-0097.

## Scope and result

Five cases per area, each twice in a fresh native context. Native session records confirm gpt-6-luna/high in all 70. All 79 frozen runtime hashes remain unchanged. No failed answer was repaired or replaced by a passing retry. Setup was excluded. Workflow/Ask actions were offline proposals, not live service/lifecycle tests. UI has source and fake-DOM evidence, not rendered browser proof.

| Area | Pass | Minor | Partial | Fail |
| --- | ---: | ---: | ---: | ---: |
| Code | 10 | 0 | 0 | 0 |
| Handoff | 8 | 2 | 0 | 0 |
| Plan | 9 | 0 | 1 | 0 |
| UI | 9 | 0 | 1 | 0 |
| WordPress | 10 | 0 | 0 | 0 |
| Workflow | 0 | 0 | 9 | 1 |
| Ask | 6 | 1 | 3 | 0 |
| Total | 52 | 3 | 14 | 1 |

Partial means a missing/wrong required detail or a material unresolved evidence concern, not total failure. UI01-r2 is a focus-retention concern from disabling a focused button, not a browser-reproduced defect. Plan04-r2 is accepted: paused state and explicit decision-first Next action preserve the dependency despite empty Blocked by. Plan04-r1 lacks that decision-first action.

## Material findings and attribution

- Handoff01 both promote a preference to a requirement; r2 also lacks opening outer fence.
- Workflow repair prompts omit carried message authorization. Some cursors omit state or infer executor settings from coordinator settings. Asking for the existing result is permitted under the run authorization; that tool choice alone is not a failure.
- Workflow05-r2 runs another test and two checkpoints after stipulated context_handoff, replacing supplied state with a new fixture failure. This violates the scenario and existing stop rule; it is not an observed product failure.
- Ask02 both omit essential native adviser/delivery instructions. Ask03-r2 changes the reference and adds another query while still requesting the original exact review scope. This is extra overhead, not evidence of an unauthorized new review. Its repeat performs direct recovery.
- No successful helper output was shown to need repair. Observed repair rounds arose from wrong arguments, wrong initial adviser selection, or Python quoting/input-file creation. Workflow builders were only planned, never consumed live: their actual next-step usability remains unproven by this benchmark.

The evidence does not support 'Luna is simply not intelligent enough', nor establish that adding more Skill rules will help. Several failed actions already contradict explicit short rules. Repeated omissions across several references suggest dispatch construction is still demanding, but that is a hypothesis, not a controlled causal result. Do not add a general retry/guard framework.

Test limitations also contributed: generic result.md conflicts with specific Handoff-only artifact requests; Workflow/Ask stipulated state has no real project fixture; checkout uses a supplied form.status adapter without native DOM wiring. These are retained separately from model failures. The historical CLI gate is not qualified by native testing.

## Tokens and handoffs

Native cumulative usage: 26,047,770 input tokens, including 24,250,112 cached; 1,797,658 uncached input; 286,370 output (139,382 reasoning included, not added again). This includes repeated host/context input across calls. It is neither unique Skill size nor evidence of duplicated tool output, and supplies no before/after saving claim.

Benchmark prompts were about 1.3-3.7k characters. Example generated handoffs: successor prompt 756 characters, native Ask prompt 3,440, repair assignments 708/381. Small artifacts still omitted required context. Observed avoidable work includes repeated settings resolution, source inspection instead of documented helper use, directory probing in a stipulated scenario, and running checks after the handoff boundary. Nested tool traces were not counted as duplicated emissions.

## Numbering change after the benchmark

Authorized child-role numbering is now per exact assigned Work Item/Step range; new unit resets, same-unit new task increments. Coordinator count remains per run. Rollover preserves assigned unit and logical repair attempt. The 70-run snapshot predates this change.

Separate native gpt-6-luna/high test (thread 01a0de89-87dd-7743-b7d7-ec0141a180cc) correctly derives repeat-review, new-unit, fixer-successor and manager-rollover titles. Codex suite built and package check passed; 17 Workflow tests and 19 CLI-runner tests passed. Generic Skill Creator validator rejects the pre-existing compatibility frontmatter key; it did not validate this package. Repository package validator passed. Numbering is installed from built output in local Codex; Claude has no Workflow package.

## Next action

The original 70 results remain retained. Corrected fixtures, minimal instruction fixes and targeted repeats are recorded in [targeted-regression-2026-09-26.md](targeted-regression-2026-09-26.md). Publication is authorized with the reported limits under ADR-0097. Do not claim all helpers or live coordination have passed from offline proposals.

## Evidence

Bench root: <bench-root>

- evidence/author-grades.json: all 70 semantic dispositions.
- evidence/grades-ui-independent.json and grades-workflow-ask-independent.json: independent artifact review, checks, caveats, helper analysis and handoff sizes.
- evidence/native-run-results.json and native-details.json: original finals, native identity, calls and usage.
- evidence/token-summary.json, runtime-hashes.json, run-manifest.json: costs, immutable runtime and original inputs.
- evidence/numbering-postbench.md: separate post-change naming test.

Correction: scoped requests for existing results are authorized. See Bench evidence/message-assessment-correction.md; earlier tool-choice-only judgments are withdrawn.
