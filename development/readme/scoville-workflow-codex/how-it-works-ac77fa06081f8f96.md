## How it works

The launcher starts one coordinator in the existing checkout. The coordinator
selects a Plan unit, chooses its configured model and sends a helper-built prompt
to one worker. The prompt contains the selected work and referenced Decisions,
not the entire project history.

The dispatch helper keeps the payload separate from its compact delivery receipt.
An unchanged payload is reused. An uncertain delivery is recovered through its
identity and recorded state, not sent again on the assumption that nothing happened.

Instructions follow the same principle. A small required core routes to twelve
phase references. The coordinator loads the rules needed now and reuses them
while their complete, unchanged contents remain available. After context loss,
it reloads the current rules. Remembering that a file was read is not remembering
what it said.

Completed results are validated before review, acceptance or archival. Accepted
work and its accumulated Plan state enter one unit commit. The coordinator then
selects the next eligible unit within the requested scope.

Messages announce real transitions, findings and decisions. Unchanged waits stay
silent. The exact recovery and ownership rules live in
[Native Codex operations](scoville-workflow-for-codex/references/operations.md).
