# Deep research

Add this route when the user explicitly asks for deep, exhaustive, comprehensive, audit-ready, long-running, or interruption-prone research. It overlays the applicable General, Development, or Academic route.

For chat-only Deep, read and apply `Work in passes` and `Stop honestly`, then
stop reading this reference. Read `Create durable state` and `Validate the
package` only when the user explicitly requested saved artifacts.

## Work in passes

1. Freeze the brief and initial evidence questions before retrieval. For a requested saved package, also create `run.json` before retrieval.
2. Run a discovery pass with varied terms and source types.
3. Inspect the strongest sources and build the first evidence and claim sets. Store them in the specified ledgers only when a saved package was requested.
4. Run a dedicated contradiction and later-version pass.
5. Run gap queries against the weakest decision-relevant claims.
6. Draft once the stop conditions are met; do not draft around missing evidence.
7. Recheck every affected claim after revising the report. A correction must not silently regress an earlier supported claim or citation.
8. Complete the research only after semantic evidence review and any required external-job cleanup succeed. For a saved package, also complete its structural validation before marking the run complete.

When resuming a saved package, validate it, read `brief.md`, `run.json`, and the four ledgers, then continue from the recorded phase. Without a saved package, use the available conversation context and state any missing continuation facts. Do not repeat completed queries merely to look busy.

## Stop honestly

Stop when the Core conditions hold and targeted contradiction and gap passes no longer change a decision-relevant claim. Explicitly unresolved questions or conflicting evidence may remain in a completed, bounded report; completion does not certify those claims. Use blocked only when an unmet required check, access condition or external-job obligation prevents this closure. Name that obligation, not merely the existence of uncertainty. Required semantic review and job cleanup still gate completion. For a saved package, record the corresponding run state.

## Create durable state

The package files, schemas, file-resume rules, and package validation below apply
only when the user requests saved artifacts. Deep research alone requires no
saved documents. Without a saved-artifact request, perform the research passes
and return the result in the conversation without creating this package.
When saved artifacts are requested, use the user-specified output path. If none
was supplied, ask for an allowed project-owned or temporary path before writing.
The Core owns this narrow write authority. Every new durable Deep run uses the
v2 package below:

```text
<output-path>/
|-- brief.md
|-- run.json
|-- queries.jsonl
|-- sources.jsonl
|-- evidence.jsonl
|-- claims.jsonl
`-- REPORT.md
```

Do not create this package for bounded research that fits cleanly in the conversation. A directory without `run.json` is a legacy v1 package: it may still be inspected and validated, but do not mutate or silently migrate it. Continue in a separate v2 package only with authorization to create that durable state.

### `brief.md`

Use these headings:

```text
# Research brief
## Research question
## Decision or reader
## Scope
## Evidence lanes
## Deliverable
## Data boundary
```

Record the date, material assumptions, explicit exclusions, freshness requirement, and what would count as decision sufficiency.

### `run.json`

Create one JSON object before retrieval begins:

```json
{"schema":"scoville-research-run.v2","skill_sha256":"<64 lowercase hex characters>","created":"2026-08-19T12:00:00Z","updated":"2026-08-19T12:00:00Z","phase":"brief","status":"in-progress","last_completed_query":null,"external_jobs":[]}
```

Obtain `skill_sha256` from the exact package that will execute the run:

```text
python <skill-dir>/scripts/validate_research_artifacts.py --print-skill-sha256
```

The hash covers every portable Skill file through a stable relative-path manifest. On resume, validate before changing an artifact. A `skill_drift` failure means the executing Skill bytes differ from the run owner; do not continue until the user chooses the old package or a deliberate new v2 run.

Allowed phases: `brief`, `discovery`, `inspection`, `contradiction`, `gap`, `synthesis`, `validation`, `complete`, `blocked`. Allowed statuses: `in-progress`, `complete`, `blocked`. The `complete` status and phase occur together, as do `blocked` status and phase. Update the RFC 3339 timestamp, phase, status, and `last_completed_query` only after the corresponding durable write succeeds.

External backends remain optional. When a stateful or asynchronous backend creates a job, append this exact record shape to `external_jobs`:

```json
{"id":"J001","backend":"Example Research API","trust_boundary":"Third-party hosted service","estimated_cost_usd":1.5,"timeout_seconds":1800,"job_id":"job-123","status":"running","last_polled":"2026-08-19T12:20:00Z","disclosed_data":"Public query text only","upload_sha256":[],"contains_private_data":false,"private_upload_authorized":false,"cleanup_status":"pending"}
```

Allowed job statuses: `planned`, `submitted`, `running`, `completed`, `failed`, `cancelled`. Allowed cleanup statuses: `not-required`, `pending`, `complete`, `failed`. Record cost as a non-negative number or `null`, set a positive timeout, retain the provider job ID and last poll time, summarize disclosed data without copying it, and hash uploaded bytes when available. A private upload requires explicit user authorization for that disclosure. A run cannot become `complete` while a job is non-terminal or cleanup is pending or failed.

This ledger records trust, cost, polling, disclosure, and cleanup. It does not authorize a provider, upload, purchase, or network call.

### `queries.jsonl`

Append one JSON object per material query or retrieval attempt:

```json
{"id":"Q001","query":"exact query or endpoint purpose","lane":"general","purpose":"discovery","result":"new-source","source_ids":["S001"]}
```

Allowed lanes: `general`, `development`, `academic`. Allowed purposes: `discovery`, `verification`, `contradiction`, `gap`. Allowed results: `new-source`, `new-claim`, `no-new-evidence`, `dead-end`, `blocked`.

Do not put secrets or private source text into this log. Record a sanitized description when the actual input must remain private.

### `sources.jsonl`

Keep one current record per stable source ID:

```json
{"id":"S001","url":"https://example.com/source","title":"Source title","kind":"docs","publisher":"Example","published":"2026-08-01","accessed":"2026-08-19","inspection":"section","disposition":"used","notes":"Owns the API contract."}
```

Allowed kinds: `spec`, `docs`, `code`, `release`, `issue`, `pull-request`, `benchmark`, `paper`, `preprint`, `dataset`, `institutional`, `community`, `other`. Allowed inspection values: `full`, `section`, `abstract`, `metadata`, `snippet`. Allowed dispositions: `used`, `context`, `contradiction`, `rejected`, `dead`, `blocked`.

Keep rejected, dead, and blocked sources. They are part of the audit trail, but they never become supporting citations.

When a finalization check or retrieval boundary makes one of these facts decision-relevant, add any of the optional v2 fields below:

```json
{"accessibility":"public","final_url":"https://example.com/canonical-source","link_status":"redirected","content_quality":"usable"}
```

- `accessibility`: `public`, `authenticated`, `user-provided`, `private`, or `unknown`.
- `final_url`: the absolute HTTP(S) URL actually reached after redirects, or `null`.
- `link_status`: `live`, `redirected`, `dead`, `blocked`, or `unchecked`.
- `content_quality`: `usable`, `abstract-only`, `paywall-stub`, `mismatched`, `degraded`, `unreadable`, or `unknown`.

Keep these dimensions separate. An authenticated source may be usable; a public source may be mismatched; a live URL may still fail to support the claim. They are descriptive states, not inputs to an aggregate credibility score. During finalization, re-open a cited URL when the claim changed, the run was interrupted, the source is mutable, current link state matters, or the user requested link verification. A stable source fully inspected in the same unchanged run needs no duplicate retrieval. When a required check cannot run within the authorized tools or network boundary, record `unchecked`. Preserve dead links visibly and never invent a replacement. `paywall-stub`, `mismatched`, and `unreadable` content cannot support a claim merely because its metadata looks right.

### `evidence.jsonl`

Keep one current record per smallest practical inspected evidence unit:

```json
{"id":"E001","source_id":"S001","locator":"Conditional requests, paragraph 2","relation":"supports","inspection":"section","excerpt":"The endpoint accepts an If-None-Match header.","observation":null,"content_sha256":"<64 hex characters or null>"}
```

Allowed relations: `supports`, `contradicts`, `context`. Inspection uses the source inspection values. The locator must let another reader find the evidence. Keep the shortest sufficient excerpt, capped at 1,000 Unicode scalar values. When retaining source text would expose private material or exceed the permitted source boundary, set `excerpt` to `null` and record a scoped observation instead. At least one of `excerpt` and `observation` must be present. `content_sha256` is optional and hashes the inspected bytes when those bytes are available.

An evidence record is traceability, not proof that the text is true or correctly interpreted.

### `claims.jsonl`

Keep one current record per atomic claim:

```json
{"id":"C001","claim":"The documented API supports conditional requests.","basis":"reported","status":"supported","support":["E001"],"contradict":[]}
```

Allowed basis values: `supplied`, `reported`, `observed`, `inferred`. Allowed status values: `supported`, `single-source`, `mixed`, `unresolved`, `rejected`.

- `supported` has one or more adequate supporting evidence records and no contradiction; independence is explained when it matters.
- `single-source` has supporting evidence from exactly one source and no contradicting evidence.
- `mixed` has both supporting and contradicting evidence.
- `unresolved` preserves a material gap or conflict without a false verdict.
- `rejected` records a candidate claim that the gathered evidence does not support.

Evidence IDs in `support` and `contradict` must exist, match their relation, and must not overlap. Separate evidence from one source may support and contradict the same claim. Reader-facing citations still use source IDs.

For a time-sensitive claim only, add optional `"as_of":"YYYY-MM-DD"`. Leave it absent or `null` for a claim permanently scoped to an immutable specification, release, record, or historical event. Source publication and access dates remain separate facts. `as_of` narrows the claim's temporal boundary; it is not a confidence score.

### `REPORT.md`

Use these headings unless the user requested another compatible form:

```text
# Research report
## Answer
## Method and coverage
## Findings
## Contradictions and open questions
## Implications and next step
## Sources
```

Cite source IDs inline as `[S001]`. Every cited ID must exist in `sources.jsonl`; every non-obvious factual claim must map through `claims.jsonl` and `evidence.jsonl` to inspected evidence rather than memory.

## Validate the package

For a saved package only, when Python 3 and the bundled script are available, run:

```text
python <skill-dir>/scripts/validate_research_artifacts.py <research-directory> --format json
```

A new package succeeds with `package_version: 2` and `legacy: false`. An unchanged v1 package without `run.json` or `evidence.jsonl` may still succeed with `package_version: 1` and `legacy: true`; validation never migrates it. Mixed and unknown schemas fail instead of falling back.

Exit `0` with `valid: true` proves only required files, JSON or JSONL shape, stable IDs, run-state consistency, exact Skill-byte continuity, cross-references, report headings, and citation identifiers. It performs no network request and proves neither link health, source truth, source independence, semantic claim support, completeness, nor research quality. Fix structural errors, then perform the semantic evidence check yourself.
