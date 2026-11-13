## How it works

- Before writing, the agent looks for what the project already has: the
  function that does the job, the module it belongs in and the way the project
  builds that kind of thing.
- It names the simplest approach in one sentence and holds its code to it.
- While writing, it keeps one path, uses other modules through their public
  interfaces, keeps each fact in one place and reads its own loops for work
  that repeats per item. That is a reading check, not a benchmark.
- It names the test that proves the request, sees it fail without the change
  and pass with it, and reports it by name.
- It ends by checking its diff against these rules and puts the proof in the
  report: what it reused, which guard covers which real case, which test ran.
- A review goes through the same points in someone else's change and names
  the existing function, path or interface to use instead.
