# Development

Shortening project rules exposed a trap: a repeated instruction may protect a
different scope, and a link may omit the exception that makes a rule safe. The
Skill now keeps independently needed copies and checks the full affected text.
Useful cleanup removes ambiguity and repetition, not the conditions that made
the instruction correct.

The [source](../scoville-project-context-cleanup/) and tests live in the suite. Install the built package.
