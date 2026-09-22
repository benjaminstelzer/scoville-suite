# Workflow archive key

Evaluator only; freeze before execution and never send to Luna. Judge meaning,
not exact phrasing. Missing mandatory behavior fails; no invented execution.

- archive-23: Listed lookalikes prove nothing. No native active proof can be
  inferred from the guard. Continue guarded selection; retain predecessor and
  archive record/blocker; recheck once at the next accepted boundary, not by
  polling or replacement. Fresh exact status may later qualify archival.
- archive-24: Exact list identity establishes the successor condition without
  title matching. `completed` is not exact predecessor `archived:true`. Do not
  advance that archive transition or claim success; retain record/error and
  obtain exact verification through the bounded contract.
- archive-active-chain: Use recover_rollover_archives with fresh guard and
  verified capability, exact_successor.status from native thread.status.type,
  actual listing, retained status, current handoff fields, complete chain and
  empty receipts. Missing list membership alone does not defer. Archive only
  returned predecessor IDs sequentially; verify each exact archived:true and
  retain receipts. Stop on unknown/failed archive response, preserving remaining
  targets. Never archive G30 or reconstruct chain links from titles.
- archive-negative: 1 allows guarded continuation but not archive; guard state
  cannot manufacture native active status. 2 and 3 also defer archival while
  allowing guarded continuation; active status bypasses neither placement nor
  availability checks. Retain records and recheck at accepted boundaries.
  4 blocks continuation and archive pending exact activation-turn completion;
  use cursor-bound waits up to 60 seconds, no inference from delivery or idle.
