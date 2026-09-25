# Native editing safety

Edit native Markdown and YAML directly. Read the affected records, apply the
change and check the result. These edits are not atomic transactions.

## Write compact worker-ready records

Write complete instructions for the task without selecting a model profile.
Keep facts needed to execute, review or resume the work. Put each fact in its
owning field, prerequisites before actions, and checks after the behavior they
prove. Remove repetition without dropping scope, authority or acceptance.

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

Write for a recipient with no hidden conversation context. The
worker and reviewer must be able to identify the result, scope, applicable
choices, exact order, targets, blockers, and proof without reconstructing omitted
intent. Split a dense compound instruction instead of compressing it into an
ambiguous sentence. Do not repeat rationale to make a record look complete.

Preserve constraints, alternatives, tradeoffs, uncertainty, exact identifiers,
Acceptance, and Evidence. Brevity never authorizes immutable-history changes,
weaker proof, or invented verification. Keep already concise text. Use no fixed
word or sentence count as a quality substitute. The structural validator does
not perform this semantic check.

## Read, edit and verify

Use one run at a time. Do not edit affected project files or change model
settings in parallel. Plan does not lock files or recover concurrent edits.

1. Resolve the project root and read PROJECT_INDEX.md, the active Plan header
   and the complete affected Work Item or Decision. Read referenced Decisions
   and relevant proposals. Inspect other records only for affected references,
   dependencies or ID allocation. Unknown root or unsupported format stops the
   affected change.
2. Make a context-bound edit in the owning file. Preserve unrelated content,
   record IDs and authored history. P, W, L and D own format and lifecycle.
   For a change involving several files, prepare their consistent final state
   together and write the project index last when routing changes. A normal
   single-file edit needs no multi-file preparation.
3. Reread changed blocks and inspect the scoped diff. Check user authority,
   meaning, preserved history, actual evidence and the next unfinished action.
   {{ profile: general }}When Python is available, run the bundled validator
   through V. Without Python use its manual route.{{ /profile }}{{ profile: codex }}Run the required
   bundled validator through V; Python 3.11+ is required.{{ /profile }} A structural
   pass does not establish acceptance or prove that work happened.

Use UTF-8 without BOM and LF for authored files. Keep canonical paths inside
this project and reject traversal or redirected targets. Never overwrite an
existing ID or invent evidence. Apply the operation date only for real changes.

Use bounded reads for current work and complete records when meaning or a
relation is unclear. Truncated output is not evidence of absence. Reuse loaded
instructions; reread only when they changed or their contents are unavailable.
No hash, byte receipt or saved copy is required for routine record edits.

Report visible contradictions, partial writes and errors honestly. Repair a
format defect only when it does not change authored intent. An interrupted
lifecycle change needs the user's decision before completing or undoing it.
Successful verification belongs to the inspected state; relevant later changes
require the affected check again. Report result, evidence limits and next action.
