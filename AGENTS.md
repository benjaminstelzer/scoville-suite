# Suite project context

Scoville Suite owns checks and procedures. This file contains only
project-specific source ownership, boundaries and release-test scope.

## Canonical sources

- `suite.json`: membership, visibility, package files, helper contracts,
  README composition, family metadata and export destinations.
- `members/`: canonical Skill sources and member development material,
  not separate Git repositories.
- Root Plan profile: suite planning. Member profiles: historical member records.
- `../shared/`: shared build tools and runtime-helper sources.
  Suite-local copies, including `development/shared/`, are generated snapshots.
- `development/readme/`: README fragments. Member READMEs are generated previews.
  Each member's `description_fragments` owns its complete description.
- `development/shared/instruction-writing.md`: Suite authoring rules for
  AI-consumed content and public copy, generated from `../shared/instruction-writing.md`.

## Project boundaries

Plan Viewer binaries come from GitHub Actions for Windows x64, Linux x64,
macOS Apple Silicon and macOS Intel. Local Rust installation and native Viewer
compilation are prohibited.

Installed Skills contain their own runtime dependencies. They depend on neither
shared source directory and do not import installed siblings as helper libraries.

GitHub-facing README and CHANGELOG wording uses Benjamin's voice.

## Release-test scope

Choose release tests from changed behavior and affected dependencies. Test a
changed file and its consumers only where the change can affect their results.
An unchanged Python helper needs no new test merely because a release is being
prepared. Reuse applicable verified results when its code, dependencies and
runtime contract are unchanged. Instruction or documentation edits alone do
not justify rerunning every Python helper. A changed package hash alone is no
reason for new runtime tests. Check the current package structure,
file completeness, generated copies and published artifacts separately.
