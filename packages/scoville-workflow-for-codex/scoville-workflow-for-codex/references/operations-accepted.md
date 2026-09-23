# Accepted phase

Load [scope](operations-scope.md) and [rollover](operations-rollover.md) before the accepted transition so the checkpoint can run immediately. The review gate is owned by [review](operations-review.md).

## Batch the accepted transition

Once a valid child result or required review result is available, use one
coordinator transition pass whenever no user choice intervenes. In that pass:

1. use fresh selector output and only the separate bounded reads required for
   preflight, successor, proposal, or paused-return state;
2. inspect the scoped diff, changed paths, and named evidence once and classify
   the review boundary;
3. after the applicable review gate is satisfied, send the required
   completion-phase announcement, prepare the narrow Plan transition, run
   complete structural validation, stage only accepted paths, inspect the staged
   diff, capture status evidence, and create the optional scoped commit; and
4. evaluate the requested-scope terminal condition from the resulting Plan and
   index; rerun the selector only when an active Plan and another in-scope unit
   remain.

From the first child dispatch until this accepted transition, keep every
coordinator-owned Plan change for the unit uncommitted, including child task IDs,
results, reviewer and repair records, Evidence, blockers, and `Next action`.
Never create a standalone Plan checkpoint commit after dispatch. When Git is in
use, the next accepted unit commit contains its accepted project changes and all
coordinator-owned Plan changes accumulated since the previous accepted unit
commit that are required for one coherent profile. This may include retained
terminal blocker state from an earlier unit after that child was archived and
verified, but never that unit's unaccepted project changes. No commit may occur
before observed Acceptance and the satisfied review gate.

Run independent read-only observations in one tool batch when the host supports
it. Never parallelize dependent writes, treat direct Plan edits as atomic, stage
before acceptance, or let batching bypass a failure. A failed gate stops the
remaining transition steps. After the required completion-phase announcement,
do not insert narration turns between successful deterministic operations.

Before a Plan-backed commit, require observed Acceptance and a satisfied review
gate. A required review `pass`, an observed initial not-required result, or a
corrected `changes_requested` result with an observed not-required follow-up can
satisfy it. Load Scoville Plan and apply its correct lifecycle transition. For
remaining work, select the valid successor through that owner. For the final
Work Item, complete the item, Plan, and `PROJECT_INDEX.md` together; terminal
items retain no `Next action`, the Plan retains no `current_item`, and the index
becomes idle. Run the available read-only profile validator on the resulting
records. Zero diagnostics are required before staging. Stage only accepted
project paths or separable project hunks, plus each complete changed canonical
Plan, Decision, and index file. Never stage `.scoville-workflow/guard.json` or
any other transient guard artifact. Never split canonical planning records into
unit-local staged hunks. Require no unstaged difference for those staged
canonical files, verify their staged bytes equal the validated working bytes,
and treat that exact complete staged profile as the validator's subject. A valid
working profile never substitutes for checking a different partial staged
projection.
Commit with the unit ID and reviewer task ID when review occurred. Add
`followup-review-not-required` when corrections skipped a second pass, or use
`review-not-required` when no reviewer was created. Commit or staged-scope
failure prevents the completion report. Do not initialize Git, stash, reset,
discard, amend, bypass hooks, push, publish, or rewrite history.

Honor repository-owned backup and commit hooks without weakening them. A
required pre-change backup must still be valid against the `HEAD` used for the
unit commit. No Plan-only or other intermediate commit may advance `HEAD`
between that backup and the accepted source commit. If earlier history already
made the backup stale and the tracked source is still unchanged, use Scoville
Plan's permitted live-state mutation only when the whole Work Item is the
dispatch unit and its projected `Next action` can carry fresh backup creation.
For a Step dispatch, proceed only when backup creation already appears in the
selected Step, a referenced Decision, or a demonstrated repository instruction
the executor must load. Never rely on excluded Work Item `Next action`, rewrite
a started Step, or add prose outside the helper output. If no projected owner
can authorize the backup, ask for the exact recovery decision before dispatch.
The authorized executor creates and verifies the project-compliant backup
before its first source edit; the coordinator only checks its returned named
result. If source changes already exist without a valid pre-change
backup, preserve every commit and working-tree change, retain the failed hook
diagnostic, and ask for the project-authorized recovery; never backdate or
relabel a backup, discard work, or bypass the hook.

### Unit commit scenarios

| State | Commit action | Preservation rule |
| --- | --- | --- |
| Active unit before Acceptance or required review | No commit | Keep project and Plan changes uncommitted |
| Valid backup followed by an accepted reviewed source unit | One unit commit | Stage accepted project changes and all accumulated unit Plan changes together |
| Plan checkpoint commit advanced `HEAD` after the backup while source is unchanged and whole Work Item dispatches | No source commit yet | Put backup creation in projected Next action before executor source edits |
| Same stale backup with a started Step that lacks projected backup authority | No dispatch or source edit | Ask the exact recovery decision; do not rewrite the Step or rely on excluded Next action |
| Blocked unit retains source changes after a HEAD-bound backup | No other same-workspace unit dispatch or commit | Preserve the interval and ask for disposition |
| Earlier unit has retained terminal blocker state but no protected source interval | Next accepted independent unit may commit | Stage the complete valid accumulated Plan profile but none of the earlier unit's project changes |
| Candidate independent transition cannot stage a complete valid Plan profile | No dispatch | Ask for disposition before creating another child |
| Source changes exist but no valid pre-change backup remains | No commit or destructive recovery | Preserve all work and ask for the project-authorized recovery |
| Commit hook fails | No bypass or completion report | Retain the complete diagnostic and every change for correction |

After a successful unit commit, evaluate the requested-scope terminal condition
and run the coordinator checkpoint before selecting again. If an active Plan
and another in-scope unit remain, only the retained or newly activated
coordinator reruns deterministic Plan selection and continues the next eligible unit. Finish
remaining dispatch units in the current Work Item before advancing to another
Work Item. If the Plan became idle or an explicit boundary is complete, do not
invoke the selector; follow the completion rule below. Do not ask for
confirmation or emit a final receipt between nonterminal units.

Interpret comparison-command exit semantics before reporting a failure.
`git diff --no-index` returns `0` for no difference and `1` after successfully
showing a difference; only `2` or greater is an error. A command used to display
an expected untracked-file diff must normalize either successful comparison
result to successful tool status, or use a different read-only inspection. Do
not surface exit `1` alone as a failed check.

For `whole_active_plan`, completion requires the active Plan to be complete.
For an explicit boundary, completion requires every named unit through that
boundary to be accepted; out-of-scope Plan work remains untouched. Only then
does the coordinator post one concise completion report as the final workflow
action for this run. Keep the final coordinator unarchived after the report so
it remains visible to the user. Only a transferred rollover predecessor is
archived by its activated successor through the exact handshake below; no
terminal-completion coordinator is archived. Completed child tasks remain
archived.

### Post-commit scenarios

| State | Selector action | Next action |
| --- | --- | --- |
| Active Plan retains eligible in-scope work | Run the coordinator checkpoint first | Continue permits selection; rollover requires transfer first; blocked requires configuration correction |
| Explicit boundary is accepted while out-of-scope work remains | Do not run selector | Report boundary completion |
| Final Work Item completes the Plan and index becomes idle | Do not run selector | Report whole-Plan completion |
