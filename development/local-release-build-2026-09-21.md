# Local release candidate — 2026-09-21

User requested all Skills, including Workflow, generated for the next live
project test. No publication, installation, task mutation or visibility change.
W-009 remains paused; this build does not resume its configuration work.

Build root: `<workspace-root>/temp/2026-09-21-local-release-build/`.
Keep this candidate until the project test/installation decision is settled.

| Suite | Output subdirectory | Verified packages/files | Receipt SHA256 |
| --- | --- | --- | --- |
| Scoville | `scoville` | 9 / 170 | `d4afb9c8adac59404e8fbdbf9e5b6715ddf14d28fb8ce04f7c4985d8edd975fd` |
| Ask | `ask` | 5 / 51 | `2d17065e9c7d7eb0b29c2b4a045ed69d492f7aa14d39d677eb7a93af22221026` |

From each suite root, ran `python -B development/build_suite.py --output
<output>` without a member filter or public-only flag. Both `--check-packages`
and shared `verify_package_set.py --root <output> --receipt
<output>/build-receipt.json` returned valid:true with no errors.

Workflow remains suite-only at
`scoville/scoville-suite/packages/scoville-workflow-for-codex/scoville-workflow-for-codex`.
All its receipt-listed files match the Terra-tested W-023 package exactly.
Thresholds remain coordinator 33 / worker 66. No new model tests were run.

Sources are uncommitted; receipts identify content hashes rather than a release
commit. This is a local test candidate, not a published or installed release.
Before the real-project test, install the chosen built packages separately;
do not run member templates or assume current installed Skills were updated.
