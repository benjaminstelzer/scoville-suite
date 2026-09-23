# Saved Deep package without Python

Load this reference only when a saved Deep package must be created or inspected
and Python 3 is unavailable. Use a host JSON parser. A new v2 package also
needs a byte-exact SHA-256 primitive. If a required capability is absent, stop
the saved-package operation; chat-only Deep can still proceed.

## Skill hash

Compute `skill_sha256` over the exact installed Skill directory. List every
regular file recursively except `.pyc` files and files below any `__pycache__`
directory. Sort by case-sensitive relative POSIX path. For each file, feed
these bytes into one SHA-256 stream: relative path as UTF-8, one NUL byte,
the file's raw bytes, one NUL byte. Store the final lowercase 64-hex digest.
Do not hash per-file digests, text-decoded files, host path separators, or a
source checkout. Stop if a path is a link or the file list or bytes change
while hashing. On resume, recompute and compare before changing an artifact.
A mismatch means the executing Skill differs from the run owner. Use the old
package or start a deliberate new v2 run only after the user chooses.

## Choose the package version

If neither `run.json` nor `evidence.jsonl` exists, treat the package as legacy
v1 and inspect it read-only. Never add either file or migrate it in place. If
`evidence.jsonl` exists without `run.json`, or `run.json` has an unknown schema,
report a mixed or unsupported package and stop. With a valid v2 `run.json`,
follow the v2 inspection below.

For v1, require readable UTF-8 `brief.md`, `queries.jsonl`, `sources.jsonl`,
`claims.jsonl` and a nonempty `REPORT.md`. Parse each nonblank JSONL line as
one object. Check the brief headings in order; check the default report
heading order when that form is used, as specified by
[deep-research.md](deep-research.md). Require unique `Q`, `S` and `C` IDs with
at least three digits; check required fields and allowed values against that
reference, with no v2-only optional source or claim fields. Every query
`source_ids` value and every claim `support` or `contradict` value must name a
source ID, not an evidence ID. Reject overlap, snippet support, and support
from a source marked contradiction, rejected, dead or blocked. Enforce claim
status rules, require contradiction and gap queries, and resolve every report
citation to a source. Every used or contradicting source must be cited. Record
the inspected files and gaps as manual legacy inspection. Do not require a
run-state hash, evidence ledger or external-job state from v1.

## Manual v2 structural inspection

Inspect the complete package on its final unchanged bytes, not just changed
rows. Record `manual structural inspection`, never validator output. Check
each item before marking `run.json` complete:

1. Require readable UTF-8 `brief.md`, `run.json`, `queries.jsonl`,
   `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` and, by validation phase,
   `REPORT.md`. Parse `run.json` as one object and each nonblank JSONL line as
   one object. Reject missing or unknown keys against the record shapes in
   [deep-research.md](deep-research.md); only the listed optional source and
   claim fields are additional.
2. Check `run.json` schema, all RFC 3339 timestamps, `updated >= created`,
   allowed phase/status and their complete/blocked pairings, and that
   `last_completed_query` is null or names a recorded query. Recompute the
   installed Skill hash by the byte procedure above; reject drift.
3. Require unique IDs matching `Q`, `S`, `E`, `C` or `J` plus at least three
   digits in their own ledgers. Check nonempty strings, null allowances,
   unique-string lists, ISO dates, absolute HTTP(S) URLs, enums and 64-hex
   hashes against the field descriptions in [deep-research.md](deep-research.md).
   External jobs need a positive integer timeout, nonnegative cost or null,
   Boolean privacy fields and a unique hash list. Reject a private upload
   without authorization.
4. Check every query source ID, evidence source ID, claim evidence ID and
   report citation against its ledger. Support and contradiction evidence
   must have the matching relation and never overlap in one claim. Reject
   snippet support and support from rejected, dead or blocked sources, or
   sources whose content is a paywall stub, mismatched or unreadable. Enforce
   the `supported`, `single-source` and `mixed` status rules.
5. Require the brief headings in order. In `synthesis`, `validation` or
   `complete`, require at least one contradiction and one gap query. At
   validation or completion, require a nonempty report; check default heading
   order when used. Every used or contradicting source must be cited and every
   citation must resolve. A completed run may retain only terminal external
   jobs (`completed`, `failed`, `cancelled`) with cleanup `not-required` or
   `complete`; a planned job has no provider ID, other job states need one,
   and running or terminal jobs need a last-polled timestamp.

If a check is uncertain or fails, record the file and field, keep the run open
or blocked, and do not claim a structurally checked package. Manual inspection
does not produce the validator's `valid: true` result or prove source truth or
claim support; perform the semantic evidence review separately.
