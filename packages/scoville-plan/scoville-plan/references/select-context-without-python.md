# Select dispatch context without Python

Use the `W-NNN` ID in the requested unit, not `current_item`. Require one
matching active Plan and one matching Work Item. If the item has Steps, require
`W-NNN/step-N` or `W-NNN/steps-N-M` with an existing Step or an ascending
adjacent range of at least two Steps. Without Steps, require `W-NNN` alone.

Return the same four semantic areas described in [read-only.md](read-only.md):
exact Plan frontmatter, Goal and Non-goals; the requested unit ID and selected
Work Item's heading, Status, Depends on, Blocked by, Decisions, Outcome and
Acceptance lines, plus only the selected Step lines; direct dependency IDs
with their Status lines; and every complete Decision referenced by the Work
Item. For an item without Steps, also include Next action. Exclude Evidence,
unselected Steps and Work Item-wide Next action from a Step unit. Resolve each
reference from canonical records. If a record, boundary or reference is missing
or ambiguous, stop without supplying a partial dispatch context.
