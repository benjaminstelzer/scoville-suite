## Background

Code grew from engineering work in large, evolving projects. Early versions
could turn a small change into a ritual: extra safeguards, repeated checks and
elaborate proof that added little to the result. The useful shift was toward
the actual problem, a maintainable solution and tests that protect real
behavior.

In a review of 18 real changes that each hid a defect, Claude Opus 5.5 found
16 with Code and 10 without, `gpt-6.2-sol` 12 and 10 - one or two runs with
an earlier revision of the rules, so a direction and not an effect size.

The [full instructions]({{ var: contract_url }}) are what the agent reads.
The [development notes]({{ include: suite.repository }}/blob/main/members/scoville-code/development/README.md)
have the test tables and the sources.
