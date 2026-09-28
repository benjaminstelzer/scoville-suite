# Code and UI release verification, 2026-09-28

Candidate: Code and UI v2.0.4, general and Codex suites v2.1.3.
All previously open Code, UI, README and comparison-evidence changes are
committed in c7ccf23. The source workspace remains the development owner.

Code now prefers the simplest adequate safeguard, distinguishes retained output
from resumable execution, and questions states introduced only by the design.
Useful recovery output remains available where permitted, without authorizing
premature completion or publication. Astra High reviewed the Skill and diffs,
identified that last distinction as ambiguous, and confirmed its correction.
No Skills were applied during authoring or that review.

UI owns new interface wording and consistent terminology, derives unsettled
task structure from user needs, and reassesses affected composition after edits.

## Checks

- 222 mechanical tests passed across shared, suite, Plan, Workflow, Ask and Setup.
- README and source projection checks passed. All three built package inventories
  passed: Codex suite, general suite and the two changed standalone Skills.
- Both changed Skills were installed for Codex and Claude. Installed runtime
  files match the built packages. Previous installations were backed up.
- Ran all 45 selected comprehension cases in fresh contexts with GPT-6 Luna
  Medium, plus four focused Code/UI cases. Native turn records confirm model
  and effort for every accepted run.
- 44 selected cases passed directly. Workflow-21 first attempted an unexpected
  collaboration tool call and was stopped by the bounded runner. Its fresh
  repeat left unavailable-current telemetry behavior ambiguous. A clarified
  fixture explicitly stating that no current value is available passed:
  continue without guessing or searching. All original evidence is retained.
- The four focused cases passed: unsaved result recovery, avoiding an invented
  execution lifecycle, new multilingual UI wording and local responsive
  composition. These are comprehension checks, not implementation comparisons.

There are 51 recorded runs: 49 accepted answers, one rejected transport and one
inconclusive answer resolved by the clarified fixture. This is not 45 direct
passes of the original prompts. Expected behavior was retained during the
clarification. Neither the gate nor the focused cases prove reduced
overengineering across repeated design/review/fix rounds or live integrations.

Raw prompts, frozen expectations, answers, native identity records, package
receipt, grading, installation records and publication verification are in
workspace temp/2026-09-28-code-ui-release/. Published packages must match the
tested runtime bytes. Existing Viewer assets retain their earlier provenance;
this release does not rebuild or retest the Viewer.
