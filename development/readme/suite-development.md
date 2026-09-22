## Development and builds

Edit member sources under `members/`. Edit README fragments under
`development/readme/` and their ordered paths in `suite.json`. Member README
files are generated previews, not a second authoring source.

Keep `scoville-suite/`, `ask-suite-for-codex/` and `shared/` as siblings.
Both suites use the builder and common templates in `shared/`. That directory
is a build dependency, never an installed Skill dependency.

The shared Development block appears in this suite and its member previews.
Individual releases omit it. Maintain its source, test and note paths in each
member's `development` metadata in `suite.json`.

Regenerate previews with `python development/build_suite.py --write-readmes`.
Use `--check-readmes` to detect stale previews.

Build to a new directory outside this repository:

```text
python development/build_suite.py --output <new-output-directory> --public-only
```

Omit `--public-only` only for private local staging. Each output directory
contains the member package, README, license and changelog where supplied.
Development files stay in the suite. The build receipt records file hashes,
target visibility and the source revision. An uncommitted source produces a
local development build, not a release candidate.

Standalone members use their individual repositories. Workflow is suite-only
and is staged under `scoville-suite/packages/scoville-workflow-for-codex/`.
Its installable Skill is the nested `scoville-workflow-for-codex/` directory.
Publication requires a separate authorized publication step with the
GitHub Skill. Never push a private suite tree to a public member repository.
