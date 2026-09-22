# Development

The [member source](../scoville-workflow-for-codex/) belongs to
[Scoville Suite](../../../README.md#development-and-builds). Build before
installing. Development files stay in the suite, whose root Plan owns current
work. Member Plans are historical records.

## Validate

Run the focused contract suite from `members/scoville-workflow-for-codex/`:

```text
python -B -m unittest discover -s development/tests -v
```

Run package validation against a generated build. Validate the planning profile
at the suite root. Contract tests cover source rules, not the live task lifecycle.
See the suite's [context-fix evidence](../../../development/workflow-context-fix.md)
for the bounded runtime and model checks.

## Installation identity

Install only the generated package. Before replacing an existing installation,
wait for every workflow using it to become terminal. Then compare the complete
build and installed inventories and file content. Do not infer adoption from a
copy command alone.

## Retention

Keep current tests, Plans, Decisions, and this maintenance summary. Store raw
model reviews, transcripts, screenshots, and one-off runtime evidence in
temporary task storage unless a published artifact explicitly depends on them.
