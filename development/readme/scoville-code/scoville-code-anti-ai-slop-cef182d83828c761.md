# Scoville Code

A coding agent can finish the wrong thing quite thoroughly. The tests are green,
the report sounds certain, but the behavior you asked for is still missing.

Scoville Code is the engineering foundation of the suite. Before substantial
editing, it requires the agent to establish what must work, which existing code
owns that behavior, what the change could break and which check would expose
that failure. Those answers guide the work. They are not another form to fill in.

The rules require the agent to:

- **Find the cause before patching the symptom.** Read the responsible code and
  the relevant callers, contracts and tests. Expand the search only when the
  evidence points elsewhere.
- **Fix the existing implementation.** Keep behavior in its established owner
  instead of adding a parallel path, speculative abstraction or unrelated
  cleanup. Preserve the project's conventions and your unfinished changes.
- **Test the claim, not just the code.** Choose a check that could reveal the
  reported defect or the failure the change might introduce. A passing mock
  does not prove an integration that the mock replaced.
- **Investigate failures.** Do not call a failing test pre-existing without
  evidence, or weaken its assertions to get green output. If two corrections
  fail on the same underlying problem, reread the cause and change the approach.
- **Report what was actually verified.** A successful build is not a working
  user flow. Missing evidence stays visible, and required acceptance checks
  remain open when they cannot run.

The point is to connect the requested result, the implementation and the proof.
Each constrains the next. That makes it harder to substitute plausible code,
busywork or a confident completion message for the behavior you asked for.
It also limits unnecessary work. Once the changed behavior and its material
risks have decisive evidence, more searching and testing need a concrete reason.

Reading the relevant code and checking the result can use more tokens and time
than producing an immediate patch. The rules keep that cost tied to the actual
change, rather than requiring a full audit for every edit.

Use it for implementation, diagnosis, review and removal of code or engineering
artifacts. It can investigate without editing. Small changes should stay small,
while migrations, security boundaries and irreversible work need closer checks.
