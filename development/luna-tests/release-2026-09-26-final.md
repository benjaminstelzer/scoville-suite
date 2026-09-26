# Release candidate verification, 2026-09-26

Candidate: suites 2.0.2, Code 2.0.1, Handoff 2.0.19, Plan 1.9.1,
UI 2.0.1 and Ask 1.0.2. Workflow 0.6.2 ships only in the Codex suite.

Build/readme/source checks and all package inventories pass. Automated tests:
suite 31, shared 59, Ask 21, Plan 74, Setup 2, Workflow 17 (204 total).
Code and Handoff have no Python unittest cases. PLAN-0016 retains targeted
SOL 6 Medium native-workflow and editing evidence.

Local installations match the built runtime files: Codex seven packages,
Claude four general packages. Previous installs are backed up in workspace state.

## Luna gate remains blocked

All 45 selected cases ran through the bounded CLI runner with Luna 6 Medium.
The initial run produced 40 protocol passes and five failures. One fresh retry
per failed case produced 42 protocol passes and three remaining failures.
A protocol pass is not semantic acceptance. No full gate pass is claimed.

- Code-25 repeatedly logs a disabled code-mode host error.
- Workflow-12 mixes a read request with its answer after the retry.
- Ask-Claude-06 correctly requests config.default.json, but the runner rejects
  this JSON path. The existing harness cannot serve that required configuration.
- Handoff-25 asks for missing concrete facts instead of explaining the given
  hypothetical size/recovery boundary.
- Ask-single-06 does not resolve the exact model ID/effort or exact task title.
  Ask-paired-06 also leaves settings unresolved without loading configuration.
- Workflow-11 gives route descriptions without loading the required dispatch
  reference. These answers need resolution before semantic acceptance.

Raw runs, prompts, native identity checks, hashes and retry history are under
workspace temp/2026-09-26-release-final. gate-results.json enumerates all cases.
The source gate and historical expected keys also reference retired Ask types
and model defaults. Do not repair production Skills merely to satisfy stale
test expectations, or reuse the older release-only gate exception.
