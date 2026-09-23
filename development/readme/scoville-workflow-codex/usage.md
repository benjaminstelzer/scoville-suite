## How to use

Activate the workflow explicitly:

```text
Use $scoville-workflow-for-codex to execute the active Scoville Plan in this saved project.
```

Name a Work Item or end boundary to limit the run. Without one, the coordinator
continues through the active Plan.

The first activation may ask to install or update the managed project
`AGENTS.md` block. After that decision, activate again to start the coordinator.
The launcher ends once it has handed over. It does not become a second supervisor.

`$scw` is recognized after loading the Skill, but native short-name discovery
is not yet verified. Use the full name for installation checks.
`scoflow codex` is also accepted. Ordinary requests such as “implement the plan”
or “use workers” do not activate Workflow.

Task titles identify the work and role:

```text
SCW PLAN-0001 W-001/step-1 WORK RUN [#1]
SCW PLAN-0001 W-001/step-1 REVIEW RUN [#1]
SCW PLAN-0001 W-001/step-1 REPAIR RUN [#2]
```

### Routing

The coordinator classifies each fresh dispatch unit and maps its effective route
to one executor pair. The reviewer pair is used only when the material-change
review gate requires review.

| Route | Typical task | Executor | Reviewer |
| --- | --- | --- | --- |
| `coordinator` | Workflow coordination | `gpt-6-sol` / `medium` | Not applicable |
| `ultra_low` | Simple bounded local change with trivial verification | `gpt-6-sol` / `low` | `gpt-6-sol` / `medium` |
| `low` | Nontrivial local judgment with one known owner, understood helpers, and established checks | `gpt-6-sol` / `medium` | `gpt-6-sol` / `high` |
| `medium` | Unresolved helpers, diagnostic discovery, interacting owners, harness boundaries, or interpreted checks | `gpt-6-sol` / `high` | `gpt-6-sol` / `xhigh` |
| `high` | Consequential changes to state, authorization, or integration contracts | `gpt-6-astra` / `low` | `gpt-6-astra` / `medium` |
| `ultra_high` | Unusually consequential or complex work beyond `high` | `gpt-6-astra` / `medium` | `gpt-6-astra` / `high` |

`low` is fail closed. The coordinator must positively know the target, single
owner, helper contracts, and exact mechanical checks, with no required discovery,
cross-language or component contract work, harness uncertainty, or interpreted
validation. One false or unknown fact raises the unit to at least `medium`.

Change these assignments in
[`scoville-workflow-for-codex/assets/workflow.toml`](scoville-workflow-for-codex/assets/workflow.toml).
The `[coordinator]`, `[execute.CLASS]`, and `[review.CLASS]` sections own model
assignments. `[context]` sets coordinator and worker rollover thresholds.
The file also contains the coordinator title. Other protocol limits remain in
the operations contract. Update this table when the published defaults change.

A Step's `[route: CLASS]` is its planned minimum. For every fresh execution
unit, the coordinator chooses the highest applicable class and raises the
effective dispatch route above an insufficient annotation, even when the task
has not changed since planning. It never dispatches below the retained
annotation. Repairs and context rollover retain their launched pair. Many files or a large known test suite alone do
not raise the class. Route, model, and reasoning are separate values; the final
route selects the configured pair before a Step-level execution override is
applied.
