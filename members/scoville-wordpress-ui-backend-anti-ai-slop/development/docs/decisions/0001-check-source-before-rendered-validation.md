---
format_version: 1
id: ADR-0001
status: accepted
created: 2026-09-10
accepted: 2026-09-10
scope: wordpress/validation-order
---

# Check generating code and CSS first

## Decision

Benjamin explicitly requires correcting source-visible implementation and CSS errors before measurements and visual inspection. Apply this order to WordPress Backend UI independently of Scoville UI activation. Implementation remains unstarted.

## Problem

Benjamin reports wrong or inconsistent spacing, unnecessary custom CSS despite design-system use, unequal element heights and text misalignment. No failing plugin page was supplied or reproduced in this planning task. Existing spacing ownership and CSS exception rules do not require a sufficiently explicit source-first acceptance sequence.

## Drivers

Preserve native WordPress behavior and enforce evidence for deviations. Do not use a pleasing screenshot to justify inappropriate code.

## Considered alternatives

Visual-first correction can accumulate compensating CSS. Source-only checking misses runtime geometry. The selected source-first sequence retains source, measurement and visual proof.

## Consequences

Correct known source violations before rendered implementation validation. Audit mode remains read-only and reports failures. A runtime limitation is an evidence gap rather than a successful check.

## Confirmation

Observe source correction before the first visual inspection, measured relationships against actual native owners, and final visual proof. Include a native-default negative control so the Skill does not normalize valid differences.

## Revisit when

The user changes the order or a supported WordPress runtime changes the owning component API.
