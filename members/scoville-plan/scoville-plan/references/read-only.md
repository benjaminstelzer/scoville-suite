# Read-only project state

Use this route to answer questions about existing project knowledge without
changing canonical files. It does not require the native format guides.

## Select Work Item or dispatch-unit context

When Python 3 is present, select the current or explicitly named Work Item
with the bundled script. A missing script or script error is a blocker; it
never enables manual selection. The commands below specify the complete
invocation; do not load the Python source just to call them. Run:

```text
python <skill-directory>/scripts/select_context.py --root <project-root> [--work-item W-001] --format json
```

For a worker dispatch, select the exact unit instead:

```text
python <skill-directory>/scripts/select_context.py --root <project-root> --unit W-001 --format json
python <skill-directory>/scripts/select_context.py --root <project-root> --unit W-003/step-2 --format json
python <skill-directory>/scripts/select_context.py --root <project-root> --unit W-003/steps-2-3 --format json
```

The success object contains exactly four top-level semantic areas:

- `plan`: the exact Plan frontmatter plus Goal and Non-goals sections;
- `work_item`: the complete selected Work Item block in recovery mode, or exact
  structured unit fields in dispatch mode;
- `direct_dependencies`: only each direct dependency ID and its `Status` line;
- `decisions`: the complete Decision records referenced by the selected item.

Dispatch mode requires one exact Step or adjacent Step range when the Work Item
has Steps. Without Steps, the Work Item itself is the unit. `source_text` is
the unchanged selected single-line Step text, adjacent lines, or complete Work
Item block, including its Evidence for a whole-item unit. Text uses UTF-8/LF
and one final newline; trailing block-separator blank lines are excluded.
Other structured fields supply parent context. All referenced Decisions remain
present. Unselected Steps and Work Item-wide Next action are excluded for Step
units. Never rewrite source_text. Do not insert dependency Evidence into it.

The selector reads canonical files internally, emits no unrelated Work Item or
Decision body, never truncates, and never falls back to raw files. Its default
UTF-8 output budget is 65,536 bytes; use `--max-output-bytes` only when the
caller has an explicit bounded budget. A malformed profile, ambiguous record,
redirected path, missing reference, or budget overflow returns one structured
diagnostic and no partial context.

This projection does not replace every read operation. Inventory Decision
frontmatter and load relevant proposals separately, or all for a full audit. Read relevant dependency
Evidence, bounded graph state, queued or paused return state, and complete
relevant Work Items separately when the operation requires them. Keep those
reads bounded and never widen the selector response. {{ profile: general }}If Python 3 is unavailable,
load [select-context-without-python.md](select-context-without-python.md) only
for current-or-named recovery or manual unit selection; do not install a runtime. If Python is available but
the helper fails, report its diagnostic and do not invent partial context.{{ /profile }}{{ profile: codex }}If Python or the selector is unavailable or fails, report its diagnostic
and stop the selection. Do not invent partial context.{{ /profile }}

## Read state outside the selector

Use direct reads for Plan or Decision listings, proposal inventory, relevant
dependency Evidence, and graph inspection. These operations complement the
selector; they never replace current-or-named Work Item or dispatch-unit
{{ profile: general }}selection when Python is available.{{ /profile }}{{ profile: codex }}selection.{{ /profile }}

For a Plan or Decision listing, read only frontmatter and the H1 title unless
the request asks for record content. Read other Work Items only for the
requested state, dependencies, blockers, or authored content. Read a
prerequisite's status for readiness and its full block when its result or
Evidence matters. Inventory Decision frontmatter and surface proposals through
the next section without loading unrelated accepted Decisions.

Extract sections by their boundaries rather than dumping a large file or
truncating it at an arbitrary line count. For a graph or item inventory, ordered
H3 headings and `Status`, `Depends on`, and `Decisions` lines expose identity,
order, and references without loading Outcome, Steps, or Evidence history.
This is a graph view, not complete structural validation. Resolve ambiguous
boundaries or diagnostics from the original blocks; never treat missing output
from a truncated read as a missing record. These bounded reads require no
generated index or cached status file and never bypass a selector diagnostic.

Completed Work Items stay in their original format-version-1 Plan. Load their
details when relevant; do not delete, summarize in place, or move them into an
unsupported archive to shorten context. Use a successor Plan only when the old
goal is actually complete and the ordinary lifecycle permits the transition.

Do not infer status, completion, authority, or acceptance from filenames,
directory presence, implementation files, Git history, or old audit evidence.
Stop if the index is malformed, the declared version is unsupported, or a
referenced record cannot be resolved unambiguously.

## Surface proposals

Keep every proposed Decision ID discoverable through the inventory. Read and
report title, recommended choice and practical effect for proposals relevant to
the current work, or every proposal during a full audit. Ask for accept, reject, or
revise only when requested work depends on the choice or the user asks to handle
Decisions. A status/listing request does not require a decision answer. Preserve
unresolved proposals at handoff without repeating unchanged decision questions
on each status turn. New decision-relevant evidence may warrant asking again.
Continue unrelated work, but stop before work whose direction depends on a
proposal. Never infer acceptance from silence, continued work, or implementation
that follows the recommendation.

## Report the boundary

Name the canonical records that supplied the answer. Do not claim complete
project validation when only the index, selected Work Item, and proposal
summaries were inspected.
