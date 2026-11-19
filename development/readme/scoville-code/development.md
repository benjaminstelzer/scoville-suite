## How it was developed

Code grew from engineering work in large, evolving projects. Early versions
could turn a small change into a ritual: extra safeguards, repeated checks and
elaborate proof that added little to the result. The useful shift was toward
the actual problem, a maintainable solution and tests that protect real behavior.

Ideas are tried in focused tests, then checked against complete workflows in
real projects. Missed requirements, unnecessary complexity and wasted work feed
into the next revision. The revised rules go through the same cycle again.

### What the tests showed

Two tests, each with the Skill against no Skill: a review of 18 real changes
that each hold a defect fixed later, and a new web application built from
five consecutive requests. The state of November 2026:

**Claude Opus 5.5, medium reasoning effort**

| Test | Measure | With the Skill | Without |
| --- | --- | --- | --- |
| Review | Defects found (of 18) | **16**\* | 10 |
| Review | Misplaced module boundaries found (of 3) | **3**\* | 0 |
| Review | Time per review | **143 s**\* | 145 s |
| New application | Hidden acceptance checks | all passed | all passed |
| New application | Versions with quadratic work | **none** | 1 of 2 |
| New application | Mechanisms nobody asked for | **2 to 4**\* | 14 to 18 |
| New application | Places with repeated work | **0 to 2**\* | 2 to 9 |
| New application | Hidden errors | **0 to 1**\* | 4 to 6 |

**gpt-6.2-sol, medium reasoning effort**

| Test | Measure | With the Skill | Without |
| --- | --- | --- | --- |
| Review | Defects found (of 18) | **12**\* | 10 |
| Review | Misplaced module boundaries found (of 3) | **2**\* | 0 |
| Review | Time per review | 260 s\* | **178 s** |
| New application | Hidden acceptance checks | all passed | all passed |
| New application | Versions with quadratic work | none | none |
| New application | Mechanisms nobody asked for | **4 to 8** | 5 to 9 |
| New application | Places with repeated work | **0** | 3 |
| New application | Hidden errors | **0** | 0 to 1 |

The better result of each row is bold. \* An older run, measured with an
earlier revision of the rules.

With the current rules neither model builds locks, synchronisation between
windows, paging or caches the requests did not ask for, and a failed write or
file read is reported to the user.

The limits: one or two runs per cell show a direction, not an effect size.
The rules grew from the same two projects the review cases come from. The
Sol counts with the Skill were made by other readers than the counts without
it, so that pair is a rough comparison.
