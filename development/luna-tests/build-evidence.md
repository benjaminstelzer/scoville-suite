# Evaluation package checks

Observed 2026-09-21. Local candidates only, not publication approval.

- `E:/Dropbox/AI Projects/skills/public`: 13 package directories and 187 files
  match the union of both suite receipts exactly by relative file inventory
  and SHA-256. No extra package-root directory was found.
- Scoville receipt: `skills/public/build-receipt.json` relative to workspace.
- Ask receipt: `temp/2026-09-21-suite-migration/ask-luna-candidate/build-receipt.json`.
  It covers the five copied Ask packages, not Scoville. Do not overwrite one
  receipt with the other or claim the public-root receipt covers both suites.
- Current-source `--check-packages` passed for Scoville public packages and
  Ask's original staging. Public Ask file hashes match that staging's receipt.
- Fresh private Workflow build: `temp/2026-09-21-suite-migration/workflow-luna-final`.
  Its `--check-packages` passed; member file hashes match the previously reviewed
  private build. Test the nested suite package there, never a standalone repo.

All builds have `source_commit:null` and `source_dirty:true`. These are evaluation
candidates, not clean-revision release evidence. No package was published or
installed. Shared `build/verify_package_set.py` now verifies multiple receipts
against one exact output inventory without merging or overwriting receipts.
Its focused positive/negative test passed. The public check passed for 13
packages and 188 files including the root Scoville receipt (187 package files).
It checks output identity only, not source freshness or publication readiness.

## Informative byte sizes

The existing builder adds per-file, entrypoint and complete-package byte counts
to each member in build-receipt.json. They are informative, with no size gate or
token estimate. Inspect current payloads without writing a build:

```text
python development/build_suite.py --size-report --profile general --member scoville-plan
```

Add `--load-trace MEMBER PATH_TO_SUMMARY` for an existing runner summary. The
report lists the reference files actually served on that route, counting repeat
reads. It reports observed_reference_bytes only when their recorded hashes
match the current files. Otherwise that field is null and the separately named
current_equivalent_reference_bytes is only a current-size comparison. Entrypoint
size is separate: the trace does not prove how the prompt loaded the entrypoint,
and these counts exclude host instructions, helper output and model responses.
This adds reporting to the builder, not another runner.
