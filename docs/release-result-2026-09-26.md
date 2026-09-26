# Release result, 2026-09-26

PLAN-0012 publishes the verified source at `06b73dd0df359ea47fc79ae4bff8c7e38d629581`.
The four clean build receipts and both public exports match that source.
PLAN-0014 supplies the completed SOL/Luna and Astra evidence. The later
coordinator boundary received the requested Astra Medium review without findings.
The release-specific exceptions remain ADR-0080 and ADR-0081.
The earlier W-009 evidence remains valid: ADR-0082 defaults were installed,
23 Ask, 16 Workflow and two Setup tests passed, as did Codex package validation.

## Published targets

| Repository | Version | Commit |
| --- | --- | --- |
| scoville-suite | v2.0.0 | 8949cb1dcc47831b7ca41273074abd6332316963 |
| scoville-suite-for-codex | v2.0.0 | c084ae7b3c86154b8fb283229da95026bd301b87 |
| scoville-code | v2.0.0 | 57151cb651e20362811fe656e3f6a3529e770cae |
| scoville-plan | v1.9.0 | ea9a5d0b96ed0290a577b6fcbca728976fd9039a |
| scoville-handoff | v2.0.18 | 869bd20f5f09813a042666cd01cc126cf3f46021 |
| scoville-ui | v2.0.0 | aa35bf02e254edee68014b5df7e791efdfded2ad |
| scoville-ask-for-codex | v1.0.0 | bf47d3d2c00e79a263085236ca33d427f09c6ab2 |
| benjaminstelzer-github-skill | v1.0.2 | bf69867eda778cde2cf7aa1011a366a28582f873 |
| benjaminstelzer-imitate-me | v1.0.6 | 7c7d76bbdc01b2c3681a2bb1ffb27568809cc616 |
| benjaminstelzer-skillwriter | v1.0.0 | 2c79c7c3434bc697b4e248efcdec8c73286a4f84 |

The three Benjamin repositories remain private. The four retired repositories
from ADR-0070 are private. Code was renamed with its Git history preserved.
Workflow is published only inside the Codex suite.

## Observed publication checks

All ten remote branches and annotated tags resolve to the intended commits.
Remote Git trees equal the verified candidate trees. Release bodies and asset
inventories equal their prepared inputs. All 56 uploaded files were downloaded
again and match local SHA-256 values. Plan and both suites each include all
eleven Viewer 1.3.3 applications/installers and `SHA256SUMS.txt`, plus their
Skill ZIP and checksum. Viewer provenance and runtime limits remain in
`release-inventar-2026-09-25.md`.

All ten pre-cleanup publication audits passed. Only the six recorded replaced
releases and their old version tags were then removed. Their URLs are retired.
The profile README at `63aa0cd` lists the two suites and five public members.
Pins now show both suites, Code, Plan, UI and Handoff. The obsolete UI pin was
replaced. The general suite description no longer advertises Workflow Beta.
Existing repository topics were preserved and missing publication topics added.

Evidence is retained under `<workspace-root>/temp/2026-09-26-release/`:
`publication.json`, `github-preflight.json`, `remote-branches.json`,
`remote-release-verified.json`, `download-verification-first.json`,
`download-verification-rest.json`, `precleanup-audits.json`,
`retired-releases.json`, `retired-visibility.json`, `profile-pins.png` and
`installed-final.json`. The regular installations contain seven Codex and four
Claude Skills matching the final runtime packages.

The legacy family auditor rejects General's intentionally filtered family
order. The suite publication route replaces that legacy gate with manifest,
receipt and complete remote-tree equality checks. No generated manifest was
changed to satisfy the obsolete check.

## Final acceptance

All ten final remote audits passed. Each target has exactly one stable release
and one annotated release-version tag at the commit listed above. No drafts or
unrelated operational tags were removed. `final-audits.json` and each target's
`*-final-audit.json` retain the results.

SOL 6 Medium applied the published General and Codex upgrade instructions to
isolated old installations. Both removed all sixteen named legacy IDs and their
settings, retained the unrelated Skill and its settings, and installed exactly
four or seven current members. All 43 General and 78 Codex runtime files match
the published packages by SHA-256. Native Codex `skills/list` with isolated
`CODEX_HOME` discovered every member enabled with no errors. General discovery
in another host was not tested. The initial ad-hoc foreign-Skill fixture lacked
a description, and intermediate test roots encountered transient Windows file
locks. Only that test fixture and its cleanup retry were corrected. No shipped
Skill or helper output required repair. The final run and limits are recorded
in `migration-test/evidence.md` and its result/discovery files.

PLAN-0012 is complete. PLAN-0015 remains untouched and unstarted. Final evidence
is source-only documentation added after publication and does not change the
verified release packages or their commits.

## Verified topics

Existing topics were retained. The final sets below were read from GitHub:


- `scoville-suite`: `agent-skills`, `claude-code`, `codex`, `developer-tools`, `workflow-automation`.

- `scoville-suite-for-codex`: `agent-skills`, `codex`.

- `scoville-code`: `agent-skills`, `ai-agents`, `claude-code`, `claude-code-skills`, `code-quality`, `codex`, `codex-skills`, `developer-tools`, `openai-codex`, `prompt-engineering`, `software-engineering`.

- `scoville-plan`: `agent-skills`, `ai-agents`, `claude-code`, `claude-code-skills`, `codex`, `codex-skills`, `developer-tools`, `openai-codex`, `project-management`, `project-planning`, `prompt-engineering`.

- `scoville-handoff`: `agent-skills`, `ai-agents`, `claude-code`, `claude-code-skills`, `codex`, `codex-skills`, `context-management`, `openai-codex`, `prompt-engineering`, `session-recovery`, `workflow-automation`.

- `scoville-ui`: `agent-skills`, `claude-code`.

- `scoville-ask-for-codex`: `agent-skills`, `codex`.

- `benjaminstelzer-github-skill`: `agent-skills`, `claude-code`, `codex`, `codex-skills`, `developer-tools`, `github`, `github-cli`, `openai-codex`, `prompt-engineering`, `python`, `release-automation`.

- `benjaminstelzer-imitate-me`: `agent-skills`, `ai-agents`, `claude-code`, `claude-code-skills`, `codex`, `codex-skills`, `openai-codex`, `prompt-engineering`, `technical-writing`, `writing-tools`.

- `benjaminstelzer-skillwriter`: `agent-skills`.
