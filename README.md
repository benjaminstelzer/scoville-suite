# Scoville Suite

Scoville helps your agent plan work, write code, improve interfaces and carry
unfinished tasks into the next conversation. Along the way, the Skills keep
the goal, the project's conventions and the verified results in view.

Scoville is the scale for chili heat. These Skills aim for sharper work and
less diluted context. Adding more instructions is easy. Keeping the useful
ones is the point.

Using Claude Code or another Agent Skills host? Take
[Scoville Suite](https://github.com/benjaminstelzer/scoville-suite).
On Codex desktop, take
[Scoville Suite for Codex](https://github.com/benjaminstelzer/scoville-suite-for-codex),
which adds Workflow, Ask and Setup.

| Skill | Purpose |
| --- | --- |
| [Code](#scoville-code) | Keeps implementation, risk assessment and checks focused on what you asked for. |
| [Plan](#scoville-plan) | Keeps longer work, decisions and progress easy to pick up again. |
| [UI](#scoville-ui) | Builds and checks interfaces with their framework and design system. |
| [Handoff](#scoville-handoff) | Passes unfinished work to another session. |
| [Project Context Cleanup](#scoville-project-context-cleanup) | Keeps requested project rules and index text clear without losing required context. |

## Scoville Code

Passing tests are useful. Passing tests for the wrong behavior, rather less so.
Scoville Code keeps implementation, debugging and review tied to the result you
asked for: find the cause, work with the existing architecture and check what
actually changed.

Scoville measures chili heat. Code aims for sharper reasoning before a small
fix acquires its own framework.

### How it works

- Establish the requested result and find the code responsible for it.
- Fix the cause within the project's architecture and your authorized scope.
- Check the affected behavior and relevant performance costs.
- Reassess failed fixes, report remaining limits and stop when further checks
  would no longer change the decision.

### What it enforces

- **Work that serves the request.** Refactors, safeguards and tests need a
  concrete purpose. The agent asks about material choices and settles routine
  details from the project.
- **Your conventions.** Existing architecture and project rules take precedence.
  New projects start with a small structure organized by responsibility.
- **Evidence that fits the change.** Check the behavior, preserve guarantees and
  distinguish observed results from what remains unverified.

Keep personal conventions outside the installed Skill so updates preserve them.
See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
and [full instructions](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md).

### What it costs

- Reading relevant code and checking behavior takes tokens and time. The extra work is aimed at avoiding fixes that merely look finished.

[How to use Scoville Code](members/scoville-code/README.md#how-to-use).

## Scoville Plan

Scoville Plan keeps goals, decisions and progress in the repository so longer
work survives the next conversation. You can see what is done, what remains
and why a choice was made without reconstructing it from chat history.

Use it for work with dependencies or several sessions. Settle the requirements
and acceptance criteria before implementation, get independent advice where
useful, and revise the Plan when the facts change. A contained fix can stay small.

Scoville measures chili heat. Plan keeps the direction from being diluted by
one more perfectly reasonable detour.

[Plan Viewer](https://github.com/benjaminstelzer/scoville-plan/releases/latest)
shows these records on Windows, macOS and Linux.

### How it works

- Use the repository's existing planning system and relevant Plan, Work Items and Decisions.
- Check current sources before starting the next item.
- Edit Markdown and YAML records with observed Step progress and any additional Instructions.
- Record evidence before completion, preserve accepted history and validate the records.

### What it enforces

- **Resumable work.** Goals, ordered Steps, dependencies and the current position
  stay explicit in the project's records.
- **Decisions with an owner.** Confirmed choices are recorded. Open questions
  remain proposals and block only the work that depends on them.
- **Evidence before completion.** Finished means acceptance was checked.
  Changes of direction preserve completed work and relevant history.

Edit records from one session at a time. Concurrent edits need reconciliation.
See the [full instructions](https://github.com/benjaminstelzer/scoville-plan/blob/main/scoville-plan/SKILL.md).

### What it costs

- Maintaining records takes tokens and time. It pays for continuity on dependent work. A small fix rarely needs a large Plan.

[How to use Scoville Plan](members/scoville-plan/README.md#how-to-use).

## Scoville UI

Scoville UI builds and audits interfaces with the project's framework and
design system. It covers clear wording, useful hierarchy, responsive layouts
and accessible interactions, then checks the rendered result. A tidy component
tree is a start. People still have to use the page.

It includes specific guidance for plugin-owned WordPress admin pages, using
Core components and WordPress conventions.

Scoville measures chili heat. UI aims for a sharper interface without making
the user sweat.

### How it works

- Establish the user's task, approved design direction and framework components.
- Build the affected views, wording, states and responsive behavior.
- Inspect the rendered interface and try its relevant interactions.
- Apply the WordPress adapter to supported plugin-owned admin pages. Editor
  surfaces and metaboxes keep their host's conventions.

### What it enforces

- **A coherent interface.** Hierarchy, controls and terminology follow the task
  and the existing design system.
- **Usable states.** Loading, empty, error and success states receive the same
  attention as the convenient example with perfect data.
- **Access across devices.** Check responsive layout, zoom, reading order,
  contrast, focus and keyboard or touch operation where applicable.
- **Rendered proof.** Source checks alone cannot establish that the interface
  works. Unchecked rendering or interaction stays explicitly unverified.

See the [full instructions](https://github.com/benjaminstelzer/scoville-ui/blob/main/scoville-ui/SKILL.md).

### What it costs

- Rendered inspection and interaction checks take tokens and time. They catch problems the source alone cannot show. WordPress tasks also load platform guidance.

[How to use Scoville UI](members/scoville-ui/README.md#how-to-use).

## Scoville Handoff

Scoville Handoff turns the current task into one copy-ready continuation
prompt: the goal, decisions, unfinished work, blockers and next action.
Another session can pick up the work without asking you to explain it all again.

Scoville measures chili heat. Handoff keeps the useful context from being
diluted between conversations. The next agent already has enough imagination.

### How it works

- Read the conversation and the task sources already named or established.
- Capture the facts needed to resume, including permissions and unfinished work.
- Produce one prompt in the requested language, otherwise the conversation
  language. The receiving agent checks current state before acting.

### What it enforces

- **Explicit transfer.** A handoff starts when you request one. Preparing it is
  read-only and does not advance the task.
- **Faithful context.** Decisions, permissions, ownership and blockers survive
  the transfer. Unknown results stay unknown, and secrets stay out.
- **A useful next action.** The prompt tells the next session where to resume
  and how to recognize completion.

A targeted GPT-6 Luna High test turned a preference into a requirement. Check
that distinction in a generated handoff. Later testing has not disproved the
observation.

See the [full instructions](https://github.com/benjaminstelzer/scoville-handoff/blob/main/scoville-handoff/SKILL.md).

### What it costs

- Preparing the prompt takes tokens and time once, so the next session has less context to reconstruct.

[How to use Scoville Handoff](members/scoville-handoff/README.md#how-to-use).

## Scoville Project Context Cleanup

Project rules grow. Unfortunately, clarity does not grow automatically with
them. This Skill adds or revises the rules you request in
`AGENTS.md` or `CLAUDE.md` and
context in `PROJECT_INDEX.md`, keeping useful information where the next agent
will find it.

It preserves meaning, scope and safeguards. Suitable text stays as it is.

Scoville measures chili heat. Context Cleanup removes the dilution, not the
ingredients that made the rules useful.

### How it works

- Resolve the target file and read its relevant governing rules.
- Check the addition for useful project information, duplicates and conflicts.
- Place concise wording in the affected structure, with conditions and exceptions together.
- Inspect the saved change and use the record owner's checks where required.

### What it enforces

- Requested additions and cleanup stay within the named project-context files.
- Scope, conditions, permissions, safeguards and necessary reasons survive edits.
- Existing formats and record owners remain responsible for fields and lifecycle.
- Suitable text stays unchanged, and unresolved material choices are asked directly.

### What it costs

- Reading the rules and checking edits takes tokens and time. The useful return is clearer context for later work, without deleting necessary detail.

[How to use Scoville Project Context Cleanup](members/scoville-project-context-cleanup/README.md#how-to-use).

## Compatibility

Developed for Codex and Claude Code, with Python 3.10+ needed only for optional helpers. Fable, Astra, SOL or Opus (5.0+) are recommended. Selected Luna 6 High checks in Codex are described in each Skill's Compatibility notes; they do not establish a suite-wide baseline.

## Install the suite

Install the suite once in your agent host and it's available in all your
projects.

### New installation

Use this request in your agent host:

```text
Install and enable the complete suite for all my projects directly from https://github.com/benjaminstelzer/scoville-suite.
```

Don't mix standalone and suite copies of the same Skill.

If your host can't install directly from GitHub, download this repository and
copy all the package directories inside it to the host's Skills folder. You
end up with the same complete suite and the same requirements.

<details>
<summary>Upgrade from an earlier Scoville or Ask suite</summary>

### Upgrade from an earlier Scoville or Ask suite

Use this request in your agent host:

```text
Uninstall these Skills completely, including their settings, when present:
scoville-brainstorm, scoville-code-anti-ai-slop,
scoville-design-anti-ai-slop, scoville-handoff, scoville-plan,
scoville-research, scoville-scribe-anti-ai-slop,
scoville-ui-anti-ai-slop, scoville-wordpress-ui-backend-anti-ai-slop,
scoville-workflow-for-codex, scoville-workflow-codex,
ask-astra-for-review-for-codex, ask-sol-for-review-for-codex,
ask-claude-for-codex, ask-claude-and-astra-for-codex,
ask-claude-and-sol-for-codex.
Skip absent entries, leave unrelated Skills untouched, and keep no backup or settings migration. Then install and enable the complete suite for all my projects directly from https://github.com/benjaminstelzer/scoville-suite.
```

</details>

### Additional Scoville Skills

#### scoville-ask-for-codex

For Codex, also available as a standalone Skill. Ask your Codex host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-ask-for-codex/tree/main/scoville-ask-for-codex
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

## Configuration

Keep personal project conventions outside the installed Skills so updates
preserve them. The [Code configuration guide](members/scoville-code/README.md#configuration)
shows how to connect them to your project.



## Deprecated

These Skills are retired. In testing, they didn't do enough better than
current frontier models to be worth maintaining.

- **Scoville Scribe Anti-AI-Slop:** The writing comparisons showed no reliable
  benefit, and the tested version added claims it couldn't support.
- **Scoville Design Anti-AI-Slop:** Its comparison with modern frontier models
  ended in a tie.
- **Scoville Research:** It didn't reach the quality I expect, and good
  research tools already exist.
- **Scoville Brainstorm:** It didn't reach the quality I expect, and good
  tools for ideation already exist.

## Developer links

<details>
<summary>Development and builds</summary>

Sources live under `members/`. Edit README fragments in `development/readme/`,
then run `python development/build_suite.py --write-readmes`. The manifest
`suite.json` owns package membership and README composition.

[Development notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/docs/README.md)
explain the problems behind the suite. The
[build guide](development/shared/build/fragments.md) covers package generation,
runtime checks and Viewer assets. Installed Skills need only their own packages.

</details>

Sources, tests and notes live in this suite. Individual packages leave out
this block and the development files.

- **scoville-code**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-code/development/README.md)
- **scoville-plan**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-plan/development/README.md)
- **scoville-ui**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/development/instruction_tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)
- **scoville-handoff**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-handoff/development/README.md)
- **scoville-project-context-cleanup**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-project-context-cleanup) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/development/instruction_tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-project-context-cleanup/development/README.md)

## License

The bundled Skills use the MIT license. Each package includes its `LICENSE` file.

