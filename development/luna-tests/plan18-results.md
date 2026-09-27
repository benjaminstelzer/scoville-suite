# PLAN-0018 focused verification

The user requested targeted GPT-6 Luna High cases for the changed Plan and
Workflow rules, followed by Astra Medium review, local updates and new releases.
This release uses that focused scope rather than repeating the 45-case gate.

## Skill checks

- Six SOL Medium scenarios exercise ordered Steps, correction, handoff,
  accepted Decisions, formal wording and retained evidence. The actual packaged
  selector, validator and dispatch builder consume their results successfully.
  Two initial failures used an invalid hand-written fixture format. Corrected
  documented inputs pass without changing the parser.
- Six independent Luna cases pass protocol and semantic review. Every native
  turn records `gpt-6-luna` and `high`. Each case uses two turns and only the
  relevant packaged references. These simulate decisions, not native delivery.
- The combined repair case leaves its exact Step range unspecified. Luna
  correctly makes the title suffix conditional. SOL separately exercises the
  exact range and complete repair/continuation payloads.
- Actual assignments measure 7,255 to 8,558 characters. Character counts are
  not token counts. Per-turn Luna usage is retained separately, including
  cached inputs and reasoning outputs. No workflow-wide token saving is claimed.
- Workflow 17, Plan 74 and suite 32 automated tests pass. README/source checks,
  generated package inventories, YAML metadata and scoped diff checks pass.
  The runner correction also passes its 19 existing focused tests.

The first Luna transport attempt failed before any model answer. The existing
runner disabled a required code-mode host and emitted an unstable-feature
warning before the expected event sequence. Two CLI configuration corrections
allow the unchanged strict protocol to run. Skill package bytes are unchanged.

## Evidence

Raw scenarios, expectations, original failures, actual helper outputs, native
rollouts and per-turn usage are retained under the workspace's
`temp/2026-09-27-plan18/sol/` and `temp/2026-09-27-plan18/luna/`.
The Luna `package-provenance.json` owns the tested package hashes. Publication
requires comparing the clean builds with those hashes.

DIVI implementation and focused checks are recorded separately in
`temp/2026-09-27-plan18/divi-evidence.md`. No full M10 acceptance, active
Neutral-only reset or overall performance percentage is claimed here.
