# Changelog

## v0.4.3 - 2026-09-23

- Route new low-class execution to Luna 6 High and its review to SOL 6 Low.

## v0.4.2 - 2026-09-23

- Use Luna 6, SOL 6, and Astra 6 for new coordinators, workers, and reviewers according to the configured route. Remove Terra from the defaults.
- Verify builder assignments after the native task envelope escapes HTML characters or removes the final newline.

## v0.4.1 - 2026-09-23

- Stop agent-created workers before project access when their native task does
  not contain the complete builder-generated dispatch contract. The gate now
  checks the role, execution unit, Plan lockout, required inputs, delivery
  identity and exact reconstructed prompt bytes.

## v0.4.0 - 2026-09-22

- Ship as `scoville-workflow-for-codex`, a Codex-only Beta inside Scoville Suite.
- Configure context handover thresholds and generate SCW task titles through
  bundled helpers.
- Generate dispatch payloads once and load coordinator rules by phase, with
  retained recovery state for interrupted dispatches.
- Allow exact active-successor evidence to resolve a missing normal-list entry.
  Archive only verified predecessors after guard transfer and turn completion.
- Recover outstanding predecessor chains in order. Verify each archival reply
  and retain its receipt before continuing. Failed or unverified replies stop
  the chain without archiving the current coordinator.

## v0.3.6 - 2026-09-21

- Make `low` fail closed: every owner, helper, target, boundary, and mechanical
  verification fact must be positively known or the unit routes to at least
  `medium`.
- Route discovery, mirrored cross-language contracts, generated-source parity,
  harness uncertainty, and interpreted broad checks to at least `medium`, even
  when the authored Step uses a simple local-edit verb.

## v0.3.5 - 2026-09-21

- Isolate prompt-builder stdout from routing reads, diagnostics, shell
  transcripts, and other command output. Child creation now requires the exact
  role marker at byte zero, so `workflow.toml` and coordinator-only data cannot
  leak into worker, reviewer, or repair prompts.

## v0.3.4 - 2026-09-21

- Treat each authored route as a minimum and re-evaluate the complete execution
  and verification scope before every fresh execution-unit dispatch. The
  highest applicable class becomes the effective route without rewriting the
  annotation or requiring a later scope change. Repairs and context rollover
  retain their launched pair; file count and known test volume alone do not
  inflate routing.
- Define `low` and `medium` at behavior-owner, harness-boundary, integration,
  local-diagnostic, and result-interpretation boundaries, and keep route class
  distinct from the selected model and reasoning level.
- Enforce the accepted-Decision prerequisite before bundling adjacent compatible
  Steps; without that authority, one Step remains one dispatch unit.

## v0.3.3 - 2026-09-21

- Keep the active coordinator in the normal task list during rollover. The
  successor proves its unarchived visibility without pinning itself, then alone
  archives its predecessor after that predecessor turn completes.

## v0.3.1 - 2026-09-20

- Separated the initial launcher from active coordinator transitions and fixed
  the parking and ready-task handoff fields.

## v0.3.2 - 2026-09-21

- Added one permission-inheritance probe to installation. Runtime tasks keep
  inherited technical permissions and report only actual access failures, which
  the coordinator preserves before asking about a configuration repair.
- Kept the coordinator active and visible while an executor, repair task, or
  reviewer runs. It now waits only on that exact child with bounded cursor-based
  waits, stays silent on unchanged timeouts, and preserves all state on a real
  wait failure.
- Made the child's exact final JSON the recovery path when its one authorized
  result-delivery message fails. The child still returns the validated final
  bytes and never retries a definite delivery failure.
- Closed the same liveness gap in coordinator rollover. The predecessor waits
  for the exact successor validation turn, remains visible through failed
  activation delivery, and never archives itself. Only an activated, visible,
  unarchived successor may archive the exact predecessor after its turn ends.

## v0.3.0 - 2026-09-20

- Added a user-approved first-project setup that installs one concise managed
  write contract at the start of the project-root `AGENTS.md`. Setup always
  ends its invocation; only a later explicit activation can start a workflow.
- Added a transient, process-serialized workflow guard. Pending task identities
  are read-only, exact ready IDs require explicit activation, one coordinator
  owns Plan, staging, and commits, and only one executor or repair may write its
  assigned unit. Reviewers, audits, consultations, and unrelated cooperating
  tasks remain read-only. The documented boundary is cooperative rather than a
  filesystem-level prevention claim.
- Added coordinator rollover at accepted dispatch-unit boundaries. A fresh
  exact measurement at or above 33 percent transfers the existing guard to one
  validated successor and activates it; that successor then archives the exact
  predecessor ID. Missing or
  stale telemetry continues in the same coordinator; provisional or unknown
  creation never permits a duplicate successor. One identity-bound validation
  acknowledgement wakes the predecessor for transfer; activation needs no
  return acknowledgement or polling loop.
- Defined native `waitingOnApproval` message calls as one pending delivery with
  no retry, relay, polling turn, duplicate task, or progress narration.

## v0.2.2 - 2026-09-20

- Prevented persistent Codex goals from driving a workflow coordinator. Whole-
  Plan and keep-going requests now remain scope and continuation instructions in
  the event-driven operations loop, so ending a coordinator turn for an active
  child cannot trigger automatic wait, polling, or status turns.
- Added recovery for older runs: an explicitly requested goal pause stops the
  automatic continuation without pausing the canonical Plan or cancelling its
  active child.

## v0.2.1 - 2026-09-20

- Made coordinator phase changes visible in the launcher-retained language. The
  coordinator now identifies the exact Plan unit when execution, required
  review, assigned repair, and the accepted completion transition begin, while
  active-child waits and unchanged state remain silent.

## v0.2.0 - 2026-09-20

- Hardened terminal `context_handoff` behavior across automatic host compaction. A resumed
  child now uses a deterministic read-only inspector on its exact own rollout
  before project action. It distinguishes continue, missing delivery,
  already-delivered replay, and fail-closed states; inherited handoffs never
  count as the child's own result. Rollover
  successors are keyed to the exact predecessor, so a retry cannot create a
  duplicate and a later legitimate rollover still has its own transition.
  Successors treat inherited handoffs only as continuation input and a
  coordinator-owned progress gate stops copied or paraphrased no-progress
  handoffs after one successor without creating a grandchild.
- Replaced recurring coordinator wait turns with one single-use result delivery
  from each child. The coordinator remains dormant while the child runs and
  wakes once for one bounded native completion confirmation. A delivery race
  remains pending without transition or another wait; after completion the
  existing recovery chain runs before byte comparison, validation, archival,
  and transition. Transport timeouts never become a polling fallback.
- Bound post-compaction delivery recovery to the actual native Codex
  `functions.exec` wrapper, its direct inline coordinator call, correlated tool
  output, exact delivery reference, destination, and result bytes.
- Made terminal detection monotonic across repeated same-turn compactions and
  fail closed on conflicting task, mirror, replacement-history, or
  compaction-gap evidence.
- Made prompt generation UTF-8 deterministic on Windows, made Git stage/commit/
  push/history prohibitions unconditional, and required complete compact
  continuation state for every handoff.
- Added exact repair assignments as reviewer-finding indices, so repair workers
  receive the full verdict but change only unresolved executor-owned findings.

## v0.1.0 - 2026-09-20

- Made `context_handoff` terminal across automatic host compaction. A resumed
  child now checks its exact own rollout before project action, repeats the same
  terminal result when found, and stops on ambiguous evidence. Rollover
  successors are keyed to the exact predecessor, so a retry cannot create a
  duplicate and a later legitimate rollover still has its own transition.
- Added a final exact-session recovery for completed results omitted by both
  task APIs. Only one identity-bounded final assistant message can supply bytes;
  completion and cursor authority remain with the task API, and malformed,
  stale, quoted, or ambiguous output still fails closed.
- Kept model, reasoning, coordinator title, and configuration schema in
  `workflow.toml`, while removing decorative protocol limits that were never
  consumed. Explicit continue or resume requests now reach fresh and existing
  coordinators as a trusted field and no longer trigger the same initial
  question twice.
- Resolve explicit Step executor overrides property by property against the
  route default, block unsupported effective pairs without substitution, split
  bundles when the effective pair changes, and preserve the launched pair for
  repairs and context rollover. Reviewer and coordinator routing stay
  route-owned.
- Allow the initial executor plus three repair executors. If executor-owned
  findings remain after repair three, preserve the work and ask the user for a
  disposition instead of silently creating another attempt.
- Deferred child IDs, results, review and repair records, Evidence, blockers,
  and `Next action` to the accepted unit commit, preventing Plan-only commits
  from advancing `HEAD` after a required pre-change backup. Failed hooks now
  preserve both the diagnostic and all work without bypass or destructive
  recovery. Outstanding backup-to-source-commit intervals also gate otherwise
  independent units, fresh backup creation remains executor-owned, and later
  accepted commits carry complete valid accumulated Plan state without carrying
  earlier unaccepted project changes.
- Required exact-ID `archived: true` state before Plan mutation or another child
  transition. Generic tool completion and task-list membership no longer count
  as proof, and interrupted workflows get one bounded same-ID reconciliation.
- Embedded the complete selected Plan context and referenced Decisions directly
  in executor prompts, removed the prompt-size cap, and removed free-form
  transition prose so workers do not reread the canonical Plan.
- Added one deterministic prompt helper for executor, reviewer, and repair. It
  sends only the exact Work Item or selected Step range with all referenced
  Decisions, excludes Evidence and other Steps, and excludes the Work
  Item-wide `Next action` from Step units so later work cannot leak into the
  current assignment.
- Replaced projected review booleans with exact `yes` or `no` strings and added
  one identity-bound source-message recovery when a completed native wait
  projection is invalid, preventing valid executor results from becoming false
  format blockers while keeping native state and cursor authoritative.
- Added deterministic coordinator selection through Scoville Plan's exact
  four-area projection, with separate bounded proposal, preflight, graph, and
  recovery reads and no raw full-Plan fallback.
- Added guarded adjacent-Step bundles when outcome, owner, authorization, route,
  workspace, and Acceptance boundary all match; changed facts retain a dispatch
  boundary and review remains result-based.
- Moved result, checkpoint, wait, review, repair, and completion contracts to
  one operations owner, materially reducing the always-loaded entrypoint and
  batching safe deterministic coordinator transitions.
- Made missing, stale, or contradictory context telemetry non-blocking by
  itself while preserving the strict above-66-percent rollover for fresh exact
  occupancy with material work remaining.
- Evaluate terminal scope before rerunning the selector, so final Plan
  completion and explicit boundaries report success without turning the
  selector's intentional idle-state diagnostic into a blocker.
- Added an explicit native Codex workflow with launcher-only activation, one
  Plan coordinator, Plan-shaped worker dispatch, risk-based model routing,
  fresh review, bounded repairs, same-task user decisions, and terminal child
  task archival.
- Added measured native context rollover strictly above 66 percent without CLI
  compaction or a private runtime.
- Added compact validated handoffs, sparse coordinator output, explicit stop
  handling, and source-contract tests.
- Suppressed routine coordinator transition narration and defined expected
  `git diff --no-index` exit codes so displayed differences are not false
  failures.
- Adjusted medium, high, and ultra-high executor-reviewer routing to the
  requested SOL and Astra reasoning levels.
- Prepared the exact nested package for installation from a separate private
  GitHub repository.
- Added a result-based review threshold. Codebase and critical documentation
  changes still receive independent review, while preparation, project
  inspection, Plan maintenance, and routine documentation no longer create a
  reviewer by themselves. Executors report both change classes explicitly, and
  the coordinator performs only a bounded result comparison before skipping
  review. Reviewer-requested Plan fixes and routine non-critical documentation
  corrections also avoid a second pass when that comparison is clear, while
  code, critical documentation, and material risk-boundary corrections remain
  review-gated.
- Stopped the coordinator from reading active child chats during normal waits.
  Generic status uses a bounded wait snapshot, and chat inspection happens only
  once when the user explicitly requests a named child conversation.
- Made the active Plan the default coordinator scope when no Work Item range or
  end boundary is named. The coordinator now continues eligible items without a
  new confirmation after each accepted unit and returns control mid-scope only
  for a concrete user decision. Explicit boundaries remain binding, and one
  blocked unit or unavailable required model pair no longer stops independent
  eligible work. Remaining subplan points finish before the coordinator advances
  to another Work Item.
- Kept the coordinator open after its final completion report. Self-archival
  could terminate the turn before the report became visible; terminal child
  tasks are still archived after their results are retained.
- Kept the coordinator and every child or successor conversation in one shared
  live checkout by default. Git no longer implies a worktree; explicit isolation
  requires a disclosed reintegration path and non-inherited state, while missing
  same-workspace support now stops for a user decision.
