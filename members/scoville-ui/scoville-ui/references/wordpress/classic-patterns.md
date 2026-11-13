# Classic Core patterns

These are observed WordPress 7.1 implementation patterns at
[`b998fef9238af183f9523b3df71618e6e57498b6`](https://github.com/WordPress/WordPress/tree/b998fef9238af183f9523b3df71618e6e57498b6).
Recheck them for the version the plugin actually supports. No row defines a
universal gap.

## Declarations and context

Paths below are relative to that Core checkout. Keep authored units.
Resolved values assume the font rule named in the row wins. Other selectors,
inheritance, display behavior and media queries can change the result.

| Context and source | Authored declarations | Interpretation |
| --- | --- | --- |
| `wp-admin/css/common.css:314` p | font-size 13px, line-height 1.5, margin 1em 0 | 13px block margins only at that font. Preserve 1em. This is not a universal paragraph-to-button gap. |
| `common.css:346` h2/h3 | font-size 1.3em, margin 1em 0 | Font context and more-specific heading rules matter. |
| `common.css:604` wrap | margin 10px 20px 0 2px | Core page gutter, not modern Page padding. |
| `common.css:608` wrap h1 and compatibility headings | font-size 23px, margin 0, padding 9px 0 4px, line-height 1.3 | `.wp-header-end` at 624 has visibility hidden and margin -2px 0 0. Hidden visibility does not remove its layout participation. |
| `common.css:1476` notice/updated/error | margin 5px 15px 2px, padding 8px 12px, left border 4px | Inspect parent and final classes before selecting the rule. |
| `common.css:1491` Notice paragraphs | margin 0.5em 0, padding 0, font-size 13px, line-height 1.54 | Resolved block margins are 6.5px at that font. Includes a more-specific form-table Notice rule. |
| `common.css:1650` wrap Notice | margin 5px 0 15px | More specific than the generic mobile `.notice` margin. |
| `wp-admin/css/forms.css:902` form-table | margin-top 0.5em, border-collapse collapse, font-size 14px | Keep table flow. Cell margins do not behave as ordinary block gaps. |
| `forms.css:916` td | margin-bottom 9px, padding 15px 10px, line-height 1.3, vertical-align middle | Evaluate display and responsive overrides. |
| `forms.css:931` th | padding 20px 10px 20px 0, width 200px, line-height 1.3, vertical-align top | Different from td by design. |
| `forms.css:947` ordinary td p | margin-top 4px, margin-bottom 0, font-size 14px from 909 | Actual context-specific pixels. Do not apply this to all help and status text. More-specific Notice paragraphs differ. |
| `wp-includes/css/buttons.css:43` base button | font-size 13px, unitless line-height 2.92307692, min-height 40px, margin 0, padding 0 16px | Minimum height is not fixed rendered height. |
| `buttons.css:73` compact / 81 small / 98 hero | min-height 32px / 24px / 48px, distinct padding and typography | Preserve deliberate variants. Equalize only where the owner requires the same variant. |

## Narrow widths and final DOM

At `max-width: 782px`, `common.css:4088` sets generic Notice margin
`20px 0 10px`, padding `5px 10px`, font-size `14px` and line-height `175%`.
The earlier `.wrap .notice` margin can still win by specificity. Mobile
`.wrap div.updated` and `.wrap div.error` have their own matching selector
paths. Inspect the actual Notice kind rather than treating all as equivalent.

`forms.css:1582` and `1651` give matching text inputs and selects a 40px minimum.
At 1675, matching form-table headers and cells become blocks. This is Core's
table transformation, not a universal one-column rule for plugin dashboards.
`buttons.css:383` changes matching mobile button variants and adds a 4px bottom
margin. Later context-specific exceptions still apply.

`wp-admin/js/common.js:1081` moves Notice divs after `.wp-header-end`, or the
first wrap heading when no marker exists. `.inline` prevents relocation.
`.below-h2` is historical compatibility, not a new recommended API.

## Prove the actual relationship

When implementing, write the change from the declarations above and report
the resulting distance as unverified. A review, audit or requested check
proves it in the render:

1. Inspect loaded stylesheet URLs, order and relevant minified rules selected by
   `SCRIPT_DEBUG` in `wp-includes/script-loader.php:1620`. Registration or a file
   on disk is not loading proof.
2. Inspect final DOM after scripts, then the computed cascade.
3. Measure geometry at relevant wide and narrow conditions.

There, for a named paragraph and control pair, record the authored
`margin: 1em 0`, its resolved value, the flow and line boxes in between and
the measured edges. Margin collapsing, table layout, padding and inline line
boxes can change the visible separation. Do not publish a gap assumed from
this table.

Core's native CSS and its token definitions are independent, although Core
supplies both. A Classic page stays Classic on 7.1. For a relationship Core
really leaves unspaced, follow [spacing.md](spacing.md); do not apply the
fallback scale here.
