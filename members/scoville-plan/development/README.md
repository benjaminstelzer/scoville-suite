# Development

The [member source](../scoville-plan/) is part of
[Scoville Suite](../../../README.md#development-and-builds). Build the Skill
before you install it. Development files stay in the suite. The read-only
profile validator ships with the Skill. General packages offer a manual route
without Python, while Codex requires the helpers. Fixtures and Viewer sources
stay in development.

## Validate

Run these checks from `members/scoville-plan/` in the suite:

```text
python -B -m unittest discover -s development/tests -v
```

For Viewer changes, run from `development/viewer`:

```text
npm ci
npm run check
cargo test --manifest-path src-tauri/Cargo.toml
```

These checks cover the native profile structure and the Viewer's behavior.
They don't prove that agents follow the Skill or that file writes are
transactional.

## Retention

Tests, fixtures, Viewer source, dependency locks and this summary are kept.
Benchmark profiles, token measurements, model outputs, audits and reviews go
to temporary storage. An evaluation summary stays only if it teaches
something useful and a published release links to it.
