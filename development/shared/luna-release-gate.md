# Release validation

The fixed 45-case Luna CLI series is no longer a release requirement, following
an explicit user decision on 2026-09-29. Use targeted cases when a changed
behavior calls for them; no fixed historical case catalog is retained.

Validate the changed behavior with appropriate technical checks and requested
model or real-workflow tests. Record the actual results and remaining limits.
Do not claim a test passed when it was not run. No fixed model, CLI transport,
case count or coordinator is required for publication.

For native Luna tests, retain each test agent's exact handle and final result.
Close or archive a terminal agent only when the host provides a documented
operation and its completion is verified. Send no routine messages after native
completion. A capacity refusal preserves the actual diagnostic, pending work,
results and exact handles. Do not wake completed agents for cleanup, retry the
spawn automatically or create replacement chats. Necessary questions and
unfinished assignments may continue on their retained handles.

Package integrity, helper/fallback contracts, compatibility, committed source,
publication authority and remote verification still apply. Follow the suite's
AGENTS.md for staging and distribution ownership.
