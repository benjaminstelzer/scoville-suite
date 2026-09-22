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
