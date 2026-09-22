---
format_version: 1
id: ADR-0022
status: accepted
created: 2026-09-20
accepted: 2026-09-20
scope: workflow/result-recovery
---

# Recover omitted completed results from the exact native rollout

## Decision

When `wait_threads` identifies one exact completed child turn but both its result projection and the single permitted `read_thread` recovery omit the assistant message, permit one final read-only recovery from the exact active or archived native rollout selected by recorded host, session, and turn identities. Retain wait state as lifecycle authority and accept only one schema-valid final assistant message identity bounded by that turn's context, completion event, event ordinals, and assistant phase.

## Problem

The DIVI W-006 executor produced valid final JSON twice, but the task APIs projected `latestAssistantMessage: null` and an empty completed turn, causing a false `WORKFLOW-NORESULT` blocker despite preserved valid output.

## Drivers

- Valid project changes must not be repeated or stranded because one task projection omits an existing result.
- A stale or cross-task JSON object must never authorize review, Plan mutation, commit, successor creation, or success archival.
- Native rollouts are already read by exact `CODEX_THREAD_ID` for context telemetry.
- Recovery must stay exceptional, bounded, read-only, identity-checked, and fail closed.

## Considered alternatives

- Keep task APIs as the only source: Retains the narrowest trust boundary but repeats the observed false blocker and recovery work.
- Start a fresh recovery executor whenever projections omit a message: Preserves API-only reads but spends tokens, repeats checks, and can duplicate or conflict with valid retained changes.
- Recover one exact completed-turn result from the matching rollout: Recommended because it preserves the original worker result while retaining strict host, session, turn, completion, ordinal, assistant-phase, message-identity, role, uniqueness, and schema gates.
- Accept the latest JSON found in any session data: Rejected because recency cannot prove task identity, turn ownership, or lifecycle state.

## Consequences

- Normal results still use `wait_threads`; one bounded `read_thread` remains the first recovery path.
- Rollout recovery runs only for an exact completed task and turn with an omitted projected message and all required identities present.
- The rollout supplies message bytes only; it never replaces native completion state, cursor, archival state, or task identity.
- The lookup checks the exact identity in bounded active and archived storage, fails on duplicate rollout files, excludes tool, commentary, and quoted JSON, and normalizes mirrored records only when they carry one message identity.
- A newer turn or intervening activity requires fresh native-state reconciliation before any transition.
- Missing, ambiguous, malformed, stale, truncated, failed, aborted, or mismatched candidates authorize no successful downstream transition. Actual malformed output retains one same-task formatting correction; unrecoverable identity or absence permits terminal-failure archival and a coordinator-owned blocker.

## Confirmation

1. Replay both retained DIVI W-006 omitted-message turns and recover their one valid role result without another executor.
2. Reject fixtures for a wrong host, session, turn, pre-turn result, duplicate rollout files, multiple message identities, quoted JSON, tool or commentary output, malformed JSON, mismatched role, incomplete, aborted, or failed task, intervening newer turn, and missing rollout or identity.
3. Confirm mirrored records with one message identity are not false ambiguity, ordinary wait payloads and valid `read_thread` recovery never access a rollout, and one truly malformed result still receives only the existing formatting correction.

## Revisit when

The task API guarantees complete final-message projection for every completed turn or native rollout identity and ordering cease to be available.
