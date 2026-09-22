# Workflow archive retest — 2026-09-22

SOL Medium coordinated four fresh Luna Medium cases against the built package
under workspace `skills/public/rollover-fix-2026-09-22/scoville/`. No live
Workflow action was executed by the tester. Cases and the hidden key were
frozen before execution; no retry or runtime change followed the answers.

| Case | Protocol | SOL semantics | Author disposition |
| --- | --- | --- | --- |
| archive-23 | PASS | PASS | Accepted: no native active proof inferred from guard or title. |
| archive-24 | PASS | PASS | Accepted: completed is not exact archived:true confirmation. |
| archive-active-chain | PASS | FAIL | Not accepted: incomplete explicit failure-path coverage. |
| archive-negative | PASS | PASS | Accepted: idle, placement, availability and incomplete-turn guards preserved. |

The chain answer correctly selects `recover_rollover_archives`, accepts fresh
native active status despite list omission, and requires sequential exact-ID
verification with retained receipts. It omits the key's explicit stop on an
unknown/failed archive response, preservation of remaining targets, and current
coordinator exclusion. Sequential required verification suggests fail-closed
intent, but does not fully demonstrate those mandatory behaviors. Preserve SOL's
failure; do not claim a demonstrated unsafe call or a complete comprehension pass.

The author independently read every final answer and checked all 16 native
Luna/medium contexts, complete event streams, zero exits, empty stderr, clean
process results, 19 delivered-file hashes and all 28 package-file hashes.
All four cases took four turns. The shared case-file preamble was omitted from
initial prompts; no answer blocked on that omission. This limits the frozen
prompt provenance and must not be silently changed in a repeated run.

## Reproduce and resolve

Use [codex-cli-execution.md](codex-cli-execution.md), the exact four cases in
[workflow-archive-cases.md](workflow-archive-cases.md), and the separate hidden
[key](workflow-archive-expected.md). Preserve this attempt. Before publication,
resolve the chain-case comprehension gap and rerun that case against the final
built package. Include its complete hypothetical setup and explicitly exercise
an unknown/failed middle archive response; freeze any revised case separately
before execution. Do not add hints from this answer or weaken the existing key.

Raw prompts, commands, answers and protocol evidence remain in workspace
`temp/2026-09-22-workflow-archive-luna/`. `frozen/frozen.json` records all input
and package hashes; `semantic-grades.json` contains SOL's independent reasons.

- Frozen manifest SHA256: `99c4e5563d567b5b581b2e0d2d65fab329da6baed795cf20ddbb88112bf9519b`.
- Build receipt SHA256: `6e462e3e17e5c114a5576aa91311ed72962b8ca0365e85dae9fdc0591351c4d4`.
- Cases SHA256: `b265c42c1ed9a79411794d90c9a97c6d922c2f0b941002f3001a91d1fa8207ad`.
- Hidden key SHA256: `30899973eae771f86318daf44f32557cef2aef0e16dbdbf2e51f70d51679097c`.
- SOL grades SHA256: `bed994027e8533d9618a8234d8a97874e6ae0a37b5fad4b7db1d8870605116a1`.

The changed runtime package matches current sources. Its receipt retains the
original pre-commit build provenance; it is not a final clean-release receipt.

## Instruction correction and bounded retries

The shared contract now gives an ordered archive loop: predecessor IDs only,
never the current coordinator; exact verification before the next target;
failure or unknown reply stops the loop and retains the chain, verified receipts
and all unverified targets. No helper logic or key changed. Both suites bundle
the updated source; the built Codex contract was installed with a backup under
workspace `state/2026-09-22-rollover-wording-fix/`.

The r2 build under `skills/public/rollover-fix-2026-09-22-r2/scoville/` differs
in only `scripts/rollover_readiness.md` among the 28 Workflow runtime files.
Its SHA256 is `2bf23fe34d709e52a781edd9d051b214eca6d2c0e09a422d4512ce9775049e49`.
Current-source package verification and all 11 rollover tests pass.

SOL coordinated two bounded attempts of the unchanged chain case and key:

- R2 reused the original initial prompt. Four valid READ turns exhausted the
  limit before an answer; the last request was the changed contract.
- R3 supplied the exact core and operations invariant text upfront, following
  the existing context-test transport, and restored the shared hypothetical
  setup. Four READ turns again exhausted the limit; the last request was the
  lifecycle contract. No phase-specific hint or key was supplied.

Both are `turn_limit_without_final_answer`, semantic `NOT_GRADED`, not new
Skill failures or passes. SOL verified eight native Luna/medium contexts and
clean tool-free process results. Raw evidence remains under workspace
`temp/2026-09-22-workflow-archive-luna-r2/` and `...-r3/`.
Frozen manifest hashes are respectively
`357ee03d28a58c1e59975ac300b27af0910620dfdd7a335216a55231247cdac6`
and `06558de7002e12a16bdbd461e2b01c42851ef97f19ec5161a64d72fa24a7e298`.

No further retry was made. The wording correction is implemented; model
comprehension remains unverified. Before another model run, resolve the bounded
reference-delivery issue without weakening the fixed semantic key or silently
extending the qualified runner limits. Publication remains open for this case.

## Authorized eight-turn qualification — accepted

The user then explicitly authorized raising the test limit. The runner now
defaults to eight turns and accepts 1–8; explicit four-turn historical runs
remain reproducible. All 18 offline tests pass, including fifth-turn completion
after four READs and failure when an explicit four-turn budget is exhausted.
Timeout, isolation, path, hash, event and native identity checks are unchanged.

R4 uses the original initial prompt and hidden key, unchanged r2 package,
and the new runner with `--max-turns 8`. It completes in six turns: five READ
exchanges and a final answer. SOL semantic PASS and independent author acceptance
confirm all required behavior: exact active status can replace list membership;
only returned predecessors may be archived; never the current coordinator;
exact archived:true verification and retained receipt precede each next target;
failed or unverified replies stop the chain while preserving outstanding targets.

The author independently checked all six native Luna/medium contexts, complete
event streams, clean exits/stderr/process results, six delivered hashes and
the unchanged initial prompt. This qualifies the extended runner through real
continuation beyond turn four and closes this chain-case comprehension gap.
Earlier failures remain historical, not relabeled. No publication is claimed.

Evidence: workspace `temp/2026-09-22-workflow-archive-luna-r4/`.

- Runner SHA256: `ce08138d98d846bcd5d29a6324469ef8bab3b80e9ae5fbab2d400b3a39fc2009`.
- Frozen manifest SHA256: `0c4325514644a0a46f347c52283e300ca1a578e8ff5d414d91bb9706837b2149`.
- SOL grade SHA256: `25786313b84f1221aaca3521b886a5f40798be8f86a8cb6f9d9941206d7e95c7`.
- Package receipt SHA256: `5c2b12d11674d35dca10f1d0714578290d4c457de732f2bf5ff2524523f9fdc7`.
