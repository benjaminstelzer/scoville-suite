---
format_version: 1
id: ADR-0023
status: accepted
created: 2026-09-20
accepted: 2026-09-20
scope: workflow/config-ownership
---

# Keep routing configurable and protocol limits in operations

## Decision

Keep the consumed `schema_version`, coordinator title, and coordinator, executor, and reviewer model and reasoning assignments in `assets/workflow.toml`. Remove the nonfunctional `[limits]` table. Retire the prohibited 7,000 and 8,000-character handoff caps instead of relocating them; keep each still-operative result shape, length, finding, and repair boundary owned once by `references/operations.md` and copied explicitly into affected child prompts.

## Problem

The routing tables influence actual `create_thread` arguments, but `[limits]` is never consumed; its stale two-repair value contradicts the operative three-repair contract while tests remain green.

## Drivers

- Model and reasoning choices are genuinely user-editable and already mapped through the routing table.
- Protocol limits must reach every affected prompt and validation branch without two sources drifting, while retired limits must not reappear under another owner.
- The Skill has no runtime parser or process that automatically enforces arbitrary TOML limits.
- ADR-0020 already fixes the default at three repairs and requires user disposition before a fourth.

## Considered alternatives

- Change only `max_repairs_per_unit` from two to three: Removes the current mismatch but leaves every `[limits]` key decorative and able to drift again.
- Implement every protocol limit as TOML-owned configuration: Makes limits editable but requires validation, propagation, unsupported-value behavior, and tests for each key across every prompt and result branch.
- Remove `[limits]`, retire the handoff caps, and keep operations as the sole owner of remaining protocol boundaries: Recommended as the smallest truthful contract while preserving the already functional routing configuration and coordinator label.

## Consequences

- `schema_version` remains the configuration-format guard and `coordinator.title` remains the consumed native task label; editing route pairs continues to affect coordinator, executor, and reviewer creation subject to documented overrides.
- Protocol limits stop appearing user-configurable when they are not dynamically consumed.
- Contract tests parse all remaining TOML keys, assert no unknown tables, and verify deterministic modeled call construction for every route plus the operations-owned three-repair boundary. Native task creation remains qualified only by an observed workflow run.
- Former 7,000 and 8,000-character handoff caps remain retired because handoff context must be lossless and untruncated.
- A future configurable limit requires an explicit owner, validation rules, propagation path, and behavioral tests before it enters TOML.

## Confirmation

1. Prove coordinator plus ultra-low, low, medium, high, and ultra-high executor and reviewer creation uses deliberately changed supported TOML model and reasoning pairs unless a documented override applies.
2. Remove `[limits]`, search for every former key, confirm the handoff caps are absent, and confirm each still-operative value remains exactly once in operations plus its required child-prompt projection.
3. Assert one initial executor plus three repairs is allowed, a fourth is blocked for user disposition, and no stale two-repair value remains.

## Revisit when

Users need a protocol limit to be configurable and the Skill can validate and propagate that value through every affected native task branch.
