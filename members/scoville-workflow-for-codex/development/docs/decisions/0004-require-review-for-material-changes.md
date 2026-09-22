---
format_version: 1
id: ADR-0004
status: accepted
created: 2026-09-19
accepted: 2026-09-19
scope: project/review
---

# Require review for material changes

## Decision

Require an independent workflow review when a completed unit changed the codebase or changed documentation whose correctness materially governs security, permissions, data handling, migrations, deployment, operations, public behavior, or required acceptance and lifecycle behavior. Do not require review merely because the unit performed read-only discovery, project inspection, preparation, planning-record maintenance, or routine documentation work. An explicit user, Plan, or repository review requirement still applies.

## Problem

The workflow currently creates a reviewer after every completed executor, so preparatory and inspection-only units incur review even when they produced no material result to review.

## Drivers

- Keep independent review where an incorrect change can alter executable behavior or a critical operating contract.
- Avoid review work that repeats read-only preparation or project inspection without a material changed result.
- Decide from the completed result rather than the activity label used in the Plan.

## Considered alternatives

- Review every completed unit: simple orchestration, but preparation and inspection always pay for a reviewer without a material changed result.
- Review only codebase changes: removes unnecessary review, but leaves critical documentation contracts unchecked.
- Review codebase and critical documentation changes: preserves review at the material boundary while allowing non-material units to advance after acceptance.

## Consequences

- The coordinator must classify the completed unit's actual changed result before creating a reviewer.
- A qualifying change still uses the existing fresh review and bounded repair loop.
- A non-qualifying unit may advance after observed Acceptance and required Plan validation without creating reviewer or repair tasks.
- Ambiguous materiality or an explicit review requirement resolves to review.

## Confirmation

1. Run the focused contract tests and confirm they cover one qualifying and one non-qualifying completed unit.
2. Inspect `scoville-workflow-codex/SKILL.md` and `scoville-workflow-codex/references/operations.md` for matching threshold, repair, commit, and archival rules.
3. Confirm the local installed package matches the validated nested source package.

## Revisit when

Observed workflow runs show that the threshold skips review for a materially consequential change or still creates reviewers for non-material preparation without an explicit requirement.
