# Scoville Suite

Scoville helps your agent plan work, implement code, improve interfaces and
carry unfinished tasks into the next conversation. Its Skills keep the goal,
project conventions and verified results in view as the work progresses.

## Suite requirements

Install and enable every Skill in the suite. For individual Skills, use their
standalone packages.

The agent uses the Skills relevant to your request.

## Scoville Code

A coding agent can produce passing tests while missing the behavior you asked
for. Scoville Code connects the requested result, the existing implementation
and the evidence that a change works.

Use it to develop, diagnose, review or remove code. It directs the agent to find
the cause, respect the project's architecture and check the affected behavior
with effort proportionate to the task.

### How it works

- Identify the outcome, responsible code, risks and decisive check before editing.
- Read relevant code, callers and tests. Expand the investigation when evidence requires it.
- Fix the cause within the existing architecture and requested scope.
- Check the changed behavior and report what the evidence actually proves.
- Investigate failures without weakening guarantees. Revise obsolete assertions only for an authorized contract change. Reassess after two failed corrections of the same cause.
- Inspect the complete change, report remaining gaps and stop checking when further evidence would not change the decision.

### What it enforces

- **The requested result.** Plans, tests and refactors support the outcome;
  completion requires the behavior itself.
- **Existing ownership.** Changes follow the project's architecture, records,
  terminology and workflow.
- **Proportionate checks.** Verification addresses concrete failure risks.
  Broader security, migration or release checks follow the task and project rules.
- **Supported claims.** Reports distinguish observed results, failed checks
  and unverified behavior.
- **Root-cause correction.** Repeated failure triggers a reassessment of the approach.
- **Navigable code.** Existing conventions and module boundaries guide changes.
  New projects start with a small layout organized by responsibility. The
  2,000-line default ceiling permits justified exceptions.
- **Necessary questions.** Ask when a choice changes behavior, authority, cost,
  reversibility or scope. Resolve ordinary details from the project.
- **Your conventions.** Project instructions take priority. Defaults apply only
  to a wholly new project. Keep personal conventions outside the installed
  Skill and reference them from `AGENTS.md` to preserve them across updates.
  See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions).
- **Useful completion reports.** State changed behavior, validation, unresolved
  failures and relevant repository state.

The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-code/scoville-code/SKILL.md).

### What it costs

- Source inspection and checks use more tokens and time than an immediate patch.

[How to use Scoville Code](members/scoville-code/README.md#how-to-use).

## Scoville Plan

Work spread across conversations needs a durable record of the goal, decisions
and next action. Scoville Plan keeps those facts in the repository, with Work
Items that describe resumable outcomes and evidence required for completion.

Use it for dependent work and long-running projects. It follows the project's
existing planning owner and keeps small tasks proportionate.

### How it works

- Use the repository's planning owner and relevant Plan, Work Items and Decisions.
- Check current sources before starting the next item.
- Edit Markdown and YAML records with an explicit next action.
- Record evidence before completion, preserve accepted history and validate the records.

### What it enforces

- **One planning owner.** Repository instructions and canonical records remain authoritative.
- **Clear work units.** Goals name the target, Work Items define resumable outcomes, and ordered Steps describe the work.
- **Current assumptions.** Check the next item against sources and completed work before execution.
- **One active item.** Record current work and its first unfinished action.
- **Durable direction.** Preserve additions, stops, priorities and requested returns after a redirect.
- **Evidence before completion.** Record observed results that establish acceptance.
- **Explicit decisions.** Save human choices; keep inferred choices proposed until accepted.
- **Direct maintenance.** Update Plan records without creating extra work items for routine edits.

Edit the records from one session at a time; concurrent changes require reconciliation.

See [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-plan/scoville-plan/SKILL.md) for the complete contract and editing limits.

### What it costs

- Reading, updating and checking Plan records add token usage and maintenance time.

[How to use Scoville Plan](members/scoville-plan/README.md#how-to-use).

## Scoville UI

A page must work across screen sizes, input methods and error states.
Scoville UI implements and audits those behaviors through the project's
framework and design system, using rendered evidence to check the result.

For supported WordPress admin pages, it applies Core components, spacing,
version requirements and translation conventions.

### How it works

- Identify the design system, responsible components and approved product decisions.
- Read relevant code and use the framework's supported components.
- Apply WordPress guidance to supported plugin-owned `wp-admin` pages. Editor surfaces and metaboxes retain their host conventions.
- Implement affected states and responsive behavior, then inspect the rendered result and interactions.
- Resolve blocked product decisions with their owner. Where visual direction is open, stay within existing framework conventions.

### What it enforces

- **Design consistency.** Follow the existing design system and approved product decisions.
- **Clear hierarchy.** Distinguish primary decisions, supporting information and secondary actions.
- **Complete states.** Cover relevant loading, empty, error, disabled, success and input states.
- **Responsive behavior.** Preserve the task across narrow, wide, zoomed and content-heavy layouts.
- **Accessibility.** Check reading order, names, relationships, contrast, focus and keyboard or touch behavior.
- **Matching evidence.** Support visual and interaction claims with rendered and interactive checks.
- **WordPress conventions.** Respect Classic, Core Components, bundled WPDS and hybrid regions. Using tokens does not require a React migration.

The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-ui/scoville-ui/SKILL.md).

### What it costs

- Browser inspection, interaction checks and corrections take tokens and time.
- WordPress tasks load platform-specific guidance.
- Source-only checks leave rendering and interaction unverified.

[How to use Scoville UI](members/scoville-ui/README.md#how-to-use).

## Scoville Handoff

Continuing a task requires its current blocker, unfinished changes and relevant
decisions. Scoville Handoff gathers those facts into one compact, copy-ready
prompt with the objective, permissions and next action, so another session can
resume the work.

### How it works

- Read conversation facts and named sources, recovering incomplete reads within the user's limits.
- Capture decisions, ownership, evidence and blockers while excluding secrets.
- Organize and check one copy-ready prompt with Receiver Instructions, Objective, State and Resume Steps.
- Preserve necessary facts under length limits. The receiver checks current state before acting.

### What it enforces

- **Explicit transfer.** A requested handoff produces one continuation prompt.
- **Usable context.** Material facts from the conversation and named sources
  appear in the prompt, including blockers and incomplete work.
- **Preserved authority.** Permissions, file ownership, user changes and
  boundaries on commits, publication or destructive actions remain explicit.
- **Honest state.** Unobserved results remain unknown. Secrets stay out.
- **Actionable continuation.** The first Resume Step gives the next safe action;
  the last defines observable completion.
- **A faithful snapshot.** Creating the handoff reads and describes the task
  without editing, testing or advancing it.

The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-suite/blob/main/packages/scoville-handoff/scoville-handoff/SKILL.md).

### What it costs

- Reading the task state and preparing the handoff use additional tokens and time.

[How to use Scoville Handoff](members/scoville-handoff/README.md#how-to-use).

## Additional Scoville Skills

### scoville-ask-for-codex

Codex online. Available as a standalone Skill.

Ask your Codex host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-ask-for-codex/tree/main/scoville-ask-for-codex
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

## Install the suite

### New installation

Use this request in your agent host:

```text
Install and enable the complete suite for all my projects directly from https://github.com/benjaminstelzer/scoville-suite.
```

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

Do not mix standalone and suite copies of the same Skill.

If the host cannot install directly from GitHub, download this suite repository
and copy all its inner package directories to the host's documented Skills
location. This uses the same complete suite packages and requirements.

## Development and builds

Edit member sources under `members/`. Edit README fragments under
`development/readme/` and their ordered paths in `suite.json`. Member README
files are generated previews, not a second authoring source.

An isolated clone builds from the shared tools and templates bundled under
`development/shared/`. In the authoring workspace, the sibling `shared/`
directory owns those sources and builds both the general and Codex editions. Installed Skills use
only the helpers inside their own package.

The shared Development block appears in this suite and its member previews.
Individual releases omit it.

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
and `--layout standalone|suite`. Standalone projections retain family guidance.
suite projections require the full member set. Export always produces a complete
suite with its selected profile and layout. An exported single-profile source
does not offer the other profile.

Uncommitted sources produce development builds. Publication requires inspected
committed sources and the release checks.

### Developer links

Sources, tests and notes stay in this suite. Individual packages omit this block
and the development files.

- **scoville-code**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-code/development/README.md)
- **scoville-plan**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-plan/development/README.md)
- **scoville-ui**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/tests/test_build_suite.py) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui/development/README.md)
- **scoville-handoff**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-handoff/development/README.md)

## Deprecated

The following Skills are retired. Testing did not establish enough benefit over
frontier models to justify their continued maintenance.

- **Scoville Scribe Anti-AI-Slop:** The writing comparisons did not establish a reliable benefit. The tested version also introduced unsupported claims.
- **Scoville Design Anti-AI-Slop:** Its comparison with modern frontier models ended in a tie.
- **Scoville Research:** It did not reach the quality level I expect, while capable research alternatives already exist.
- **Scoville Brainstorm:** It did not reach the quality level I expect, while capable alternatives for ideation already exist.

