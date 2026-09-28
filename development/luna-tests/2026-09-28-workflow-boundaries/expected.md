# Frozen evaluator expectations (not supplied to models)

## handoff
Run coordinator checkpoint now, rollover coordinator before worker creation; transfer original worker handoff/ID and authority; new coordinator creates sole successor. No acceptance or review from handoff alone.

## split
At third handoff split only remaining work into ordered Steps of same Work Item; preserve completed evidence, goal/acceptance/order; use Plan allowance, validate; no counter file/new Work Item/automatic review; group coherently without recreating oversized Step.

## dependent-review
Default review before dependent extensive test, exact unreviewed diff and affected acceptance/context. Project explicit cadence takes priority.

## defect-worker
Worker returns checked fix and remaining tests before further broad testing; coordinator reviews only fix/unreviewed delta, not marks Step complete; next worker continues after review.

## test-only
No early review for pure tests/evidence; retain evidence/checkpoint and continue next unit; final review due if required.

## final-review
Review unreviewed mobile delta + affected acceptance/interactions, reuse prior PASS for unchanged parts; recheck affected interactions if assumptions changed, not repeat whole diff.

## unrelated
Active sole writer can do task; separately identify in plan update and commit description or separate commit; cannot hide change in export result.

## messages
A completed; B blocked; C context_handoff; D pass; E changes_requested; F blocked/unfinished evidence not acceptance. No fixed output schema demands or invented success.
