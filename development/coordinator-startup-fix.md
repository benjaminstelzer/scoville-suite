# Coordinator startup contract

2026-09-25. Canonical source and built packages only. No commit, publication,
local Skill installation or DIVI workflow restart.

## Cause and correction

DIVI generation G9 used subagents after its rollover prompt omitted the Skill
path and it did not load the Workflow instructions. The project model rule also
requested subagents. That rule was removed in DIVI and the workflow was stopped
at its worker boundary. Deferred step review followed the separate Work Item
review cadence; a completed W-052 reviewer independently returned pass.

The normal coordinator phases are now supplied together by
`coordinator_contract.py`, composed from their existing authoritative sources.
Only labelled scenario examples and obsolete routing introductions are omitted.
Actual rollover and worker context recovery keep their conditional references.
The complete contract is approximately 72,000 characters and is supplied at each
startup stage. This increases startup context; no model efficiency gain is claimed.

The guard checks exact native creation evidence, current contract contents and
workflow identity before coordinator authority. Writer binding requires native
creation by that coordinator. A subagent or fork cannot satisfy this check.
After native compaction, complete tool-delivered instructions must appear again.
Hashes and read acknowledgments alone do not qualify. Windows CRLF output and
nested native JSON tool wrappers are handled. Legacy Stop cleanup stays available.

## Evidence and limits

- All 80 Workflow tests passed against generated package payloads, including
  missing/stale/truncated instructions, native versus subagent provenance,
  post-compaction restoration and unchanged guard state on rejection.
- Independent read-only review found the digest-field parser, rollover header
  and Windows newline defects. All three were corrected and covered by tests.
- Comparison with the saved dirty-tree baseline preserved existing phase rules,
  review requirements, routing, Stop cleanup and prior unrelated changes.
- `git diff --check` passed for the Workflow member and manifest.
- The final Codex Suite projection passed `--check-packages` with no errors;
  the synchronized package helper matches the corrected canonical source hash.
- Skill Creator's generic validator still rejects the pre-existing
  `compatibility` frontmatter key. No generic-validator pass is claimed.
- These are helper integration tests, not a new live native workflow run or
  proof that a model understands every supplied instruction. The guard controls
  its own transitions, not arbitrary host tools or filesystem access.

Local installation is deferred: the installed Plan selector lacks the
`source_text` interface already required by the newer canonical Workflow.
Installing Workflow alone would produce an incompatible pair. Installed model
preferences also differ from current defaults. A compatible Suite installation
must preserve those preferences and happen only after active consumers stop.
DIVI remains paused and its existing installation is unchanged.
