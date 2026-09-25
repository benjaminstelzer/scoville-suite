# Native editing safety

Direct edits are the only Scoville Plan write path. They have no publication
gate, expected-hash writer, typed request validation, rollback, or multi-file
atomicity. Compensate with narrow reads, exact-byte checks, complete
proposed-state inspection, and honest reporting.

## Contents

- Write compact worker-ready records
- Read before writing
- Guard the write
- Preserve the profile
- Handle invalid or changing state
- Verify and report

## Write compact worker-ready records

Select writing depth per Step, or per whole item without Steps. Run the bundled
`scripts/resolve_prompt_profile.py --config <skill-directory>/assets/prompting.toml`
with `--model <exact-recipient-model>` when known. Only without a target model,
pass `--task-class` if a class already exists. If neither is known, omit both
options: `auto` resolves to `medium`. Do not search for a model, create an
assessment or block writing to fill these optional inputs. An explicit
user low/medium/high request uses `--profile` within its stated scope. The
helper returns the common rules and only the selected profile. Apply those
rules to the authored point; never assume conversation history. Each installed
Skill owns its settings. An unknown model uses medium, even for a high task class.
{{ profile: general }}Python 3.11+ is required for this helper. Python 3.10 or older is present but
unsupported: report the version error and do not use a manual route. Only when
no Python executable is available, load
[prompt-profile-without-python.md](prompt-profile-without-python.md).
A helper or configuration error is a diagnostic, never permission to use that route.{{ /profile }}{{ profile: codex }}Python 3.11+ and this helper are required. Missing or unsupported Python,
helper failures and configuration errors block the affected operation; report the diagnostic.{{ /profile }}
Added explanation does not create extra Steps or worker dispatches.

Before drafting or refining a Plan, Work Item, or Decision:

1. Resolve and apply the writing profile through the helper contract above.
2. Keep only facts needed to choose, execute, review, resume, or verify the work.
3. Assign each fact once to its owning field or section.
4. Put prerequisites before dependent actions and checks after the behavior they prove.
5. Remove any sentence that changes no choice, action, order, constraint, check, or recovery fact.

Before any Goal write, classify every fact in the complete proposed Goal, not
only the changed sentences. Goal owns only the current target, its boundary,
and genuinely plan-wide constraints. Route exclusions to Non-goals, material
choices to Decisions, point-specific scope, order, checks, model, or reasoning
to the affected Work Item or Step, observed results to Evidence, the next move
to Next action, and repository policy to its canonical project instruction;
omit irrelevant prose. Operational messages that change none of the Goal-owned
semantics leave its bytes unchanged. Moving existing Goal facts to other fields requires separate authorization.
Before that normalization, check that every affected future dispatch can still
reach each needed requirement through its selected Work Item, a referenced
Decision, or a repository contract demonstrably loaded for that dispatch. Do
not create a second requirement registry, truncate selector output, or use a
size limit as a substitute for ownership.

State the concept first in Goal, Outcome, or Decision. Use compact bullets for
equal-rank facts and numbered Steps for execution order. Each Step names one
concrete action, its target, and the necessary result. When a repository-relative
file is already known, cite it directly in the Step that changes or checks it.
When the owner is unknown, prefer bounded read-only discovery before starting
the item, then refine its `todo` Steps with the observed path. If discovery must
happen after start, keep its ownership criterion in the immutable Step and put
the observed path in Evidence and the next concrete action. Never invent a path.

Write each future Step from the mechanism the worker must perform, not only the
small final edit it may produce. Name required search or inventory, every known
language or component boundary, mirrored contract or interacting owner, helper,
mock, harness, generator, and any validation whose result needs interpretation.
If one of these facts is unknown, say what must be discovered instead of hiding
it behind a simple verb. For example, write “inventory the PHP and JavaScript
mirrors, identify each owner, update their reciprocal contract comments, and run
the parity checks,” rather than only “add reciprocal comments.” Plan still does
not assign the route; this wording gives the coordinator the facts needed to
choose it safely.

Write for the selected recipient profile with no hidden conversation context. The
worker and reviewer must be able to identify the result, scope, applicable
choices, exact order, targets, blockers, and proof without reconstructing omitted
intent. Split a dense compound instruction instead of compressing it into an
ambiguous sentence. Do not repeat rationale to make a record look complete.

Preserve constraints, alternatives, tradeoffs, uncertainty, exact identifiers,
Acceptance, and Evidence. Brevity never authorizes immutable-history changes,
weaker proof, or invented verification. Keep already concise text. Use no fixed
word or sentence count as a quality substitute. The structural validator does
not perform this semantic check.

## Read before writing

1. Resolve the nearest project root containing `PROJECT_INDEX.md`,
   `docs/plans/`, and `docs/decisions/`. When profile existence is unknown,
   list the workspace root before reading a canonical path.
2. Read the index and resolved Plan frontmatter and require `format_version: 1`
   in each. Read the current and affected complete Work Item blocks, the title,
   Goal and Non-goals needed to interpret the work, referenced Decisions, and
   relevant `proposed` Decisions found through a frontmatter inventory. Keep
   other proposal IDs discoverable; read their bodies only for a full audit.
   Load other records only for the selected operation's relation or evidence checks.
3. Inventory all valid records only when allocating an ID, validating the
   complete profile, or checking a cross-record relation.
4. Capture the exact bytes and SHA-256 of every affected existing file. Re-read
   and compare those exact bytes immediately before a context-bound patch.
   Keep complete byte snapshots in the execution environment; return the hash
   or comparison result, not unchanged file bodies, to model context. A hash
   detects change; it proves neither valid content nor permission to write.

### Scope output without narrowing checks

For identity, order, or graph checks, extract ordered H3 headings and `Status`,
`Depends on`, and `Decisions` lines. For current work, changed authored text,
acceptance, or evidence, read the complete relevant blocks. ID allocation must
still inspect all IDs in its namespace. Proposal discovery still covers every
Decision. A selected slice never proves that unrelated records are valid.

Machine reads may cover whole files or the complete proposed profile while
returning only selected blocks, hashes, scoped diffs, and validator diagnostics.
Preserve the full captured bytes for unchanged-content comparisons. Verify
proposed and written structure completely when required; do not replace this
with a grep result, a zero-length diff, or an old validator result.

{{ profile: general }}For a manual structural check when Python is unavailable, load
[profile-without-python.md](profile-without-python.md). {{ /profile }}Use full reads for
full-content audits and relevant malformed-state diagnosis. If extraction
boundaries or output completeness are uncertain, widen the read; never
interpret truncated output as absence.

Reuse relevant Skill instructions while their contents remain available and
their source identity is current. Reload missing contents even when a retained
hash is unchanged. Observed edits, version changes or stale-source signals
require reloading the affected reference before dependent work; if freshness is
uncertain, inspect that source. Do not hash or reload every reference merely
because another operation began. Reread the required live project records and
preserve their exact-byte write guards above; unchanged instructions do not
establish unchanged project state.

## Guard the write

- Prepare every member of a multi-file change and inspect the complete proposed
  profile before applying any member. Publish the canonical routing file last
  when that reduces, but cannot eliminate, partial-state risk.
- Create new files exclusively after rechecking ID and path collisions. Never
  overwrite another record or reuse an interior ID gap.
- Use context-bound patches for existing files. If affected bytes changed,
  stop and reconcile instead of replaying a stale edit.
- For physical deletion, validate the complete proposed project with the exact
  file or Work Item absent before removing it.
- Never describe direct multi-file edits as atomic. If only a proper subset is
  written, report the exact partial state and stop.

## Preserve the profile

- Preserve UTF-8 without BOM, LF endings, exact frontmatter and section order,
  Work Item key order, stable IDs, authored H3 order, optional Steps, retained
  batch metadata, and every lifecycle invariant in the routed format guides.
- Keep canonical paths relative to the project root. Reject traversal,
  cross-project targets, redirected canonical files, and symlink escapes.
- Use the operation date for each permitted change. It may equal but never
  precede the affected record's stored date. A no-op changes no bytes or date.
- Verify every dependency, Decision, supersession, blocker, `current_item`, and
  active-Plan reference against the complete proposed profile.
- Never invent authored text, evidence, authority, status, acceptance, or a
  lifecycle result to make the profile valid.

## Handle invalid or changing state

Stop on an unsupported version, foreign or partial profile, ambiguous root,
path-security failure, ID exhaustion, changed bytes, or a write whose result is
unknown. Do not create a parallel profile or edit around the failure.

Repair invalid state autonomously only when an observed diagnostic identifies
one specific format defect and the repair changes no authored choice, scope,
acceptance, lifecycle result, or evidence. Never autonomously complete or
revert an interrupted multi-file transition. Interrupted activation,
completion, supersession, or Decision-batch state requires explicit user
authority.

## Verify and report

After writing, reread changed frontmatter and the complete affected Work Item
or Decision blocks, inspect the complete scoped diff, and compare full resulting
bytes with the prepared result so unexpected edits outside those blocks are
not hidden. {{ profile: general }}When Python is available, run the bundled read-only validator{{ /profile }}{{ profile: codex }}Run the required bundled Python read-only validator{{ /profile }}
on that final unchanged state as described in
[profile-validation.md](profile-validation.md). A complete successful run owns
its reported structural invariants for those exact bytes, so do not repeat the
same full structure matrix manually. {{ profile: general }}Without Python, load
[profile-without-python.md](profile-without-python.md); never make an
executable a dependency of this Skill. In both cases,{{ /profile }}{{ profile: codex }}Missing or unsupported Python and validator failures block the affected
operation. Always{{ /profile }}
manually review authorization, meaning, Acceptance and Evidence sufficiency,
preserved history and user changes, prepared versus written bytes, uncovered
graph or lifecycle invariants, and changed prose under the compact-record rules.
Structural validity alone does not establish precision or sufficiency.

Report exact changed records, manual checks, validator output when actually
observed, unresolved proposals, partial-state risk, and the next concrete
action. Say `native structural inspection passed`; do not imply executable,
transactional, or typed validation that did not occur.
