---
format_version: 1
id: ADR-0012
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/coordination
supersedes: ADR-0005
---

# Recover completed result payloads by native identity

## Decision

Keep `wait_threads` authoritative for child state and cursor. When its completed-result payload is syntactically or schema-invalid, permit one bounded `read_thread` call and accept that payload only when the task, host, completed turn, and assistant-message identities match the wait result exactly and the complete message validates.

## Problem

Native `wait_threads` output can corrupt an otherwise valid JSON result payload and turn successful child work into a false format blocker.

## Drivers

- Preserve valid completed work without weakening the role-specific result schema.
- Continue forbidding reads of active child conversations and chat polling.
- Keep native wait state and cursor authoritative across the recovery read.
- Bound the exceptional read by exact identities and the existing result-size contract.

## Considered alternatives

- Keep wait-only validation: Preserves the former rule but converts observed projection corruption into false child failure.
- Replace booleans with string values: Avoids the observed symptom but does not establish transport integrity for other payload fields.
- Always read completed child chats: Avoids the damaged projection but duplicates every normal result and increases coordinator context.
- Recover only an invalid completed payload by exact identity: Adds one bounded exceptional read while keeping normal coordination wait-only.

## Consequences

- Valid `wait_threads` payloads never trigger a chat read.
- Active and nonterminal child conversations remain unread during normal coordination.
- A recovery read may replace only damaged message text; it never replaces native state or cursor.
- Missing, mismatched, truncated, or invalid recovery data follows the existing correction and blocker path.

## Confirmation

1. Add focused contract coverage for valid wait payloads, identity-matched recovery, identity mismatch, and active-child exclusion.
2. Verify the recovery call is limited to the newest completed turn without tool outputs and retains the wait cursor.
3. Recheck the observed DIVI result shape through the updated contract before resuming the real-project run.

## Revisit when

Reconsider when native wait results preserve the exact assistant-message payload or expose a typed role-result field.
