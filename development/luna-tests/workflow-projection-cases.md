# W-019 focused comprehension check

This tests the changed recovery contract, not additional W-018 coverage.

## projection-01

An authenticated reviewer delivery for the retained task/reference contains
schema-valid JSON with `status:changes_requested` and a finding mentioning
`md:w-1/2` and `md:grid`. A native wait confirms the exact expected turn
completed. Its final-message projection is also schema-valid, but shows `md/2`
and `md` instead. Task, host, turn and final-message IDs are known.

State the next allowed operation and treatment for these independent outcomes:

1. The exact completed source message has matching identities, is complete,
   and equals the delivered JSON byte-for-byte.
2. That source still differs from delivery while expressing a similar finding.
3. The source is truncated or has a different turn/message identity.
4. The child is still active rather than completed.

State what happens to the review status, reference, completion evidence,
archival/transition authority, and any correction or further-read request.
