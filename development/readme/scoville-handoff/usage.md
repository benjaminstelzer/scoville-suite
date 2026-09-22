## How to use

Request an explicit transfer and name any task sources the receiver will need:

```text
Use Scoville Handoff to transfer this active task to a new session. Read docs/plans/0001-migration.md and ADR-0002.md, include the current Git state, and return one copy-ready continuation prompt.
```

```text
Create a compact handoff for another agent. Preserve the objective, accepted decisions, dirty files, observed test evidence, current blocker, and next safe action. Do not continue the task.
```

```text
Use Scoville Handoff for the work completed in this session. Mark unverified commands and external state as unknown rather than inferring success.
```

Explicit `$scoville-handoff` invocation also works on hosts that support named
Skill invocation. The former `$compact-handoff` identifier is retired. Natural
requests such as “compact handoff” still activate this Skill.
