---
name: scoville-plan
description: Maintain, resume, audit and hand off repository Plans, Work Items and Decisions, including their wording. Use for Scoville Plan requests, repository-owned planning or Decisions, durable work across interruption or compaction, format-version-1 projects, messages during active planned work, and adding, removing, reordering or cleaning up Plan points. Exclude pure informational questions with no retained action, small contained tasks needing no durable Plan, and explicit opt-out.
compatibility: "{{ profile: general }}Any Agent Skills host with repository read/write access. Direct Markdown/YAML planning; no service or network required. The writing-profile helper needs Python 3.11+; selector, validator and Decision-batch helpers need Python 3. Manual alternatives load only without Python; helper errors remain errors. Developed for Codex and Claude Code; other hosts untested.{{ /profile }}{{ profile: codex }}Codex with repository read/write access and Python 3.11+. Direct Markdown/YAML planning; no service or network required. Bundled writing-profile, selector, validator and Decision-batch helpers are required for their operations. Missing dependencies or helper errors block the affected operation.{{ /profile }}"
---

# Scoville Plan

Maintain repository direction through direct Markdown and YAML edits. Preserve
supported native `format_version: 1` behavior: setup, read-only
recovery, Plans, Work Items, Decisions, proposals, lifecycles, blockers,
evidence, and narrow repair. Require no CLI, MCP server, database, journal, or
hidden state; remove or reinterpret no project-knowledge feature.

A record does not prove work.

On explicit opt-out: read no references; do not create or change planning files;
make no Skill-derived claims. Report any exact conflict with a higher-priority
project instruction requiring this Plan system.

## Ownership and limits

Precedence:

1. system, safety, and explicit current-request instructions;
2. repository instructions and their canonical planning mechanism;
3. an existing supported native profile (the project index, Plans, and Decisions);
4. these defaults for gaps.

Use the existing durable owner; never create a parallel Plan. Apply compatible
guardrails only; runtime plans are disposable mirrors.

Never invoke a planning CLI. {{ profile: general }}The optional bundled selector and validator are{{ /profile }}{{ profile: codex }}The required bundled selector and validator are{{ /profile }}
strictly read-only and never a write path. The selector owns only the exact
current-or-named Work Item or dispatch-unit projection defined in the read-only route; proposal
discovery, relevant Evidence, graph inspection, and successor recovery remain
separate bounded reads. Claim no locking, atomic publication, typed mutation,
or semantic proof; report observations only.

{{ profile: general }}Load a `*-without-python.md` reference only after confirming that no Python
executable is available and its operation is needed. Unknown availability does
not meet that condition; check the environment before choosing the route.
{{ /profile }}

{{ include: family.contract }}

{{ package: standalone }}Relevant neighboring owners:{{ /package }}

{{ include: family.neighbors }}

Plan owns native record wording, permitted edits, format and lifecycle.
Step decomposition follows G; Plan records explicit executor choices but never
chooses a dispatch route or starts Workflow. Language rules belong to P and D.

## Choose planning and route references

Use a Plan for dependent outcomes, material sequencing, durable
handoff, or a binding workflow. Implement one small reversible change directly
unless the project requires a tracked Work Item.

Exact reference codes: `R` [read-only.md](references/read-only.md); `G`
[planning-granularity.md](references/planning-granularity.md); `P`
[native-plan-format.md](references/native-plan-format.md); `L`
[native-project-lifecycle.md](references/native-project-lifecycle.md); `E`
[native-editing.md](references/native-editing.md); `W`
[native-work-items.md](references/native-work-items.md); `D`
[native-decision-format.md](references/native-decision-format.md); `B`
[native-decision-batches.md](references/native-decision-batches.md); `V`
[profile-validation.md](references/profile-validation.md).

Classify the operation and edited record, then load exactly its route. An edit
inside a Work Item uses the Work Item route even though its file is a Plan.

| Operation | Load |
| --- | --- |
| Read direction or list records; no write | R |
| Initialize a wholly absent profile | G, P, L, E |
| Create or restructure Plan | G, P, L, E; W when editing Work Items |
| Delete an unstarted Plan | P, L, E |
| Queue additive work received during active work | G, P, W, E |
| Directly insert, refine, move, select, block, advance, or remove Work Item | P, W, E |
| Record explicit human choice or possible material Decision | D, P, E |
| Apply explicitly authorized Decision transition | D, P, E |
| Apply explicitly authorized accept-or-reject batch | D, B, P, E |
| Activate, complete, or cancel Plan | P, L, W only if current work changes, E |
| Audit Plan structure or lifecycle | P; add G only for decomposition judgment |
| Audit Decision structure or lifecycle | D |
| Audit record wording | P for Plans or Work Items; D for Decisions; E writing section only |
| Rewrite Plan Goal or Non-goals | P, L, E |
| Rewrite Work Item wording | P, W, E |
| Rewrite Decision wording | D, P, E |
| Validate after writes or diagnose a complete supported profile | {{ profile: general }}Use V for validation: run its optional validator when Python is available; load the manual inspection route only without Python.{{ /profile }}{{ profile: codex }}Use V for validation: run its required Python validator.{{ /profile }} Then load only the native reference needed for a reported diagnostic or correction |

For read-only, preload no format guides. If profile existence is unknown,
list the root before canonical reads; never probe absent
`PROJECT_INDEX.md`. {{ profile: general }}When Python 3 is available, use the bundled selector for
current-or-named Work Item selection through R; load R's bounded manual route
only when Python is unavailable.{{ /profile }}{{ profile: codex }}Use the required bundled Python selector for
current-or-named Work Item selection through R.{{ /profile }} For an explicitly requested new durable Plan, use the
workspace as setup root, classify the whole profile, and initialize only if all
three canonical paths are absent. Use an existing complete supported profile.
If all three paths are absent and no durable Plan was requested, report that
absence without initializing. Preserve and stop
on partial, foreign, unsupported, invalid, or intent-invalid state unless the
route permits intent-preserving repair.

## Preserve authority and lifecycle

| Input or state | Required treatment |
| --- | --- |
| Goal, Non-goals, blocker, dependency, acceptance result, evidence, or lifecycle choice | Never invent. Implementation, ordinary documentation, source, silence, and current behavior are evidence, not authorization. |
| Activation, cancellation, Plan deletion, changed scope, weaker Acceptance, ambiguous successor, or adoption of a possible material choice | If the required explicit choice has not already been authorized, ask before changing durable state. |
| User selects a direction, asks to preserve it in project rules, or applicable project instruction clearly records the human-selected direction | Create and accept its Decision without re-asking. |
| Analysis reveals a possible material Decision about scope, architecture, public behavior, stored data, security, dependencies, reversibility, Acceptance, migration, or rollout | Create `proposed`; report recommendation, alternatives, tradeoffs, and effect; ask to accept, reject, or revise. Do not pre-accept. |

Link each created Decision to every affected mutable Work Item.

Apply a historical stop to its recorded subject and scope. Compare it with the
current authorized work before blocking a different workflow; a stop for one
provider does not automatically stop another. Preserve applicable restrictions.
If their scope is material and unresolved, ask only about the dependent action;
do not infer permission from silence or discard a stop because it is old.

A proposal request creates `proposed`; a clear request to record the stated
choice authorizes acceptance. Reject, deprecate, supersede, activate, or cancel
only with the explicit lifecycle choice required by the route. For an
authorized multi-Decision accept-or-reject transition, use B and its helper
route; never substitute single-transition or audit behavior.

At work start, inventory Decision frontmatter so proposal IDs remain discoverable.
Read and report ID/title/recommendation/effect for proposals relevant to the
current work, or all proposals during a full audit.
Request accept|reject|revise when the requested work depends on that choice or
the user asks to handle Decisions. A status/listing request does not require a
decision answer. Preserve unresolved proposals at handoff; do not repeat an
unchanged decision question merely because another status turn occurs. New
decision-relevant evidence may warrant asking again. Stop only dependent work.

Mark a Work Item `done` only after observing Acceptance and adding concise
evidence. A captured structural-validation result supports only structural
judgment and reporting, never acceptance evidence or mutation authority. Keep
failed or partial work `in_progress`, `paused`, or explicitly blocked.

## Handle active work

For a message received during active work, use W's message classification before
changing execution or native state. Direct Plan maintenance goes through its
normal route and never creates a Work Item for maintaining the Plan itself.
For item pre-flight, progress and succession use W; final Plan completion uses L.

## Write and verify

For any write, E owns the writing-profile selection, compact-record rules,
exact-byte guards, prepared multi-file result and post-write checks. Load V
when validating the final state. Wording-only audits use E's writing section
without authorizing a mutation. No-op reads and Skill upgrades require no
migration, reformatting or changes to existing project records.

## Report durable state

Lead with Plan outcome. Name changed canonical files, active/blocked work,
observed checks/evidence, unresolved choices, and next action. Distinguish native
structural inspection from behavioral verification; omit routine file narration.
