# Dispatch phase

Before creating any task, use [activation](operations-activation.md) and [wait](operations-wait.md). Select context using [selection](operations-selection.md).

## Build one dispatch unit

Use Scoville Plan's complete structural validator at the normal Plan-validation
gate. `Steps` is optional: absence means the complete Work Item is one unit;
presence requires a non-empty consecutive numbered block with valid route and
execution annotations. The named-unit selector then independently rejects a
missing, malformed, non-adjacent, or out-of-range requested Step. Never treat an
absent optional `Steps` block as an invalid Plan.

Without Steps, the selected Work Item is one dispatch unit. With Steps, the next
unperformed Step is the default unit. Form a longer maximal authored-order
prefix of adjacent unperformed Steps only when a referenced accepted Decision
explicitly authorizes compatible-Step bundling for this Workflow and every
Step's compatibility tuple is identical:

```text
(outcome, owner, authorization, route, effective executor pair, workspace, Acceptance boundary)
```

Outcome and Acceptance come from the selected Work Item. Determine owner and
authorization from the actual requested effects and current risk. Treat an
authored `[route: CLASS]` as the minimum route. Before every fresh execution-unit
dispatch, compare the complete execution and verification scope with the route
classes in the entrypoint from `ultra_high` down to `ultra_low`, and choose the
highest class whose criteria apply. Raise the effective route above an
annotation that was initially too low or incomplete; no later fact change is
required. Never dispatch below the annotation. Do not reclassify a repair or
context-rollover continuation; retain its original launched pair as required by
their role contracts. Before mapping a fresh unit to `low` or `ultra_low`, apply
the entrypoint's complete fail-closed eligibility check. Every required fact must
be positively established from the selected context and bounded preflight. One
false or unknown fact selects at least `medium`; an action verb, authored route,
or expected small diff never substitutes for that evidence. Keep this check
transient: do not add it to the Plan or child prompt.

`low` requires nontrivial local implementation or
verification judgment, one known behavior owner, understood helper contracts,
established verification commands,
and no diagnosis across component or test-harness boundaries. Use at least
`medium` for an unresolved helper contract or required local diagnostic
discovery, interacting behavior owners, helper or mock availability across a
harness boundary, integration diagnosis, or broader checks whose results need
interpretation. File count, generated metadata, or a known large test suite
alone does not raise the class. `high` requires consequential changes to state,
authorization, or integration contracts, not mere involvement with those
systems. Route, model, and reasoning are separate: map
the final route through the configuration before applying any execution
override.
Use `ultra_low` only when none of `medium`, `high`, or `ultra_high` applies and
no nontrivial local implementation or verification judgment is needed.
Resolve each Step's effective executor pair property-wise from its Step
execution annotation and then the route default; use the route default for an
item without Steps. Parse only the strict native form and never infer an
override from Goal, Decision, or action prose. Validate the effective pair against model and
reasoning combinations currently exposed by the host before dispatch. A
malformed or unsupported effective pair blocks that unit without fallback or
substitution. Keep reviewer and coordinator pairs route-configured. Use the
retained workflow workspace. If any fact is unknown, differs, or changes between
adjacent Steps, stop the bundle before that Step. A changed
applicable Decision, a user-decision boundary, a separately authorized external
effect, materially higher risk, another workspace, another canonical owner, or
an independently resumable result always forces a boundary. Never bundle across
Work Items, skip or reorder Steps, or create a hidden Plan field.

Name the runtime unit with the Work Item and exact Step number or contiguous
range, for example `W-013/steps-1-5`. The Plan remains the sole durable owner;
handoff and Evidence identify completed ranges. One executor owns the whole
bundle. Classify review from the complete resulting change, so a compatible
bundle receives at most one behavior-boundary reviewer unless correction rules
require a follow-up.

After unit formation, preflight, and routing succeed, use the pending-writer
parking and activation sequence above. Build the prompt with the ready task ID
and predicted activation revision, activate and verify that revision, then send
the required initial-execution announcement immediately before sending that
complete assignment.

### Step-bundle scenarios

| Scenario | Dispatch result | Review boundary |
| --- | --- | --- |
| Five adjacent Steps share all seven compatibility facts | One executor for the five-Step range | At most one initial reviewer |
| Adjacent Step changes route or material risk | Split before that Step | Each resulting behavior boundary |
| Adjacent Step changes effective executor model or reasoning | Split before that Step | Reviewer still follows each unit's route class |
| Adjacent Step changes Decision or authorization | Split before that Step | Each resulting behavior boundary |
| Adjacent Step starts a separately authorized external effect | Split before that Step | External-effect result stays isolated |
| Adjacent Step has an independently resumable result | Split before that Step | Independent Acceptance ownership |
| Adjacent Step changes owner or workspace | Split before that Step | Each owner or workspace boundary |
| Work Item has no Steps | One executor for the complete Work Item | One behavior boundary |
