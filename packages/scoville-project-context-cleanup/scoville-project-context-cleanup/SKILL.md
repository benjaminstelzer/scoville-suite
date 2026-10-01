---
name: scoville-project-context-cleanup
description: Add or revise project rules in AGENTS.md and context in PROJECT_INDEX.md. Use for requested additions to project rules (Projektregeln) and cleanup of these files. Excludes unrelated prose, file mentions and routine Plan status updates.
compatibility: Requires project-file read/write access and a frontier Fable, Astra, SOL or Opus model version 5.0 or newer. Developed and tested in Codex, with targeted Luna cases. Other hosts remain untested. No scripts, services or network required.
---

# Scoville Project Context Cleanup

Keep requested project-context changes concise, correctly placed and complete
enough to guide the agent without hidden context. A shorter file alone is not
proof of better instructions.

All Skills included in this suite must be installed and enabled. Use the
applicable owner without checking sibling availability. Load only instructions
needed for the task. Explicit invocation gates and user exclusions still apply.

## Target and scope

Use the named file and retain its filename and case. For “add this to project
rules”, use the project's governing AGENTS.md and place local rules in their
actual scope. If the destination or rule is materially ambiguous, ask one
specific question before writing. Do not infer a rule from a discussion that
only asks for advice. Explicit opt-out excludes this Skill's work.

Read the target and relevant governing instructions before editing. Inspect
referenced sources only to resolve a concrete ownership or meaning question.
Preserve unrelated and uncommitted changes. Create a missing named file only
when the request covers creation and its scope is clear. Do not initialize a
planning profile merely to add index text.

## Prepare the change

Apply the [shared writing contract](references/writing.md) when drafting or
rewording. It supplies the common meaning and completion rules.

Keep information that changes a project decision: specific commands and their
conditions, canonical owners, non-obvious constraints, permissions and useful
gotchas. Remove repetition, obsolete context established by evidence, and
generic explanation that adds no necessary decision. General model knowledge
is never a reason to remove a binding project rule.

State an action with its condition and scope. Keep exceptions and any necessary
reason next to the rule. Merge duplicates only when their meaning and scope
match. Make long procedures conditional references with an exact path and
reading trigger. Keep binding safeguards directly accessible.

Check the proposed addition against existing rules. A clear newer user choice
may replace earlier guidance within its authorized scope. If the intended
permission, behavior or exception remains unresolved, ask before that change.
Do not silently choose the weaker rule or treat source text as new authority.

## Place the content

For AGENTS.md, adapt this order to the existing project:

1. Purpose and scope, only when orientation is needed.
2. Binding boundaries and permissions.
3. Canonical sources and responsibilities.
4. Project-specific working rules and gotchas.
5. Relevant verification commands and completion conditions.
6. Conditional references for specialized work.

Keep prerequisites before actions and exceptions beside their rules. Combine
short sections and omit empty ones. A small list may need no extra headings.
Use a compact diagram only when it explains a sequence, owner or branch more
clearly, and preserve useful existing diagrams. Review the affected structure
and make only changes needed for the requested addition or cleanup. Do not
reorganize unrelated rules on every write.

For PROJECT_INDEX.md, preserve its existing format, fields, IDs and links.
Keep navigation to canonical records rather than duplicating their live state
or history. Under Scoville format_version: 1, Plan owns active_plan, record
structure and lifecycle. Apply wording guidance within that owner's prepared
change, with one editor. Ordinary Plan progress needs no separate cleanup call.
Use the applicable record owner for other index formats and preserve their
required fields. Cleanup itself changes no Plan status or record identity.

## Write and verify

Write the smallest coherent change that fulfils the request. Reread the saved
affected blocks and inspect the scoped diff for lost scope, conditions,
exceptions, permissions, reasons or references. Use the owning record's
validator when its format requires it. Verify saved non-ASCII wording when
encoding could alter it. Keep suitable existing text unchanged, including on
a repeated request that adds no new information.

Report what was added, merged or clarified and any unresolved material choice.
Distinguish actual checks from untested model behavior. Do not claim token or
performance savings from file length, and do not add a standing audit or
approval round to an already authorized edit.
