# Family fragments

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

Suite-specific tests run from `development/tests`. Shared cross-suite tests
retain their authoring-workspace layout requirement: `shared/`, `scoville-suite/`
and `ask-suite-for-codex/` as siblings. The bundled copy retains those test sources
for development, but installing a Skill requires none of them.

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
How it was developed uses bullets and stays outside the suite description block.

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
