# Native evaluation metadata

SOL preflight observed its own runtime on 2026-09-21:

- Task: `01a0c3a5-3a12-7fc2-9d19-ca42956a1486`.
- Exact rollout: `C:/Users/benja/.codex/sessions/2026/09/21/rollout-2026-09-21T13-06-20-01a0c3a5-3a12-7fc2-9d19-ca42956a1486.jsonl`.
- `session_meta.payload.id` matched its runtime `CODEX_THREAD_ID`.
- Native `turn_context.model` was `gpt-5.6-sol`; `effort` was `medium`.

This is native configured-runtime evidence, not provider/backend attestation.
The task-tool response alone did not expose these fields. In this record,
`session_meta.payload.session_id` named the parent session, not the child task;
do not use it to identify the child.

For each case, bind the exact task to its own runtime record and current turn,
then project model/effort only. Never infer from requested settings, parent
metadata, titles or recency. Conflicting or absent identity/turn evidence blocks
that case. Pilot code-01 verified this path for Luna: task
`01a0c3a9-efcf-7a42-8e59-aa34a88c1a0a`, model `gpt-5.6-luna`, effort `medium`.
The author independently checked its answer and native record. See results.md
for current accepted cases; this preflight alone does not pass the release gate.
