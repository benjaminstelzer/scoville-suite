## handoff-v2
Coordinator rollover first, carry checked-fix review due; new coordinator reviews fixed quote-decoding delta before dependent tests; no premature Step acceptance.

## worker-v2
Return completed checked fix with unfinished Step tests. No extra checkpoint or broad tests, no claim full Step completion. Result text ready for coordinator without rewrite.

## coordinator-fix-v2
Review only checked product fix and affected acceptance; do not mark Step complete. Archive completed worker normally, preserve remaining tests, new worker after review/checkpoint.

## reviewer-v2
Use actual builder assignment, review only unreviewed delta+affected acceptance and interactions; reuse review A unchanged; if changed dependency reassess affected interaction.