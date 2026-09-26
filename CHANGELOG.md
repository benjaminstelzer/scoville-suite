# Changelog

## v2.0.1 - 2026-09-26

- Preserve existing user authorization through native Workflow and Ask handoffs, and report answers that could not be delivered.
- Respect host-required progress waits while keeping internal coordination free of extra polling and archival checks.

## v2.0.0 - 2026-09-25

- Group related consecutive Workflow Steps, receive results through native messages and continue unfinished work through compact context handoffs.
- Keep native Ask advisers in separate chats with S-ASK model titles, without a lifecycle helper between Codex and its task tools.
- Bundle Plan Viewer v1.3.3 and build its Windows, Linux and macOS assets with one checksum manifest from the suite workflow.
- Replace the old Code and UI package names, combine Ask variants, add Setup and simplify Plan and Workflow configuration.
- Install General and Codex suites through short migration prompts that remove only listed old Skills before a fresh complete installation.

## v1.1.0 - 2026-09-24

- Build general and Codex suites from one manifest; keep Python replacement procedures only in the general edition.
- Require complete suite installations from their own packages; standalone Skills remain independent.
- Add shared writing profiles with independent Plan and Workflow configuration.
- Preserve exact plan-point text and bind additional context and writing rules into Workflow dispatches.
- Bundle the compatible Plan v1.8.0 and Workflow v0.5.0 pair. Plan Viewer v1.3.2 remains unchanged.

## v1.0.10 - 2026-09-24

- Keep High risk classification for concrete planning or risk review of high-impact operations, even when execution is deferred.
- Make Workflow operation routing and helper use explicit for the coordinator.

## v1.0.9 - 2026-09-23

- Resolve WORK and REVIEW pairs from the configurable route table and raise the second and third repair attempts along its WORK rows.
- Bundle project-contract and coordinator-guard verification with bounded Work Item selection in one preflight helper.
- Require Python 3.11+ during suite installation; Workflow stops an affected operation when a required helper cannot run.
- Document Plan's no-Python dispatch-unit selection and Decision-batch hashing routes.

## v1.0.7 - 2026-09-23

- Route new high-class Workflow work to SOL 6 XHigh with Astra 6 High review, and raise ultra-high work and review to Astra 6 High and XHigh.

## v1.0.6 - 2026-09-23

- Route new Workflow work through SOL 6 and Astra 6 with the updated reasoning levels for every class.

## v1.0.5 - 2026-09-23

- Route new low-class Workflow execution to Luna 6 High and its review to SOL 6 Low.

## v1.0.4 - 2026-09-23

- Recognize a verified parking prompt and the complete writer assignment when Codex delivers both in one native turn, while blocking duplicate or conflicting assignments.

## v1.0.3 - 2026-09-23

- Keep Workflow's dispatch binding stable when the writer moves from pending to active, while retaining the separate target and guard checks.

## v1.0.2 - 2026-09-23

- Route new Workflow tasks through Luna 6, SOL 6, and Astra 6; remove Terra from the default routing table.
- Verify builder assignments after the native task envelope escapes HTML characters or removes the final newline.

## v1.0.1 - 2026-09-23

- Stop Workflow workers before project access unless their native task carries
  the complete builder-generated dispatch contract for the assigned role and
  execution unit.
- Let established codebases keep their local conventions. For Greenfield work,
  start with the smallest coherent responsibility-based layout without
  prescribing an architecture or directory tree.

## v1.0.0 - 2026-09-22

- Install the Scoville Skills together from one suite or use individual
  distributions for the concerns you need.
- Include Scoville Workflow as a Codex-only Beta, available only in the suite.
  It coordinates Plan execution, reviews, repairs and context handovers.
- Include the renamed WordPress UI Backend specialist. Replace an existing
  `wordpress-backend-ui` installation with
  `scoville-wordpress-ui-backend-anti-ai-slop`.
- Bundle runtime helpers inside each Skill so installed packages need neither
  the suite source tree nor a shared directory.
