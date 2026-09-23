# Selection phase

Form the selected unit using [dispatch](operations-dispatch.md). Create/activate and transport it using [activation](operations-activation.md).

## Select bounded Plan context

After Scoville Plan resolves the canonical `plan_root`, derive
`<plan-skill-directory>/scripts/select_context.py` from the exact loaded
Scoville Plan Skill. Require that helper and an already available Python 3
interpreter. For coordinator recovery and unit formation, select
the current item or one explicitly selected item with:

```text
python <plan-skill-directory>/scripts/select_context.py --root <plan_root> [--work-item W-001] --format json
```

When coordinator preflight also requires project-contract and guard checks, use
one bundled call:

```text
python <workflow-skill-directory>/scripts/inspect_dispatch_preflight.py --workspace <workspace_root> --plan-root <plan_root> --selector <plan-skill-directory>/scripts/select_context.py --workflow-id <workflow_id> --expected-revision <revision> --expected-generation <generation> [--work-item W-001]
```

It checks the installed project contract, verifies coordinator Plan capability,
returns the same four selected semantic areas under `selection`, then verifies
the unchanged guard revision. Accept only
`valid:true`; on failure, stop this preflight and use its diagnostic. It does
not perform structural Plan validation or authorize dispatch. Run the complete
Plan validator separately when a Plan write requires it.

Accept only exit `0` with exactly these four top-level semantic areas:

1. `plan`: exact Plan frontmatter plus Goal and Non-goals;
2. `work_item`: the complete selected Work Item block;
3. `direct_dependencies`: each direct dependency ID and only its `Status`
   line;
4. `decisions`: the complete Decisions referenced by that Work Item.

The coordinator uses that complete Work Item selection to form the next exact
unit. It never embeds this recovery object in a child prompt. After unit
formation, the Workflow prompt helper internally invokes:

```text
python <plan-skill-directory>/scripts/select_context.py --root <plan_root> --unit <exact-unit> --format json
```

A Work Item without Steps uses unit `W-NNN`. A Work Item with Steps requires
`W-NNN/step-N` or the exact authorized adjacent range `W-NNN/steps-N-M`. The
range form is valid only when `M > N`, so it contains at least two Steps in
forward order. Reject a same-number or reversed range before dispatch. The
unit projection retains exact Plan frontmatter, Goal, Non-goals, Work Item
identity and live control fields, Outcome, Acceptance, only the selected Step
text, direct-dependency status lines, and every Work Item-referenced Decision.
It contains no Work Item Evidence, unselected Step, or Work Item-wide `Next
action`; the selected Step is the executable action. A whole-item unit without
Steps retains `Next action`. The coordinator never filters Decisions; correct
an irrelevant Decision link only while its Work Item is mutable.

### Dispatch-unit identifier scenarios

| State | Result |
| --- | --- |
| `W-001` | Valid Step-less Work Item unit |
| `W-001/step-2` | Valid single-Step unit |
| `W-001/steps-2-3` | Valid forward range containing at least two Steps |
| `W-001/steps-2-2` | Reject before dispatch |
| `W-001/steps-3-2` | Reject before dispatch |

Invoke the prompt builder with the exact loaded helper paths and workflow
workspace:

```text
python <workflow-skill-directory>/scripts/build_dispatch_prompt.py --selector <plan-skill-directory>/scripts/select_context.py --plan-root <plan_root> --unit <exact-unit> --role <executor|reviewer|repair> --workspace-root <workspace_root> --return-to-thread-id <coordinator_self_id> --delivery-reference <unique-reference> --guard-workflow-id <workflow_id> --guard-generation <generation> --guard-revision <revision> --guard-dispatch-key <dispatch-key> [--guard-task-id <activated-writer-threadId>]
```

Supply the role-input object on stdin when required. Accept only exit `0`.
Send the retained reviewer prompt unchanged at creation. For executor and repair, build it
while the reconciled parking task is still pending, using the predicted next
guard revision, then send it unchanged only after activation returns that exact
revision. Require `--guard-task-id`; omit that argument for reviewers.
Build once per new dispatch after its last Plan write. Before sending, use
`--binding-only` with the same current inputs to detect changed Plan/Decision,
role-input, helper, target or guard bindings without generating another prompt. A helper or selector diagnostic becomes one
coordinator-owned blocker without a hand-built prompt or raw-file fallback.

Never append proposal inventory, Work Item or dependency Evidence, graph state, queued or
paused-return state, unrelated Work Items, unreferenced Decisions, or a complete
Plan body to this projection. Never truncate it and never use a raw-file
fallback. A missing helper or Python runtime, nonzero exit, malformed JSON,
unexpected field, malformed boundary, ambiguous record, or output-budget
diagnostic becomes one coordinator-owned Plan blocker containing the structured
diagnostic. Do not dump the source or infer the missing facts.

Keep other native semantics as separate bounded reads:

- inventory Decision frontmatter and load every `proposed` Decision;
- read a direct dependency's complete block only when its Evidence changes the
  selected item's preflight;
- extract ordered Work Item headings plus title, `Status`, `Depends on`,
  `Blocked by`, and `Decisions` lines when eligibility, authored queue order,
  or an exact successor must be resolved;
- read the complete current and named paused-return blocks when recovery requires
  their mutable state; and
- run complete structural validation separately when a Plan write requires it.

These reads may inspect their canonical files internally but return only the
named semantic slice to coordinator context. They never widen selector output,
reuse an old selection after a Plan write, or treat a bounded graph view as
validation.

### Plan context scenarios

| State | Coordinator input | Required result |
| --- | --- | --- |
| Coordinator current or named Work Item | Selector success | Exactly the four semantic areas for unit formation |
| Work Item without Steps | Prompt-helper success for `W-NNN` | Whole-item unit fields all referenced Decisions and no Evidence |
| Work Item with Steps | Prompt-helper success for exact Step or adjacent range | Only selected Step text all referenced Decisions and no Evidence |
| Reviewer or repair | Prompt-helper success plus validated role input | Same exact unit plus only the required prior result object |
| Unrelated proposed Decision | Separate Decision-frontmatter inventory | Load and surface that proposal separately |
| Relevant dependency Evidence | Separate complete dependency block | Use only for that preflight |
| Queued successor | Separate bounded graph and title view | Resolve authored order without Work Item bodies |
| Paused return target | Separate complete named blocks | Preserve the recorded return state |
| One-MiB Plan with small selected item | Selector success | Same selected facts without unrelated bodies |
| Missing helper malformed boundary or budget overflow | Structured selector diagnostic or invocation diagnostic | Record one blocker with no raw fallback |
