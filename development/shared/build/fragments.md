# Family fragments

## Runtime helper policy

Register every packaged Python file under `helper_contracts`, keyed by its
Skill-relative `scripts/<name>.py` path. Use `kind: helper` for executable
entrypoints and `kind: library` for imported support code. General helpers also
declare `fallback: references/fallbacks/<name>-fallback.md`; libraries do not.
List each fallback file in the manifest with `profiles: ["general"]`.

Put `{{ include: helper.policy }}` once in the Skill entrypoint. The builder
generates helper-first routing and the conditional reference table. Each manual
file begins with `<!-- helper-fallback: scripts/<name>.py -->`, followed by its
complete no-Python procedure. Do not inline or separately link these optional
routes. Codex strips fallback metadata and rejects fallback files and links.
Package building and verification check the exact registry and route structure.
Behavioral equivalence and diagnostic quality still require consumer tests.

## Portable suite sources

The workspace sibling `shared/` is the authoring source. Before release run
`python ../shared/build/sync_suite_sources.py --root .` from each suite, then
repeat with `--check`. This copies shared build/runtime sources and their tests under
`development/shared/`, with file hashes in `sources.json`. Unexpected files
block synchronization rather than being deleted.

The suite entrypoint uses the sibling builder in the authoring workspace and
the bundled builder in an isolated clone. Shared paths resolve beside that
builder, never against an unrelated installed Skill. Runtime dependencies are
still copied into each Skill package. The development snapshot is not installed.

Both suite repositories retain their member/template sources and development
files. Release assembly also places every installable Skill under `packages/`.
Individual distribution repositories contain only their package and user-facing
root files. Workflow has no separate distribution repository.

Suite-specific tests run from `development/tests`. Shared tests use `shared/` and `scoville-suite/` as siblings, covering both build profiles and the standalone Codex Ask package. The bundled copy retains those test sources
for development, but installing a Skill requires none of them.
`build/run_portability.py` runs those complete tests in authoring sources. In an
export it validates only the selected manifest, fixed layout and exact packages;
it never asks a projected tree to recreate an excluded profile.

Members default to `distribution: standalone`. `distribution: suite` targets
the suite repository and stages its package at `<suite>/packages/<member>`.
The receipt records `distribution` and `package_path`. Publication and tests
must use that path, not assume `<member>` at the staging root. Visibility gates
apply equally to both kinds. A suite-only member has no standalone repository.

README manifests accept `shared:filename.md` for templates owned by
`shared/readme/`. Other paths stay suite-relative. Shared templates use the same
`{{ var: key }}` and `{{ include: key }}` expansion as local fragments. Missing
files/variables and paths escaping the template directory fail the build.
Exported READMEs contain expanded text, not references to this source directory.
Build receipts record each consumed member README template's SHA-256.

Package `files` entries also accept `shared:<relative-path>`, rooted at the
canonical shared directory. Existing `shared_helpers` entries use the same
resolver and retain their scripts-only destination constraint. Snapshots and
receipts include consumed shared files. Installed packages never import them
from another Skill or a development checkout.

`{{ include: prompting.defaults }}` expands `prompting/models.toml` inside
Markdown or TOML package sources. Plan installs these defaults as its own
`assets/prompting.toml`; Workflow embeds them in its own `assets/workflow.toml`.
Installed configuration edits remain independent.

For suite-only README sections use
`{"source": "shared:member-development.md", "audience": "suite"}` in the
member's `readme` list. Strings apply to both targets. Member previews render
the suite target. Packages always render the release target, including private
Workflow builds. Unknown audience values fail instead of silently dropping text.

Each member's `development` object defines suite-relative `source`, `tests` and
`notes` paths. Targets must exist. The suite `repository` supplies the final
GitHub URL. `member.development` renders compact links inside the suite-only
block. `suite.development` renders all members in the suite README, including
Ask variants without creating member previews. Use the shared templates for both.

Keep current development links in that block, not in release prose. Builds
reject unresolved local Markdown file links and development files. Relative
links resolve against the generated package, never the source checkout.
Code examples and historical CHANGELOG links are excluded from the link check.
External URLs and heading anchors need separate release checks. Historical
evidence stays explicit, never automatically rewritten to an imported commit.

`suite.json` owns membership. Scoville members also define `family.order`
(unique nonnegative integer), `label`, `owner`, and `summary`. Add a member once;
full lists follow its order. Ask uses manifest member order.

Use `{{ include: KEY }}` in exported Markdown or README source fragments:

| KEY | Output |
| --- | --- |
| `suite.members` | Member preview links, or public repository links when `member_previews:false` |
| `suite.descriptions` | Suite README only: each member's first README fragment, with `featured_member` first, then family order |
| `family.owners` | Public members and their ownership |
| `family.links` | Public family links; private member READMEs also include private members |
| `family.install` | Only approved public installation URLs |
| `family.neighbors` | Current member's explicit `family.neighbors` subset |

Neighbor entries use `member` for a suite member or `external` for another
Skill, plus `description` and optional `optional: true`. Preserve specialized
scope and authored order; adding a family member never expands a subset.
An existing optional private neighbor reference is not publication approval.
Historical evidence and ordinary prose references are not membership lists.

The first four member README fragments form `description_fragments`: title and
introduction, How it works, What it enforces, What it costs. The last three use
bullets. Suite descriptions reuse the complete block and demote headings outside
code fences. Keep absolute links and no include tags inside these fragments.
Follow [the common project template](../readme/README-template.md) for all projects.
How it was developed uses brief prose and stays outside the suite description block.

The shared builder expands placeholders before packaging. Packages contain
complete Markdown and need no shared directory. Never install source templates.
Unknown fragments, unknown internal neighbors and invalid order fail the build.

With `member_previews:false`, `--write-readmes` updates only the suite README;
`--check-sources` validates payloads without creating member copies. Other suites
retain previews by default. Regenerate them with `--write-readmes` and check with
`--check-readmes`.
After building, run `--check-packages --output <build-directory>` to detect
edited or stale package content against current sources. Receipt hashes alone
detect changed output, not a stale source projection.

For a shared output containing several suites, use
`python verify_package_set.py --root <output> --receipt <receipt-a> --receipt <receipt-b>`.
This read-only check requires the exact combined file/directory inventory and
SHA-256 values. Keep each original receipt; never overwrite one with another.
It does not prove source freshness, model-test success or release authority.

## Distribution profiles

Scoville uses `--profile general` (default) or `--profile codex`. `suite.json`
contains two flat profile objects with name, repository and optional README
sources. Member and file entries may declare `profiles: ["general"]` or
`profiles: ["codex"]`; omission selects both. The resolved manifest owns every
projection. Optional neighbors and the featured member disappear when excluded.
Unknown profiles fail. Visibility checks still apply to the selected members.

Keep short text alternatives beside their owner using flat blocks:
`{{ profile: general }}portable text{{ /profile }}` and
`{{ profile: codex }}required-helper text{{ /profile }}`. Empty alternatives may
be omitted. Unknown, nested or incomplete blocks fail; no expression language
or runtime conditionals are supported. Built packages contain plain text.

Default README previews remain in the source tree. Other profile previews
require `--write-readmes --profile codex --output <new-preview-directory>`.
Package verification selects the profile recorded in its build receipt.

`export_suite.py --profile <profile>` requires inspected committed sources and
a current shared snapshot. It replaces tracked generated packages, filters
excluded members and file sources, and writes an effective `suite.json` plus
matching README previews. Runtime source profile blocks are resolved; shared
build tools remain unchanged. The exported tree rebuilds its selected profile
without the authoring workspace. Export never grants publication authority.

## Installation layout

`--layout standalone` builds independent general Skills with family guidance.
`--layout suite` builds every selected-profile member inside its suite's own
`packages/` tree. Codex defaults to suite layout. `standalone_profiles: ["codex"]` permits the Ask standalone projection; other Codex members remain suite-only. `catalog_profiles` lists editions whose README advertises an excluded member without bundling its sources. `availability` supplies its host label; `suite.catalog` renders that installation catalog. A suite build rejects member subsets and
unapproved public members; it never silently produces a partial suite.
Exports always retain `layout: suite` and rebuild only that edition/layout.

`{{ package: standalone }}...{{ /package }}` and
`{{ package: suite }}...{{ /package }}` select installation-contract prose.
These flat blocks are independent of the general/codex Python profile.
`family.contract` expands canonical `runtime/skill_composition.md`;
other family projections are absent from suite packages. README requirements
come from `readme/skill-installation-contract.md` and
`readme/suite-requirements.md`. Suite installation uses only its own packages;
missing members are errors, never permission to fetch individual repositories.

Local release staging uses exactly `<workspace-root>/skills/temp/release`.
Do not keep dated/numbered candidate builds in the regular Skill directories.
Synchronize every generated Skill distribution from this verified build,
including the fixed public suite targets. Remove obsolete generated files;
preserve source repositories and Git history. Regular Skill directories contain
only their current verified output, never build candidates or stale copies.

## Runtime build gate

Builds containing Python runtime helpers require a successful private GitHub
Actions matrix for the exact generated packages and current tests. The matrix
runs Windows, macOS and Linux on Python 3.11 and the current stable Python.
It exercises packaged helpers and their actual local consumers; no live
adviser calls or credentials are needed. The private CI repository is
`benjaminstelzer/scoville-runtime-ci`. Never push private sources to public CI.

Prepare the test snapshot under the sole release staging tree:

```text
python development/build_suite.py --prepare-runtime-ci <release/runtime-ci>
```

Commit and push this generated snapshot to the private CI repository, then wait
for all six `Runtime helpers` jobs. Use `--refresh` only after existing readers
finish and while inventory is unchanged; it preserves `.git` and refuses edited
staging files. Do not maintain snapshot copies separately from canonical sources.

Pass the successful run URL to the normal build:

```text
python development/build_suite.py --profile codex --layout suite --public-only --output <package-build> --runtime-run https://github.com/benjaminstelzer/scoville-runtime-ci/actions/runs/ID
```

The builder verifies GitHub run/job status, tested commit, exact package files,
helper registry and test/workflow hashes before producing a verified build.
Changed packages or tests require a new run. Missing, failed, skipped or stale
evidence blocks the build. Authenticated `gh` access to private CI is required.
`--check-release` rechecks the run retained in `build-receipt.json`.
The Python `build()` function remains a local candidate constructor for tests;
its receipt says `runtime_validation.status: pending`, never runtime acceptance.

## Viewer release gate

Package checks alone do not approve a release. For Plan and both suites, build
the current Viewer only through the canonical suite's `Plan Viewer` Actions
workflow. Download its four platform artifacts and `SHA256SUMS.txt` unchanged
to `skills/temp/release/viewer/`. Add `BUILD.json` with `version`, `platforms`,
`workflow_run` and `source_commit` from that successful run.

Before publication, run for each suite package build:

```text
python development/build_suite.py --check-release --output <package-build> --viewer-assets <release/viewer>
```

This checks package freshness, all five version owners, the exact eleven
binaries and checksums, successful platform/checksum jobs, current Viewer and
workflow source identity, and bytes downloaded from the Actions artifacts.
Its JSON `viewer.assets` is the exact attachment list for the release consumer.
Attach every listed file directly to Plan and both suite releases.

After upload, repeat with all three `--release owner/repository=vX.Y.Z`
arguments. Check upload state, exact attachment names, sizes and GitHub's SHA-256
digests against the approved files. Never download release attachments again,
including drafts and final audits. Initial Actions artifact downloads remain
required. Keep both successful results as release evidence.
Missing assets, source drift or failed provenance checks stop publication or
installation. A renamed old binary is never a current build.
