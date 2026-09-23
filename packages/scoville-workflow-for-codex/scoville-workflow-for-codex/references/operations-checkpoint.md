# Checkpoint phase

Post-compaction and inherited-handoff progress gates: [compaction](operations-compaction.md). Successor creation: [review](operations-review.md), [activation](operations-activation.md).

## Native context checkpoint

Only at a natural internal boundary with material work remaining, the child
invokes the prompt-embedded `scripts/check_context_checkpoint.py --role <role>`
once. `action=context_handoff` requires the normal role handoff result;
`action=continue` permits continued work. If the helper cannot run, stop this
checkpoint and report the failure; do not search telemetry manually. A helper
result with `telemetry=unavailable` still permits bounded work.
This read-only helper reads the latest `token_count` event in its own active native rollout,
identified by exact `CODEX_THREAD_ID`. The sample is fresh only when its event
ordinal is later than both the current turn's latest `turn_context` event and
any latest `compacted` event in that rollout. Missing fields, missing rollout,
stale ordering, or contradictory ordering makes telemetry unavailable. Do not
estimate, poll repeatedly, or derive occupancy from message count or prose size.

Unavailable telemetry alone creates neither a blocker nor a successor. Continue
the same bounded task while it can still make progress, and return its normal
role result when complete. An independently observed host failure remains an
ordinary blocker with that failure as evidence. When telemetry is fresh,
calculate
`last_token_usage.input_tokens / model_context_window * 100`; never use total
or cumulative usage.

Use `context.worker_percent` from `assets/workflow.toml`. At that percentage
or below, continue in the same task. Strictly above it,
return a schema-valid `context_handoff` containing only missing state and named
evidence in `summary`, plus only unresolved defects in `findings`. The
coordinator archives the predecessor after retaining that handoff and creates
exactly one successor with the same unit, role, launched model, launched reasoning, authorization,
remaining work, logical attempt, `workspace_mode`, and exact `workspace_root`.
The successor sees the predecessor's uncommitted changes immediately through
that same directory. This transition is neither a repair nor a review. Never
estimate the percentage, request manual compaction, or recreate workspace state.
If the host compacts after that final message but before turn completion, the
post-compaction terminal gate runs before anything else.

When the task itself was created from an inherited `context_handoff`, any later
handoff summary also carries the exact `progress_after_dispatch` and `evidence`
labels defined above. If it cannot name both from its own post-dispatch work, it
returns its ordinary `blocked` or `needs_user_decision` result instead of a
handoff.

Completed work returns its normal role result without a checkpoint because no
material work remains.

### Context checkpoint scenarios

| State | Child action | Workflow effect |
| --- | --- | --- |
| Exact rollout or metric unavailable | Continue bounded work | No telemetry-only blocker or successor |
| Ordering stale or contradictory | Continue bounded work | No telemetry-only blocker or successor |
| Fresh occupancy at or below the configured worker percentage | Continue same task | No handoff |
| Fresh occupancy strictly above the configured worker percentage with material work remaining | Return `context_handoff` | One same-role successor |
| Fresh post-compaction sample follows the compacted event | Evaluate its exact occupancy | Apply the same strict threshold |
| Compaction follows an emitted final `context_handoff` | Run the terminal gate and repeat the same bytes | No same-task project work; reconcile one predecessor-keyed successor after completion |
| Work completed before another natural boundary | Return normal role result | No checkpoint or successor |
| Host failure independently prevents progress | Return ordinary blocked result | Block on the observed failure not missing telemetry |
