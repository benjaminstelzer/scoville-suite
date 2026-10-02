# Project README contract

Use this structure for every project, including Skills of any family. Write public text in
English with Benjamin's voice. Preserve technical requirements and install paths. Explain the benefit first,
with real limits in proportion. Use restrained humor where natural. Remove
internal detail and repetition that do not help readers choose or use the tool.
Write concise, complete explanations without TL;DR sections. Preserve existing
flowcharts. Each Scoville suite and member README briefly connects the chili-heat
scale to its purpose, with a small, relevant joke where it fits.

1. `# Project name`: concise prose explaining the problem, purpose and benefit.
2. `## How it works`: concrete process bullets.
3. `## What it enforces`: requirement bullets.
4. `## What it costs`: actual added tokens, time, fees or required user effort as bullets. One useful point is enough. No invented metrics, activation rules or disclaimers against unclaimed benefits.
5. `## How it was developed`: short prose about setbacks, useful changes and lessons.
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
Keep prerequisites in a two-sentence Compatibility section, setup and required
configuration under Install, and operational examples under How to use. Put material
compatibility or evidence limits beside the affected claim, not in What it costs.
After building, read each distinct assembled README for flow, connected
reasoning, repetition and correct section placement. Fix sources, rebuild and
recheck affected output before publishing. Keep developer links under How it was developed. Suite-only developer
links stay absent from standalone distributions. Preserve historical evidence.
