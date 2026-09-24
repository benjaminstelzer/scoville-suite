# Suite source ownership

Family lists are build projections, not copied text. Maintain membership and
Scoville `family` metadata in `suite.json`; use `{{ include: suite.members }}`,
`family.owners`, `family.links`, `family.install`, or `family.neighbors`
in Markdown sources. See `development/shared/build/fragments.md` before changing them.
Never install template sources directly; install the built package.

Apply [shared writing rules](development/shared/instruction-writing.md) to all AI-consumed
content, including AGENTS.md. Write briefly and precisely. Plan writing and additional Workflow instructions
use the selected shared writing profile; other instructions remain clear for Luna.

`suite.json` owns distribution membership, visibility, exact package files and
README composition. `members/` contains canonical member sources and their
development material. These directories are not independent Git repositories.
The root planning profile coordinates suite work. Preserve member profiles as
historical member records unless that member's work explicitly requires them.

README fragments under `development/readme/` are authoritative. Member README
files are generated previews. Build them from the fragments, never edit both.
Each member's `description_fragments` owns its complete description block. The suite
uses `suite.descriptions` and manifest `featured_member` to place Workflow first.
Keep those fragments self-contained with absolute links and no include tags.
Use development/shared/readme/README-template.md for section order and lists.
Skill descriptions explain the problem, the solution and how the rules produce
it. Briefly name relevant costs or limits, including extra tokens and process
overhead where applicable. Keep benefits central. Do not invent measured gains
or force four headings onto every description.
Shared helper sources must have one canonical owner and explicit manifest
destinations. Every exported Skill includes its own runtime dependencies.
Never import a sibling installed Skill as a helper library.

Development links belong in the shared suite-only README block. Maintain each
member's `development` paths in `suite.json`. Release READMEs must not depend on
excluded files. See `development/shared/build/fragments.md` for audience and link checks.

Build release packages with `python development/build_suite.py` under the sole
`E:/Dropbox/AI Projects/skills/temp/release/` tree, selecting `--profile`,
`--layout` and `--public-only`. Use `--refresh` only after existing readers
finish; changed inventory requires reconciliation first. Synchronize verified
outputs to regular Skill directories, removing obsolete generated files while
preserving sources and Git history. Build output is not publication authority.
Scoville Workflow is authorized for suite-only Beta publication by ADR-0009.
It remains Codex-only. Publication still requires the release gates.

Shared build tools and runtime-helper sources are maintained in the sibling
`../shared/` directory. Both suites consume that source during builds and bundle
the required runtime helpers in each exported package. Suite-local tool copies
are generated, never separate authoring sources. Record source hashes and check
them before release. Isolated clones build from generated `development/shared/`.
Installed Skills must not depend on either shared directory.
