---
format_version: 1
id: ADR-0097
status: accepted
created: 2026-09-26
accepted: 2026-09-26
scope: suite/release-2-0-2
---

# Release after the targeted Luna tests

## Decision

Release both suites v2.0.2 and changed standalone Code v2.0.1, Handoff
v2.0.19, Plan v1.9.1, UI v2.0.1 and Ask v1.0.2 with the reported test limits.
Workflow remains exclusive to the Codex suite. No additional Luna series is
required for this release.

## Problem

The targeted tests retain comprehension gaps and do not prove live delivery.

## Drivers

- After the result and open issues were reported, the user instructed:
  "Mache weiter mit dem vollständigen Release".

## Considered alternatives

- Continue withholding publication: not the user's selected next action.

## Consequences

This release-specific direction overrides the unresolved-comprehension block.
It does not turn failed tests into passes or change future release gates.
Build integrity, visibility, source history and remote asset checks remain required.

## Confirmation

Retain all test results and verify the published trees, tags and assets.

## Revisit when

The release scope changes or another release is prepared.
