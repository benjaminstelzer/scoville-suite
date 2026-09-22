# Suite source ownership

Family lists are build projections, not copied text. Maintain membership and
Scoville `family` metadata in `suite.json`; use `{{ include: suite.members }}`,
`family.owners`, `family.links`, `family.install`, or `family.neighbors`
in Markdown sources. See `development/shared/build/fragments.md` before changing them.
Never install template sources directly; install the built package.

Apply [shared writing rules](development/shared/instruction-writing.md) to all AI-consumed
content, including AGENTS.md. Write briefly and precisely for Luna.

`suite.json` owns distribution membership, visibility, exact package files and
README composition. `members/` contains canonical member sources and their
development material. These directories are not independent Git repositories.
The root planning profile coordinates suite work. Preserve member profiles as
historical member records unless that member's work explicitly requires them.

README fragments under `development/readme/` are authoritative. Member README
files are generated previews. Build them from the fragments, never edit both.
Each member's first README fragment owns its title and description. The suite
uses `suite.descriptions` and manifest `featured_member` to place Workflow first.
Keep those fragments self-contained with absolute links and no include tags.
Shared helper sources must have one canonical owner and explicit manifest
destinations. Every exported Skill includes its own runtime dependencies.
Never import a sibling installed Skill as a helper library.

Development links belong in the shared suite-only README block. Maintain each
member's `development` paths in `suite.json`. Release READMEs must not depend on
excluded files. See `development/shared/build/fragments.md` for audience and link checks.

Run `python development/build_suite.py --output <new-external-directory>` for
local packages, adding `--public-only` for public staging. Build output is not
publication authority. Do not overwrite a checkout or change target visibility.
Scoville Workflow is authorized for suite-only Beta publication by ADR-0009.
It remains Codex-only. Publication still requires the release gates.

Shared build tools and runtime-helper sources are maintained in the sibling
`../shared/` directory. Both suites consume that source during builds and bundle
the required runtime helpers in each exported package. Suite-local tool copies
are generated, never separate authoring sources. Record source hashes and check
them before release. Isolated clones build from generated `development/shared/`.
Installed Skills must not depend on either shared directory.
