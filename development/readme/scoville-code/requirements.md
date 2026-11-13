## What it enforces

- **Code the next reader can extend.** No second implementation of logic the
  project already has, no parallel path beside the one that works, no reaching
  into another module's internals and nothing left behind.
- **Effort in proportion.** A safeguard, an abstraction or a test needs a real
  case in this application. A local script is not hardened like a payment
  service, and a small request stays a small diff.
- **Tests that prove something.** The test checks the requested result and
  actually runs; for a bug fix or costly behavior it is seen failing first. "All tests pass" does not count when the relevant test was
  not among them.
- **Your conventions.** Existing architecture and project rules take precedence.
  New projects start with a small structure organized by responsibility.
- **Honest evidence.** The report keeps what was observed apart from what
  remains unverified. The agent asks about material choices and explains
  conflicting requirements instead of substituting a different result.

Keep personal conventions outside the installed Skill so updates preserve them.
See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
and [full instructions]({{ var: contract_url }}).
