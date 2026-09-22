# README unification

Requested on 2026-09-22. W-030 owns the source-suite change and repository
publication. The later clarification extends the template to ordinary projects.

## Contract

Intro, How it works, What it enforces and What it costs form the description
block. The three named sections use bullets. How it was developed also uses
bullets. Compatibility, Install, How to use, Sources, Family or Related projects,
and License follow. Suite framing remains separately authored.

`shared/readme/README-template.md` owns the reusable template. Each member's
`description_fragments` names its four source fragments. Both suite and member
READMEs use them. Suite projection only nests headings. Workflow keeps its
flowchart. Brainstorm and paired Ask use compact branching diagrams. Other
members use shorter lists.

## Repository fix matrix

All names below belong to benjaminstelzer. Preserve visibility, history, tags,
release assets and runtime behavior. All 22 changed repositories were pushed and verified on 2026-09-22.
Remote commit and complete Git tree identities matched each candidate.

| Repository | Canonical change | State |
| --- | --- | --- |
| scoville-suite | Shared builder and full member blocks | Verified `a01b770e1aee` |
| ask-suite-for-codex | Same builder and three variant templates | Verified `f17792d15e9a` |
| scoville-code-anti-ai-slop | Suite-generated README | Verified `018131fe4c8e` |
| scoville-plan | Suite-generated README | Verified `a13b736445ed` |
| scoville-scribe-anti-ai-slop | Suite-generated README | Verified `74c8111f5767` |
| scoville-ui-anti-ai-slop | Suite-generated README | Verified `d12ab5a092e2` |
| scoville-wordpress-ui-backend-anti-ai-slop | Suite-generated README | Verified `ce628745efce` |
| scoville-design-anti-ai-slop | Suite-generated README | Verified `610ea753b5fc` |
| scoville-handoff | Suite-generated README | Verified `d507a97382a7` |
| scoville-research | Suite-generated README | Verified `4ade04269f5f` |
| scoville-brainstorm | Suite-generated README and branching diagram | Verified `b3420e96e660` |
| ask-astra-for-review-for-codex | Shared single-adviser block | Verified `916c31fcaf48` |
| ask-sol-for-review-for-codex | Shared single-adviser block | Verified `b7babadb9f33` |
| ask-claude-and-astra-for-codex | Shared paired block and diagram | Verified `a6900b0cd4ce` |
| ask-claude-and-sol-for-codex | Shared paired block and diagram | Verified `25dbea7e824f` |
| ask-claude-for-codex | Claude-only source block | Verified `d973249a6e5b` |
| benjaminstelzer-github-skill | README and future-project publication policy | Verified `d94ab4cdc049` |
| benjaminstelzer-imitate-me | Independent README | Verified `e8f1754a99a8` |
| gemini-worker | Independent README; existing usage retained | Verified `50a00edf97f9` |
| empco-check | Project README; setup boundaries retained | Verified `c5a383989f75` |
| divi-5-fluid-base | Project README; build commands retained | Verified `76be0141e328` |
| scoville-workflow-codex | Superseded private source | Preserve; no second maintained Workflow |
| BenjaminStelzer | Personal profile, not a product README | Verified `3fe638b4bc0d` |

## Validation

- Shared tests check exact description reuse, nested headings, required lists,
  family order, both Workflow thresholds and retained flowchart.
- Builds check package inventories and links, including Ask variant expansion.
- Isolated suite builds must match authoring-workspace outputs.
- Standalone projects receive README-only commits. Their application sources,
  local installations and live workflows are not changed.
- Full remote tree and commit checks distinguish a push from a verified result.

Publication is complete. Existing releases and tags were not changed.
The four reordered standalone family lists contain the same lines; suite runtime
files are byte-identical to their previous published versions. GitHub Skill policy
and publication-check changes were included as requested.

Validation: 40 shared tests, 5 Scoville build tests, 8 Ask tests and 49 GitHub
publication tests passed. All 15 packages passed layout, frontmatter and README
contract checks. Mermaid source was preserved or inspected; browser rendering
was not tested. The profile retained its personal structure.
