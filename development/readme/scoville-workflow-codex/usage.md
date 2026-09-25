## How to use

Activate the workflow explicitly:

```text
Use $scoville-workflow-for-codex to execute the active Scoville Plan in this saved project.
```

Name a Work Item or end boundary to limit the run. Without one, the coordinator
continues through the active Plan.

The calling task coordinates the run directly. A project `AGENTS.md` addition is
optional setup on explicit request. It is not a prerequisite for execution.

`$scw` is recognized after loading the Skill, but native short-name discovery
is not yet verified. Use the full name for installation checks.
`scoflow codex` is also accepted. Ordinary requests such as “implement the plan”
or “use workers” do not activate Workflow.

Task titles identify the work and role:

```text
S-MNGR-#2-PLAN-0011
S-WORK-#3-W-010/STEP-2
S-REVW-#2-W-010/STEP-2
S-FIXR-#1-W-010/STEP-2
```

The number counts tasks separately for each role within the workflow run. A new
successor gets the next number; continuing the same task keeps its number.
The manager shows the Plan ID. Workers, reviewers and repair workers show their
assigned unit without its title. A whole Work Item has no Step suffix. Uppercase
affects display only. Rollover keeps the same logical workflow run even
though the successor's displayed number increases.

### Configuration

Save settings under `workflow` in the project's `.scoville/config.json`.
`execute.CLASS` and `review.CLASS` contain model/reasoning pairs. `context`
sets coordinator and worker rollover thresholds. Missing values come from
this Skill's imported `assets/workflow.toml`. Reading or starting creates no
configuration file. One run uses one workspace. Change settings between runs,
and do not edit the same project files in parallel while a run is working.
Concurrent edits have no automatic conflict-recovery guarantee.
Route classification, Step overrides and repair escalation follow the
[dispatch rules](scoville-workflow-for-codex/references/operations-dispatch.md).
Use Scoville Setup to display these settings or save explicit changes. It is
part of the suite and does not start workflows. Default rollover thresholds
are 25 percent for the coordinator and 75 percent for child roles. The
coordinator hands over at or above its threshold, child roles strictly above
it. The run cursor is ordinary Markdown in `.scoville/workflow.md`.
