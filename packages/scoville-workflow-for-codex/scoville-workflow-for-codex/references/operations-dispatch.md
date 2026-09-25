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
authorization from the requested effects. Apply Route and model selection below
before comparing compatibility tuples. Keep classification transient; do not
copy it into Plan points or child prompts.

Parse each Step's execution annotation property-wise and pass only its specified
model or reasoning values as helper overrides; an item without Steps has none.
Parse only the strict native form and never infer an
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

## Route and model selection

Use the Plan hierarchy. A Work Item without Steps is one dispatch unit. A Step
is the default unit; adjacent Steps may share one unit only through the guarded
compatibility procedure in [operations.md](operations.md). Never
invent subdivisions, combine Work Items, or split activities that share one
behavior and Acceptance boundary.

For every fresh execution unit, classify the complete execution and verification
scope from actual consequence and reasoning demand, not file or activity count.
Check the classes from `ultra_high` down to `ultra_low` and choose the highest
class whose criteria apply. If a Step begins with `[route: CLASS]`, treat that
class as the planned minimum: raise the effective dispatch route when the
annotation was too low or incomplete, even when no fact changed after planning,
and never dispatch below it. Do not reclassify a repair or context-rollover
continuation. New repair attempts follow the WORK-row escalation in
[review](operations-review.md); context-rollover successors retain
their own launched pair.

- `ultra_low`: simple bounded local change with trivial verification.
- `low`: nontrivial local implementation judgment or verification, with one
  known behavior owner, understood helper contracts, established verification
  commands, and no diagnosis across component or test-harness boundaries.
- `medium`: an unresolved helper contract or required local diagnostic
  discovery, interacting behavior owners, helper or mock availability across a
  harness boundary, integration diagnosis, or broader checks whose results
  require interpretation.
- `high`: consequential changes to state, authorization, or integration
  contracts, rather than mere involvement with those systems.
- `ultra_high`: unusually consequential or complex work beyond `high`.

`low` is allowed only when every low criterion is positively established from
the selected Plan context and bounded preflight. The targets and single behavior
owner must already be known; helper, mock, harness, and generator contracts must
be understood; verification commands and expected results must be exact and
mechanical; and execution must require no search, inventory, diagnosis, or result
interpretation across files, components, languages, runtimes, or harnesses. If
any one of these facts is false or unknown, use at least `medium`.

Use at least `medium` when execution must locate or classify affected targets,
decide ownership among duplicated or mirrored definitions, preserve a contract
across languages or components, discover how helpers or tests work, coordinate
generated artifacts with their source, or interpret broad validation results.
A simple verb such as add, rename, comment, document, or test is not evidence for
`low`; classify the mechanism and verification needed to complete it.

Use `ultra_low` only when none of `medium`, `high`, or `ultra_high` applies and
the work needs no nontrivial local implementation or verification judgment.

Many files, generated metadata, or a known large test suite alone do not raise
the route. Route class, model, and reasoning level are separate decisions; a
model's `medium` reasoning setting does not make a `low` route equivalent to a
`medium` route. Resolve the final class through the operations-owned
`scripts/resolve_model_pair.py`, which reads [workflow.toml](../assets/workflow.toml).
Resolve the executor model and reasoning independently: the selected Step's strict
`[execute: ...]` annotation overrides the matching route-default property.
An explicitly chosen pair for a still-`todo` Work Item without Steps must be
retained by adding one behavior-complete annotated Step; do not add a field.
Validate the resulting pair against current host support and block the unit
rather than substitute when either property or their combination is
unavailable. This override changes neither route risk nor review requirements.
When the operations contract requires review, use the configured reviewer pair
for the same class; point overrides never affect coordinator or reviewer
routing. Do not probe unused models.
