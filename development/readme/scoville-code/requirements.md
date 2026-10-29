## What it enforces

- **Work that serves the request.** Refactors, safeguards and tests need a
  concrete purpose. The agent asks about material choices and settles routine
  details from the project. It explains conflicting requirements or evidenced
  feasibility limits without substituting a different result.
- **Your conventions.** Existing architecture and project rules take precedence.
  New projects start with a small structure organized by responsibility.
- **Evidence that fits the change.** Check the behavior, preserve guarantees and
  distinguish observed results from what remains unverified. Code review traces
  relevant loops, scans and recursion; nested syntax alone is not a defect.

Keep personal conventions outside the installed Skill so updates preserve them.
See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
and [full instructions]({{ var: contract_url }}).
