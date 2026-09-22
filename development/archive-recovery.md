# Coordinator archive recovery

The observed DIVI5 G3 → G4 transition activated G4 and completed G3's
activation turn, but `list_threads(limit=50)` omitted G4. G4 reported that
visibility blocked archival and continued. No archive call was present in the
inspected activation turn. Both installed and source contracts required that
visibility; this was not an observed archive API failure.

Shared `runtime/task_lifecycle.py` now returns retained handoff identity and
explicit archive blockers. Recovery runs once at activation or an accepted-unit
boundary with fresh guard and visibility evidence. A contiguous handoff chain
allows a later coordinator to resolve older predecessors. Exact successful
archive receipts prevent repeated calls; failed calls retain their targets.

The existing visibility safeguard remains: an unlisted, pinned or sectioned
current successor does not authorize predecessor archival. Missing visibility
permits guarded work, not a replacement coordinator. This patch fixes retained
recovery, not the host's incomplete listing. It cannot promise archival while
that blocker persists.

Local evidence: 58 Workflow tests and 20 Shared tests passed. The private
`workflow-archive-recovery` staging build matches its current sources. Tests
cover deferred recovery, contiguous generations, invalid completion/identity,
stale guards and exact archive receipts. No live task was archived, no provider
consultation ran, and Luna comprehension was not independently evaluated.

## Rollout

Do not replace an active task's installed Skill. At an idle boundary, install
the verified private build using the rename procedure in `workflow-rename.md`.
Keep the previous install backup. New rollovers retain the chain from creation;
legacy open predecessors require their original exact handoff/completion proof.
Missing historical proof is a reported blocker, never inferred from titles.
Verify the first real rollover and exact archive response before claiming live
recovery. Do not archive existing DIVI5 tasks merely to test this package.
