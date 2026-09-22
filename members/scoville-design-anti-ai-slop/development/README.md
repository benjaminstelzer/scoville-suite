# Development

The [member source](../scoville-design-anti-ai-slop/) belongs to [Scoville Suite](../../../README.md#development-and-builds).
Build the Skill before installing it. Development files stay in the suite.

## Validate

Run these checks from `members/scoville-design-anti-ai-slop/` in the suite:

```text
python -B -m unittest discover -s development/tests -v
python -B development/scripts/validate_package.py --root scoville-design-anti-ai-slop
python -B development/scripts/validate_design_ui_boundary.py
```

The validator checks the canonical module registry, generated router, source IDs, package files, links, examples, and Design/UI ownership boundary. These deterministic checks do not establish visual quality or a general model-performance result.

## Retention

Keep current package tools, tests, and this maintenance summary. Generate render iterations, browser state, benchmark corpora, model transcripts, blind-review packets, audits, and research working notes in temporary storage. Retain a concise evaluation summary only when it explains a useful result or
development lesson and a published release links it. Routine checks and
inconclusive miniature runs stay temporary.
