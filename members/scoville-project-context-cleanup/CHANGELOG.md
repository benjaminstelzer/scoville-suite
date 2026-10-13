# Changelog

## Unreleased - 2026-10-13

- Load detailed command capture and full-file delivery only when needed. Keep complete output, failure diagnostics and role permissions.

- Keep saved oversized results out of Git status with `.scoville/temp/.gitignore`;
  existing ignore files and tracked files stay unchanged.
- Send oversized results as a file path only; recipients read the whole file
  without hash checks. Save composed text without a separate verification pass.
- Simplify shared writing rules; command-specific size details now live in the
  shell-command rules.

## Unreleased - 2026-10-12

- Return complete command output directly when it fits; save only oversized
  captures. Verify supplied artifacts once and compare saved native Finals
  directly, avoiding repeated hash checks for unchanged text.

## Unreleased - 2026-10-11

- Read required files completely with an agent-chosen method. Remove the document-reading helper and multipart protocol; keep output capture and result delivery separate.

## Unreleased - 2026-10-10

- Load command capture and large-result delivery only when needed; preserve complete outputs and role permissions.
## Unreleased

- Keep agent messages and internal commentary compact. Reference readable source text instead of copying it; preserve required facts and exact controls.
- Keep the full reading procedure in one reference and load host command details when needed. Preserve complete reads and existing permissions.

- Read complete bounded UTF-8 input and capture command output before display while preserving its failure status.
- Preserve complete oversized findings through compaction or a hashed temporary file. Keep the separate manual helper procedure available only without Python.
- Use the host's applicable project rules in general packages, while Codex packages use AGENTS.md alone.
- Place rules in their governing subtree file and allow a project's own rule file
  under inherited workspace rules. Preserve independently needed copies and the
  instructions requiring them.
- Require complete references or a requested extraction. Keep approval requirements
  and external-action prohibitions, with their conditions and exceptions, in the
  rule file. Check every changed file, including extracted references.
- Add requested project-rule and index maintenance with preserved scope,
  safeguards and record ownership.
- Choose a missing rule or index file from the stated project owner and format.
  Keep existing native and foreign index formats, and preserve useful repeated
  rules when cleaning a grown project.
