# Workflow rename

Canonical package: `scoville-workflow-for-codex`. It is distributed only inside
`scoville-suite-for-codex`, never through a standalone Workflow repository.
Source and tests use the canonical package name.

The old installed `scoville-workflow-codex` directory stays intact while tasks
may still reference it. No installation, task restart, remote rename or source
publication is part of this local change.

## Short invocation

The [official Skill documentation](https://learn.chatgpt.com/docs/build-skills)
describes named explicit invocation and `allow_implicit_invocation`, but the
2026-09-21 search and page inspection did not establish native aliases.
Do not add an invented `aliases` field. `$scw` is accepted in the loaded core's
launcher instructions, but discovery through the host picker is unverified.
Use `$scoville-workflow-for-codex` until a native alias or forwarding Skill has
been qualified. No second launcher implementation is maintained.

## Installation boundary

1. Build the private member to a new staging directory; verify its receipt and
   `--check-packages` result.
2. At an authorized idle boundary, back up the existing installed Skill and
   install the new package. Keep the old files while any task references them.
3. Disable the old entry through Codex's documented Skill configuration; do not
   delete files to hide it. Both versions remain explicit-only.
4. Verify new-name discovery and one coordinator launch in a permitted test
   project before claiming live readiness. Qualify `$scw` separately.

Do not restart Codex or disable a Skill during active DIVI5 work merely to
finish this check. A file/build test does not prove host discovery or launch.
