# Scoville Workflow for Codex

**Beta.** Available for real-project testing. Host-level behavior remains under qualification.

A plan needs someone to keep it moving. It does not need that someone to do
every job as well.

Scoville Workflow coordinates a repository-owned Scoville Plan through normal
Codex project tasks. Workers implement, fresh reviewers check material changes,
and one coordinator updates the Plan and commits accepted work. The suite's
specialist Skills keep their own activation rules and responsibilities.

Workflow is available only as part of Scoville Suite, not from a separate
repository. It requires Codex desktop and native task controls. Other suite
Skills have their own host requirements.

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

Code and critical documentation changes require review. Routine changes can
skip it after a bounded consistency check. Findings go to their actual owner,
so a Plan correction does not need a repair worker. Material or unclear
corrections require another review. After three repair workers, unresolved
project findings require your decision instead of a fourth attempt.
The diagram follows completed work. Blockers, failed checks and unresolved
decisions do not count as acceptance. Finished child tasks are archived only
after their results have been retained, with confirmation for the exact task.

The context check happens after an accepted unit, not halfway through work.
Its configurable coordinator threshold defaults to 33 percent. A successor
continues from the repository Plan and a compact handoff. The old coordinator
loses write ownership before the new one takes over. Archival requires separate
host confirmation. If that proof is missing but safe continuation is verified,
the predecessor stays open for later cleanup. Missing context measurements are
not guessed. A stop or completed scope creates no successor.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
In Workflow Codex, that means preserving the Plan's intent and the few facts
needed at a task transition without repeating the Plan or carrying a work log.

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

## Compatibility

Requires Codex desktop, a saved local project, native task creation, waiting,
messaging and archival controls, access to the task's own `CODEX_THREAD_ID`,
and a supported Scoville Plan profile. Python 3.11+ runs the deterministic helpers.
There is no CLI or Claude Code execution path.

Tasks must share the existing checkout. If the host cannot provide that,
Workflow asks for a decision instead of silently creating another workspace.
Measured rollover uses native `token_count` data when available. Missing or
contradictory measurements do not by themselves block valid bounded work.

Native approval can hold a cross-task message pending. Workflow waits without
polling or duplicate delivery. A definite result-delivery failure still leaves
the child's validated final result available to the coordinator's recovery path.

## Routing

The coordinator classifies each fresh dispatch unit and maps its effective route
to one executor pair. The reviewer pair is used only when the material-change
review gate requires review.

| Route | Typical task | Executor | Reviewer |
| --- | --- | --- | --- |
| `coordinator` | Workflow coordination | `gpt-5.6-sol` / `medium` | Not applicable |
| `ultra_low` | Simple bounded local change with trivial verification | `gpt-5.6-luna` / `medium` | `gpt-5.6-terra` / `medium` |
| `low` | Nontrivial local judgment with one known owner, understood helpers, and established checks | `gpt-5.6-terra` / `medium` | `gpt-5.6-sol` / `medium` |
| `medium` | Unresolved helpers, diagnostic discovery, interacting owners, harness boundaries, or interpreted checks | `gpt-5.6-sol` / `medium` | `gpt-5.6-sol` / `high` |
| `high` | Consequential changes to state, authorization, or integration contracts | `gpt-5.6-sol` / `high` | `gpt-6-astra` / `low` |
| `ultra_high` | Unusually consequential or complex work beyond `high` | `gpt-6-astra` / `low` | `gpt-6-astra` / `medium` |

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

## Install

### Install this Skill

The repository is private. In an authenticated local Codex session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-suite/tree/main/packages/scoville-workflow-for-codex/scoville-workflow-for-codex
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether Codex discovers the Skill.
As the final installation check, create one no-tool normal project task and verify that its approval policy, access to the project root, and network access match this calling task. Archive the probe. If they differ, do not mark the Skill ready; report the exact mismatch and ask whether to apply the needed Codex configuration change.
```

The agent needs authenticated source access and permission to write to the
personal Skills location. The installable package is the nested
`scoville-workflow-for-codex/` directory, not the repository root. Manual fallback:
[Codex Skills guide](https://learn.chatgpt.com/docs/build-skills).

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

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

The canonical Plan owns progress. Workflow does not add a persistent Codex goal
or another continuation loop alongside its coordinator.

For delivery recovery, permission boundaries and failure handling, see
[Native Codex operations](scoville-workflow-for-codex/references/operations.md).

## How it works

The launcher starts one coordinator in the existing checkout. The coordinator
selects a Plan unit, chooses its configured model and sends a helper-built prompt
to one worker. The prompt contains the selected work and referenced Decisions,
not the entire project history.

The dispatch helper keeps the payload separate from its compact delivery receipt.
An unchanged payload is reused. An uncertain delivery is recovered through its
identity and recorded state, not sent again on the assumption that nothing happened.

Instructions follow the same principle. A small required core routes to twelve
phase references. The coordinator loads the rules needed now and reuses them
while their complete, unchanged contents remain available. After context loss,
it reloads the current rules. Remembering that a file was read is not remembering
what it said.

Completed results are validated before review, acceptance or archival. Accepted
work and its accumulated Plan state enter one unit commit. The coordinator then
selects the next eligible unit within the requested scope.

Messages announce real transitions, findings and decisions. Unchanged waits stay
silent. The exact recovery and ownership rules live in
[Native Codex operations](scoville-workflow-for-codex/references/operations.md).

## How it was developed

Workflow grew out of a CLI-based Scoville workflow whose communication and
supervision added work of their own. The native version kept Plan ownership,
routing, review and rollover, while moving execution into ordinary Codex tasks.

Later task-history audits exposed repeated dispatch text and unnecessary full
rule reads. Dispatch now separates the payload from its receipt, and the
operations contract loads by phase. Contract tests and focused model cases
check those paths. They do not settle the host-level limits listed below.

The current source belongs to Scoville Suite. Common helpers are built into the
package, so an installation does not depend on the development workspace.

## Status

The source contract and focused tests pass. Two host-level qualifications remain
open: automatic compaction immediately after a terminal handoff, and event-driven
coordinator dormancy beyond the 120-second native wait ceiling. Until those
traces pass, the repository does not claim either host behavior as observed end
to end. Workflow is now maintained in the suite. The earlier standalone
version history does not constitute a suite release.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web, GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns engineering scope, implementation, risk, and validation.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns visual definition, art direction, design systems, critique, and repair.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns framework-aligned implementation, interface mechanics, accessibility, and rendered evidence, with a standalone design fallback.
- [WordPress UI Backend](https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop) owns plugin-owned WordPress admin interfaces, platform components, spacing, accessibility and internationalization.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans, Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active work to another agent or session.
- [Workflow Codex](https://github.com/benjaminstelzer/scoville-suite) coordinates explicit Plan execution through native Codex project tasks.

## Sources

- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package and progressive disclosure model.
- [OpenAI coding-agent best practices](https://developers.openai.com/codex/learn/best-practices)
  for explicit outcomes, constraints, planning, and completion evidence.

## Development

Maintained in the suite. Individual repositories contain generated packages.

[Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-workflow-for-codex) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-workflow-for-codex/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-workflow-for-codex/development/README.md)

## License

MIT. See [LICENSE](LICENSE).

