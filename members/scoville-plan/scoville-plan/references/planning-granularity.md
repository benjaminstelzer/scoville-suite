# Planning granularity

Use Work Items for outcomes that can be resumed, blocked, accepted, or handed
over independently. Use Steps for ordered implementation work inside one such
outcome. Approval, testing, documentation, and release checks remain acceptance
or evidence unless they are independently requested deliverables.

Keeping at most one Work Item `in_progress` controls concurrent execution. It
does not limit the Plan to one Work Item. Multiple `todo`, `done`, or
`cancelled` items preserve the real outcome boundaries.

## Decomposition checks

Split an outcome when at least one of these differs materially:

- observable acceptance boundary;
- dependency readiness;
- responsible owner or component boundary;
- ability to pause and resume independently;
- rollout, migration, or compatibility timing; or
- blocker that should not stop otherwise independent work.

Do not split merely by activity. Implementing, testing, reviewing, documenting,
and releasing one behavior normally belong to the same Work Item.

## Write the execution sequence

Use numbered Steps for ordered behavior-complete units. Coordinate related
file changes within their unit; file count does not create Step boundaries. Keep the concept in Goal and Outcome; Steps contain only
the ordered work needed to realize it.
1. Place prerequisites and canonical-owner changes before dependent consumers.
2. Name each known repository-relative file in the Step that changes it.
3. Keep one behavior-complete unit per Step. Use the selected recipient profile for detail, with full context at every profile. Ordered intermediate actions stay within that Step line.
4. Put proof in Acceptance and observed results in Evidence, not in duplicate Steps.

Do not add a Step solely to locate an owner or file that is already known. Keep
bounded behavior or contract inspection when its result can change the
implementation or when it is an explicit prerequisite. When ownership is
unknown, prefer bounded read-only discovery before the Work Item starts and
refine its `todo` Steps with the observed path. If discovery must occur during
execution, keep the ownership criterion in the immutable Step and continue
through permitted live fields. A reviewer must be able to follow the Step order
and map each action to the outcome without inferring missing intermediate work.

## Batch deferred additions

When the core classifies a mid-task request as additive, combine it with the
latest queued `todo` Work Item only when all requested changes remain one small,
behavior-complete outcome. They must share the same observable result,
Acceptance boundary, dependencies, Decisions, blockers, ownership, rollout
timing, authorization, and material risk. One joint check must be able to prove
every included change. Size alone never makes unrelated work compatible.

Keep the requests in arrival order as Steps when subordinate order matters, and
rewrite the batch Outcome, Acceptance, and Next action so every addition remains
explicit. Never use a vague maintenance or follow-up bucket. Merge only into a
`todo` item and only when doing so does not move the new request across an
earlier separate queued item. Preserve the visible deferred title prefix while
refining the batch. The prefix records queue provenance, while the remaining
title and Outcome still name the observable result.

Create a separate Work Item when the new request is complex, independently
resumable, separately acceptable, differently dependent or blocked, owned by a
different component, subject to another Decision or rollout, or materially
different in risk or routing demand. A small request that arrives after such an
item starts a new small batch rather than jumping ahead to an older batch.

## Workflow-ready subplan points

Shape optional Steps so a dispatcher can
later dispatch them without re-decomposing the Work Item. This planning aid does
not activate the Workflow, require it, or authorize execution.

One Step is one subplan dispatch point. Keep its outcome slice, authorization,
Acceptance cue, and expected reasoning demand coherent. Split Steps when their
consequence or reasoning needs differ materially: for example, a simple text correction and a
complex persistence redesign must not share one Step. Do not split merely
because the same result needs code, UI, copy, installation, browser work, or
live QA; those activities stay together when they share one risk and Acceptance
boundary.

{{ profile: general }}Steps can serve as later execution units.{{ /profile }}{{ profile: codex }}Scoville Workflow can use Steps as dispatch units. Its explicit invocation
rule still applies; writing a Plan does not start Workflow.{{ /profile }} Group each
Step around one coherent outcome slice with comparable consequence and
reasoning demand. Evaluate the complete expected execution and verification
scope. Treat a bounded change needing no nontrivial local implementation or
verification judgment as `ultra_low`; nontrivial local judgment with one known behavior owner,
understood helpers, established checks, and no component or harness-boundary
diagnosis as `low`; unresolved helper contracts, required local diagnostic
discovery, interacting owners, harness-boundary helpers, integration diagnosis,
or interpreted broader checks as at least `medium`; consequential
changes to state, authorization, or integration contracts as `high`; and work
beyond that consequence or complexity as `ultra_high`. Use these boundaries to
separate Steps, but do not write the class. Treat every unknown low-eligibility
fact as at least a `medium` boundary while shaping the Steps; never assume a
single owner, known helper, mechanical check, or local scope when the Plan does
not establish it. File count, generated metadata, and
known test volume alone do not raise it. Separate a trivial text edit from a complex structural change;
do not split code, UI, browser work, or other activities that share the same
outcome, risk, authorization, and Acceptance boundary. A user-selected executor
model or reasoning effort may be recorded only through the strict Step
annotation in the native format. Plan does not assign a route class. Preserve an
existing route prefix and record one only when the user explicitly supplies it;
the Workflow coordinator owns the current route, model, and reasoning choice at
dispatch.

Keep independently resumable outcomes as separate Work Items even when their
routing class matches. Workflow-ready Steps remain subordinate sequence: they
gain no status, ID, dependency, blocker, Evidence, or lifecycle of their own.

## Representative shapes

A small application may need separate Work Items for independent outcomes.
For example, a calculator can separate its arithmetic domain from its responsive
interface when they have distinct acceptance boundaries. Each item owns its implementation steps,
acceptance, evidence, and current action.

For a stored workflow, domain transition, persistence adapter, and user-facing
flow may have independent outcomes. For a structural change, migration,
compatibility, consumer update, and rollout may be separately resumable.

For one UI behavior, a suitable Workflow-ready shape could be:

```text
Steps:
1. Correct the approved button label and verify the exact copy.
2. Implement and browser-check the responsive interaction across its affected component states.
```

The different consequence and reasoning demand justifies two Steps. The second Step keeps code,
UI, and browser validation together because they prove the same behavior.

Dependencies express genuine boundary order. Keep subordinate sequence in
Steps. After each performed phase, rewrite `Next action` to the first unobserved
action. If implementation exists but the agent cannot run checks, explicitly
name evaluator-owned tests, build, browser verification, or review.
