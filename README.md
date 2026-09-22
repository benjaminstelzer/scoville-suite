# Scoville Suite

Scoville gives planning, research, code, design and writing their own Skills.
Use the ones your task needs. Installing a family does not make every task a
family gathering.

This monorepo keeps their sources and development together. Shared helpers and
README blocks have one maintained source, and builds produce self-contained
packages. Individual Skills can be installed separately, except Workflow,
which is available only through this suite.

Workflow is a Codex-only beta and is explained first below. Other Skills retain
their own compatibility limits.

## Scoville Workflow for Codex

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

## Scoville Brainstorm

Three versions of the same idea do not give you three useful choices. A queue,
an event queue and a queue with different arrows may still solve the problem
in exactly the same way.

Scoville Brainstorm explores alternatives by how they work. It compares them
against the fixed constraints and existing approaches, challenges their weak
assumptions and returns a shortlist you can make a decision from. It stops
before choosing or implementing a direction.

Use it for architecture, product, workflow or research questions that need
materially different approaches, including competing explanations for an unknown
cause. A known fix, ordinary review or wording question does not need this process.

## Scoville Research

A source list can look convincing while the answer rests on very little. Five
articles may repeat the same press release. A real citation may concern the
right topic without supporting the sentence attached to it.

Scoville Research follows claims back to the evidence that can answer the
question. It covers current web research, GitHub-first implementation discovery,
academic literature and longer investigations that need saved records. It
keeps contradictions and gaps visible and stops when another search would no
longer change the decision.

Use it for questions that need several sources examined together. A summary of
one known page or paper, ordinary repository inspection, brainstorming,
implementation or wording work belongs with the corresponding task.

## Scoville Code Anti-AI-Slop

A coding agent can finish the wrong thing quite thoroughly. The tests are green,
the report sounds certain, but the behavior you asked for is still missing.

Scoville Code keeps the requested outcome at the centre of engineering work.
It asks the agent to find the code that owns the problem, make a proportionate
change and check the behavior affected by it. A failing check needs a cause.
Calling it pre-existing, or weakening the assertion until it passes, does not
resolve it.

Use it for implementation, diagnosis, review and removal of code or engineering
artifacts. It can investigate without editing. Small changes should stay small,
while migrations, security boundaries and irreversible work need closer checks.

## Scoville Design Anti-AI-Slop

A design can look polished and still miss the brief. An 80s reference becomes
neon, chrome and VHS noise, but the combination says little about the actual
subject. Or every element is neatly spaced, yet nothing tells the reader where
to start.

Scoville Design connects the visual choices to the content, audience and medium.
It helps create a direction, develop it into an artifact, inspect the result and
repair specific problems. A critique should explain what is wrong and why,
while preserving the parts that work.

Use it for graphic, editorial, brand, advertising, packaging, wayfinding, web,
interface, information and motion design. It also handles style interpretation.
Mechanical edits to a settled design, conversion or rendering alone, backend
work and prose-only editing do not need it.

## Scoville UI Anti-AI-Slop

A good desktop screenshot does not tell you whether someone can use the page.
The main action may disappear on mobile, keyboard focus may be missing, or an
error may leave the user with no way forward.

Scoville UI helps implement and audit interfaces through the framework and
design system the product already uses. It covers components, interaction
states, responsive behavior and accessibility, then asks for evidence from the
actual rendered interface.

When Scoville Design is active, UI implements its design decisions. Otherwise
it can develop a bounded direction for a new interface. Backend-only work and
wording alone do not activate it.

## Scoville WordPress UI Backend Anti-AI-Slop

A plugin settings page can look tidy and still fight WordPress. Native controls
get rebuilt, a second spacing scale appears, and React is treated as proof that
the page uses WPDS. None of those choices follows from the task.

Scoville WordPress UI Backend implements and audits plugin-owned `wp-admin`
interfaces through the WordPress layer that actually owns them. It covers
Classic PHP pages, Core Components and supported mixed runtimes, with explicit
rules for spacing, responsive behavior, states, accessibility and i18n.

It owns implementation and UI acceptance for those surfaces. Scoville UI does
not run a second acceptance process. Frontends, the editor canvas and extensions
inside Core screens remain outside this Skill's scope.

## Scoville Scribe Anti-AI-Slop

A rewrite can sound better and say something different. "May reduce latency"
becomes "will improve performance", or a summary drops the condition that made
the result true. Smooth prose does not repair a changed claim.

Scoville Scribe drafts, edits, summarizes, localizes and audits requested text.
It preserves meaning, evidence, attribution, terms and behavior while removing
filler and unclear wording. Explanations must introduce their concepts,
identify what they refer to and give the reader enough information to act.

Use it for articles, reports, help, interface text and exact-source work.
Ordinary answers and status updates do not activate it merely because they
contain prose. When Scoville Plan applies, Plan owns its own records, including
wording audits. Neither Skill requires the other.

## Scoville Plan

A useful plan lets you pick up the work again without reconstructing the whole
conversation. It says what is active, which decisions apply and what needs to
happen next. If maintaining the plan becomes most of the work, the structure
is getting in the way.

Scoville Plan keeps Plans, Work Items and Decisions in the repository. Use it
when work spans dependent outcomes, needs explicit decisions or must survive
interruption. It preserves the existing planning owner and keeps completion
tied to an observed result, rather than the presence of a file or a checked box.
Small reversible changes usually need no durable Plan.

## Scoville Handoff

The next session needs enough information to continue the work. A long account
of the conversation can still miss the current blocker, the uncommitted changes
or the reason an earlier approach failed.

Scoville Handoff turns active work into one compact continuation prompt. It
preserves the objective, decisions, permissions, file ownership, observed
results and next safe action. A test that is still running stays unresolved.
Changes belonging to the user remain identifiable.

Request it when you want to transfer work to another agent or session. Ordinary
summaries, low context and ending a conversation do not activate it.

## Install the suite

Use one request in your agent host:

```text
Install all Scoville Skills compatible with this host for all my projects from
https://github.com/benjaminstelzer/scoville-suite/tree/main/packages
Each packages/<name>/<name>/ directory contains one installable Skill.
Inspect each Skill's compatibility first. Workflow requires Codex desktop.
Preserve personal configuration and unrelated installed Skills. Do not install
members/, development/, or another copy from the individual repositories.
Report installed locations, skipped incompatibilities and discovery results.
```

The suite supplies all its Skills from one repository. Your host still sees
separate Skills, so you can enable or disable them individually. Workflow is
suite-only. The specialist Skills are also available from their individual repositories.

If your host cannot fetch or install them, copy each compatible inner Skill
directory to its documented Skills location. See the
[Codex Skills guide](https://developers.openai.com/codex/skills/) or
[Claude Code Skills guide](https://code.claude.com/docs/en/skills).

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

Build to a new directory outside this repository:

```text
python development/build_suite.py --output <new-output-directory> --public-only
```

Omit `--public-only` only for private local staging. Each output directory
contains the member package, README, license and changelog where supplied.
Development files stay in the suite. The build receipt records file hashes,
target visibility and the source revision. An uncommitted source produces a
local development build, not a release candidate.

Standalone members use their individual repositories. Workflow is suite-only
and is staged under `scoville-suite/packages/scoville-workflow-for-codex/`.
Its installable Skill is the nested `scoville-workflow-for-codex/` directory.
Publication requires a separate authorized publication step with the
GitHub Skill. Never push a private suite tree to a public member repository.

### Developer links

Sources, tests and notes stay in this suite. Individual packages omit this block
and the development files.

- **scoville-brainstorm**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-brainstorm) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-brainstorm/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-brainstorm/development/README.md)
- **scoville-research**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-research) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-research/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-research/development/README.md)
- **scoville-code-anti-ai-slop**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-code-anti-ai-slop/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-code-anti-ai-slop/development/README.md)
- **scoville-design-anti-ai-slop**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-design-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-design-anti-ai-slop/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-design-anti-ai-slop/development/README.md)
- **scoville-ui-anti-ai-slop**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-ui-anti-ai-slop/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-ui-anti-ai-slop/development/README.md)
- **scoville-wordpress-ui-backend-anti-ai-slop**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-wordpress-ui-backend-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/blob/main/development/luna-tests/wordpress-sol-results.md) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-wordpress-ui-backend-anti-ai-slop/development/README.md)
- **scoville-scribe-anti-ai-slop**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-scribe-anti-ai-slop) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-scribe-anti-ai-slop/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-scribe-anti-ai-slop/development/README.md)
- **scoville-plan**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-plan/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-plan/development/README.md)
- **scoville-handoff**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-handoff/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-handoff/development/README.md)
- **scoville-workflow-for-codex**: [Source](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-workflow-for-codex) | [Tests](https://github.com/benjaminstelzer/scoville-suite/tree/main/members/scoville-workflow-for-codex/development/tests) | [Notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-workflow-for-codex/development/README.md)

