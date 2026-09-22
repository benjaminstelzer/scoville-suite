# Development

The [member source](../scoville-plan/) belongs to [Scoville Suite](../../../README.md#development-and-builds).
Build the Skill before installing it. Development files stay in the suite. The optional read-only
profile validator is bundled with the Skill. Fixtures and viewer sources are not.

## Validate

Run these checks from `members/scoville-plan/` in the suite:

```text
python -B -m unittest discover -s development/tests -v
```

For viewer changes, run from `development/viewer`:

```text
npm ci
npm run check
cargo test --manifest-path src-tauri/Cargo.toml
```

These checks cover native profile structure and viewer behavior. They do not prove agent compliance or transactional filesystem writes.

## Retention

Keep current tests, fixtures, viewer source, dependency locks, and this maintenance summary. Create benchmark profiles, token measurements, model outputs, audits, and review packets in temporary storage. Retain a concise evaluation summary only when it explains a useful result or
development lesson and a published release links it. Routine checks and
inconclusive miniature runs stay temporary.
