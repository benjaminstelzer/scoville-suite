# Rollover phase

Task creation/identity: [activation](operations-activation.md); waits: [wait](operations-wait.md). After the handoff gate permits continuation use [scope](operations-scope.md) and [selection](operations-selection.md).

## Coordinator rollover

At each accepted dispatch-unit boundary with eligible requested work remaining,
run the following read-only command before any selector, next-unit Plan write,
`authorize-writer`, or child creation:

```text
python <workflow-skill-directory>/scripts/check_context_checkpoint.py --role coordinator --accepted-unit <just-accepted-unit>
```

Retain its result for this boundary. `action=rollover` requires the sequence
below before selecting any next unit; `action=continue` permits selection.
`action=blocked` reports invalid configuration: correct that configuration
before proceeding, without substituting a threshold or treating it as missing
telemetry. `assets/workflow.toml` owns both thresholds under `[context]`.
An absent checkpoint result is not unavailable telemetry: run the command.
If the command cannot run, use the exact-own-rollout procedure below once and
retain its result or concrete unavailable diagnostic before continuing.
Do not substitute a worker's telemetry, cumulative usage, a remembered sample,
or a host compaction for this checkpoint. Compaction keeps the same coordinator
identity and does not satisfy rollover. After resuming at an accepted boundary,
perform this checkpoint before proceeding if its result was not retained.
Do not reload the full operations reference between the commit and checkpoint;
run the checkpoint immediately. The currently running unit still owns its
execution, review, repair, acceptance, and commit before this boundary.

The helper reads one fresh exact-own-rollout `token_count` sample. Require its ordinal after
the latest current-turn context and compaction event. Compare integers:

```text
input_tokens * 100 >= model_context_window * coordinator_percent
```

Below the configured coordinator percentage continues in the same coordinator.
Exactly the configured percentage or above
starts the transition below. Missing, stale, malformed, or contradictory
telemetry is never estimated and continues in the same coordinator. Completed
scope, a complete Plan, or explicit Stop creates no successor.

The accepted boundary is one Step, one authorized compatible Step bundle, or
one Step-less Work Item. It need not wait for the enclosing Work Item. A
blocker, unresolved user decision, failed validation, failed commit, or
unaccepted unit is not a boundary.

Perform this sequence once:

1. Announce the accepted unit and coordinator transition. Reverify the project
   contract, current guard, no writer authorization, and workspace drift.
2. Call `begin-rollover` with the expected guard revision and generation, exact
   accepted unit, one predecessor-and-unit transition key, and one unique
   successor title from `task_title` using the next generation.
3. Create one successor with only `scoville_role=coordinator`,
   `coordinator_start=rollover_parking`, exact workspace, retained
   `workspace_mode`, saved-project identity, workflow ID, transition key,
   predecessor ID, and the instruction to perform no project, Plan, or guard
   action and end that turn awaiting validation.
4. If the create result is provisional or unknown, reconcile visible host tasks
   by saved project and exact unique title. Never create again until that
   bounded reconciliation proves no successor exists. A `clientThreadId` is not
   a ready identity.
5. Call `reconcile-successor` for the one ready `threadId`. Send that same task
   one validation message containing `coordinator_start=rollover_validation`,
   its reconciled task ID, exact workspace, retained `workspace_mode`, and
   saved-project identity, requested scope and retained language, canonical
   Plan reference, expected Git HEAD or
   `not_applicable_non_git`, accepted unit, predecessor ID, current revision and
   generation, workflow ID, transition key, and configured coordinator model
   and reasoning. Include retained `archive_chain` and `archive_receipts` for
   unresolved predecessors. Include no free-form dialogue summary. Remain in the
   predecessor turn and wait for exactly that successor validation turn through
   cursor-bound `wait_threads` calls of at most 60 seconds. Unchanged timeouts
   repeat silently with the returned cursor; a real wait error leaves the
   predecessor visible with the exact blocker.
6. The successor verifies those values, the Plan profile, Git or non-Git state,
   accepted boundary, and next eligible unit without Plan or project writes. It
   calls `validate-successor` with the exact transition key, sends one
   identity-bound validation acknowledgement to the predecessor through
   `send_message_to_thread`, and ends. If that delivery fails, it still ends
   with its validation receipt. After authoritative completion, the predecessor
   reconciles the same successor identity, transition key, revision, generation,
   and `rollover_validated` guard state; it never creates another successor.
7. After the completed validation turn and exact validated guard check, the
   predecessor calls `transfer-coordinator`. This atomically removes predecessor
   ownership and leaves the successor in `coordinator_pending_activation`;
   neither may write.
8. Send the successor one explicit activation message naming the transferred
   workflow, revision, generation, transition key, and exact predecessor task
   ID plus retained `archive_chain` and `archive_receipts`. The successor calls `activate-coordinator` and verifies
   `capability=plan`. After successful delivery, the predecessor's activation
   turn ends; it performs no further action. If the host holds this message in
   `waitingOnApproval`, the predecessor remains in that same turn and keeps only
   that exact pending call; it never ends the turn, retries, or relays the call.
   A definite delivery failure leaves both tasks unarchived and the
   predecessor visibly reports the handoff blocker without Plan or project
   writes. Reconcile or retry only that same-key activation after proving that no
   successor activation turn exists; never create another successor.
9. After activation and fresh `capability=plan` verification, the successor
   confirms its exact task ID and host are reachable through an exact-ID host
   read, then waits for the exact predecessor activation turn to complete through
   cursor-bound `wait_threads` calls of at most 60 seconds. Unchanged timeouts
   repeat silently with the returned cursor. Wrong identity, terminal failure,
   needs-attention state, or unconfirmed predecessor completion blocks both
   continuation and archival. Do not infer completion from an idle task.
   The successor calls `list_threads` without moving itself between sidebar
   sections and follows [rollover_readiness](../scripts/rollover_readiness.md) with
   the fresh verified guard, exact reachability and completed-turn evidence.
   For archival only, require
   `threads` to contain that same task ID and host ID and require
   `pinnedThreads` not to contain it. Derive its exact section item key as
   `codex:thread:<hostId>:<taskId>` and require every `sections[].itemKeys` list
   to omit that key. Only these checks together prove that the successor is
   unarchived, visible in the normal task list, unpinned, and outside custom
   sections. It posts or retains the current user-facing phase or blocker.
   If these visibility checks are incomplete but exact reachability, active
   guard identity/generation and predecessor completion are confirmed, continue
   ordinary guarded Plan selection without archiving either coordinator. Retain
   the helper's `archive_record` and `archive_blockers` as an open handoff
   reference; the predecessor remains unauthorized. At the next accepted-unit
   boundary, before selection or rollover, recheck once with fresh guard,
   exact reachability, listing and status evidence. Retain the record after
   an archive error. For older predecessors use `recover_rollover_archives` as
   specified in the helper contract; retain intermediate chain links and exact
   archive receipts until all targets are verified. Pass unresolved records
   to the next coordinator; at scope completion report
   any remaining predecessor IDs and blockers. Never poll for visibility.
   Never create another successor or infer visibility from a title prefix.
   Only after visibility and completion proofs does the successor call
   `set_thread_archived` for the exact predecessor task ID and require the
   response to prove that same predecessor ID has `archived: true`. The
   predecessor never calls archival on itself. A wait tool error, terminal
   failure, needs-attention state, wrong ID, or archive
   failure keeps both tasks and the guard intact and reports the exact blocker.
   An unchanged timeout remains in the silent cursor-bound loop. The successor
   sends no activation acknowledgement.

After successor creation, the predecessor performs only reconciliation, guard
transfer, and activation messaging needed to complete or safely stop this
handoff. It performs no Plan change, project work, next-unit selection, or
self-archival. A failure before transfer leaves the predecessor visible owner.
A failure after transfer leaves the predecessor visible but unauthorized for
Plan or project writes until the successor is both activated and visibly owns
status reporting. Guard ownership never substitutes for that visible status
proof. A ready or validated ID alone never permits archival. Retries use the
same transition key; an unknown create outcome never creates a second successor.

### Coordinator rollover scenarios

| State | Required action |
| --- | --- |
| Fresh occupancy below the configured coordinator percentage | Continue in the same coordinator |
| Fresh occupancy at the configured coordinator percentage | Run one rollover after the accepted unit |
| Telemetry missing, stale, malformed, or contradictory | Continue in the same coordinator |
| Mid-unit phase or failed transition | Do not roll over |
| Provisional or unknown successor creation | Reconcile; do not recreate or archive |
| Ready successor not yet validated or transferred | Both remain read-only for handoff; predecessor stays visible |
| Ready successor completed validation checks | Successor validates and ends; predecessor confirms its exact completed turn and reconciles the same validated guard even if acknowledgement delivery failed |
| Guard is `rollover_validated` and predecessor is awake | Predecessor transfers the guard and sends same-key activation; it never self-archives |
| Activated visible successor sees predecessor turn completion | Successor alone archives that exact predecessor and requires same-ID `archived: true` before selection or dispatch |
| Transfer succeeded but activation delivery failed | Keep both tasks unarchived; predecessor visibly reports the blocker without Plan or project writes and reconciles only the same-key activation |
| Successor list visibility is unproven but exact reachability and predecessor completion are proven under the active guard | Continue guarded selection; retain predecessor open; create no replacement coordinator |
| Successor exact reachability or predecessor completion is unproven | Archive neither task; preserve the guard and report the exact blocker |
| Scope complete, Plan complete, or Stop | Create no successor |
