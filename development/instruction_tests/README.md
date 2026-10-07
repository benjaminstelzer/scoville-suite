# Instruction test catalog

`catalog.py` is the portable entrypoint for the private PLAN-0034 dataset.
`dataset.json` pins its files by SHA-256. The dataset is deliberately outside
the exportable repository; missing or changed data is unverified and exits 3.
Invalid CLI syntax exits 2. Neither produces partial successful output.

```text
python development/instruction_tests/catalog.py --data-root <private-dataset-directory> --skill scoville-ui
```

Use `scoville-project-context-cleanup` for Cleanup, or omit `--skill` for all cases.
Successful stdout is one ASCII-escaped JSON document, valid UTF-8 on every host.
The default `--view questions` contains only the request and explicitly visible
prior conversation, with opaque case IDs. It excludes files, tool state, expected
activations, grading keys and semantic Skill labels. `--view keys` supplies the
matching evaluator keys. `--view runner` supplies private fixture materialization,
tool behavior, preconditions and context-package routes. Never send it to the model.
`--view catalog` exposes the full case definitions only for review and runner setup.
Use `--selection involved` with `--skill` for every trigger where that Skill is
required, allowed or forbidden, as well as its own cases. Final suite trigger
acceptance must use the full catalog, not separate owner-only subsets.

The reader does not invoke a model, mutate fixtures or authorize execution.
`fixtures.json` pins literal input files, requests, runtime prerequisites and
observable checks. `environments.json` pins trigger states and conversation
preludes. The runner must prepare the pinned tool/runtime prerequisites and
verify required real prelude reads before the scored turn. Those setup checks
are evaluator/runner-only metadata; never forward the full catalog to the model.
File contents become model-visible only through permitted actual tool results.
Context-package routes configure available read tools; they do not preload text.
Record the host-local execution date before dispatch for date-based checks.

Keep hypothetical comprehension separate from observed compliance and effects.
W-001 supplies isolated runners; W-014 performs authorized tests. A model runner
must receive questions without expectation keys. The independent evaluator
receives hidden expectations and anonymized results, not the change rationale.
Record all attempts and transport failures. Never adjust expectations to answers.

## Model-free preparation and grouped evaluation

`prepare.py` verifies the frozen dataset and selected build receipt, then creates
one fresh private directory. `workspace/` contains literal fixture files,
`host-home/` contains fresh host directories, and `question.json` contains only
visible conversation. Only `<FIXTURE_ROOT>` is expanded. The evaluator key and
runner prerequisites are written under a required `--private-output` in a
separate tree, not inside, above or directly beside the run directory. Preparation
metadata stays there too. The old W-001 preparations are historical and must not
be launched. This separation is not an OS read barrier: shell/browser cases must run in an environment that
cannot read those keys, the real home or live projects. Do not launch them until
that isolation is qualified. No credentials or installed Skills are copied.

```text
python development/instruction_tests/prepare.py --data-root <private-dataset> --case-id <catalog-id> --variant codex-suite-luna-high --package-root <built-suite-root> --receipt <build-receipt.json> --output <runs/case> --private-output <vault/case>
```

The preparation records hashes, requested identity and unmet prerequisites.
The two Plan comprehension cases requiring both General and Codex comparison
roots are rejected before output creation until a multi-root serving route exists.
`prepared_not_executed` proves only preparation. Native handles, real prelude
reads, partial-read tools, Git state, WordPress and browser evidence require their
actual consumer. Files alone do not satisfy them. UI HTML fixtures can be served
with `python -m http.server --bind 127.0.0.1 --directory <workspace> <port>` in an
isolated environment; view and interact with them before claiming browser proof.
Setup fixtures use the built Setup helper and the actual built Ask resolver,
with `--project-root <workspace>`. Never use the real project for this check.

`trigger.py command --codex <executable> --prepared <runs/case> --private-prepared <vault/case>` emits a
proposed argv, environment overrides and cwd, never launches a process. It
enables Skill discovery and shell with read-only sandbox settings. All isolation
settings repeat on `--thread-id <exact-id>` resume. Discovery payloads retain
the sibling member layout in the isolated Codex home. Verify the full required
host catalog before launch, particularly Codex standalone Ask cases whose build
receipt alone does not supply the other Codex Skills.
`trigger.py observe --events <target-turn.jsonl> --skills-root <isolated-skills>`
recognizes an absolute-path Get-Content/cat/type command, directly or inside one
explicit PowerShell `-Command` wrapper, whose successful output contains the full
expected SKILL.md. Windows backslashes are preserved. It ignores claims and
failed reads. Complex wrappers, truncated, implicit, Claude and unknown reads
remain unverified until qualified against actual host events.
Positive read signals do not prove use or absence of other activation.

Use exactly one retained register for all PLAN-0034 Luna attempts:

```text
python development/instruction_tests/evaluation.py init --register <private-attempts.jsonl>
```

The Codex comprehension runner requires this `--register`, a separate
`--host-home`, `--preparation <private-preparation.json>` and an explicit
`--run-set <evaluation-revision>`. The preparation binds case ID, dataset registry,
variant, candidate receipt and exact generated prompt before reserving a run.
The separate `--catalog` is the model catalog, not the case dataset. Change that label
after corrections to a candidate, prompt, model catalog, CLI binary or runner.
Every reservation counts toward 300, including crashes and
transport failures. Preserve incomplete attempts and never create a replacement
register to gain budget. READ continuations stay within that attempt's existing
eight-turn bound. Use `--receipt-member @suite` with a suite root, or the member
name with a standalone Skill root. Suite READ paths retain `packages/<member>/<member>/`.
All requested files are receipt-verified. Authentication must be provisioned and
host isolation qualified separately, without exposing credentials in evidence.

After collecting at least three evaluable runs per selected case variant, prepare the
whole test group once, instead of interleaving tests and individual reviews:

```text
python development/instruction_tests/evaluation.py group --data-root <private-dataset> --register <private-attempts.jsonl> --case-id <catalog-id> --run-set <evaluation-revision> --output <new-private-review-directory>
```

This route currently supports comprehension results. It requires every registered
attempt in that revision and group to have a terminal summary. It verifies manifest
identity, the frozen case/prompt, identical input/runner hashes and identical
`max_turns`/`timeout_seconds` within each selected variant. Older
revisions remain charged, are recorded as excluded in `selection.json`, and never
fill the current repetition count. Mixed identities inside one revision fail.
Transport and harness failures stay separate from semantic results and do not
satisfy the minimum. Observed model behavior failures such as an unmanifested or
duplicate READ and exhausting the turn limit count as fixed FAIL, not as missing
transport. The local consumer can parse `assignment.json` directly
as native spawn arguments for **gpt-6.1-sol/high** with fresh context, after review
authorization. Use an opaque review directory name. The assignment reads only the
complete blinded `review.txt`; it permits no other tools or file reads. The
question, expectations, supplied text and shuffled opaque run
IDs are visible to the judge; model identity, result paths and source IDs stay in
`mapping.json`. Preserve the original answer and judge result. Actual judge
execution and semantic grading remain unverified until observed.

Use `evaluation.py score --group <review-directory> --judgment <judge-result.json>`
to consume the grouped judge response. It preserves fixed failures, requires
complete IDs, and calculates per-variant results. Mixed judgments need five
evaluable runs within the shared 300-attempt cap. Unknown judgments cannot yield a
pass. No subset of successful transport can silently satisfy the three-run
minimum. The prepared assignment is not an actual Sol execution.

ADR-0162 required external Opus 5.5 review before model tests and Sol judging.
Opus v4 now gives conditional approval for comprehension only. Its two real host
controls must pass before case tests. ADR-0165 supersedes the later review stop
and commissions a fresh Astra/high full review plus plan execution. Its three
findings are corrected locally. The runtime catalog is cases-v10. It retains
the v9 cases except for explicit prerequisites in three clarified comprehension
cases; their expectation lists are unchanged. Earlier datasets, imported cases,
runner sources and original results remain in the private test project.
Claude comprehension/trigger execution remains unverified. No prepared command,
fixture, double or CLI help output establishes host safety or Skill acceptance.

New data revisions need an explicit reason and new identity. Preserve earlier
data and raw results in the private test project. Model selection, total budget,
transport limits and native probes still require their recorded approvals.

The comprehension host must exclude ambient project instructions as well as
native tools. `--ignore-rules` disables execpolicy files, not AGENTS.md discovery.
The runner sets `project_doc_max_bytes=0` on initial and resumed calls and rejects
native traces containing an injected AGENTS.md instruction message. Qualify the
actual model-visible inputs, not only tool outcomes. The same CLI's
`debug prompt-input` can test discovery without a model call. The optional real
host regression uses `CODEX_TEST_BINARY` and `CODEX_TEST_CATALOG`; its positive
ambient-loading control must reproduce the defect before the fixed route passes.
The 194 selected-v9-r3 attempts contain ambient test-project rules. Their original
grades remain recorded and charged, but do not establish isolated comprehension.
Use a new run revision for corrected inputs; do not replay or silently relabel r3.

Each run saves `model-instructions.md` and uses that exact file for initial and
resumed CLI calls. Group preparation verifies its recorded hash and includes the
frame in each blinded result. Missing or changed framing invalidates preparation.
The judge reports a conflict between frame and expectations as UNVERIFIED while
preserving fixed observed failures. Model identity and source result paths remain
private. `SCOVILLE_TEST_DATA` and `SCOVILLE_TEST_BUILD` enable the model-free
integration checks for this actual packet consumer.
