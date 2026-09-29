# Release validation

The fixed 45-case Luna CLI series is no longer a release requirement, following
an explicit user decision on 2026-09-29. Use targeted cases when a changed
behavior calls for them; no fixed historical case catalog is retained.

Validate the changed behavior with appropriate technical checks and requested
model or real-workflow tests. Record the actual results and remaining limits.
Do not claim a test passed when it was not run. No fixed model, CLI transport,
case count or coordinator is required for publication.

Package integrity, helper/fallback contracts, compatibility, committed source,
publication authority and remote verification still apply. Follow the suite's
AGENTS.md for staging and distribution ownership.
