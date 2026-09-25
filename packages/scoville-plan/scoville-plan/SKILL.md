---
name: scoville-plan
description: Maintain, resume, audit and hand off repository Plans, Work Items and Decisions, including their wording. Use for Scoville Plan requests, repository-owned planning or Decisions, durable work across interruption or compaction, format-version-1 projects, messages during active planned work, and adding, removing, reordering or cleaning up Plan points. Exclude pure informational questions with no retained action, small contained tasks needing no durable Plan, and explicit opt-out.
compatibility: "Any Agent Skills host with repository read/write access. Direct Markdown/YAML planning; no service or network required. Selector and validator need Python 3.10+. Manual alternatives load only without Python; helper errors remain errors. Developed for Codex and Claude Code; other hosts untested."
---

# Scoville Plan

Maintain native `format_version: 1` Plans, Work Items and Decisions through
direct Markdown/YAML edits. Preserve setup, recovery, proposals, lifecycles,
blockers, evidence and narrow repair. A record does not prove work.

Use a Plan for dependent outcomes, material sequencing, durable continuation or
a binding project workflow. A small reversible task needs no new Plan unless
the project requires one. On explicit opt-out, load no references, change no
planning records and make no Skill-derived claims; report any conflicting
higher-priority project requirement.

## Ownership

Follow system/safety and explicit user instructions, then repository rules,
then the supported native profile; these defaults fill gaps. Use the existing
planning owner, never a parallel Plan. Runtime plans are disposable mirrors.

All Skills included in this suite must be installed and enabled. Use the
applicable owner without checking sibling availability. Load only instructions
needed for the task. Explicit invocation gates and user exclusions still apply.





Plan owns record wording, permitted edits, format and lifecycle. P and D own
language rules; G owns decomposition. Record explicit executor choices but
never choose a dispatch route or start Workflow merely by writing a Plan.

The bundled selector and validator only read. Never use a planning CLI or
infer locking, atomic writes or semantic proof from their output. The selector
returns the exact current/named Work Item or dispatch unit under R. Relevant
Evidence, proposals, graph checks and recovery remain separate bounded reads.

## Load the operation's references

`R` [read-only](references/read-only.md); `G`
[granularity](references/planning-granularity.md); `P`
[Plan format](references/native-plan-format.md); `L`
[project lifecycle](references/native-project-lifecycle.md); `E`
[editing](references/native-editing.md); `W`
[Work Items](references/native-work-items.md); `D`
[Decision format](references/native-decision-format.md); `B`
[Decision batches](references/native-decision-batches.md); `V`
[validation](references/profile-validation.md).

Classify by operation and edited record. A Work Item edit uses W even though
its file is a Plan. Load only the applicable route:

| Operation | Load |
| --- | --- |
| Read direction or list records | R |
| Initialize absent profile; create or restructure Plan | G, P, L, E; W when editing Work Items |
| Delete an unstarted Plan; rewrite Goal or Non-goals | P, L, E |
| Insert, refine, move, select, block, advance, remove or rewrite Work Item | P, W, E; G when changing outcome boundaries or Steps |
| Queue additions during active work | G, P, W, E |
| Create, rewrite or transition a Decision | D, P, E; B for an authorized accept-or-reject batch |
| Activate, complete or cancel Plan | P, L, E; W if current work changes |
| Audit structure/lifecycle | P for Plans; D for Decisions; G only for decomposition judgment |
| Audit wording | P for Plan/Work Item or D for Decision; E writing section only |
| Validate writes or diagnose the complete profile | V; add only references needed for a reported diagnostic |

Read-only work preloads no format guides. If profile existence is unknown,
list the root before reading canonical paths. Use an existing complete supported
profile. If PROJECT_INDEX.md, docs/plans and docs/decisions are all absent,
initialize on an explicit durable Plan request or report absence without creating
records. Preserve partial, foreign, unsupported or invalid state and stop the
affected operation unless the route permits intent-preserving repair.

Use the bundled selector and validator when Python is available; they are
optional dependencies of the general Skill. Check availability before loading
the needed `*-without-python.md` manual route. Helper errors with Python
available remain errors, never a manual pass.
Current/named selection follows R; validation follows V.

## Preserve authority

Record actual scope, choices, blockers, dependencies, evidence and acceptance.
Source code, current behavior, documentation and silence do not authorize a
lifecycle or material choice. Ask only when the necessary choice is still missing.

- Explicit human direction to record a choice authorizes its accepted Decision
  without asking again. A proposal request creates `proposed`.
- An unresolved material choice about scope, architecture, public behavior,
  stored data, security, dependencies, reversibility, Acceptance, migration or
  rollout becomes `proposed`. Report recommendation, alternatives, tradeoffs
  and effect; request accept, reject or revise. Never pre-accept it.
- Activation, cancellation, deletion, scope changes, weaker Acceptance,
  ambiguous succession and Decision transitions need the explicit authority
  required by their route. Use B for an authorized accept-or-reject batch.
- Link each new Decision to every affected mutable Work Item. Do not rewrite
  started history to add the link.

At work start inventory Decision frontmatter. Read and report ID, title,
recommendation and effect for relevant proposals, or all proposals in a full
audit. Ask when execution depends on a choice or the user requests decisions;
a status question alone needs no decision answer. Stop only dependent work.
Retain unresolved proposals on handoff and do not repeat unchanged questions
unless new evidence matters.

Apply historical stops to their actual subject and scope, not unrelated work.
Preserve applicable limits; ask about unresolved material scope before the
dependent action. Age or silence does not revoke a stop.

## Execute, edit and report

Use W to classify messages during active work and for pre-flight, progress,
queueing and succession. Direct Plan maintenance never creates a Work Item
whose outcome is maintaining the Plan. Use L for final completion and idle state.

E owns compact writing and the read/edit/check sequence. Prepare a consistent
multi-file result only when multiple files change. Validate the final state
through V. A wording audit grants no write authority. Reads and Skill upgrades
require no record migration or reformatting.

Mark work done only after observed Acceptance and retained evidence. Structural
validation proves only the inspected format invariants. Keep partial or failed
work in progress, paused or explicitly blocked.

Report the Plan outcome, changed canonical records, active/blocked work,
observed checks, unresolved choices and next action. Distinguish structural
validation from behavioral acceptance.
