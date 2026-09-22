---
format_version: 1
id: ADR-0021
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/execution-routing
supersedes: ADR-0019
---

# Keep execution overrides in existing Step text

## Decision

Record an explicitly selected executor model or reasoning effort only in a strict `[execute: ...]` annotation in existing Step prose. Add no Work Item field and make no Viewer data-model change.

## Problem

A new Work Item field expands the native Plan schema and Viewer surface even though the point-scoped choice can remain in the existing Step text.

## Drivers

- Existing format-version-1 projects must remain readable without migration.
- The selected pair must remain visible in the exact Plan point it governs.
- The user explicitly rejected a new Work Item field and new Viewer binaries for this change.

## Considered alternatives

- Add a Work Item field plus Step annotation: Supports two scopes but expands the schema and Viewer.
- Use only a Step annotation: Preserves the existing field set and still gives the dispatcher a strict point-local source.
- Put the choice in Goal prose: Avoids schema work but makes a point choice global and repeats it in unrelated dispatches.

## Consequences

- A `todo` Work Item without Steps receives one behavior-complete annotated Step when an explicit pair must be retained.
- The dispatcher resolves each property from the Step annotation and then the route default.
- Existing Viewer binaries need no replacement because Steps already render as text.
- Reviewer and coordinator routing remain unchanged.

## Confirmation

1. Remove the Work Item field, Viewer model, rendering, and binary-release scope from the implementation.
2. Validate old DIVI and EMPCO profiles with the corrected validator.
3. Cover valid, malformed, reversed, and duplicate Step annotations in validator tests.

## Revisit when

Reconsider only if an explicit pair must govern a Work Item that cannot be represented by a Step before start.
