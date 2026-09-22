# Project README contract

Use this structure for every project, including Skills of any family. Write public text in
English with Benjamin's voice. Preserve technical requirements and install paths.

1. `# Project name`: concise prose explaining the problem, purpose and benefit.
2. `## How it works`: concrete process bullets.
3. `## What it enforces`: requirement bullets.
4. `## What it costs`: cost, overhead and limitation bullets. No invented metrics.
5. `## How it was developed`: factual development bullets, not a prose recap.
6. `## Compatibility`
7. `## Install`
8. `## How to use`
9. `## Sources`
10. `## Family`: generated family links. Use `## Related projects` without a family.
11. `## License`

The first four parts form one description block. Store their ordered fragment
paths in `description_fragments`, also as the first four `readme` entries.
Suite READMEs reuse this exact block, shifting headings down one level outside
code fences. Never write a separate summary. Suite introduction, installation
and development text remain suite-specific sources.

Use a flowchart only when it clarifies branches or dependent steps and replaces
longer explanation. Keep the Workflow flowchart. Lists may precede a diagram.
Keep operational examples and configuration under How to use, limitations under
What it costs and developer links under How it was developed. Suite-only developer
links stay absent from standalone distributions. Preserve historical evidence.
