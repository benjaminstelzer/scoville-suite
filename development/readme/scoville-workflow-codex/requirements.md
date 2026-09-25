## What it enforces

Scoville Workflow requires a frontier LLM from the Fable, Astra, SOL or Opus
families, version 5.0 or newer. Earlier policy qualification used GPT-6 SOL Medium. The simplified workflow
is undergoing fresh validation; those earlier results do not qualify this revision.

- **Explicit activation.** Asking for implementation or delegation alone does not start Workflow.
- **Separate responsibilities.** The coordinator owns Plan updates, dispatch and accepted commits. Workers implement. Reviewers stay read-only.
- **One live checkout.** Tasks use the existing working state. Workflow does not create an isolated worktree without an explicit choice.
- **Single-run operation.** One worker handles one unit at a time. The run record retains the active task and next action. Change configuration between runs and avoid parallel project edits.
- **Complete but bounded context.** Dispatch includes the selected Plan unit and its Decisions without truncation. Workers do not reconstruct it from a summary or reopen the Plan.
- **Configured routing.** Risk selects the model and effort. Unsupported required pairs block rather than silently falling back.
- **Independent review where needed.** Code and critical documentation changes require a fresh reviewer. Unresolved worker findings allow at most three repair workers before user input is required.
- **Measured rollover.** By default, the coordinator hands over at or above 25 percent after an accepted unit. Child roles hand over strictly above 75 percent at a natural boundary. Missing or stale measurements are not guessed. Both thresholds are configurable.
- **Retained results before cleanup.** Results are retained before children are archived. A rollover successor takes ownership before archiving its predecessor, whose turn must have ended. Archive by exact task ID and check the reply once. Report errors without blocking accepted work. Tasks awaiting a user decision and the final coordinator remain open.
- **Accepted work before commit.** When committing is already authorized, a unit commit includes its accepted changes and complete accumulated Plan state. Failed hooks and outstanding backup requirements are not bypassed.
- **A binding scope.** Without a narrower boundary, continue through the active Plan. Preserve explicit stops and decisions. Archiving a task is not cancelling it.

- The canonical Plan owns progress. Workflow does not add a persistent Codex goal or another continuation loop alongside its coordinator.

- For delivery recovery, permission boundaries and failure handling, see [Native Codex operations](https://github.com/benjaminstelzer/scoville-suite-for-codex/blob/main/packages/scoville-workflow-for-codex/scoville-workflow-for-codex/references/operations.md).
