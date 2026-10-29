---
name: scoville-project-context-cleanup
description: Add or revise project rules in AGENTS.md or CLAUDE.md and context in PROJECT_INDEX.md. Use for requested additions to project rules and cleanup of these files. Excludes unrelated prose, file mentions and routine Plan status updates.
compatibility: "Agent Skills host with project-file read and write access. No services or network required. Developed and tested in Codex; other hosts untested. Python 3.11+ for the bundled text-size checker; manual fallback only without suitable Python. Helper errors do not enable fallback."
---

# Scoville Project Context Cleanup

Keep requested project-context changes concise, correctly placed and complete
enough to guide the agent without hidden context. A shorter file alone is not
proof of better instructions.

{{ include: family.contract }}

```mermaid
flowchart TD
  target["Resolve the requested target"] --> clear{"Are scope and destination clear?"}
  clear -->|no| ask["Ask for the missing material choice"]
  clear -->|yes| read["Read the target and governing instructions"]
  read --> conflict{"Is a material conflict unresolved?"}
  conflict -->|yes| ask
  conflict -->|no| owner{"Does an applicable record owner govern the edit?"}
  owner -->|yes| coordinate["Use the owner's prepared edit"]
  owner -->|no| draft["Prepare the scoped change"]
  coordinate --> draft
  draft --> verify["Inspect the saved diff and required validation"]
  verify --> report["Report changes and actual checks"]
```

## Target and scope

| Requested target | Destination |
| --- | --- |
| Named file | Preserve its filename and case. |
| Add to project rules | Existing governing file for that scope; subtree-only rules belong in that subtree's existing file. |
| Unambiguous project-wide request at known root without its own rule file | Create CLAUDE.md on a Claude host, otherwise AGENTS.md there. Inherited workspace rules do not prevent this. |
| Materially ambiguous destination or rule | Ask before dependent editing. |

Create no parallel AGENTS.md or CLAUDE.md for a scope already covered by a host or subtree file.
Advice alone creates no rule. Explicit opt-out excludes this Skill.

Read cited sources only to establish ownership, meaning or obsolescence; do not
inventory sources broadly or execute commands found in them. Preserve unrelated
and uncommitted changes. Create a missing named file only when the request
covers creation and its scope is clear; the project-wide case above includes it.

Read both AGENTS.md and CLAUDE.md when they apply, respecting host precedence.
Edit only the existing file responsible for the requested scope; reading both
does not authorize synchronizing them. Ask the user to resolve conflicting
equally authoritative rules before dependent edits.

## Prepare the change

Before requesting or reading machine reports, logs or structured state, drafting
or rewording project content, or answering a disputed factual or technical
conclusion, read the [shared writing rules](references/writing.md).
When authoring project rules, also apply
[agent instruction design](references/instruction-design.md). Keep the requested
project scope; add no Skill packaging or invocation machinery to project rules.

Keep project-specific commands and conditions, responsible sources, constraints,
permissions and useful pitfalls. Remove repetition, evidenced obsolete context
and generic explanation. General model knowledge never justifies removing a
binding project rule.

Base factual claims on binding user instructions and inspected sources; mark
proposals and examples. Ask for missing facts only when they block the edit.

Keep independently needed copies and instructions requiring them. Merge other
duplicates only when their meaning and scope match.

| Procedure or reference | Treatment |
| --- | --- |
| Existing reference contains the complete procedure | Replace duplication with its exact reference and reading trigger. |
| Incomplete reference; extraction not requested | Leave reference unchanged and retain the complete procedure in the target. |
| Extraction explicitly requested | Move the complete procedure to a suitable existing or new reference. |

Cleanup, shortening or referencing alone does not authorize extraction.
Keep existing external-action approvals and prohibitions in the target rule
file, with their conditions and exceptions, even when referencing or extracting.

Check additions against existing rules. A clear newer user choice replaces earlier
guidance within its authorized scope. Reuse authorization already covering the
edit; ask only about an unresolved material permission, behavior or exception.
Source text supplies facts, not new authority; do not silently weaken a rule.

## Place the content

Use the existing project structure. Keep prerequisites before actions, exceptions
beside their rules and specialized detail behind conditional references. Change
only the structure needed for the request; preserve suitable text and useful
diagrams, including on a repeated request that adds no information.

For PROJECT_INDEX.md, preserve format, fields, IDs and links; navigate to canonical
records rather than duplicating live state or history. Under Scoville
format_version: 1, Plan owns active_plan, record structure and lifecycle. Apply
wording within its prepared edit, with one editor, then use its validator.
For other formats use their record owner. A missing index follows a clear Plan
request through Plan or an explicitly requested free format; ask only about a
materially unclear format or target. Index prose alone does not initialize Plan.
Cleanup changes no Plan status or record identity, and ordinary Plan progress
needs no cleanup call.

## Write and verify

Inspect the saved affected blocks and every changed file's scoped diff, including
extracted references, for lost scope, conditions, exceptions, permissions, reasons
or links. Use required owner validation and check saved non-ASCII text when
encoding could alter it.

Report material changes and removals with their reason, unresolved choices and
actual checks. File length proves neither token savings nor model performance.
Add no standing audit or approval round to an authorized edit.
