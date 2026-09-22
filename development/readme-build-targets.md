# README build targets

W-026 separates suite documentation from release READMEs in both suites.

- `suite.json` owns each member's source, test and note paths.
- Shared templates render the links in suite READMEs and Scoville member previews.
- `audience: suite` excludes that complete fragment from every package, including
  private Workflow staging. Ask still uses three template bases, without previews.
- Local Markdown file links are checked against package contents. Missing files,
  escaping paths and excluded development files stop the build. Changelogs retain
  historical links. External reachability and heading anchors are not checked.

Removed the legacy development-link rewrite. Corrected the SOL-to-Astra file
link, moved current Ask test links into the shared block, aligned documented
Astra defaults with `high`, and corrected member development paths and ownership.

Validation on 2026-09-22: 13 shared README tests, 5 Scoville build tests and
8 Ask suite tests passed. README freshness checks passed. Both complete builds
contain 15 packages. Their 223 non-README files match the preceding Scoville
WordPress build and Ask local release build. No Skill behavior changed.

Local candidates are under workspace `temp/2026-09-22-readme-audit/`, in
`final-scoville/` and `final-ask/`. No installation or publication occurred.
Future public URLs are prepared, not claimed reachable.

The broader prose audit remains separate from this build-target change.
