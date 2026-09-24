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

### Configuration

Configure model pairs in this Skill's `assets/workflow.toml`:
`[coordinator]`, `[execute.CLASS]` and `[review.CLASS]` own the respective
assignments. `[context]` sets coordinator and worker rollover thresholds.
Route classification, Step overrides and repair escalation follow the
[dispatch rules](scoville-workflow-for-codex/references/operations-dispatch.md).
Writing depth does not lower a task's route or rewrite a Plan point.

### Writing depth

Configure additional instruction depth in `[prompting]` inside this Skill's
`assets/workflow.toml`. `profile` accepts `auto`, `low`, `medium` or `high`.
Explicit user depth takes precedence for its stated recipients. Auto uses the
actual recipient model; unknown IDs use medium. Edit exact model assignments
locally. Plan's configuration is independent. Canonical Plan points are passed
unchanged at every depth. The helper requires Python 3.11+.
