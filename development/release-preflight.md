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
The r4 exports were rebuilt in fresh temporary Git checkouts using only bundled
sources. Complete two-way inventories and SHA-256 comparisons match the r4
public builds: 188 Scoville files and 50 Ask files, with no missing, extra or
different package files. This closes the package reproducibility finding.
R3 evidence and frozen model-test builds remain unchanged.

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
The classification row now states the risk override directly. A separate r2
run on the rebuilt package passes cases 06 and 24 under SOL review. The author
read both answers and agrees: Normal remains core-only, while Structural adds
Change. Case 24 also selects Validation for the evidence judgment. Four native
contexts identify Luna Medium. Original failure evidence remains unchanged.

## Historical release mismatch

Live release notes exist without matching local changelog headings for
Brainstorm v1.1.13, Code v1.0.33, Handoff v2.0.16, Research v1.1.10,
Scribe v1.0.33, UI v1.2.8 and WordPress v1.2.9. Their release bodies describe
functional changes. On 2026-09-22 the user authorized restoring verified entries
only when useful to users; omit housekeeping. RELEASE-HISTORY is resolved as a
decision, not as completed reconciliation. Restore relevant behavior, routing,
compatibility and limitation changes from the release bodies. Existing tags
remain unchanged; version reconciliation is still required before publication.

## Rollover archive correction

DIVI5 G30 retained G27-G29 with `successor_not_listed`, although its exact-ID
host read reported `active` and the predecessor activation turn was complete.
The shared helper now accepts that fresh native active status as an alternative
to exact list membership. Guard, identity, completed-turn, placement and retained
status checks still apply. Unavailable listing sources also defer archival.

Two regression cases failed before the code change and pass afterward. All 11
rollover, 38 shared, 21 Scoville build and 8 Ask build tests pass. Both suites
bundle the changed shared source. Local packages were built under
`skills/public/rollover-fix-2026-09-22/`; only the three affected Workflow files
were installed into Codex, with previous files retained in
`state/2026-09-22-rollover-fix/` and installed hashes checked against the build.
G30 applied recovery at the accepted W-021/step-3 boundary. Its fresh helper
result had no archive blockers; exact-ID `verify_archive` passed for G27
`01a0c725-88d5-70e3-84e7-bdf9632feceb`, G28
`01a0c7a6-b32f-79b3-a856-0108aa9b0f24` and G29
`01a0c7d4-a40d-77a3-ae21-29e4dc9a1491`. G30 then resumed rollover to G31.
This is live recovery evidence, not merely a fixture result. No DIVI5 guard
or project files were changed by this task.

The targeted SOL/Luna retest is complete: four protocol passes, three accepted
semantic passes and one chain-case failure. Luna understood the missing-list
exception but omitted explicit archive-failure recovery and current-coordinator
exclusion. The shared contract now states these rules as an ordered loop, but
both bounded retests exhausted four READ turns without a final answer. They
are inconclusive, not passes. Publication remains unqualified for that case. See
`development/luna-tests/workflow-archive-results.md` for fixed inputs, independent
author checks, the precise evidence limit and the remaining targeted test.

## Handoff and UI qualification

SOL accepted Handoff 06, 09, 15 and 25 and UI 01, 04, 08 and 17.
The author read these eight answers against the fixed keys and agrees.
Handoff preserves unknowns, source-recovery limits, secret redaction and the
size-conflict boundary. UI preserves specialist ownership and evidence limits.
UI 25 also passes SOL and independent author review. It preserves Design and
component ownership, rejects global overrides and retains missing rendered
proof. Raw runs are under workspace
`temp/2026-09-22-release-handoff-ui-luna/`.

Independent native-record inspection confirms Luna Medium for all 16 turns in
the nine runs. Every turn has a successful process/protocol result without
stderr, timeout or stream failure.

Two-way runtime inventories and SHA-256 comparisons against r5 show no changes
from the tested release build for Handoff's four files, UI's six, WordPress's
fifteen and Workflow's twenty-eight. This supports carrying their test results
to r5. It does not cover changed Code or Plan instructions.

## Distribution boundaries

The exact receipt checks and distribution-layout checks pass for all fifteen
packages in Scoville r5 and Ask r4. No development directory is included in
those standalone distribution trees. Full suite source exports intentionally
retain development material outside their installable packages.

## Frontmatter validation

All fifteen r4 packages parse as YAML and have matching directory/name values,
nonempty descriptions and compatibility strings of 1-500 characters. The generic
Skill Creator validator rejects the supported compatibility field, so its result
is not counted as a pass. The explicit contract checks above cover these fields.

## Design correction and Plan pilot

Design 24's initial semantic PASS was overturned by independent review and SOL
reassessment: its proposed next action included repair under read-only Critique.
The mode row now makes that authority boundary explicit. The r6 package's
Design 24 answer preserves read-only inspection and reporting. Repair 06 also
passes SOL and independent author review, preserving the authorized alignment
fix without reopening settled choices. Native records confirm Luna Medium for
all four turns, with clean process/protocol results. Original answers and revised
judgments are retained.

Plan 07 passes SOL and independent author review against the fixed key. It
preserves the partial profile and stops before initialization or writes.
Its two native turns confirm Luna Medium and clean process/protocol completion.
Four packaged references were supplied before the final answer, qualifying the
new continuation prompt. Plan 13, 19 and 25 also pass SOL and independent author
review. They preserve narrow execution-annotation changes, explicit successor
priority and unresolved Decisions without inventing completion or queue writes.
Independent native checks confirm all eight turns as Luna Medium, with no
process, stderr, timeout or stream failures.

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
