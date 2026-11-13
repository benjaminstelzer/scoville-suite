# Planning and Decisions

Use the project's existing plan and decision records; a runtime plan only
mirrors them. A small contained change needs no new record unless the project
requires one.

## Work items

Keep one behavior-complete item active at a time: an observable, separately
resumable outcome with its implementation and verification. Commands, review
and documentation are its steps. Split only where outcomes are accepted and
resumed separately. Acceptance names the results that must hold; a method
belongs in the steps unless it is itself required. Continue with the next
authorized item whose dependencies are met; a checkpoint needs no new
go-ahead.

For native records, follow Plan's selected
progress, authoring or maintenance route; load no other Plan route for this
reference.

## Decisions and field reviews

Record each material decision with its source and status in the existing
plan, ADR, decision log, authorized commit or pull request; without one, use a
handoff only when future work depends on it. In unattended work, choose within
the decision space the user authorized, record an open material choice as a
proposal, hold only the work that depends on it and continue the rest.
`scoville-plan` owns Plan, Work Item and Decision changes. In its `SKILL.md`,
use **Load only the current route** to select the operation's contract. Read
its `references/planning-granularity.md` only when Work Item or Step
boundaries need judgment.

For an assigned review of native Plan or Decision fields, read Scoville
Plan's read-only route and applicable field rules. Code's engineering
criteria do not define those fields. The review reads; maintenance, selectors,
tests and record writes stay with their owner.

## Hand off and resume

Only when Scoville Handoff is active for an explicit transfer, use its
`SKILL.md` sections **Read within the transfer scope**, **Preserve continuation
facts** and **Compose and check the prompt**, with its
`assets/continuation-prompt.md`.

Otherwise a requested handoff or project record retains the requested
outcome, binding constraints, current state, decisive evidence, the next
concrete step and any material decision not yet recorded. On resume, treat a
handoff as a snapshot: re-read the applicable instructions, inspect repository
and plan state, reconcile any mismatch and reuse completed work whose evidence
still matches the current tree.
