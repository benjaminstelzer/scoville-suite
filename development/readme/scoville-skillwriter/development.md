## How it was developed

Maintained in the Scoville Suite source project. Standalone and Suite packages share the same instruction-design source.

### Model tests

On 2026-10-29, controlled local tests in Codex with `gpt-6.1-sol` / `low` loaded
the public Skillwriter entry and the host's Skill Creator. The approved,
limited revision was applied with an exact pre-edit copy retained; metadata
and boundaries were preserved, and a separate review-only copy stayed unchanged.
The host's format validator passed. These observations cover the tested revision
and review cases. This run did not cover other authoring cases, installed
discovery or current Claude behavior; the edited Skills were not executed.

A separate standalone-prompt revision preserved the requested meaning and
baseline. The agent also read Skill Creator outside that fixture's permitted
scope. The task result passed; compliance with that reading boundary did not.
