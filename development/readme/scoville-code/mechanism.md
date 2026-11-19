## How it works

- Before writing, the agent looks for what the project already has: the
  function that does the job, the module it belongs in and the way the project
  builds that kind of thing.
- It starts from the simplest approach that solves the request and holds its
  code to it.
- While writing, it keeps one path, uses other modules through their public
  interfaces, keeps each fact in one place and reads its own loops for work
  that repeats per item. That is a reading check, not a benchmark.
- It names the test that proves the request and reports it by name. For a
  bug fix, or new behavior whose failure would charge a wrong amount, grant
  access, lose data or open a security hole, it sees that test fail first. A refactoring keeps the existing tests green
  before and after; a change without runtime behavior gets the fitting source
  or build check, not a test.
- It ends by reading its diff against these rules and reports the test that
  proves the request.
- Where the host can start a separate agent, a change to code behavior is
  then read once by an agent that has not seen the author's reasoning. The
  author declines findings that only ask for more protection. Under a
  workflow that already reviews each change independently, that review takes
  its place.
- A review goes through the same points in someone else's change and names
  the place, the problem and, where one exists, the function, path or
  interface to use instead.
