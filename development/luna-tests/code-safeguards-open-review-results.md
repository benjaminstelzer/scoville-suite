# Code follow-up: open design and review

Date: 2026-09-28. Original baseline: `5fc235bb94bdcc87dd89421cc213b910baf54085`.
This comparison uses the original Skill, the final follow-up text and an
explicit no-Skills control. It does not isolate each individual wording change.

## Follow-up changes

- Validation: restrict the new safeguard check to material failures. Distinguish
  early rejection from a stale successful check; a checked path can change
  before deletion. Preserve the existing bounded-evidence paragraph.
- Change: restore the exact original retry/cancellation/timeout condition:
  request, existing contract or observed failure.
- Core: internal tooling is neither inherently harmless nor inherently critical.
- Review: a requested safeguard needs a consequence that justifies it;
  a conceivable edge case alone is not a finding.

## Comparison

Inputs: `code-safeguards-open-review-cases.json`. SOL/Astra Medium, one fresh
context per task and variant: 12 calls. Explicitly forbid all Skills in the
control and all other Skills in the two Code variants. Complete standalone
Code text/references are supplied. The open design chooses its interface and
files; the synchronous host worker adapter is the only prescribed interface.
The review task supplies a deliberately small implementation and its actual
limited purpose. No real host adapter or external chat is invoked.

Tool-free generation, followed by source inspection, is not a sandboxed
autonomous implementation/review/fix workflow. No claim of that stronger test.
Raw inputs, answers, commands, rubric and checks remain in workspace
`temp/2026-09-28-code-safeguards/open-review/`.

## Review observations

Unjustified demands for extra safeguard machinery: 0 in all six answers.
Five answers have no findings. SOL with final Code reports that `Exception()`
produces an empty error while the next action asks the user to inspect it.
This is reproduced directly; an exception-type fallback is a bounded diagnostic
fix, not additional integrity/recovery machinery. Other answers were not given
that observation. This task does not reproduce review-driven overengineering.

## Open-design observations

All 12 calls completed. Each design supplies an implementation, invocation and
test-double checks. All 12 Python blocks (implementation plus tests) compile.
Physical lines below are descriptive, not a quality metric.

| Model | No Skills code/tests | Original code/tests | Final code/tests |
| --- | --- | --- | --- |
| SOL | 187/52 | 128/45 | 187/64 |
| Astra | 252/103 | 150/129 | 154/138 |

- SOL without Skills adds an assignment lock despite the single-coordinator,
  single-worker sequential contract. This is a concrete unnecessary mechanism.
  Its Git snapshots are context, not integrity proofs; a file called manifest
  is not classified as overhead merely by its name.
- SOL original uses one saved record per task and a direct assign/resume flow.
  Final Code instead separates assign/run/resume/retry and maintains a task
  history plus status gates. That is more machinery than the original output;
  the explicit manual retry command is not an automatic transport retry loop.
  The new wording has not established a consistent simplicity improvement.
- Astra without Skills chooses SQLite, a single-active-task index, attempt
  counters, claim/finish transitions, retry and manual recovery. The original
  and final Code outputs use one JSON record per assignment and manual creation
  of a fresh assignment after failure. SQLite itself is not a finding, but
  the additional lifecycle/recovery workflow is not required by this prototype.
- All variants store results, as later-session continuation requires. JSON
  versions use temporary-file replacement and fsync. These mechanisms can
  protect required saved output; their mere presence does not establish
  overengineering. No output adds content-proof hashes, receipts or generations.

One execution attempt on SOL's original output hit local file-lock failures:
generated tests errored during temporary-directory removal; a retained-fixture
check completed the successful handoff but later failed at `os.replace` while
saving a worker failure. The error path is not verified. No generated code was
repaired, and there is no claim that all six prototypes execute successfully.
Source/syntax evidence is separate from runtime evidence.

## Conclusion

The follow-up text implements the four review recommendations. The open task
now exposes some unnecessary machinery, particularly in the no-Skill designs.
However, final Code is not consistently simpler than original Code, and the
review task produces no unjustified machinery requests in any variant. These
observations do not demonstrate that the final wording reliably prevents
overengineering. Multi-round review/fix behavior remains untested.

## Checks and limits

- 32 suite/build tests passed against these final source edits.
- Source projection check and scoped whitespace check passed.
- The previous 222-test run predates these four follow-up edits; it is not
  described as a fresh full-suite pass.
- Neither a single sample nor fewer lines establishes an improvement.
- There are no repeated review/fix rounds, real chat consumption or production
  safety tests in this comparison. Earlier critical failures remain relevant;
  this comparison does not establish that the final wording fixes them.
