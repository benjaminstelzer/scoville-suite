---
format_version: 1
id: ADR-0003
status: accepted
created: 2026-09-10
accepted: 2026-09-10
scope: wordpress/source-units
---

# Preserve authored CSS units and expressions

## Decision

Benjamin explicitly requires preserving source units rather than replacing them with currently equivalent pixel values. Preserve Core's authored `margin: 1em 0`; 13px is only its resolved value at the checked 13px element font. Apply this clarification when interpreting ADR-0002 and its historical shorthand, alongside the current Plan's unit-preservation acceptance.

## Problem

ADR-0002's incident description and confirmation use the shorthand native 13px paragraph margin/preservation. They describe a resolved value, not a native authored pixel rule. Reading them as a fixed-pixel target would contradict the actual source and the user's explicit correction. The earlier record remains unchanged as historical evidence.

## Drivers

Relative units, unitless line-height, calculations and tokens encode behavior that a single measured pixel result cannot preserve.

## Considered alternatives

Replacing `1em` with `13px` or `1rem` can match one state but changes the dependency on element or root font size. Retain the owner expression and record resolved values separately instead.

## Consequences

Read ADR-0002's operative confirmation as preserve authored margin 1em 0, with 13px only its resolved value at the checked font; do not implement a fixed 13px preservation test. Its paused-review sentence records the state when written: the user has since requested the final Astra review. Current review status belongs to PLAN-0001 evidence and Next action.

## Confirmation

Inspect `common.css:314-318` for font-size 13px, unitless line-height 1.5 and margin 1em 0; `forms.css:947-949` separately owns actual margin-top 4px and margin-bottom 0. Regression cases preserve these declarations and vary element/root font conditions independently to reveal substitutions. No browser result is claimed by this Decision.

## Revisit when

The owning Core declaration changes or the user explicitly authorizes a behavior-changing unit conversion.
