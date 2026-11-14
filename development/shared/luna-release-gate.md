# Release validation

Validate changed behavior with appropriate technical checks and authorized model
or real-workflow tests. No fixed historical case catalog or case count is required.
Model tests use gpt-6.1-sol with reasoning effort medium; a claim about another
model needs a run with that model. Record the model, effort, actual results and
remaining limits; do not claim an unrun test passed.
A model test shows an effect only on a task the instruction was not written
against. Keep a test task's values, names and planted defects out of the
instruction text. After changing an instruction because of a task's result,
confirm the effect on a task with another domain and other specifics, built
from the wanted behavior, not from the changed instruction's wording or
examples. A re-run of the failing task shows only that the change matches
that task. A pass from a scorer that only matches answer text shows the
wording, not the behavior: claim behavior only from scored actions or
artifacts, and read the answers such a scorer fails before counting them.
No specific CLI transport or coordinator is required for publication.

Retain each test agent's exact handle and final result. Close or archive a terminal
agent only through a documented host operation and verify its completion. Send no
routine messages after native completion. A capacity refusal preserves the actual
diagnostic, pending work, results and exact handles. Do not wake completed agents
for cleanup, retry the spawn automatically or create replacement chats. Necessary
questions and unfinished assignments may continue on their retained handles.

Package integrity, helper/fallback contracts, compatibility, committed source,
publication authority and remote verification still apply. Follow the suite's
AGENTS.md for staging and distribution ownership.
