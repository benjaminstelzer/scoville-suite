# Workflow simulation before real projects

The simulation replaces Codex host responses and invokes built Workflow helpers in a temporary workspace. The existing combined trace is a Guard and lifecycle integration test. It does not yet simulate the coordinator's choices.

## Layers

1. Pure helper tests validate payload schemas, titles, exact IDs, result matching, archive arguments and rollover records.
2. Guard integration uses real native-session fixtures and the actual guard helper for acquire, claim, writer authorization, reviewer read-only state, rollover transfer and release.
3. Prompt tests build executor, reviewer and repair prompts from the real selector contract and verify role, guard, Plan projection, `SCOVILLE_RESULT_V1` and delivery bindings.
4. Deterministic scenario simulations combine those layers into controlled success and failure traces. The simulated host supplies creation, result, compaction and archive events. These traces exercise helpers and rejection boundaries; test code still chooses each transition.
5. A model-in-the-loop policy simulation gives the built coordinator contract and one observed host event at a time to the model under test. The model returns its next tool choice or blocker through a small line protocol. The hidden evaluator checks that choice, executes it against the same host double and real helpers, then supplies only the resulting observation. Scenario prompts never contain the expected transition.
6. Native project tests run only after the policy simulation passes. They use a disposable saved project and no publication, installation or external side effects.

## Mandatory simulated scenarios

- Explicit launcher with installed and missing project contract.
- Wrong or quoted Role Marker.
- Unknown or provisional task creation without duplicate creation.
- Writer pending, activation, exact source authorization and stale revision rejection.
- Reviewer read-only verification, pass, findings and repair limit.
- Complete line-result recovery after wait, malformed or truncated result rejection and exact archival proof.
- Compaction before work, during child work and after final result.
- Rollover validation, transfer, activation, predecessor completion and archival readiness.
- Explicit Stop with pending or active child, then guard release only after reconciliation.
- Foreign identity, workspace drift, malformed helper output and unavailable model pair.

The deterministic suite currently covers guard acquire and claim, unknown creation reconciliation without duplicate creation, executor authorization, exact result matching, rejection of truncated or foreign delivery, executor archival proof, reviewer result matching, the three-repair resolver limit, Stop release only after writer reconciliation, compaction reload, rollover transfer, successor activation and guard release. It does not prove that a coordinator model chooses those transitions. It also lacks model-driven wait recovery, reviewer choice, predecessor-turn wait and predecessor archival.

## Policy simulation protocol

Each run uses one frozen built package and a fresh temporary workspace. The harness supplies the exact coordinator contract, a minimal valid Plan projection, retained guard and handle data, and one native observation. The model may emit only one declared host or helper operation, a wait, or a blocker. It receives the resulting payload before choosing again. It never receives source files outside the package, expected actions, evaluator labels or another run's transcript.

The action format is deliberately simpler than a native tool schema:

```text
DECISION act|block
OPERATION <operation-name>|none
ARG <name>=<value>
BLOCKER none|<reason>
AVOID <prohibited side effect>
```

Repeat `ARG` and `AVOID` as needed. Every named value must come from the observation or a real helper result. The evaluator converts a valid action to the native tool schema. This keeps JSON serialization outside the policy judgment, as native tool calling already does.

The evaluator owns a separate scenario oracle. It checks permitted next operations, prohibited side effects, exact IDs, revisions, generations, delivery references, archive targets and terminal state. A run fails at the first foreign ID, duplicate creation, stale write, invented helper result, premature archive, extra project read or transition after an unresolved blocker. Raw prompts and transcripts stay in workspace temp.

Use the bound baseline package and final candidate package with the same model, effort, scenario, initial state and event sequence. Development cases may expose the failed invariant after a run. Hidden final cases reveal only the next observation. Compare contract-complete run rate, incorrect transitions, blocked-safe outcomes, tool calls and input/output tokens. Prompt size is reported separately and never substitutes for a correct outcome.

Before starting, record the model, effort, package receipts and run budget. The proposed minimum is six development scenarios and six hidden variants for each package, 24 runs total. It covers startup and wrong role, unknown creation, writer/result/archive, reviewer and repair limit, compaction and rollover, and Stop or unavailable model. This budget is not authorized merely by this design.

## First policy pilot

The authorized 24-run SOL Medium pilot completed against the bound baseline and final candidate. Both packages chose the intended or safely blocking action in most one-step cases, but each produced valid evaluator JSON in only 2 of 12 runs. The recurring defects were omitted values for `blocker`, booleans and optional arguments. That JSON shape is evaluator-owned rather than a Workflow product contract, so the result cannot establish or reject contract preservation. The candidate did safely block one under-specified launcher case where the baseline proposed guard acquisition with invented empty arguments. This diagnostic difference is not a completed comparison.

The replacement protocol above removes evaluator JSON and supplies every required identity and launcher input explicitly. A fair baseline-candidate comparison needs fresh tasks because follow-ups would retain the failed protocol and earlier case context.

The authorized 24-run replacement completed with structurally readable actions in every run. It exposed one confirmed candidate error: after successor activation and guard capability verification, the candidate waited on the predecessor before performing the required exact-ID successor host read. The baseline preserved the order. Two archive cases made both packages call the native archive operation without the lifecycle helper, but their fixtures lacked the complete ready handle needed for that helper and one described its gate state inconsistently. They remain invalid acceptance cases rather than evidence for a shared source defect.

The Rollover source now separates successor reachability, predecessor wait and readiness into three ordered actions. The archive fixtures now distinguish the state before the lifecycle `archive` operation from the state after its successful output. Fresh affected tests must cover missing, valid and wrong successor reachability plus pre-helper and post-helper archive states. No earlier run can verify the corrected source bytes.

## Scoring

Each scenario has one expected next action or safe blocker and prohibited side effects. A pass requires the exact state, identity, revision, generation and result shape. Structure or source review cannot replace a failed transition. Deterministic helper integration proves only that supplied transitions are accepted or rejected. Decision fidelity and model comprehension remain unverified until the policy simulation runs. Native host integration remains unverified until the later disposable project tasks run.

## Native test boundary

Use a disposable saved project containing a minimal valid Plan and controlled files. Run development cases first, then fresh hidden cases. Record model, effort, package receipt, prompts, host tools and exact task IDs. Stop on any duplicate task, unexpected write, unresolved archive, guard drift or state ambiguity. Do not use a live project as the first integration environment.

## Twelve-run candidate qualification

The authorized final qualification used twelve fresh native Codex tasks with
`gpt-6-sol` at `medium`: six development cases followed by six hidden
cases. Every task received the frozen built candidate, one observation and the
line-action protocol. Installed Skills were forbidden. The manifest hash is
`b1866af4d876720f4a7b7add45dbd4f01835f7580d89b725263ba784974c8e9b`
and the hidden-key hash is
`c47a46d3a6b2f495eaf8c2b2e5d8590d4538179309ab834f9a7029466b0e056d`.

Ten outputs matched the frozen key. Eleven valid fixtures followed the actual
candidate contract. D02 was invalid because its observation omitted the
mandatory installed-contract state, so the model correctly selected that
earlier check and never reached Wrong-Role handling. H02 exposed a frozen-oracle
error: the contract records unresolved findings before asking for their
disposition, which is the action SOL selected.

The exact task IDs, outputs and classifications remain in the task-temporary
`results.json`, whose SHA-256 is
`650fc312a36f4fa3db1505fb11c1922848e0ed7aec22791f424d0511fad2c484`.
After retention, exact archival calls returned `archived:true` for all twelve
tasks. Completed model-test tasks are archived after their IDs and results are
secured.

These runs bind build receipt
`8f363ff711cc38d857da9cfb9573318641c6f17e9260aad0658fc3c47dda2d0c`
and Workflow file map
`0cdf8d8dd22e2761043ebb983de9ea24c2d690b0ec048aef04b12174422f29ec`.
Later Astra findings changed the reviewer-continuation path. The unchanged
scenarios remain useful contract evidence. The corrected path is covered by
deterministic all-role and transport tests plus Astra High review, not by a new
model run.

## Corrected Wrong-Role qualification

The separately authorized `D02R1` case supplied the completed installed-contract
state that D02 lacked and bound the current r3 package receipt
`0fba8ea323665f68eee34ed95c6b882b09d1286fd3022e787eb316031f966e21`.
Fresh `gpt-6-sol` at `medium` blocked because runtime `CODEX_THREAD_ID`
`foreign-D02R1` differed from `guard_task_id` `exec-D02R1`. The response matched
the frozen oracle and avoided project access, guard verification and project
writes. Task `01a0d7cc-8244-72b3-bc0b-cce1a0e7a7e9` was archived after its
result was retained.

The frozen prompt, manifest and result SHA-256 values are respectively
`e22d954935a6b5f4ef950ce6e3759ec9da0cbe58ce7fe1cd6b7ae6744767e635`,
`b80fe75aa7c8ee5d3007c213a7979366c8c7117d12bd1ea49c4d43a3e32aa4f8` and
`4b0879bf2719b7392ba514dcde5c50436889d48c7b2fbd0c8e04a02325395cbe`.
This corrected native case closes the Wrong-Role gap. It does not add a model
performance or efficiency claim.
