---
format_version: 1
id: ADR-0002
status: accepted
created: 2026-09-10
accepted: 2026-09-10
scope: wordpress/spacing-ownership
---

# Separate Classic patterns from WPDS tokens

## Decision

Following Benjamin's request to verify and incorporate the other task's suggestions, document Classic Core patterns and WPDS tokens as separate reference sets. Keep any Skill-defined fallback composition separate from both. Existing native relationships take precedence; token availability does not establish native token use or authorize normalization. This records the plan change, not completed Skill implementation.

## Problem

The other task reports initially treating a native 13px paragraph margin as a defect against the Skill's 4px control-to-status rule, then withdrawing the proposed CSS correction. That incident was not independently reproduced here. Source inspection confirms that the Skill's semantic mapping could supply the wrong comparison target even though its introduction already restricts fallback use.

## Drivers

- Preserve Classic/PHP-Core ownership, including on WordPress 7.1 with available tokens.
- Bind each source fact to a selector, markup context, runtime and version; a CSS declaration is not a measured visible distance.
- Distinguish observed Core implementation, WPDS contract, accessibility requirements and Skill choices at the point of use.

## Considered alternatives

Keeping the existing mixed spacing table with another introductory warning leaves the numeric mapping available as an accidental Classic audit target. Removing all plugin composition guidance would leave genuine owner gaps unexplained. Separate references preserve both source fidelity and bounded fallback guidance.

## Consequences

Classic references record actual horizontal/vertical margins, padding, typography, display behavior, cascade, media conditions and source locations. Record resulting distances only for named rendered markup and conditions. WPDS references record token name, value, version, stylesheet/runtime availability and gap versus padding; they imply no Classic component mapping. Fallback rules require a demonstrated missing native relationship and cannot turn native values outside a 4/8px scale into defects.

The reusable Skill must not inherit EMPCO's project-specific spacing minimum. Existing project exceptions and precedence require inspection in their own project; this task does not change EMPCO files.

## Confirmation

Source review on 2026-09-10 used the read-only local installation at `C:/xampp_lite_8_5/www/empco_master/wordpress`. Its `wp-includes/version.php:19` reports 7.1. Direct raw-file SHA-256 comparisons against WordPress/WordPress commit `b998fef9238af183f9523b3df71618e6e57498b6` matched all ten inspected implementation files: common/forms/buttons CSS and their minified versions, common JS and its minified version, design-tokens CSS and script-loader.php. The version files both report 7.1 and database version 61833; the local file also declares the de_DE package. This is bounded source provenance, not a whole-installation integrity check.

Source anchors below use one-based lines in that local checkout and the matching pinned files:

| Context | Verified declaration or mechanism | Required interpretation |
| --- | --- | --- |
| `common.css:314` ordinary `p` | 13px font; line-height 1.5; margin 1em 0 | Resolves to 13px block margins where this rule wins. It does not establish every paragraph-to-button distance. |
| `common.css:346` h2/h3 | font-size 1.3em; margin 1em 0 | Relative to the actual inherited font context; inspect more-specific heading rules. |
| `common.css:604` shell and title | wrap margin 10px 20px 0 2px; wrap h1 font 23px, margin 0, padding 9px 0 4px, line-height 1.3 | Native shell, not modern Page padding. `.wp-header-end` at 624 retains layout behavior despite hidden visibility. |
| `common.css:1476` Notice | padding 8px 12px; paragraph margin 0.5em 0 at 13px and line-height 1.54 | Paragraph block margins are 6.5px where this rule wins; do not replace them with the fallback scale. |
| `common.css:1650` and `4088` Notice cascade | `.wrap .notice` margin 5px 0 15px; mobile generic `.notice` margin 20px 0 10px and padding 5px 10px | Below 782px the more-specific wrap selector still wins the margin for ordinary `.notice`; updated/error selectors can follow different cascade paths. Verify final classes and DOM. |
| `forms.css:902` and `947` form-table | table margin-top 0.5em; td padding 15px 10px; th padding 20px 10px 20px 0; td p font 14px, top margin 4px, bottom 0 | Genuine context-specific 4px rule; Notice paragraphs have a more-specific exception. Table-cell margins are not ordinary block-flow gaps. |
| `forms.css:1582`, `1651`, `1675` | mobile text controls/selects have min-height 40px; form-table th/td become blocks | A minimum is not fixed rendered height; table reflow is not a universal one-column rule for all plugin UI. |
| `buttons.css:43`, `73`, `81`, `98`, `383` | base min-height 40px; compact 32px; small 24px; hero 48px; mobile selector changes several variants and adds bottom margin 4px | Compare identical variants and conditions; preserve native differences and inspect later context-specific overrides. |
| `design-tokens.css:235` through `261` | gap xl 24px vs padding xl 20px; separate token families | Shared suffixes do not make gap and padding interchangeable or prove Classic usage. |
| `common.js:1081` and `script-loader.php:1620` | Notices except inline/below-h2 move after the header marker or first heading; stylesheet suffix depends on SCRIPT_DEBUG | Source DOM can differ from final DOM. File presence or registration does not prove the page loaded that file. |

Pinned source entry: [WordPress/WordPress at the inspected commit](https://github.com/WordPress/WordPress/tree/b998fef9238af183f9523b3df71618e6e57498b6).

Also verified in the current Skill text: 390/600px are selected test widths, not universal Core rules; Core itself uses 600px in specific contexts, so do not claim it never does. The general one-column fallback below 782px is a Skill choice. The chosen Flex prop combination and example gap 4/2 are composition choices, not universal component defaults. The modern Page 16/24px values must remain bound to its actual package/component and be rechecked before reuse; its source was not inspected in this task.

[W3C Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) and [Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) confirm separate accessibility requirements with their applicability and exceptions; 320 CSS px/400% and 24px targets are not WordPress layout tokens or mandatory control dimensions in every case.

Remaining implementation acceptance: verify actually loaded assets, final DOM, computed cascade and geometry in matching Core markup at desktop/narrow conditions; run the native 13px preservation and context-specific 4px regression cases. No rendered EMPCO page or browser geometry was inspected during this source review. The earlier Astra conditional review predates this expansion and does not approve it; its follow-up remains paused by the user.

## Revisit when

A supported Core/package version changes these rules, source and deployed assets differ, or a reproducible native-owner gap requires an explicitly bounded composition rule.
