# Project README contract

Use this structure for every project, including Skills of any family. Write
public text in English with Benjamin's voice, for someone deciding whether to
install the project and then using it.

A README answers, in this order: what it is and what problem it solves, what
the agent does differently with it, what that costs, how to call it, how to
install it, which settings exist and where it stops. Leave out what answers
none of these: how the suite is built, internal terms the reader never types
or sees, measurements the reader cannot act on, and statements about what was
not tested or proved. Keep a negative statement only where the reader would
otherwise assume the opposite and act on it. Write to the reader; instructions
for the agent belong in the Skill.

State each fact once, in the section where the reader looks for it. What the
introduction says is not repeated below it. A Scoville README that explains
the name does so once, in the introduction. Use restrained humor where it fits.

1. `# Project name`: concise prose explaining the problem, purpose and benefit.
2. `## How it works`: three to seven bullets on what the agent visibly does,
   including what it refuses to do.
3. `## What it costs`, when the reader decides something by it: added tokens,
   time, agent runs or fees. No invented metrics.
4. `## How to use`: example requests, then only what the reader needs to call it.
5. `## Install`: requirements in one or two sentences, then the installation
   request.
6. `## Configuration`, when there are settings to explain.
7. `## Limitations`, when a limit changes what the reader does, with its workaround.
8. `## Background`, optional: where the project came from in two or three
   sentences, a measured result in one sentence that names every model it
   was measured with, a link to the full instructions and its sources in one
   line. Result tables stay in the development notes.
9. `## Developer links`, when included in this distribution.
10. `## License`

The builder checks this order for Scoville members and accepts a missing
optional section. Member READMEs stay within about 700 words. A suite README
introduces the suite, lists each member with one sentence and a link to its
README, and then covers installation and suite-wide settings; it does not
repeat member sections.

Use a flowchart only when it replaces a longer explanation of branches or
dependent steps; one per README. Keep technical requirements and install paths
exact. After building, read each distinct assembled README for flow,
repetition and correct section placement. Fix sources, rebuild and recheck
affected output before publishing.
