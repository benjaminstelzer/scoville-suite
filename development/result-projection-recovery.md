# Result projection recovery

## Observed evidence

Read-only inspection on 2026-09-21:

| Reviewer | Completed turn | Delivery reference |
| --- | --- | --- |
| 01a0c3fa-53e2-73a1-9f9e-a5a1be803249 | 01a0c3fa-5582-7e31-bcf3-00f884076741 | g8-w015-step3-reviewer-a1-turn1-result |
| 01a0c486-ce2b-7442-a7da-8885fa15658c | 01a0c486-cf7f-7ad0-bce1-adc72a7d1e80 | g8-w015-step3-reviewer-a2-turn1-result |

Each current `read_thread` final message exactly equals its recorded delivery
JSON after removing the delivery-reference line. Both results remain
`changes_requested`; `md:w-1/2` and `md:grid w-1/2` describe real class-sanitizing
findings, not strings to normalize or remove.

Coordinator `01a0c3d1-11a6-7ad2-8f01-dabf6713f211` reported a different wait
projection in turns `01a0c3e4-3b6d-76d2-9fe7-112c193c30e9` and
`01a0c485-c72b-7a62-8a03-5f16c499ec7e`: the first named `md/2` instead of
`md:w-1/2`; the second reported removed colons. These are retained coordinator
reports. The retained native coordinator rollout independently confirms both:
the original completed `wait_threads` outputs contain `md/2` and `md w-1/2`.
Their task, completed-turn and final-message IDs match the current exact source
messages. Both source messages equal their original delivered JSON, with
`changes_requested` unchanged. The current source
messages support a bounded source-recovery path, not blanket semantic equality.

## Contract gap

Canonical owner: Workflow `references/operations.md`, completed-result recovery.
It requires delivered/final byte equality, but its source-read route covers
missing or malformed projections, not a schema-valid projection with changed
string bytes. ADR-0004 authorizes automatic recovery only when exact identity
and unchanged authoritative source bytes establish a pure projection problem.

The contract now allows one exact completed-source read for this mismatch.
It accepts unchanged source bytes only when they equal authenticated delivery,
with completion/identity/schema checks intact. Conflict, truncation or uncertain
identity remains fail-closed; no extra rollout lookup, reread or new review.

Private build `temp/2026-09-21-suite-migration/workflow-projection-recovery`
passes source/package parity. Of its19 Workflow package files, only
`references/operations.md` differs from the previously tested private package.
Focused positive/negative contract checks and affected comprehension verification
remain open. No live task, installed Skill or DIVI5 file was changed.

The final private candidate is `workflow-projection-recovery-final`; it also
splits the wake table's delivery-conflict rejection from completed-projection
recovery. Its source/package parity check passes. Deterministic checks model
the written contract only, not a production recovery helper or live host.
Their identity fixtures must reject absent IDs rather than treating two missing
values as matching. Delivery binds sender/reference/dispatch; wait and source
bind completed turn/final message. Delivery need not know a later final-message ID.

## Verification

- Two focused tests pass: projection recovery and exact-child coordinator waits.
  Positive fixtures preserve both original class strings and `changes_requested`;
  negatives reject nonterminal state, absent/wrong identity, unauthenticated or
  mismatched dispatch, truncation and actual source/delivery conflict.
- Luna Medium case `projection-01` passes SOL and independent author review.
  Thread `01a0c5a4-ae61-7482-8060-74035c689090`, two turns, full protocol/input/
  native checks pass. It recovers exact source only, preserves status/authority,
  rejects conflicting or unidentifiable sources and waits for nonterminal child.
- Frozen inputs: `luna-tests/codex-cli-inputs-workflow-projection-r1.json`.
  Raw output: workspace temp `2026-09-21-suite-luna-evaluation/` directory
  `workflow-projection-r1-01-reusable-cli`.

This proves the instruction change and bounded comprehension, not live host
repair or an installed rollout. No live installation was modified.
