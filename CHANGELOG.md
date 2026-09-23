# Changelog

## v1.0.4 - 2026-09-23

- Recognize a verified parking prompt and the complete writer assignment when Codex delivers both in one native turn, while blocking duplicate or conflicting assignments.

## v1.0.3 - 2026-09-23

- Keep Workflow's dispatch binding stable when the writer moves from pending to active, while retaining the separate target and guard checks.

## v1.0.2 - 2026-09-23

- Route new Workflow tasks through Luna 6, SOL 6, and Astra 6; remove Terra from the default routing table.
- Verify builder assignments after the native task envelope escapes HTML characters or removes the final newline.

## v1.0.1 - 2026-09-23

- Stop Workflow workers before project access unless their native task carries
  the complete builder-generated dispatch contract for the assigned role and
  execution unit.
- Let established codebases keep their local conventions. For Greenfield work,
  start with the smallest coherent responsibility-based layout without
  prescribing an architecture or directory tree.

## v1.0.0 - 2026-09-22

- Install the Scoville Skills together from one suite or use individual
  distributions for the concerns you need.
- Include Scoville Workflow as a Codex-only Beta, available only in the suite.
  It coordinates Plan execution, reviews, repairs and context handovers.
- Include the renamed WordPress UI Backend specialist. Replace an existing
  `wordpress-backend-ui` installation with
  `scoville-wordpress-ui-backend-anti-ai-slop`.
- Bundle runtime helpers inside each Skill so installed packages need neither
  the suite source tree nor a shared directory.
