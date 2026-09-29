# Scoville Plan

Before an agent starts implementing, it should be clear what it is supposed to
achieve and how the result will be checked. A Plan makes the goal, dependencies
and acceptance criteria explicit. That matters in AI-assisted software
engineering, especially when the work spans several conversations.

Scoville Plan keeps those facts in the repository: Work Items, relevant
Decisions, accepted results and the next action. The next agent can pick up the
work from there. You can see what is finished, why a choice was made and what
still needs checking, without piecing it together from an entire chat.

For substantial work, the Plan deserves substantial attention before execution.
Clarify requirements, check dependencies and get independent feedback, for
example through Scoville Ask. Revise the Plan until the material questions are
settled. Complex work may need several rounds of review and changes before
Scoville Workflow starts implementing it. Its coordination overhead makes sense
when the size and dependencies justify it. Good planning is a substantial part
of software engineering. AI helps with the work, while goals, architecture and
tradeoffs still need informed judgment.

When implementation shows that an assumption was wrong, update the Plan. Its
job is to preserve direction while the work develops. Use it for dependent work
and long-term maintenance, within the project's existing planning system. Keep
small tasks small. A large Plan for a contained fix only adds work.

Here, the heat is the direction another agent can recover: the goal, decisions, current state and next action.
