# Scoville Suite

Scoville gives planning, code and UI work their own Skills, with Handoff for transfers.
Install the complete edition. The general suite supports compatible
Agent Skills hosts and supplies manual procedures only when Python is absent.
Workflow and Ask are not included.

## Suite requirements

Install and enable every Skill included in this edition. The suite assumes
that its members are available and does not check for missing sibling Skills
at runtime. Partial installation is not supported; use standalone Skill
packages if you want to install only selected Skills.

Availability does not make every Skill applicable to every task. Load the
instructions the task needs and preserve explicit user exclusions. Workflow
still starts only when explicitly named. The general edition does not include
Workflow or Ask.

## Scoville Code

A coding agent can finish the wrong thing quite thoroughly. The tests are green,
the report sounds certain, but the behavior you asked for is still missing.

Scoville Code is the engineering foundation of the suite. It connects the
requested result, the existing implementation and the evidence that the change
works. The agent must understand the cause and respect the project's architecture,
not simply produce a plausible patch. Use it to develop, diagnose, review or
remove code without turning every small change into a full audit.

### How it works

- Establish the observable outcome, responsible code, introduced risks and cheapest decisive check before substantial editing.
- Read the owner and relevant callers, contracts and tests. Expand only when the evidence points elsewhere.
- Fix the cause in the existing implementation. Avoid parallel paths, speculative abstractions and unrelated cleanup.
- Test the changed behavior. A successful build or mocked integration proves only what it exercised.
- Investigate failed checks without weakening required guarantees. Change obsolete assertions only when an explicitly authorized contract change requires it. After two unsuccessful corrections of the same cause, reassess the approach.
- Inspect the complete change and report observed results and remaining gaps. Stop checking when further evidence would not change the decision.

### What it enforces

- **Outcome over ceremony.** Plans, tests, docs, and refactors support the
  requested behavior. Producing them is not completion by itself.
- **Canonical ownership.** The change fits the project's existing architecture,
  records, terminology, and workflow instead of creating a second owner.
- **Proportionate risk.** Small reversible work stays small. Destructive,
  public-facing, security, data, or release work receives stronger gates.
- **Evidence before claims.** Checks prove only what they observed. A failed
  tool is not silently promoted to a passing product.
- **Root-cause correction.** The agent changes approach after repeated failure
  instead of repeating the same unsuccessful fix.
- **Navigable code structure.** Existing work follows project conventions and
  surrounding module boundaries. Greenfield work starts with the smallest
  coherent responsibility-based layout. A 2,000-line default ceiling remains
  a backstop with concrete exceptions, never an architecture target.
- **Material questions only.** It asks when a missing choice changes behavior,
  authority, cost, reversibility, or scope, not for details the code settles.
- **Defaults for a wholly new project.** Project instructions come first.
  Only complete greenfield work uses the stack-specific conventions in the
  Skill's `references/project-conventions.md`. Keep personal overrides outside
  the installed Skill and reference them explicitly from `AGENTS.md` so Skill
  updates do not replace them. Existing projects keep their organization.
  The [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
  explains paths, precedence and update behavior with a copyable example.
- **Complete handoff.** The final report names changed behavior, relevant
  validation, unresolved failures, and relevant repository state.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md).

### What it costs

- Source inspection and checks use more tokens and time than an immediate patch.

## Scoville Plan

Work spread across conversations is easy to lose. A task may be marked done
without evidence, a decision may disappear into chat, or the next session may
have to reconstruct the project before making one change.

Scoville Plan keeps direction, Work Items and Decisions in the repository.
It makes the current work and next action recoverable while preserving the
project's existing planning owner. Use it for dependent work and long-running
projects, not to turn a small reversible edit into paperwork.

### How it works

- Resolve the existing planning owner and whether durable records are needed.
- Read the relevant Plan, Work Item and Decisions, then edit Markdown and YAML directly.
- Check the next item against current sources before starting it. Keep one current item and an explicit next action.
- Record evidence before completion and preserve accepted decisions and completed history.
- Use optional read-only helpers for structural validation and selected-work projections. Records remain usable without them.

### What it enforces

- **One planning owner.** Existing repository instructions and records stay authoritative.
- **Records a worker can use.** Each fact has one owner. Goals describe the current target, Work Items describe resumable outcomes, and numbered Steps name the actual work.
- **Check before starting.** Compare the next item with current sources and relevant completed work. Repair stale assumptions before executing them.
- **One active item.** The Plan names the current work and its first unfinished action.
- **Durable changes of direction.** Queue additions without losing current work. Preserve explicit stops, priorities and requested returns after a redirect.
- **Evidence before completion.** A file and a green structure check do not prove that the requested result works.
- **Explicit decisions.** Record human choices without asking twice. Keep inferred choices proposed until accepted.
- **No planning for the sake of planning.** Editing the Plan changes its records directly. It does not create another Work Item to maintain them.

- When Workflow is active, Steps expose the scope and boundaries needed for dispatch. The coordinator chooses the route. Plan can retain an explicit executor choice, but does not quietly turn a small-looking edit into low-risk work.

- The complete contract, including dispatch projections and direct-edit limits, is in [SKILL.md](https://github.com/benjaminstelzer/scoville-plan/blob/main/scoville-plan/SKILL.md).

Run one task to completion before editing its files or changing model settings
elsewhere. Plan assumes this single-run workflow. It does not lock files or
promise conflict-free recovery after concurrent changes. Routine edits need
no model-profile selection or hash receipts.

### What it costs

- Reading, updating and checking Plan records add token usage and maintenance time.

## Scoville UI

A good desktop screenshot does not show whether someone can use the page.
The main action may disappear on mobile, keyboard focus may be missing, or an
error may leave the user with no way forward.

Scoville UI implements and audits interfaces through the framework and design
system already in use. One shared contract covers information structure, states,
accessibility and rendered evidence. For supported WordPress admin pages, it
loads a local adapter for Core components, native spacing, versions and i18n.

### How it works

- Identify the existing design system, implementation owner and approved product decisions.
- Load the local WordPress adapter only for admin surfaces. Other frameworks use the general route.
- Read the relevant component and styling code before changing the interface.
- Implement affected states and responsive behavior through supported framework components.
- Check the completed batch in the actual rendered interface, including relevant input and focus behavior.
- Use one common validation process with the selected platform's additional checks.
- Return blocked product decisions to their owner. Without a visual owner, use the bounded new-interface direction.

### What it enforces

- **The product keeps its visual owner.** The incumbent design system comes
  first. UI implements approved product decisions; without a visual owner, it uses a bounded local direction.
- **The task has a hierarchy.** Primary decisions, supporting information, and
  secondary actions remain distinguishable.
- **Real states exist.** Loading, empty, error, disabled, success, focus,
  keyboard, and touch behavior are covered when relevant.
- **Responsive means adapted.** The task survives narrow, wide, zoomed, and
  content-heavy conditions rather than just scaling down the desktop layout.
- **Accessibility is structural.** Reading order, names, relationships,
  contrast, focus, and input behavior are checked in their real context.
- **Evidence matches the claim.** Source inspection can prove structure.
  Rendered or interactive claims require rendered or interactive evidence.

- **WordPress keeps its native owners.** Classic, Core Components, bundled WPDS and hybrid regions remain distinct. Tokens do not require a React migration.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-ui/blob/main/scoville-ui/SKILL.md).

### What it costs

- Browser inspection, interaction checks and corrections use additional tokens and time.
- WordPress work loads extra platform references. Other frameworks do not need them.
- Source-only work leaves rendering and interaction unverified. These instructions do not establish measured usability gains.

## Scoville Handoff

The next session needs enough information to continue, not another transcript.
A long summary can still miss the current blocker, unfinished changes or the
reason an earlier approach failed.

Scoville Handoff produces one compact continuation prompt with the objective,
current state, authority and next safe action. It preserves the facts needed
to resume without quietly advancing or completing the work.

### How it works

- Use established conversation facts and read named task sources with bounded recovery when a read is incomplete.
- Capture decisions, ownership, evidence, blockers and hazards without secrets.
- Organize the result into Receiver Instructions, Objective, State and Resume Steps.
- Compare the prompt against the captured facts and return one copy-ready block.
- The receiver checks current state before acting. A tight limit removes repetition before necessary facts.

### What it enforces

- **Explicit transfer only.** Ordinary summaries and context reduction do not
  produce a handoff artifact.
- **One receiver contract.** Every handoff contains Receiver Instructions,
  Objective, State, and Resume Steps in one copy-ready block.
- **Facts instead of pointers.** Conversation facts remain available. Named sources are read with targeted recovery
  for truncation or a transient failure, within explicit user limits. Their material
  facts enter the artifact so the receiver has them when resuming.
- **Authority and ownership survive.** Commit, publication, destructive-action,
  external-effect, file-owner, and dirty-tree boundaries stay explicit.
- **Unknown stays unknown.** Running or unobserved work never becomes a success
  claim, and secret values never enter the handoff.
- **The receiver can act.** Step 1 is the next safe action. The final step names
  an observable completion result.
- **Transfer does not advance the task.** Handoff reads the named state but does
  not edit, test, publish, or otherwise improve it on the way out.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-handoff/blob/main/scoville-handoff/SKILL.md).

### What it costs

- Reading the task state and preparing the handoff use additional tokens and time.

## Additional Scoville Skills

### scoville-ask-for-codex

Codex online. Available separately; not included in this edition.

Ask your Codex host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-ask-for-codex/tree/main/scoville-ask-for-codex
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

## Install the suite

Use this request in your agent host:

```text
Uninstall these Skills completely, including their settings, when present:
scoville-code-anti-ai-slop, scoville-handoff, scoville-plan,
scoville-ui-anti-ai-slop, scoville-wordpress-ui-backend-anti-ai-slop,
scoville-brainstorm, scoville-research, scoville-design-anti-ai-slop,
scoville-scribe-anti-ai-slop.
Skip absent entries, leave unrelated Skills untouched, keep no backup or settings migration, treat Python 3.10 or newer as optional, then install and enable the complete suite for all my projects directly from https://github.com/benjaminstelzer/scoville-suite.
```

All included Skills must remain enabled. Their task scope and invocation rules
still apply; Workflow requires an explicit invocation. Choose standalone Skill
packages instead if you want only selected Skills. Do not mix standalone and
suite copies of the same Skill.

If the host cannot install directly from GitHub, download this suite repository
and copy all its inner package directories to the host's documented Skills
location. This uses the same complete suite packages and requirements.

## Development and builds

Edit member sources under `members/`. Edit README fragments under
`development/readme/` and their ordered paths in `suite.json`. Member README
files are generated previews, not a second authoring source.

An isolated clone builds from the shared tools and templates bundled under
`development/shared/`. In the authoring workspace, the sibling `shared/`
directory owns those sources and supplies both suites. Installed Skills use
only the helpers inside their own package.

The shared Development block appears in this suite and its member previews.
Individual releases omit it. Maintain its source, test and note paths in each
member's `development` metadata in `suite.json`.

Regenerate previews with `python development/build_suite.py --write-readmes`.
Use `--check-readmes` to detect stale previews.

Build this exported edition to a new directory outside the repository:

```text
python development/build_suite.py --output <new-output-directory> --public-only
```

The exported manifest fixes the edition and complete suite layout. All member
packages are bundled under the suite's `packages/` directory. An isolated build
needs no sibling source checkout or individual Skill repository.

The complete private authoring source also supports `--profile general|codex`
and `--layout standalone|suite`. Standalone projections retain family guidance;
suite projections require the full member set. Export always produces a complete
suite with its selected profile and layout. An exported single-profile source
does not offer the other profile.

The build receipt records the selected profile, layout, package inventory,
source revision and hashes. Uncommitted sources produce development builds.
Publication requires inspected committed sources and the release checks.

### Developer links

Sources, tests and notes stay in this suite. Individual packages omit this block
and the development files.

- **scoville-code**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-code/development/README.md)
- **scoville-plan**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-plan/development/README.md)
- **scoville-ui**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)
- **scoville-handoff**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-handoff/development/README.md)

## Deprecated

Scoville used to cover more ground. I did not remove these Skills because each of them failed every task. I removed them because I could no longer show a reliable advantage over modern frontier models that justified the work required to test and maintain them. That is the standard I care about. I would rather offer fewer Skills and test them properly than keep a larger suite where some are merely good enough.

The general suite contains Code, Plan, one combined UI Skill and Handoff. The Codex edition adds Workflow, Ask and Setup.

- **Scoville Scribe Anti-AI-Slop:** The writing comparisons did not establish a reliable benefit. The tested version also introduced unsupported claims.
- **Scoville Design Anti-AI-Slop:** Its comparison with modern frontier models ended in a tie.
- **Scoville Research:** It did not reach the quality level I expect, while capable research alternatives already exist.
- **Scoville Brainstorm:** It did not reach the quality level I expect, while capable alternatives for ideation already exist.

