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
