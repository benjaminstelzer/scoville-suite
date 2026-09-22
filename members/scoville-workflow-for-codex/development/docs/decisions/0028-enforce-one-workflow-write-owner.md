---
format_version: 1
id: ADR-0028
status: accepted
created: 2026-09-20
accepted: 2026-09-20
scope: project/exclusive-write-ownership
---

# Enforce one workflow write owner

## Decision

The installable Skill owns one short static project contract in
`references/agents-contract.md`. A small deterministic
`scripts/manage_agents_contract.py` helper reads that source. It can render the
canonical block, verify a project, or install the block only after the launcher
records the user's explicit setup approval. Installation creates the
project-root `AGENTS.md` when absent or prepends the block without changing the
remaining bytes. It never edits nested files, Plan state, product files, Git
state, or the active workflow guard.

The normal `SKILL.md` contains no contract text and no setup procedure. Its
entire project-contract gate is exactly two concise instruction lines: run the
helper for the exact workspace; when its compact JSON reports
`"installed": false`, load `references/agents-setup.md`, follow only that setup
flow, and end without starting the workflow. When it reports
`"installed": true`, never load that reference and continue the normal role
gate. The helper reads `agents-contract.md` without putting its text in model
context. The conditional setup reference alone owns the user question, approved
install or update, refusal, unsafe-marker handling, and re-verification.

Verification accepts only the canonical text as the first content of the
project-root `AGENTS.md`, allows only an optional UTF-8 BOM and LF/CRLF line
ending differences, requires exactly one block, and rejects every other text,
spacing, order, version, or placement change. Its structured result includes
the source version, normalized SHA-256, observed path, action, and exact failure
code. After approved installation the launcher runs verification again, reports
readiness, and ends that invocation even when verification succeeds.

On first invocation in a project, a missing, changed, duplicated, or misplaced
block does not start Scoville Workflow. The launcher asks one exact question:
whether it may set up the Scoville Workflow project contract. Approval permits
only the helper's deterministic `AGENTS.md` installation and verification.
Successful verification after setup reports readiness and still ends that
invocation. Refusal or failed verification also ends it without a coordinator,
Plan access, guard acquisition, or any other project change. Only a subsequent
explicit invocation whose first check returns `installed: true` may enter the
normal workflow. A later invocation asks again only while verification still
fails. An already valid block requires no question and starts normally without
loading setup instructions. A coordinator or successor that observes
`installed: false` treats it as contract drift and uses the conditional
reference only for its active-workflow stop path; it never installs or updates
the block while workflow ownership is active.

Every coordinator successor verifies the same contract before accepting
ownership. An active coordinator repeats verification before each new write
authorization; later contract drift stops project and Plan writes without
discarding work.

The canonical block is capped at 110 whitespace-delimited words and 900 UTF-8
bytes. It names
`.scoville-workflow/guard.json` as the one workspace-relative guard path and
contains only rules that every cooperating project task receiving project
instructions, including tasks that never load this Skill, must apply before a
write:

- while the guard exists, every task reads it before every project write; a
  Scoville task with a missing or unreadable required guard is project-read-only,
  and a task whose own write authorization is pending or identity-mismatched is
  also read-only except for an identity-checked helper transition;
- guard changes use only the bundled deterministic guard helper, which validates
  the requested identity transition;
- only its exact coordinator may edit Plan state and stage or commit;
- only its one currently authorized executor or repair may edit the assigned
  unit, and write authority cannot be delegated;
- while the guard exists, every other task, including reviewers, audits,
  consultations, and undefined workers, is project-read-only;
- project writes include create, edit, delete, rename, format, stage, and
  commit; and
- nested project instructions may tighten but never weaken these rules.

Do not place routing, model choice, context thresholds, review procedure,
Acceptance logic, result schemas, repair counts, Plan content, requested scope,
dynamic IDs, current unit, coordinator lifecycle, setup instructions, or
recovery procedure in `AGENTS.md`. Dynamic identity belongs in the guard; all
other details stay with their existing owner and load only when needed. This
keeps the always-present block short and prevents a second workflow
specification.

When the static contract is valid on a later invocation, the launcher invokes a
separate deterministic `scripts/manage_workflow_guard.py` helper to acquire one
transient machine-readable initializing guard for the workspace. The helper
serializes every read-validate-write transition across processes, acquires only
when no current guard exists, and validates every claim, pending
writer-authorization, ready-ID reconciliation, activation, coordinator transfer,
release, and recovery operation against the exact runtime caller, expected
revision, expected generation, and expected prior state. Invalid helper
requests fail without a partial transition. A direct file edit cannot be
physically prevented; the integrity field detects ordinary direct edits and
later verification fails closed. The guard
records stable workflow identity, launcher and coordinator identity as
applicable, coordinator generation, workspace root, the launcher-supplied Plan
reference or unresolved objective, state, and at most one current write authorization with its unique
dispatch key, unit, role, exact unique task title, and ready task ID when
available. A successor receives ownership through one validated helper
transition; it does not create another guard.

Parallel audits, consultations, reviews, and analyses remain allowed when they
perform no project write. Their output stays in their conversation or outside
the guarded project. Persisting an audit inside the project requires a later
coordinator-defined write unit.

## Problem

A shared local checkout exposes every task to the same files immediately. Plan
serialization prevents the workflow from dispatching two writers itself, but
an unrelated task or undefined worker can still change code or Plan records in
parallel. That can invalidate review evidence, backups, Acceptance, and commit
scope without a reliable owner for the additional change. The Workflow Skill
and its child prompts also do not govern unrelated project tasks that never load
them.

## Drivers

- Give every project task the same small write-authority rule before it acts.
- Reach cooperating workflow children and unrelated project tasks through
  project instructions without requiring them to load the Workflow Skill.
- Prove exact installation before any coordinator or project work starts.
- Make first-project setup explicit, narrow, deterministic, and user-approved.
- Keep the normal Skill path to one helper result and two instruction lines.
- Preserve one authoritative writer chain for code and Plan state.
- Permit useful parallel read-only audits without risking workspace drift.
- Preserve ownership across coordinator rollover without overlapping writers.
- Keep the project-wide context tax to one short block, avoid an additional
  explicit contract-file read on the installed fast path, and avoid duplicating
  the same rule in the Workflow Skill.

## Considered alternatives

- Repeat the full roles and lifecycle in the Skill or every child prompt: does
  not constrain unrelated tasks and duplicates context.
- Use only a guard file: provides state but gives ordinary project agents no
  stable instruction to consult it.
- Use only `AGENTS.md`: states roles but cannot identify the active workflow,
  coordinator, or authorized unit.
- Refuse a missing block without setup support: safe but makes first use manual
  and error-prone.
- Install without asking: convenient but makes an unrequested project change.
- Ask once, install only the canonical block, verify it, then start: keeps the
  first-use change explicit and proves the same contract every later run uses.

## Consequences

- The launcher may read only the exact workspace identity and run the contract
  helper before coordinator creation. Failed verification grants no broader
  project-read authority.
- `references/agents-setup.md` is never loaded on the installed path. The
  canonical block is never copied into `SKILL.md`, operations, prompts, or the
  setup reference. The helper remains its only explicit file reader and
  renderer; the installed block itself is present once in project-instruction
  context.
- The setup approval is scoped only to the canonical top-of-file block. It does
  not authorize cleanup, rewriting existing instructions, Plan creation,
  product changes, staging, or commit.
- The setup invocation is terminal even after a successful install. This keeps
  all Plan, guard, coordinator, and project execution out of the bootstrap
  context and ensures the normal path begins only from a fresh positive check.
- Project preflight inventories nested `AGENTS.md` files governing the requested
  write scope. A nested instruction that conflicts with or appears to weaken
  exclusivity blocks start or dispatch for exact user disposition; the helper
  does not pretend to prove arbitrary prose semantically.
- Before creating a write-capable child, the coordinator uses the guard helper
  to record one unique pending dispatch authorization with no write rights.
  Every child prompt carries the exact guard identity, coordinator identity,
  dispatch key, unit, role, and unique title and requires the child to remain
  read-only until an activation message names its reconciled ready task ID. The
  helper reconciles that ready ID. The coordinator builds the complete prompt
  against the predicted next revision while the task remains pending, then the
  helper verifies the expected generation and activates the same authorization
  without creating a second lease. The prompt is sent only when activation
  returns that exact revision. A failed build archives the verified unassigned
  parked task before clearing its pending authorization and recording a blocker.
- Only one write-capable child may be active. Reviewers remain read-only. A
  parallel audit cannot create, edit, delete, rename, format, stage, or commit
  anything inside the project.
- Executors and repairs never edit canonical Plan records or invoke a guard
  transition. Undefined workers never write. Only the coordinator records
  accepted Plan transitions and controls staging and commits. Launcher and
  coordinator may request only the guard-helper transitions allowed for their
  exact current identity and state.
- Before dispatch, after every child result, before review, and before commit,
  the coordinator verifies contract and guard ownership plus unexplained
  workspace drift. Ambiguous or foreign changes stop the transition without
  discarding work.
- Coordinator rollover transfers the existing guard from the confirmed
  predecessor to the one ready and read-only validated successor. The transfer
  atomically removes predecessor ownership before explicit successor activation.
  Failure, unknown creation outcome, or provisional successor identity leaves
  the predecessor as owner and starts no next unit.
- Completion or explicit cancellation releases the guard only after all
  workflow children are terminal and accepted or safely retained. A stale guard
  is never silently replaced; recovery requires exact identity reconciliation
  or user disposition.
- This is a cooperative agent-level coordination control. It does not physically
  prevent writes by a native task, external editor, or process that ignores or
  has not loaded the project instructions. Known active writers must reach a
  verified stopped boundary before activation. Guard and workspace drift are
  detected after the fact and fail closed; they do not prove who caused a
  change.

## Confirmation

1. Verify render output is stable and verification accepts only one exact first
   block with the documented BOM and line-ending tolerance.
2. Verify `SKILL.md` contains exactly the two-line helper/conditional gate, no
   contract or setup prose, `installed: false` performs no normal role-gate or
   workflow action, and `installed: true` never reads
   `references/agents-setup.md` or explicitly reads
   `references/agents-contract.md`; the single installed `AGENTS.md` block
   remains normal project-instruction context.
3. Verify an absent file, missing, changed, duplicated, misplaced, wrong-version,
   unreadable, or source-mismatched block asks once and creates no coordinator.
4. Verify approval creates or prepends only the canonical block, preserves the
   remaining bytes, re-verifies successfully, reports setup completion, and
   ends without coordinator creation; refusal and failed installation also end
   without starting the workflow.
5. Verify only a subsequent invocation with an already valid block starts the
   normal workflow without a setup question, setup-reference read, or write.
6. Verify the canonical block never exceeds 110 words or 900 bytes and contains
   only guard lookup, fail-read-only behavior,
   helper-only guard changes, role boundaries, non-delegation, the write
   definition, and nested-rule precedence; no dynamic identity, lifecycle,
   setup, recovery, review, or routing rule is duplicated.
7. Verify unrelated coding, documentation, Plan, formatting, Git, and file
   maintenance tasks choose read-only behavior while the guard is active.
8. Verify a parallel audit may inspect and report outside the project but may
   not persist its report inside the project.
9. Verify the exact authorized executor and repair can edit only their unit,
   the reviewer remains read-only, and no child edits Plan or guard state.
10. Verify missing, stale, conflicting, or mismatched guard identity blocks
    writes without replacing the guard or deleting foreign changes.
11. Verify concurrent acquisition, expected-generation mismatch, and invalid
    acquire, claim, authorization, reconciliation, activation, transfer,
    release, and recovery requests fail without a partial write; valid helper
    transitions return complete valid JSON and one exact new guard state, while
    a direct file edit is detected as drift rather than claimed to be prevented.
12. Verify pending child identity has no write rights, ready-ID reconciliation
    plus explicit activation authorizes only that child, and a coordinator
    successor inherits the guard only after read-only validation; the
    predecessor loses ownership before successor activation or next dispatch.
13. Verify completion, Stop, child failure, contract drift, and interrupted
    rollover preserve or release the guard in the defined order.
14. Run fresh Luna allow-or-refuse cases as coordinator child and unrelated
    project task, then repeat after simulated compaction. Require the same
    correct decisions without loading or repeating the Workflow Skill.

## Revisit when

Reconsider when Codex exposes an enforceable workspace write lease inherited by
native child tasks and unrelated tasks before project access.
