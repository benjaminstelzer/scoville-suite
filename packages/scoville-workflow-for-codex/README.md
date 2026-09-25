# Scoville Workflow for Codex

A long software task can leave one agent planning, coding, reviewing its own
changes and remembering every earlier decision. Context grows while unfinished
work becomes harder to track.

Scoville Workflow supports structured, AI-assisted software development and
long-term project maintenance, including larger codebases. It is not intended
for fast vibe coding or throwaway prototyping. Plan preserves direction and
decisions, Code requires maintainable changes and meaningful checks, and Workflow
coordinates workers, fresh reviewers and continuation. Together they help keep
project development recoverable without making one conversation carry its history.

**Beta.** Available for real-project testing. Host-level behavior remains under qualification.

Workflow is suite-only and requires Codex desktop with native task controls.
Other suite Skills should work with many Agent Skills-compatible hosts, subject
to their requirements. Testing has been limited to Codex, Claude Code and Antigravity.

## How it works

- The coordinator selects a bounded Plan unit and routes its model and reasoning effort by risk. Workers implement in the existing checkout.
- Fresh reviewers check code and critical documentation changes. Routine changes can skip review after a bounded consistency check.
- The coordinator corrects Plan findings. Repair workers correct project findings, with further review when changes are material or unclear.
- Accepted work and Plan updates enter one commit. Failed checks and open decisions do not count as acceptance.
- At an accepted boundary with more work remaining, the coordinator hands over at or above 33% context use. Workers, reviewers and repairs hand over above 66% at natural stopping points.
- Both thresholds are configurable and measure current context, not total tokens spent. Missing or stale measurements are not guessed.
- A successor retains the assignment and checkout. A context handoff is not another repair attempt. Results are saved before exact-task archival is confirmed.

```mermaid
flowchart TD
    P["Repository Plan"] --> C["Coordinator selects a bounded unit<br/>and routes model and effort"]
    C --> W["Worker implements and validates"]
    W --> G{"Review required?"}
    G -->|Yes| R["Fresh reviewer checks the result"]
    G -->|No| A["Coordinator records acceptance,<br/>updates the Plan and commits"]
    R -->|Pass| A
    R -->|Findings| F["Coordinator fixes Plan findings<br/>Fresh repair worker fixes project findings"]
    F --> Q{"Follow-up review required?"}
    Q -->|Yes| R
    Q -->|No| A
    A --> N{"Requested work remains?"}
    N -->|No| D["Finish"]
    N -->|Yes| T{"Context threshold reached?"}
    T -->|No| C
    T -->|Yes| H["Validate and activate successor coordinator<br/>Transfer ownership and verify predecessor archival"]
    H --> C
```

## What it enforces

- **Explicit activation.** Asking for implementation or delegation alone does not start Workflow.
- **Separate responsibilities.** The coordinator owns Plan updates, dispatch and accepted commits. Workers implement. Reviewers stay read-only.
- **One live checkout.** Tasks use the existing working state. Workflow does not create an isolated worktree without an explicit choice.
- **Cooperative write ownership.** A project guard grants one worker a bounded unit. Invalid state stops writes. This coordinates agents, not a filesystem lock against external tools.
- **Complete but bounded context.** Dispatch includes the selected Plan unit and its Decisions without truncation. Workers do not reconstruct it from a summary or reopen the Plan.
- **Configured routing.** Risk selects the model and effort. Unsupported required pairs block rather than silently falling back.
- **Independent review where needed.** Code and critical documentation changes require a fresh reviewer. Unresolved worker findings allow at most three repair workers before user input is required.
- **Measured rollover.** By default, the coordinator hands over at or above 33 percent after an accepted unit. Child roles hand over strictly above 66 percent at a natural boundary. Missing or stale measurements are not guessed. Both thresholds are configurable.
- **Verified cleanup.** Results are retained before children are archived. A rollover successor takes ownership before archiving its predecessor, whose turn must have ended. Exact task IDs matter, not titles or list visibility alone.
- **Accepted work before commit.** One unit commit includes its accepted changes and complete accumulated Plan state. Failed hooks and outstanding backup requirements are not bypassed.
- **A binding scope.** Without a narrower boundary, continue through the active Plan. Preserve explicit stops and decisions. Archiving a task is not cancelling it.

- The canonical Plan owns progress. Workflow does not add a persistent Codex goal or another continuation loop alongside its coordinator.

- For delivery recovery, permission boundaries and failure handling, see [Native Codex operations](https://github.com/benjaminstelzer/scoville-suite-for-codex/blob/main/packages/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md).

## What it costs

- Separate worker and reviewer tasks, context handoffs and Plan updates use additional tokens and time.

## How it was developed

- Workflow grew out of a CLI-based Scoville workflow whose communication and supervision added work of their own.
- The native version kept Plan ownership, routing, review and rollover, while moving execution into ordinary Codex tasks.
- Real-project histories are analyzed alongside results to identify failures and unnecessary context use.
- Targeted simulation and optimization workflows inform revisions. Changes are retained only when the required behavior survives.

- Beta testing still needs to cover automatic context compaction immediately after handoff and waiting beyond the host's maximum wait duration.

## Compatibility

Requires Codex desktop, a saved local project, native task creation, waiting,
messaging and archival controls, access to the task's own `CODEX_THREAD_ID`,
and Scoville Plan v1.8.0 or a compatible source_text selector. Python 3.11+ runs the deterministic helpers.
There is no CLI or Claude Code execution path.

Tasks must share the existing checkout. If the host cannot provide that,
Workflow asks for a decision instead of silently creating another workspace.
Measured rollover uses native `token_count` data when available. Missing or
contradictory measurements do not by themselves block valid bounded work.

Native approval can hold a cross-task message pending. Workflow waits without
polling or duplicate delivery. A definite result-delivery failure still leaves
the child's validated final result available to the coordinator's recovery path.

This package requires every Skill included in this suite to be installed and
enabled. Partial installation is not supported. Skills keep their own task
scope and invocation rules; Workflow still requires an explicit request.

## Install

Install and enable the complete
[Scoville Suite for Codex](https://github.com/benjaminstelzer/scoville-suite-for-codex/tree/main/packages).
Workflow is suite-only. Every Skill must come from this repository's own
`packages/<name>/<name>/` directory. Do not substitute individual-repository
packages or continue with missing members. The suite requires Codex and
Python 3.11 or newer; preserve personal configuration when updating.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite-for-codex).
Install its released Skill packages, not development templates.

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

## Sources

- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package and progressive disclosure model.
- [OpenAI coding-agent best practices](https://developers.openai.com/codex/learn/best-practices)
  for explicit outcomes, constraints, planning, and completion evidence.

## License

MIT. See [LICENSE](LICENSE).

