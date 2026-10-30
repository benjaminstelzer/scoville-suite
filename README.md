# Scoville Suite

Scoville helps your agent plan work, write code, improve interfaces and carry
unfinished tasks into the next conversation. The Skills keep the goal, the
project's conventions and the verified results in view.

Scoville is the scale for chili heat. These Skills aim for sharper work and
less diluted context. Adding more instructions is easy. Keeping the useful
ones is the point.

The Skills keep a short shared core and load data checks, shell details and
helper instructions when the task needs them. Project choices and existing
approvals stay with the work; shorter instructions still have to carry the
whole job.

For Claude Code and other Agent Skills hosts, use
[Scoville Suite](https://github.com/benjaminstelzer/scoville-suite).
For Codex desktop, use
[Scoville Suite for Codex Mainloop](https://github.com/benjaminstelzer/scoville-suite-for-codex-mainloop),
which adds Workflow, Ask and Setup. Mainloop is the maintained Codex suite.

| Skill | Purpose |
| --- | --- |
| [Code](#scoville-code) | Keeps implementation, risk assessment and checks focused on what you asked for. |
| [Plan](#scoville-plan) | Keeps longer work, decisions and progress easy to pick up again. |
| [UI](#scoville-ui) | Builds and checks interfaces with their framework and design system. |
| [Handoff](#scoville-handoff) | Passes unfinished work to another session. |
| [Project Context Cleanup](#scoville-project-context-cleanup) | Keeps requested project rules and index text clear without losing required context. |
| [Skillwriter](#scoville-skillwriter) | Writes and reviews Skills and reusable prompts for frontier models. |

## Scoville Code

Passing tests are useful. Passing tests for the wrong behavior, rather less so.
Scoville Code keeps implementation, debugging and review tied to the result you
asked for: find the cause, work with the existing architecture and check what
actually changed.

Scoville measures chili heat. Code aims for sharper reasoning before a small
fix acquires its own framework.

### How it works

- Establish the requested result and find the code responsible for it.
- Fix the cause at its responsible owner, including shared causes behind
  recurring workarounds, within your authorized scope.
- Review affected behavior, guarantees and algorithmic costs. Derive checks
  from the required result rather than incidental implementation details.
- Continue failed repairs only with a supported next approach. Report evidenced
  limits and stop a repair path when no viable diagnosis remains.

### What it enforces

- **Work that serves the request.** Refactors, safeguards and tests need a
  concrete purpose. The agent asks about material choices and settles routine
  details from the project. It explains conflicting requirements or evidenced
  feasibility limits without substituting a different result.
- **Your conventions.** Existing architecture and project rules take precedence.
  New projects start with a small structure organized by responsibility.
- **Evidence that fits the change.** Check the behavior, preserve guarantees and
  distinguish observed results from what remains unverified. Code review traces
  relevant loops, scans and recursion; nested syntax alone is not a defect.

Keep personal conventions outside the installed Skill so updates preserve them.
See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
and [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-code/scoville-code/SKILL.md).

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

[Plan Viewer](https://github.com/benjaminstelzer/scoville-plan-viewer/releases/latest)
shows these records on Windows, macOS and Linux.

### How it works

- Use the repository's existing planning system and relevant Plan, Work Items and Decisions.
- Check current sources before starting the next item.
- Edit Markdown and YAML records with observed Step progress and any additional Instructions.
- Record observed acceptance results before completion and validate record structure.

The validator checks structure and references. It cannot establish permission,
meaning or whether an acceptance result is true.
Selector and validator share Plan section boundaries; diagnostics identify
the location and correction without imposing blank-line layout.

### What it enforces

- **Resumable work.** Goals, ordered Steps, dependencies and the current position
  stay explicit, together with live permissions, completed effects and evidence limits.
- **Decisions with an owner.** Confirmed choices are recorded. Open questions
  remain proposals and block only the work that depends on them.
- **Evidence before completion.** Finished means acceptance was checked.
  Changes of direction preserve completed work, binding constraints and material decisions.

Edit records from one session at a time. Concurrent edits need reconciliation.
See the [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-plan/scoville-plan/SKILL.md).

### What it costs

- Maintaining records takes tokens and time. It pays for continuity on dependent work. A small fix rarely needs a large Plan.
- Writing, machine-data and command rules load for the operation that needs them.
  Required Plan and Decision text stays complete; source references and embedded
  Decision text are separate parts of a prompt, so fewer rule words do not imply
  smaller Decision records or a fixed token saving.

[How to use Scoville Plan](members/scoville-plan/README.md#how-to-use).

## Scoville UI

Scoville UI builds and audits interfaces with the project's framework and
design system. It covers wording, hierarchy, responsive layouts and accessible
interactions, with checks matched to the result being claimed. A tidy component
tree is a start. People still have to use the page.

It includes specific guidance for plugin-owned WordPress admin pages, using
Core components and WordPress conventions.

Scoville measures chili heat. UI aims for a sharper interface without making
the user sweat.

### How it works

- Establish the requested page or region, task, approved decisions and component
  owners. Audits stay read-only; a local change stays local.
- Load guidance for open concerns and build through the existing framework.
  Settled design still needs correct states, semantics and input behavior.
- Choose source, geometry, visual and interaction evidence for the actual
  claims. Group related changes and refresh only evidence they invalidate.
- Route WordPress admin advice through surface and runtime classification.
  Supported plugin pages share the same checks; excluded host surfaces have
  no general-route bypass. Pure visual concepts keep their design scope.

### What it enforces

- **A coherent interface.** Hierarchy, controls and terminology follow the task
  and the existing design system.
- **Working mechanics.** Approved design stays intact while affected states,
  semantics, focus, input and recovery receive the checks they need.
- **Access across devices.** Check responsive layout, zoom, reading order,
  contrast, focus and keyboard or touch operation where applicable.
- **Scoped proof.** Source, concepts, geometry, viewed appearance and interaction
  establish different things. Measurements need independent targets and
  tolerances chosen before measurement. Partial coverage cannot establish a
  whole-page pass.
- **Code quality.** UI construction and updates receive the shared review for
  simplicity, relevant algorithmic costs, maintainability and clarity, without
  requiring benchmarks.

See the [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md).

### What it costs

- Rendered inspection and interaction checks take tokens and time. Load them
  when the claim needs them; they catch problems source alone cannot show.
  WordPress tasks load the platform contracts relevant to their scope.

[How to use Scoville UI](members/scoville-ui/README.md#how-to-use).

## Scoville Handoff

Scoville Handoff turns the current task into one copy-ready continuation
prompt: the goal, decisions, unfinished work, blockers and next action.
Another session can pick up the work without asking you to explain it all again.

Scoville measures chili heat. Handoff keeps the useful context from being
diluted between conversations. The next agent already has enough imagination.

### How it works

- Use established conversation facts and read missing required passages from
  the task sources already named or established. Preserve any remaining gaps.
- Capture the facts needed to resume, including permissions, unfinished work
  and the original evidence for interrupted or one-time effects.
- Produce one prompt in the requested language, otherwise the conversation
  language. The receiving agent checks current state before acting.

### What it enforces

- **Explicit transfer.** A handoff starts when you request one. Preparing it is
  read-only and does not advance the task.
- **Faithful context.** Decisions, permissions, ownership and blockers survive
  the transfer. Existing approval is preserved within its scope. Unknown
  results stay unknown, and secrets stay out, including quoted secrets.
- **A useful next action.** The prompt tells the next session where to resume
  and how to recognize completion.

Keep preferences distinct from binding requirements. The receiving session
still needs the exact permissions and acceptance criteria for its next action.

See the [full instructions](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-handoff/scoville-handoff/SKILL.md).

### What it costs

- Preparing the prompt takes tokens and time once, so the next session has less context to reconstruct.
- The declared base reading routes were about 40% shorter in the current source
  comparison. Conditional references were measured separately. This is a static
  text comparison, not measured token use or transfer speed.

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
- Check useful project information, duplicates and conflicts; reuse authorization covering the edit.
- Place concise wording in the affected structure, with conditions and exceptions together.
- Inspect the saved change and use the record owner's checks where required. Plan keeps native fields and lifecycle.

### What it enforces

- Requested additions and cleanup stay within the named project-context files.
- Scope, conditions, permissions, safeguards and necessary reasons survive edits.
- Existing formats and record owners remain responsible for fields and lifecycle.
- Suitable text stays unchanged, and unresolved material choices are asked directly.

### What it costs

- Reading the rules and checking edits takes tokens and time. The useful return is clearer context for later work, without deleting necessary detail.

[How to use Scoville Project Context Cleanup](members/scoville-project-context-cleanup/README.md#how-to-use).

## Scoville Skillwriter

Scoville Skillwriter writes and reviews Skills and reusable prompts for current
frontier models. It keeps the goal, real constraints and useful context while
cutting repetition and unnecessary ceremony.

Scoville measures chili heat. Skillwriter keeps instructions sharp without
seasoning every sentence with another warning.

### How it works

It combines shared instruction-design rules with an authoring workflow. Approved
revisions preserve the exact pre-edit state for comparison; reviews return
findings without editing. The host's Skill Creator owns Skill structure,
packaging and format validation. Source review and format validation are
reported separately from observed model behavior.

### What it enforces

It preserves the intended outcome, activation boundaries, permissions and
acceptance criteria. It asks only about material changes beyond the request or
prior approval. Changed instructions and affected consumers are checked together
in the existing source review.

### What it costs

The Skill has no paid service calls. Host model usage and any explicitly requested evaluation have their usual costs.

[How to use Scoville Skillwriter](members/scoville-skillwriter/README.md#how-to-use).

## How it was developed

Scoville grew from recurring problems in real software projects. Separate Skills
addressed code, interfaces, planning and the work around them. Shared guidance
keeps their foundations aligned, while the Codex workflow evolved toward a main
chat supported by focused exploration and independent review.

Development follows a repeated cycle: develop an idea, test it, and analyze how
it behaves in real workflows on large projects. Those observations guide the
next revision, which is tested and used again. The individual Skill READMEs
describe the changes and lessons that shaped each one.

## Compatibility

Developed for Codex and Claude Code, with Python 3.11+ for helpers and
manual alternatives only when suitable Python is unavailable. Missing helpers,
dependencies or helper errors stop the affected operation.

## Install the suite

Install the complete suite in your agent host to use it across projects.
### New installation

Use this request in your agent host:

```text
Install and enable the complete suite for all my projects from the packages/ directory of https://github.com/benjaminstelzer/scoville-suite.
Preserve personal settings and unrelated Skills. Ask before overwriting conflicting customizations.
Report the installed location and whether the host discovers every member.
```

Do not mix standalone and suite copies of the same Skill. If your host cannot
install from GitHub, download the repository and copy each
`packages/<name>/<name>/` Skill directory into the host's Skills location.
The repository root and development sources are not installable Skills.

### Upgrade or migrate an existing installation

Choose the target suite explicitly. Preserve project settings and personal
customizations, then replace duplicate installed copies with the target suite's
complete packages. Remove only superseded Skills you have selected for removal.
An upgrade is not permission to erase settings or unrelated Skills.

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

Both suite editions share one maintained source and Plan. Sources live under
`members/`. Edit README fragments in `development/readme/`,
then run `python development/build_suite.py --write-readmes`. The manifest
`suite.json` owns package membership and README composition.

Shared runtime files use the same manifest file entries as member-owned files
and copy directly from their declared sources. The builder checks the packaged
inventory, source hashes and helper routes.
The shared development snapshot still supports builds from an isolated suite
checkout. The build guide gives the current checks and export commands.

[Development notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/docs/README.md)
explain the problems behind the suite. The
[build guide](development/shared/build/fragments.md) covers package generation,
runtime checks and Skill publication integrity. Installed Skills need only their own packages.

</details>

Sources, tests and notes live in this suite. Individual packages leave out
this block and the development files.

- **scoville-code**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-code/development/README.md)
- **scoville-plan**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-plan/development/README.md)
- **scoville-ui**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)
- **scoville-handoff**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-handoff/development/README.md)
- **scoville-project-context-cleanup**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-project-context-cleanup) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-project-context-cleanup/development/README.md)
- **scoville-skillwriter**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-skillwriter) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-skillwriter/development/README.md)

## License

The bundled Skills use the MIT license. Each package includes its `LICENSE` file.

