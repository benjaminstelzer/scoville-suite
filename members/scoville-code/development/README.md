# Development

Code began with a familiar failure: the patch passed its tests but missed the
requested behavior. Adding more procedure could make the same mistake more
expensive. The useful change was to connect each edit and check to the actual
outcome, then stop when more checking would not change the decision.

The [source](../scoville-code/) and tests live in the suite. Install the built package.

The unchanged [evaluation catalog](tests/evaluation-cases.json) is historical
PLAN-0034 evidence. Its cases include superseded expectations, such as a fixed
two-correction threshold, and do not define current behavior.

## What the tests showed

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

## Sources

- [OpenAI coding-agent best practices](https://developers.openai.com/codex/learn/best-practices)
  for explicit outcomes, constraints, permissions, and focused verification.
- [Cursor Thermo-Nuclear Code Quality Review](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md)
  for ownership, simplification, and complete-change review.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
  for prompt injection, unsafe output, information disclosure, and excessive
  agency.
- Martin Fowler on [internal quality](https://martinfowler.com/articles/is-quality-worth-cost.html)
  and [technical debt](https://martinfowler.com/bliki/TechnicalDebt.html).
- Simon Willison on
  [vibe coding versus reviewed AI-assisted engineering](https://simonwillison.net/2025/Mar/19/vibe-coding/).
- [Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
  for design, complexity, tests, naming, consistency, and review context.
- [DORA code maintainability](https://dora.dev/capabilities/code-maintainability/)
  for source discoverability, dependency traceability, and reproducible builds.
- Configurable file-size checks in [ESLint](https://eslint.org/docs/latest/rules/max-lines)
  and [Checkstyle](https://checkstyle.org/checks/sizes/filelength.html), whose
  different defaults are not treated as one universal standard.
