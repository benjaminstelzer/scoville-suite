# Workflow instruction refactor

## Bound baseline

- Source revision: `b0be79672dde96d58aa9a400165426038778fd73`.
- Built package: Codex suite build under the required release staging tree.
- Build receipt SHA-256: `ad99697909a92c6aab9786e07770674806963c24cc0d735c44208adb04dbff05`.
- Baseline contract tests: 80 passed.
- Raw prompts, source copies and measurements remain in task temp and are not release evidence.

| Artifact | Bytes | Words | SHA-256 |
| --- | ---: | ---: | --- |
| `SKILL.md` | 15,581 | 2,013 | `ceb2aa89ccefddecbf7c8c0423f14f1eb2da59ce8da6b28db860298bb87539b1` |
| Built coordinator contract | 73,351 | 9,921 | `c9b40eaa498cc79529b06bf5c3dd6ede6998e970e02e2bd6057dd27d5fa08ecc` |
| Representative executor prompt | 9,114 | 1,063 | `9a3e9ebb179f8af997be16f603eb5606d179a8d24e9647884ccbd8c9f7e17936` |
| Representative reviewer prompt | 8,166 | 921 | `0560d284597b68440800d323ce889cc3cab38f87eb4af29e5170167f4ba4aeaf` |
| Representative repair prompt | 9,493 | 1,096 | `212a17e4fa9642914c8990762eab480d1c5f9ef84f52797c067feaf9ef195a55` |

The prompt samples use the same selected Step, dependency and Decision. Reviewer and repair add only their required predecessor result and repair assignment.

## Rule ownership

| Contract | Canonical owner | Consumers | Failure if lost | Existing behavior proof | Treatment |
| --- | --- | --- | --- | --- | --- |
| Explicit invocation and first-line Role Marker | `SKILL.md` | Launcher, coordinator, children | Wrong task gains a role or launches Workflow | Role-gate and explicit-launch tests in `test_contract.py` | Keep exact trigger and marker semantics in the entry point |
| Installed project contract check and setup exit | `manage_agents_contract.py`, `references/agents-contract.md`, `references/agents-setup.md` | Launcher and coordinator | A writer starts without the managed project rule | Agent-contract setup, preservation and upgrade tests | Keep helper call in the entry point, setup detail conditional |
| Saved project, workspace and task identity | Launcher reference, `task_lifecycle.py`, `coordinator_contract.py` | Launcher and every native role | Work runs in another checkout or binds the wrong task | Native startup, workspace reuse and creation-envelope tests | Keep exact fields and helper validation |
| Workflow ID, guard revision and generation | `manage_workflow_guard.py` | Coordinator, writers and reviewers | Stale or foreign task mutates state | Guard authorization, concurrency, stale-state and JSON tests | Keep exact protocol fields and fail-closed result |
| Guard helper requirement | `manage_workflow_guard.py` plus operations index | Every role | Model reconstructs or edits guard state | Guard mutation and direct-edit tests | Keep helper-owned transitions, shorten explanatory prose |
| Plan selection and unit projection | Scoville Plan selector plus `operations-selection.md` | Coordinator and prompt builder | Child receives the wrong unit or unrelated Plan data | Unit, bounded-selection and selector-diagnostic tests | Keep exact unit grammar and four-area projection |
| Unchanged `source_text` | Scoville Plan selector plus `build_dispatch_prompt.py` | Executor, reviewer and repair | Canonical action is rewritten or truncated | Whole-item and Step prompt tests | Keep byte-preserving projection and digest binding |
| Child Role Marker, authority and guard binding | `build_dispatch_prompt.py` | Executor, reviewer and repair | Child writes under the wrong role, unit or guard | Prompt-shape, native-gate and transport tests | Keep ordered fields and role-specific capability check |
| Dispatch protocol | `build_dispatch_prompt.py`, `inspect_native_context.py`, `operations-activation.md` | Coordinator and children | A parking prompt or foreign assignment is accepted as a complete dispatch | Prompt-shape and native-context tests | Keep the exact `SCOVILLE_DISPATCH_V1` identifier and complete prompt binding |
| Result line protocol | `parse_role_result.py`, `build_dispatch_prompt.py`, `operations-results.md` | Children and coordinator | Coordinator accepts an ambiguous or malformed result | Parser, size-limit and recovery tests | Keep roles, statuses and limits exact; models return only `SCOVILLE_RESULT_V1`, while the helper creates the internal structured object |
| Exact-child wait and result recovery | `task_lifecycle.py`, `operations-wait.md`, `operations-results.md` | Coordinator | Receipt, another turn or truncated output is accepted | Wait, native rollout and projection-recovery tests | Keep identity and completion checks, consolidate rationale |
| Terminal archival proof | `task_lifecycle.py`, `operations-wait.md` | Coordinator and rollover successor | Transition advances while a child remains visible or active | Exact archival and reconciliation tests | Keep same-ID `archived:true` requirement |
| Compaction recovery | `coordinator_contract.py`, `inspect_native_context.py`, `operations-compaction.md` | Coordinator and children | A compacted task resumes from remembered or stale rules | Coordinator and child compaction tests | Keep full post-compaction reload and terminal-result recovery |
| Coordinator rollover | `operations-rollover.md`, guard and lifecycle helpers | Predecessor and successor coordinators | Two coordinators own writes or progress is lost | Threshold, transfer and predecessor-archive tests | Keep ordered transfer protocol and conditional reference |
| Repair limit and review threshold | `workflow.toml`, model resolver and review operations | Coordinator | Unbounded repairs or unreviewed material change | Routing and repair tests | Keep configured first executor, at most three repairs and review rules |
| Model availability and route resolution | `workflow.toml`, `resolve_model_pair.py`, `operations-dispatch.md` | Coordinator | Silent substitution changes cost or capability | Resolver and route tests | Keep helper result and explicit blocker |
| Git ownership and simple accepted commit | `operations-accepted.md` | Coordinator and executors | Partial or foreign work is staged, discarded or published | Commit-boundary and accepted-transition tests | Keep exact ownership and staging boundaries |
| External authorization | Canonical Work Item and repository instructions | Executor and coordinator | Publication or live action occurs without authority | Prompt authority and acceptance tests | Keep explicit authorization boundary |

The entry point and runtime references may simplify explanations, repeated warnings and examples. Protocol fields, ordering, schemas, identity checks, state transitions, failure meaning and authorization boundaries are not model prose and remain precise.

## Coordinator state and rule availability

The guard is authoritative for ownership and writer activation. It does not uniquely encode every coordinator operation.

| Observed authoritative state | Possible next operations | Safe contract choice |
| --- | --- | --- |
| Initializing guard without reconciled coordinator | Parking, creation reconciliation or cancellation | Startup contract only |
| Claimed coordinator, no writer and no rollover | Scope resolution, selection, dispatch preparation, accepted transition, Stop or recovery | Ambiguous - retain the complete normal coordinator contract |
| Pending writer | Prompt construction, activation reconciliation, parking cleanup or Stop | Ambiguous - retain the complete normal coordinator contract |
| Active writer | Wait, interruption handling, result recovery or Stop | Ambiguous - retain the complete normal coordinator contract |
| Read-only reviewer | Wait, result recovery, review decision, repair dispatch or Stop | Ambiguous - retain the complete normal coordinator contract |
| Rollover pending, validated or transferred | Rollover procedure and failure recovery | Load the complete rollover reference in addition to the normal contract |
| Latest native event is compaction | Contract reload, exact-result recovery or block | Reload the complete normal contract from helper output |

Reviewer completion and coordinator resumption can share the same guard state as reviewer wait. Accepted-unit selection and a blocked-unit disposition can also share a no-writer guard state. A new phase counter would become a second durable owner. The implementation therefore keeps one complete normal runtime contract and reduces only duplicated model prose. It adds no phase argument, phase counter or state file.

## Validation boundary

Deterministic tests prove helper behavior, serialization, routing, allowed state transitions and fail-closed handling. The current combined fixture proves that guard and lifecycle helpers accept one compatible executor-reviewer-rollover sequence. It does not execute the coordinator's wait, result choice, predecessor-turn wait or predecessor archival, and it does not prove that a model chooses the specified transition. Those behaviors remain open for scenario and native task checks.

## Final candidate measurements

The final candidate uses the same representative Plan unit and role inputs as the baseline. The complete contract suite passes 88 tests. The added tests extend simulated host traces and protect the revised rollover order. They do not count as model-performance evidence.

| Artifact | Baseline bytes | Candidate bytes | Change |
| --- | ---: | ---: | ---: |
| `SKILL.md` | 15,581 | 5,660 | -63.7% |
| Coordinator contract | 73,351 | 72,913 | -0.6% |
| Executor prompt | 9,114 | 7,915 | -13.2% |
| Reviewer prompt | 8,166 | 7,128 | -12.7% |
| Repair prompt | 9,493 | 8,269 | -12.9% |

The reduction is a measured size change, not evidence that a model performs better. Final build receipt SHA-256 is `8f363ff711cc38d857da9cfb9573318641c6f17e9260aad0658fc3c47dda2d0c`. The source revision field remains the bound baseline commit because the measured candidate is an uncommitted working tree; `source_dirty: true` records that condition. Prompt bytes include absolute staging paths and therefore remain tied to this build directory.

## Protocol validation

Executor, Reviewer and Repair return `SCOVILLE_RESULT_V1`. The packaged `parse_role_result.py` helper is the only parser. It enforces role-specific fields, fixed order, status values, eight findings, per-field and total prose limits, LF or CRLF line endings and the completed-result change fields. It rejects legacy result JSON, unknown or duplicate fields, bare CR, fences, blank lines and role-invalid values. Models produce no result JSON; the helper creates the coordinator's internal structured representation.

Dispatch prompts carry `dispatch_contract=SCOVILLE_DISPATCH_V1`. The native-context gate validates the complete canonical dispatch prompt. There is no Legacy route or dedicated Legacy-name check. The rename changes no role, guard, identity, delivery, recovery or archival rule.

The final source passed 88 Workflow tests, 23 suite tests and 46 shared build and export tests. The Codex suite build passed package freshness, verified six packages with 115 files and passed Skill Creator validation. A committed temporary validation checkout exported 637 files at commit `d28a2e45d34c9d68d036c4da16ac7e1ffa5ea686`; isolated builder payloads and exported package bytes matched all six canonical member payloads. The export receipt SHA-256 is `9f4f87a664dbc22027b71965c0453a14b207db7642652b99bbc8c8f0089929a3`. This temporary commit and export are validation artifacts, not project publication.

## Final source review

The continued Astra Medium task reviewed the working tree in a fix loop. It first found one stale package-test assertion after the obsolete `compatibility` frontmatter field was removed for current Skill Creator conformance. After that assertion was removed, review `workflow-refactor-astra-medium-20260925-06` returned `FREIGABE`. A later policy simulation exposed an omitted successor reachability check. The Rollover owner now states reachability, predecessor wait and readiness as three ordered actions. Review `workflow-refactor-astra-medium-20260925-08` returned `FREIGABE` for that source fix.

For the result protocol, review `workflow-result-v1-astra-medium-20260925-01` found a missing eight-Findings limit in child prompts and newline normalization before bare-CR rejection. Both defects were corrected. Review `workflow-result-v1-astra-medium-20260925-02` returned `FREIGABE` and confirmed the single parser, absence of a legacy JSON branch and preserved recovery and authority boundaries. Astra performed source reviews and did not execute the test suites. Fresh affected model tests and native host evidence remain open under W-005.

After the protocol rename, review `workflow-protocol-names-astra-medium-20260925-03` returned `FREIGABE`. It confirmed consistent `SCOVILLE_DISPATCH_V1` use, unchanged `SCOVILLE_RESULT_V1` sources and preserved role, guard, identity, delivery, recovery and archival boundaries. The reviewer inspected sources, package diffs, hashes and tests read-only. It treated all executed test and export results as Coordinator evidence and did not rerun them. The user then removed the dedicated old-name negative test because the final design has no Legacy routes.

## Policy pilot boundary

Twenty-four fresh SOL Medium tasks compared the bound baseline and final candidate over six development and six hidden one-step cases. Both packages produced valid evaluator JSON in 2 of 12 runs. Their action choices were mostly directionally correct, and the candidate safely blocked one under-specified launcher case where the baseline invented empty guard inputs. The artificial JSON failure prevents a multi-step policy score and proves no candidate benefit. Raw task outputs remain in workspace temp under SHA-256 `9dc84ae8c93d9fc27a20e319dfa0d0cd059450227cdb3bf935d29b89a5db47c0`. All 24 completed evaluation tasks were archived.

A second 24-run SOL Medium comparison used the simpler line protocol. Every response was structurally readable. Both packages bypassed the lifecycle archive helper in two under-specified fixtures; those fixtures lacked a complete ready handle and one contradicted its own gate state, so they are not acceptance evidence. In the rollover case, only the candidate waited on the predecessor before proving successor reachability. Astra confirmed that omission as a contract error. The canonical Rollover reference was corrected and rebuilt; raw second-pilot results remain in workspace temp under SHA-256 `02c773a8910bc066a6719d19c1565e8ab193754584752714afa169be0401e811`. All 24 completed tasks were archived.

## Final qualification and Astra High review

The authorized candidate-only qualification ran twelve fresh `gpt-6-sol`
`medium` tasks: six development cases and six hidden cases. Eleven valid
fixtures followed the candidate contract. D02 omitted the mandatory
installed-contract state and therefore never exercised Wrong-Role handling.
H02 used an incorrect oracle because the contract records unresolved findings
before asking the user for their disposition. All twelve exact task IDs and
outputs are retained in task temp under results hash
`650fc312a36f4fa3db1505fb11c1922848e0ed7aec22791f424d0511fad2c484`.
Exact archive calls returned `archived:true` for every completed test task.

The first Astra High pass found three candidate defects. The scenario-table
stripper removed later normative text, same-task continuation could not pass the
native gate, and the built README omitted the required frontier-model minimum.
Follow-up `workflow-final-astra-high-20260925-02` confirmed the table and README
fixes, then found that reviewer continuation still used initial-creation
provenance.

The final correction separates new reviewer creation from same-task reviewer
continuation in the builder, native inspector, execution-memory transport and
activation contract. New reviewers use lifecycle `create` and
`create_thread` with the saved project. A retained reviewer uses a fresh
complete `SCOVILLE_DISPATCH_V1` prompt through lifecycle `message` and
`send_message_to_thread` to its exact task. Compact, unbound and
wrong-transport assignments remain rejected.

The final r3 source passed 90 Workflow tests, 23 suite tests and 46 canonical
shared build and export tests. Package verification covered six packages and
115 files. Skill Creator quick validation passed. The final build receipt is
`0fba8ea323665f68eee34ed95c6b882b09d1286fd3022e787eb316031f966e21`.
The Workflow file map is
`345c3f2707d2b883464b69b55c50218d67d726a50f78dc19564b32556ff207e6`
for 42 package files.

Astra High follow-up `workflow-final-astra-high-20260925-03` independently
checked the corrected reviewer path, all three role continuations, Compaction,
transport targets and the focused harness and returned `FREIGABE`. It reran
only the read-only Node transport harness. The 90, 23 and 46 test totals remain
coordinator evidence.

The authorized corrected Wrong-Role case `D02R1` ran against the same r3
candidate with `gpt-6-sol` at `medium`. Task
`01a0d7cc-8244-72b3-bc0b-cce1a0e7a7e9` returned the exact required block for
the foreign runtime task identity, matched the frozen oracle and performed no
project access, guard verification or project write. The prompt SHA-256 is
`e22d954935a6b5f4ef950ce6e3759ec9da0cbe58ce7fe1cd6b7ae6744767e635`,
the manifest SHA-256 is
`b80fe75aa7c8ee5d3007c213a7979366c8c7117d12bd1ea49c4d43a3e32aa4f8`,
and the result SHA-256 is
`4b0879bf2719b7392ba514dcde5c50436889d48c7b2fbd0c8e04a02325395cbe`.
The task was archived after its ID and result were retained. This closes the
only missing native case without changing the candidate package.
