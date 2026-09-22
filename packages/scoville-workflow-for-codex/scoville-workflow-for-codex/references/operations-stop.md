# Stop phase

Observe completion with [wait](operations-wait.md); retain and validate the terminal result through [results](operations-results.md), then apply [review](operations-review.md)'s archival gate.

## Stop

When the user says stop, dispatch nothing else and send the exact instruction to
the active child through `send_message_to_thread`. Obtain fresh confirmation of
its resulting state. If native delivery does not interrupt it, report that fact
and the exact task the user must stop in the UI. Do not review, repair, commit,
or archive merely to simulate cancellation. After fresh state confirms a
terminal Stop result or failure and that result is safely retained, apply the
ordinary exact-ID archival gate before mutating the Plan to reconcile the Stop.
Stopping the coordinator does not imply that a child stopped; never claim a
cascade that was not observed.

Release the guard only when all children are terminal and every accepted or
retained result is safe. Completion and explicit cancellation use the helper's
`release` transition from an active coordinator with no writer or rollover.
Contract drift, a pending child, an interrupted rollover, or unexplained
workspace changes keep the guard for exact reconciliation or user disposition.
