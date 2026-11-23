## How it works

- Before writing, the agent looks for what the project already has: the
  function that does the job, the module it belongs in and the way the project
  builds that kind of thing. It doesn't add a second implementation beside
  the one that works.
- It starts from the simplest approach that solves the request. A safeguard,
  an abstraction or a test needs a real case in this application - a local
  script is not hardened like a payment service.
- It names the test that proves the request and reports it by name. A bug is
  confirmed before it is fixed and then covered by a passing test. Behavior
  whose failure would charge a wrong amount, grant access, lose data or open
  a security hole also gets a test that is seen failing first. "All tests
  pass" doesn't count when the relevant test wasn't among them.
- The report keeps what was observed apart from what remains unverified.
- Your architecture and project rules come first.
- Where the host can start a separate agent, a change to code behavior is
  read once by an agent that hasn't seen the author's reasoning.
- A review goes through the same points in someone else's change and names
  the place, the problem and what to use instead.
