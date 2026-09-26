# Evaluation execution

Owner: SOL coordinator (`gpt-6-sol`, `medium`). Subject model:
`gpt-6-luna`, `medium`. The host advertises both combinations; successful
execution and actual metadata remain unverified until observed.
Never substitute. Existing historical agent runs do not count toward this gate.

## Freeze before dispatch

1. Verify public packages against both receipts with the shared package-set
   checker. Verify the private Workflow package separately. Compare current
   source payloads using the suite builder, not only receipt hashes.
2. Record exact package paths, every package file hash, receipt hashes and all
   case/key file hashes in one evaluation manifest. Preserve the private
   Workflow path from build-evidence.md. Include the runner instructions' hash.
3. Keep expected files evaluator-only. Give each Luna case only its numbered
   prompt, common case header, needed hypothetical inputs and built Skill
   content. No private source templates, answer keys or previous responses.

## Run and grade

- One fresh context per case, no forked conversation. Cases 01-05 receive only
  discovery frontmatter; other cases receive core and access to packaged
  references/helpers. Hypothetical role markers never activate real work.
- Give SOL access to frozen keys for grading, not permission to rewrite them.
  SOL may delegate only the authorized Luna cases. No adviser/provider calls,
  live task creation/archival, project edits or publication inside simulations.
- Start with one case to verify transport, requested and observed model/effort,
  fresh-context isolation, answer capture and key separation. This case counts
  only if every gate holds. Infrastructure failure is not a Skill failure.
- Record each case ID, package hash identity, requested and observed model/effort,
  native execution handle, raw-answer path, verdict and criterion-specific
  explanation. Missing actual metadata is a gate gap, never an inferred match.
- Grade required actions and forbidden actions separately. Equivalent wording
  is valid. An answer that states the rule but then violates it fails. Preserve
  incomplete results and infrastructure errors, never manufacture an answer.
- Retain fresh handles until terminal output is captured. A timeout is not a
  terminal failure. Respect observed capacity and documented slot lifecycle;
  do not assume interrupt/archive frees an agent slot.

## Evidence and correction

Raw prompts, answers and traces belong under workspace
`temp/2026-09-21-suite-luna-evaluation/`. Keep only the concise result matrix and
references in this development directory. No raw transcript release is implied.

The author reviews SOL's judgments. Fix evidenced Skill defects in canonical
sources, rebuild and rerun affected cases plus relevant regressions. A defective
test requires an explicit versioned correction, not a silently fitted key.
Changed package or test hashes invalidate affected prior results. All 45 cases
selected by `selected-cases.json` must pass with verified settings and no
unresolved findings before the gate passes. Theoretical success neither proves
live integrations nor authorizes publication.
