# Suite project context

Scoville Suite owns checks and procedures. This file contains only
project-specific source ownership, boundaries and release-test scope.

## Canonical sources

- `suite.json`: membership, visibility, package files, helper contracts,
  README composition, family metadata and export destinations.
- `members/`: canonical Skill sources and member development material,
  not separate Git repositories.
- Root Plan profile: suite planning. Member test fixtures are test data, not
  separate project plans.
- `suite.json.private_records`: internal native planning and test records excluded
  from public source exports. Never use it to hide package or README dependencies.
- From PLAN-0058, export Plans and all their linked Audits and Decisions; keep
  PLAN-0057, its Audits and unlinked private evidence in `private_records`.
  Validate the exported profile and links with the existing Plan validator.
  Before publication, inspect new public records for credentials, personal paths
  and third-party names; present findings and the export scope for explicit approval.
- `../shared/`: shared build tools and runtime-helper sources.
  Suite-local copies, including `development/shared/`, are generated snapshots.
- `development/readme/`: README fragments. Member READMEs are generated previews.
  Each member's `description_fragments` owns its complete description.
- `development/shared/instruction-writing.md`: Suite authoring rules for
  AI-consumed content and public copy, generated from `../shared/instruction-writing.md`.

## Project boundaries

Work only on main. Do not create branches or Git worktrees. Publish only main.
When a backup is needed, preserve the work in a verified Git bundle under the
workspace's state/ directory.

Plan Viewer source and native builds belong to the independent
`projects/scoville-plan-viewer` repository. Suite builds contain Skills only.
Do not maintain a Viewer source copy or native build workflow here.

Installed Skills contain their own runtime dependencies. They depend on neither
shared source directory and do not import installed siblings as helper libraries.

GitHub-facing README and CHANGELOG wording uses Benjamin's voice.

Public source exports resolve package blocks. Online continuation lacks those
canonical blocks, private test datasets and the sibling layout required by Shared
tests; exporting the Plan does not remove these development limits.

## Release-test scope

Choose release tests from changed behavior and affected dependencies. Test a
changed file and its consumers only where the change can affect their results.
Require a new GitHub Actions runtime matrix only when packaged Python or its
Python CI tests change. Reuse successful matrix evidence for unchanged Python;
instructions, documentation, configuration and other non-Python changes need
appropriate local checks, not another Actions run. Build-tool changes use local
tests unless they change the packaged Python or Python CI tests.
Check the current package structure,
file completeness, generated copies and published artifacts separately.

Before publication, include changed instructions and affected consumers once in
the existing source review. Check authorization, activation, conflicting or
duplicated rules and complete handoffs against their owning contracts. Record
the reviewed scope and revision in that result. Recheck corrected findings where
needed; the review record requires no separate authoring review or certificate.

Before each canonical source commit, run `python development/check_all.py`.
Commit only on exit 0. This aggregate gate complements the focused checks above.
Generated distributions use the verified build of that gated source. Include a
Changelog entry in every changed distribution before its GitHub push.
