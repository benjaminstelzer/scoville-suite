# Project contract setup

Use this reference only after `manage_agents_contract.py check` reports
`installed: false`.

If this task is already a coordinator or coordinator successor, treat the
failed check as contract drift. Perform no project, Plan, guard, staging, or Git
write. Report the diagnostic and end; an active workflow never installs or
updates its own project contract.

For a launcher, ask the user exactly whether Scoville Workflow may install or
update its managed block at the start of the project-root `AGENTS.md`. Do not
interpret the request to run the workflow as approval for this project change.

On refusal, end without another workflow action. On approval, run only:

```text
python <skill-directory>/scripts/manage_agents_contract.py install --workspace <exact-workspace-root> --approved
```

The helper may create `AGENTS.md`, prepend a missing block, move one exact
current block to the start, or replace one complete recognized older block. It
preserves every unrelated byte. A malformed, duplicated, changed, or ambiguous
managed block requires manual disposition; do not edit it by hand.

Run `check` again after a successful write. Report whether setup is ready, then
end this invocation even when verification succeeds. Do not enter the role
gate, read a Plan, acquire a guard, create a coordinator, stage, commit, or
start workflow work. A later explicit invocation must begin with its own fresh
check.
