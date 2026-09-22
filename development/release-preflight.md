# Release preflight

Local candidates are under workspace `skills/public/release-2026-09-22/`.
Both receipts identify clean committed sources. Exact inventory, hashes and
current-source package checks passed. Source-only export changes after those
builds leave all installable package bytes unchanged.

Full source exports, including shared development sources and all packages,
are under workspace `temp/2026-09-22-suite-release/r2/`. Both pass isolated
`--check-sources` without the private sibling shared directory.

## Workflow qualification

SOL Medium runs the five fixed cases with Luna Medium. Initial cases 01 and 06
passed protocol and semantic review. The author read both answers and agrees.
Case 17 failed transport before a semantic answer: the READ request omitted
the package-root prefix. Its prompt did not specify the relative-path base.
No Skill defect or passing result follows from this failure.

A separate r2 attempt adds only the missing path-base instruction. Original
case, key, package, runner and failed evidence remain unchanged. Cases 20 and
25 await the transport check. Raw evidence stays under workspace
`temp/2026-09-22-release-workflow-luna/`.

## Plan Viewer

Existing release `v1.7.5` supplies eleven Viewer `v1.3.2` files and
`SHA256SUMS.txt`. All eleven downloaded files match those published checksums.
CI run `35495121742` completed successfully for Windows x64, Linux x64,
macOS Intel and Apple Silicon at source commit
`66de550e726612589295f018a628c98cf7302498`.

The candidate Viewer has the same 60-file inventory as that commit. Git blob
comparison differs only for `development/viewer/README.md`. Direct comparison
with downloaded CI artifacts remains pending. No binary execution or new
release is claimed. Old assets and releases are unchanged.
