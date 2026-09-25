# Direct dispatch

One selected Step is one unit. A Work Item without Steps is one unit. Preserve
these existing route values and treat an explicit `[route: CLASS]` annotation
as a minimum:

- `ultra_low`: bounded local change with trivial verification.
- `low`: nontrivial local work with one known owner, understood helpers and
  established mechanical checks, without component or test-harness diagnosis.
- `medium`: unresolved helper contracts, ownership discovery, interacting
  owners, integration diagnosis or checks requiring interpretation.
- `high`: consequential changes to state, authorization or integration contracts.
- `ultra_high`: consequence or complexity beyond high.

Choose the highest applicable class. Unknown low-eligibility facts mean at least
medium. File count, generated files and test volume alone do not raise a route.
Keep canonical source unchanged and do not write inferred routes into the Plan.

Resolve the executor/reviewer pair using the selected project root:

```text
python "<workflow-skill-directory>/scripts/resolve_model_pair.py" --project-root "<workspace_root>" --role executor --route <class>
```

Use `--role reviewer` for review. Pass only properties explicitly specified by
the Step annotation as executor `--override-model` / `--override-reasoning`.
For repair use `--role repair --original-model <model> --original-reasoning
<effort> --repair-number <1|2|3>`. Record the actually launched original pair.
An absent pair in the current route table blocks escalation with its diagnostic;
do not invent the cause or build an immutable repair schedule.
Reasoning syntax accepts `none`, `minimal`, `low`, `medium`, `high`, `xhigh`,
`max` and `ultra`. Shipped pairs and Setup use `low` through `xhigh`; additional
levels may be entered manually in the project configuration.
Validate required pairs against the current host's exposed model capabilities.
No silent substitution or probing of unused models is needed.

Build the full child assignment once:

```text
python "<workflow-skill-directory>/scripts/build_dispatch_prompt.py" --selector "<plan-skill-directory>/scripts/select_context.py" --plan-root "<project-root>" --unit <unit> --role <executor|reviewer|repair> --workspace-root "<workspace_root>" --return-to-thread-id <coordinator-id> --delivery-reference <reference>
```

Optional stdin is one object. A reviewer requires `executor_result`, the parsed
completed executor or repair result. A repair
requires `reviewer_result` plus `repair_assignment.finding_indices`, the sorted
unique indices of source-owned unresolved findings. Continuations add factual
`context_handoff`; necessary extra facts use `supplemental_context`. These are
separate from the unchanged selected Plan source. Do not truncate required
Decisions or replace source_text with a summary.

Pass the resulting prompt directly through the bundled
[task helper](../scripts/task_lifecycle.md) `create` operation, with
`family:workflow`, role, exact selected `unit`,
next role counter as `run_number`, project ID, model, thinking and unique
plain-text reference. Coordinator creation uses the canonical `plan_id`
instead of unit and its next coordinator counter. The helper returns
normal `create_thread` arguments. Save its handle before making that host call,
then retain the observed creation result. Native roles use normal project tasks,
not forks or a shared-history subagent. No separate parking task is created.

A ready task needs its actual `threadId` and `hostId`; `clientThreadId` alone is
not ready. Use host correlation or an exact task read containing the request's
workflow reference to resolve pending creation. Titles alone do not identify a
task. If creation remains ambiguous, stop before another creation attempt.
No byte, hash or delivery receipt is required.

The receiver owns only the assigned project changes. It cannot edit canonical
Plan records, stage/commit, create successors or change configuration. Its final
answer uses the existing `SCOVILLE_RESULT_V1` contract supplied by the builder.
The coordinator obtains it from the exact task, not a second delivery message.
