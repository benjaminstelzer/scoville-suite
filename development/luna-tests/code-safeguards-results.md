# Code safeguard comparison

Date: 2026-09-28. Baseline: Git `5fc235bb94bdcc87dd89421cc213b910baf54085`.
Scope: Scoville Code core, Change and Validation references. No publication or installation.

## Source changes

- Core: size safeguards by affected parties, detection and reversibility; each
  additional safeguard needs a requirement or concrete failure mode.
- Core: async fan-out/fan-in is High only when partial failure can lose or
  duplicate durable external effects. Other High triggers remain unchanged.
- Core: the integrity floor does not invent persistence or proof requirements.
- Change: new functionality starts with the simplest complete implementation.
- Change: agent-facing output is directly usable and errors give corrective guidance.
- Change: only required durable state needs storage-before-completion tracing.
- Change: flag ungrounded or disproportionate safeguards and unactionable errors.
- Validation, added after the comparison: changed safeguards must allow valid
  use and prevent the concrete failure at the actual affected boundary; early
  failure does not prove protection at a later step.

No new risk classes or technology bans. Bugfix rules and required safety,
authorization, privacy and validator protections remain intact. Initial source
growth before the follow-up review: core +569 bytes, Change +707 bytes,
Validation +204 bytes. Follow-up changes and comparisons are recorded in
`code-safeguards-open-review-results.md`.

## Method

Prompts: `code-safeguards-cases.json`. Five tasks, SOL and Astra Medium,
three variants: explicitly no Skills, previous Code, updated Code. Fresh
ephemeral CLI invocation for each cell; same task and output schema. Code
variants receive the complete rendered standalone instructions and references;
other Skills are explicitly excluded. The control explicitly forbids loading,
invoking or applying any Skills. Initial control runs lacking that explicit
instruction were superseded and excluded.

CLI options additionally disable automatic Skill discovery, project document
loading and tools. These settings are not proof of a fully isolated host.
Models generate a Python module as text. Inspected modules run on disposable
local fixtures, not live systems. This is not a complete sandbox or an offline
model: inference uses the model service. No real chat handoff is dispatched.
CLI: 0.158.0-alpha.2. Completed event items contain only agent messages, no tool
calls. The models did not execute tests or receive fixture failures for repair.

Raw prompts, rendered baseline/current texts, commands, responses, generated
modules, fixture checks and initial excluded controls are in workspace
`temp/2026-09-28-code-safeguards/`. The existing Luna comprehension runner was
not changed: it does not support these models or implementation testing.

## Repository checks

- `python -B ../shared/build/run_portability.py --root . --shared ../shared`:
  222 tests passed across six nonempty test paths, including package builds.
- `python development/build_suite.py --check-readmes`: passed, no stale previews.
- `python development/build_suite.py --check-sources`: passed, no stale projections.
- `git diff --check`: passed after source edits.

## Behavioral results

All 30 generation calls succeeded. Basic fixture acceptance passed in 25/30.
Cells below show physical source lines / fixture result, not quality scores.

| Model / task | No Skills | Previous Code | Updated Code |
| --- | --- | --- | --- |
| SOL selector | 45 / pass | 39 / pass | 42 / pass |
| SOL handoff | 61 / pass | 48 / pass | 61 / pass |
| SOL migration | 87 / pass | 78 / pass | 117 / pass |
| SOL cleanup | 97 / pass | 135 / pass | 63 / pass |
| SOL bugfix | 5 / pass | 5 / pass | 5 / pass |
| Astra selector | 61 / pass | 64 / pass | 67 / pass |
| Astra handoff | 77 / pass | 79 / pass | 70 / pass |
| Astra migration | 179 / fail | 187 / pass | 165 / fail |
| Astra cleanup | 227 / fail | 192 / fail | 138 / fail |
| Astra bugfix | 5 / pass | 5 / pass | 5 / pass |

Fixtures exercise selection order, empty and malformed plans; handoff writing,
reading and malformed snapshots; migration preview, row preservation, usable
backup, existing-target refusal and rollback after injected DROP failure; cleanup
preview, selected deletion, unrelated-file preservation and a static junction;
bugfix selection, identity and unchanged inputs. A failed happy path leaves later
checks unverified. Astra's updated migration uses renames; its earlier backup
failure prevents verification, including of its alternate migration boundary.

### Findings

- Updated operator helpers give clearer corrective diagnostics. Both models'
  updated handoff errors say to write/rewrite the snapshot. Astra's updated
  selector says to correct JSON, save UTF-8 or check a readable path. Previous
  versions often name only the fault; some already give corrective guidance.
- No hashes, receipts, locks, retries or generation machinery occur in the
  selector/handoff outputs in any retained variant. These small tasks therefore
  do not reproduce the reported large-project overengineering pattern.
- All six bugfix outputs make the same five-line correction without expansion.
- All SOL migrations and Astra's previous-Code migration pass the exercised
  critical checks. Astra's no-Skill and updated-Code outputs call `os.fsync()`
  on a read-only backup descriptor; Windows returns `Bad file descriptor`.
  Both stop before migration and preserve source rows, but do not deliver it.
- Astra's no-Skill cleanup refuses Windows apply operations. Previous/updated
  Code versions falsely report changed entries: `DirEntry.stat()` returns zero
  device/inode fields here while `os.lstat()` returns actual values. Ordinary
  use fails; early refusal does not establish later race protection.

### Additional concurrency probe and repeat

For SOL's initially working cleanup outputs, replace a checked subdirectory
with a junction immediately before scanning it. The target points to another
disposable fixture directory outside the supplied cleanup root. No real data
is involved. Previous Code preserves that outside file; no-Skill and updated
Code delete it. Static-junction acceptance alone missed this failure.

Repeat generation once for all three SOL cleanup variants, using unchanged
prompts and fresh contexts: 116 / 77 / 55 lines (none / previous / updated).
All three repeats fail ordinary Windows fixture use because of incompatible
identity comparisons. The previous-Code repeat exits before race injection;
the others refuse deletion for the same identity mismatch. None establishes
both working normal behavior and correct race protection. Astra's three
initial outputs likewise fail before this race can be meaningfully exercised.
No generated solution was repaired or silently substituted.

Two harness corrections are retained in raw evidence: temporary-directory
cleanup encountered a host file lock, so fixtures are now retained; the DROP
probe now observes reaching the operation instead of requiring the returned
error text to expose the injected message. Neither changes required behavior.

### Size and defensive-code indicator

An AST indicator counts statements in exception handlers, finally blocks and
branches directly raising errors, excluding imports, definitions and docstrings.
It includes useful diagnostics and is not a semantic measure of unnecessary
guards or all recovery code. D/R below means defensive / remaining statements.

| Operator task | No Skills D/R | Previous D/R | Updated D/R |
| --- | --- | --- | --- |
| SOL selector | 7/17 | 9/16 | 8/14 |
| SOL handoff | 11/12 | 7/11 | 7/11 |
| Astra selector | 13/19 | 10/22 | 11/19 |
| Astra handoff | 11/12 | 10/18 | 10/16 |

Full counts are in temporary `metrics.json`. Neither this indicator nor source
size shows a consistent reduction; more actionable errors can require more text.

## Conclusion and next review

The wording changes are implemented and repository checks pass. The sample
supports improved diagnostics and a preserved narrow bugfix, but does not
establish reliably reduced overengineering or preserved critical safety.
Critical behavioral acceptance remains open. Do not treat these results as
release approval or infer that Code caused the model failures.

Following user approval, the existing Validation paragraph was refined to
require valid use plus prevention of the concrete failure at the actual
boundary. Early refusal is not proof of protection at a later boundary.
Windows-specific API failures stay in the fixtures. This refinement was made
after the 30 comparisons and three repeat generations. Those results describe
the earlier candidate, not the final Validation wording. No claim that this
refinement fixes model behavior has been established.

## Limits

One initial sample per cell cannot establish causality or reliable model rates.
Small functions with specified interfaces do not reproduce a long autonomous
project. All references are supplied up front, so routing and token savings are
not evaluated. This is code-generation evidence, not a test of the Skill's full
implement/test/repair workflow. Passing fixtures establish only the exercised behavior.
Handoff checks cover returned prompt contents, not a second chat's consumption.
Windows checks do not establish POSIX behavior or complete concurrency safety.
No guard is classified as unnecessary merely because it increases code size.
