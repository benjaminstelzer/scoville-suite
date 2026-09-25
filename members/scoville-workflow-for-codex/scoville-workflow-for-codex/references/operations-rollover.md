# Automatic context rollover

The checkpoint reads fresh telemetry for the current runtime task ID. Its
thresholds come from `.scoville/config.json` or imported Skill defaults.
Coordinator comparison is at-or-above; worker comparison is strictly above.
Worker rules also apply to reviewer and repair roles. Native compaction and a
saved record do not replace creation and continuation in a new task.

## Worker, reviewer or repair

At a natural boundary with unfinished work, the child runs its supplied
checkpoint. `context_handoff` means: retain completed effects, current state,
checks, unresolved facts and a concrete remaining assignment, return that status
and end. A longer handoff may be a Markdown file named in the result.

The coordinator waits for the predecessor's completed turn and retains its
handoff. It then creates one successor of the same role, unit, workspace,
launched model/effort and logical attempt, with the original selected Plan
context plus the handoff. Do not restart completed work or consume a repair
attempt. Use the next counter for that role in its title while keeping the
unit. Save the new task handle. Once actual host evidence shows the successor
has started, archive the ended predecessor once by exact task/host ID and wait
for the successor's result. Pending creation alone is not takeover. An unresolved
creation is reconciled, never blindly recreated. The predecessor performs no
further work after handing off. Archival failure is reported, not a blocker.

## Coordinator

At an accepted-unit boundary with requested work remaining, `rollover` requires:

1. Save the accepted Plan state and update `.scoville/workflow.md` with the same
   run number, Plan ID, scope, workspace/project, exact predecessor
   ID, retained results, next unit/action and any unresolved task handle. Retain
   the role counters and assign the successor the next coordinator counter.
2. Start the prompt at byte zero with `scoville_role=coordinator` followed by
   a newline. Explicitly invoke `$scoville-workflow-for-codex` and give the exact
   installed SKILL.md path. Build a factual continuation with four sections: Receiver Instructions,
   Objective, State and Resume Steps. Include the exact installed Workflow path,
   record path, predecessor task/host ID, accepted boundary, current model/effort
   and the instruction to resume this same run. Load this Skill and its ordinary
   operations in the successor. Do not reopen accepted units.
3. Create one normal project coordinator task using the shared title helper and
   the successor's coordinator counter as `run_number`, same workspace and launched model/effort. Save the returned successor
   handle. If creation is pending, reconcile that attempt without recreating it.
4. End the predecessor turn after retaining the handle. It performs no next-unit
   selection, dispatch or project change. The successor waits for the exact
   predecessor turn to finish before assuming the run record and writing.
5. In the successor, verify the record names its actual task ID, this predecessor
   and the same workspace/run. Resolve pending identity through actual host
   evidence. Record itself as coordinator and continue the saved next action.
   Archive the ended predecessor once, then report any archive failure and
   continue. A missing predecessor completion or uncertain successor identity
   blocks writes; an observation timeout is not completion.

The successor's creation is the automatic task switch. No generation counter,
guard transfer, parked activation, receipt chain or model-computed signature
is involved. If creation fails or no supported host operation is available,
retain the state and report the failure. Do not present compaction, a stored
handoff or a promised future task as a successful rollover.
