# Code reference selection

Observed against the original frozen package:

- code-07 and code-08 loaded core and all three references in one tool call.
  Planning was unnecessary. A correct final route label did not reflect reads.
- code-07-v2 and code-08-v2 obeyed explicit core-first wrapper guidance.
  This is guided evidence, not repair proof for the original package.

Canonical change: Code SKILL.md now explicitly requires reading the core before
selecting references, then reading selected references only. Route predicates,
risk rules, mode rules and expected test answers are unchanged.

The current public package remains frozen for the baseline batch. After it
finishes, rebuild Code from source, freeze the new hashes separately, and rerun
affected cases plus regressions through SOL/Luna Medium. The regression wrapper
must retain the scenario-versus-classifier clarification but omit core-first
coaching; the Skill itself must supply that instruction. Preserve old runs.

Status: source clarification only; build and behavioral repair proof pending.

Structural check: skill-creator quick_validate rejects the existing
`compatibility` frontmatter field in both original public package and edited
source. This is unchanged validator incompatibility, not a passing check.
Public baseline core hash still matches evaluation-manifest.json.
