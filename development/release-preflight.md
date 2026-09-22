# Release preflight

Local candidates are under workspace `skills/public/release-2026-09-22/`.
Both receipts identify clean committed sources. Exact inventory, hashes and
current-source package checks passed. Source-only export changes after those
builds leave all installable package bytes unchanged.

Full source exports, including shared development sources and all packages,
are under workspace `temp/2026-09-22-suite-release/r3/`. Both pass isolated
`--check-sources` without the private sibling shared directory. Scoville's 634
tracked files and Ask's 150 match their source Git blobs exactly. The exports
identify commits `a3e6789` and `355845e`, respectively. Later documentation
commits require a fresh final export.

The export now reads Git blobs in one batch. The previous worktree read could
export different line endings despite a clean Git status. A regression test
reproduced that failure and passes with the fix. Portable-source verification
also passes. Both frozen test builds still pass current-source package checks.

An isolated rebuild from r3 needs a Git checkout for receipt provenance.
After creating temporary local repositories, both builders completed. Comparison
with the frozen builds found six Scoville and eight Ask files differing only
in CRLF/LF line endings. Source export is exact, but package byte reproducibility
is still open. Fix the package reader and reassess affected evidence before
publication. Do not overwrite the frozen test builds.

The package reader now normalizes CRLF to LF for the supported text formats
and preserves binary and unknown formats byte-for-byte. All 38 shared tests
pass, including the new normalization test. Both suites bundle the fix.
An isolated final rebuild still needs comparison before closing this finding.

## Workflow qualification

SOL Medium runs the five fixed cases with Luna Medium. Initial cases 01 and 06
passed protocol and semantic review. The author read both answers and agrees.
Case 17 failed transport before a semantic answer: the READ request omitted
the package-root prefix. Its prompt did not specify the relative-path base.
No Skill defect or passing result follows from this failure.

A separate r2 attempt adds only the missing path-base instruction. Original
case, key, package, runner and failed evidence remain unchanged. Cases 17, 20
and 25 passed in r2. SOL reviewed all five answers against the fixed keys.
The author independently read them and agrees with those judgments.

Native session records confirm Luna Medium for all 13 turns across the five
accepted runs. Every process exited successfully, with no stderr, timeout or
stream error. This verifies theoretical comprehension, not live execution of
the simulated actions. Raw evidence stays under workspace
`temp/2026-09-22-release-workflow-luna/`.

## Upstream preservation

The four existing Ask repositories still have the exact default-branch commits
recorded as their `import_commit` in `ask-suite-for-codex/suite.json`.
The live GitHub check found no later upstream changes to reconcile. The new
SOL single-adviser distribution has no existing history to compare.

## WordPress qualification

All five fixed cases passed protocol checks and SOL's semantic review against
the frozen keys. The author independently read every answer and agrees.
Native records confirm Luna Medium for all ten turns, with no process,
stderr, timeout or stream failure. Raw evidence remains under workspace
`temp/2026-09-22-release-wordpress-luna/`.

The spacing case rejects an arbitrary scale, an unnecessary React migration
and plugin-defined WPDS tokens while preserving Core spacing ownership. The
other cases cover hybrid gaps, hidden fields, focus recovery, portals, i18n,
version boundaries and excluded surfaces. These are comprehension results,
not proof of a rendered WordPress implementation.

## Code qualification

All fifteen selected runs passed transport checks. SOL accepted fourteen
answers and rejected case 24. The author confirmed that failure: Luna identifies
Structural risk but selects no route, overlooking the mandatory Change override.
The failed answer remains unchanged under workspace
`temp/2026-09-22-release-code-luna/code-release-24-run/`.
Publication remains blocked on correcting and retesting this routing ambiguity.

## Plan Viewer

Existing release `v1.7.5` supplies eleven Viewer `v1.3.2` files and
`SHA256SUMS.txt`. All eleven downloaded files match those published checksums.
CI run `35495121742` completed successfully for Windows x64, Linux x64,
macOS Intel and Apple Silicon at source commit
`66de550e726612589295f018a628c98cf7302498`.

The candidate Viewer has the same 60-file inventory as that commit. Git blob
comparison differs only for `development/viewer/README.md`. All eleven release
files are byte-identical to the corresponding successful CI artifacts. This
supports reusing the unchanged Viewer without renaming or rebuilding it.
No binary execution or new release is claimed. Old assets and releases are unchanged.
