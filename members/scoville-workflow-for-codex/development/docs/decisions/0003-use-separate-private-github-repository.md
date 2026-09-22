---
format_version: 1
id: ADR-0003
status: accepted
created: 2026-09-14
accepted: 2026-09-14
scope: project/publication
---

# Use a separate private GitHub repository

## Decision

Initialize and publish this project only as the private GitHub repository `benjaminstelzer/scoville-workflow-codex`. Install from its exact nested `scoville-workflow-codex/` package. Do not reuse or recreate the deleted `scoville-workflow-for-codex-win` repository, and create no release or tag without a later explicit request.

## Problem

The native Codex workflow is a separate implementation with different lifecycle and installation behavior from the CLI workflow. Reusing the old repository would mix unrelated histories and make the install source ambiguous.

## Drivers

- Keep native Codex and legacy CLI implementations clearly separated.
- Preserve one canonical source and one exact installable package path.
- Keep the new implementation private as requested.
- Avoid inheriting obsolete CLI release, runtime, and installation history.

## Considered alternatives

- Reuse the deleted CLI repository name: rejected because it conflates two implementations and contradicts the requested separation.
- Publish this package inside another Scoville repository: rejected because it weakens ownership and installation identity.
- Create a new private repository dedicated to the native package: selected because source, installation, and history remain unambiguous.

## Consequences

Authenticated GitHub access is required for remote installation. The repository starts on `main` without a release or tag. The local installed package must match the nested package, not the repository root. Public Scoville suite documentation may continue to omit this private Skill.

## Confirmation

Verify the local package inventory and content against the nested source. Verify `origin`, local and remote commit identity, repository visibility, default branch, and absence of releases and tags.

## Revisit when

Reconsider only if the repository is intentionally made public or the native workflow is merged into another canonical owner.
