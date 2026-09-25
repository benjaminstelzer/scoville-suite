# README style audit

W-027 reviewed the active README fragments for all ten Scoville and five Ask
packages, both suite introductions, shared blocks and current development
READMEs. Imported historical documents were not rewritten.

The edits keep Benjamin's direct, qualified voice. Existing strong openings
remain. Plan and Workflow now explain reader consequences instead of repeating
their operating contracts. Exact rules stay linked from the README. Ask
distinguishes native and Claude-only hosts, and
Workflow describes phase-based loading and dispatch reuse.

Development copy now identifies the suite owner. The viewer's retained
member-local Actions file is not presented as an active suite workflow.
WordPress theory tests remain distinct from live UI evidence. Workflow's open
host qualifications remain explicit. No new performance claims were added.

Release README word counts, measured by whitespace:

| README | Before | After |
| --- | ---: | ---: |
| Plan | 1526 | 1143 |
| Workflow | 3237 | 1758 |

These counts describe length, not measured token use or style quality.

Validation: 26 focused README/build tests, fresh README checks and both complete
package comparisons passed. Fifteen packages were built under workspace
`temp/2026-09-22-readme-style/`. All 223 non-README package files match W-026.
No model tests, installation or publication were performed.
