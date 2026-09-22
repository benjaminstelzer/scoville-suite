# WordPress UI validation

Use within the selected mode and focus. WordPress owns the comparison targets
through [spacing.md](spacing.md). Keep Classic source patterns, WPDS tokens and
Skill fallback composition separate. This reference also works without Scoville UI.

## Source first, then measurement, then sight

For implementation, complete these gates in order within the affected scope.
For an audit, inspect and report source defects first, then measure and inspect
without repairing them. Audit findings never authorize edits.

1. **Source:** Inspect generating markup/components, supported props/variants,
   styles and their owner. For implementation, correct known in-scope source
   defects before the first layout measurement or viewed render. For an audit,
   report those defects without correcting them, then continue with measurement
   and sight. Check duplicate spacing owners,
   arbitrary dimensions/offsets, token bypass, primitive rebuilds and obsolete
   overrides. Run relevant existing syntax, lint, component or build checks.
   A build does not audit design-system ownership. Source/API/stylesheet
   inspection is not a layout measurement.
2. **Measurement:** After source inspection and any implementation corrections,
   measure the affected
   relationships in the actual runtime against independently established
   references. Follow the measurement contract below.
3. **Sight:** View the rendered image and apply the visual routine below.
   Numeric equality does not establish optical alignment.

Before writing a custom styling exception, including inline styles and styling
props, name the unmet requirement, concrete owner API/component checked, why
it fails and the smallest scope. An official token alone does not justify the
exception. Prefer supported composition and variants. Inspect the final diff
for unnecessary custom styling and remove compensation made obsolete by the fix.

Complete related edits before source, measurement and sight checks. Batch any
corrections, then repeat affected checks once; do not check after each small
edit. Reuse compatible evidence when composing with Scoville UI. Associate final
measurements and viewed images with the same revision, content and state.
Available usable tools cannot be skipped for
convenience. Missing tools or source limit the conclusion, never create a pass.
Source-only and screenshot-only requests retain those limits without requiring
unrequested work. Preserve every known required gap in the result.

## Measure relationships, not declarations

Before the evaluated measurement, identify reference elements and edges, the
expected relationship and its source, and any justified tolerance. Derive these
from an unchanged owner contract or demonstrably suitable reference. Do not
choose tolerance after seeing the result or derive a target from candidate CSS.
An unresolved target stays unresolved. There is no universal pixel tolerance.

Record compact evidence for each affected relation:

`target/group | revision/state/viewport | source declaration + owner | expected relation + tolerance | resolved value | measured geometry | result`

Keep the authored unit/expression, computed value and measured distance separate.
Preserve `em`, `rem`, `px`, percentages, unitless line-height, token references,
calculations and logical properties. Equal current pixels do not authorize
substitution. Record the relevant element/root font or container basis.

Wait for required fonts, content and transitions to settle. Inspect loaded
styles and final DOM where they affect the claim. Compare peers with the same
relevant role, variant, state, typography and layout conditions. Explain
deliberate differences. Peers sharing a wrong override can be equally wrong.

For vertically ordered non-overlapping boxes, `B.top - A.bottom` measures their
border-box separation. It does not measure glyph whitespace or a baseline.
Account for margins and collapsing, padding, borders, line boxes, wrapping,
intervening elements and fractional rounding. Do not sum declarations and call
the result observed geometry. A minimum height is not a fixed height.

## Inspect with a comparison and a hypothesis

View the scoped region in context first, then details at a consistent scale.
Keep an unaltered context image/crop when guides help comparison. For each
applicable concern, record a located deviation or scoped pass. Explain relevant
exclusions without producing boilerplate for unrelated lenses.

| Look for | Compare |
| --- | --- |
| Grouping and rhythm | Equivalent relationships within and across sections |
| Content edges and text alignment | Intended shared edge, top, baseline or center, not an assumed universal alignment |
| Apparent whitespace | Line boxes and glyph position alongside measured box gaps |
| Controls and icons | Same-variant size, internal padding and icon/text placement |
| Content/state changes | Wrap, clipping, overlap, hidden-content holes and reading order |

**Worked diagnosis:** Two same-variant controls have equal outer heights, but
the text in B sits visibly lower than in reference A. Mark their shared top
edge or use a side-by-side crop at the same scale. State that observation first.
Then inspect font/line-height, internal padding and alignment props. If an icon
is displaced, inspect its viewBox or font metrics too. Confirm the cause before
correcting its owner. Do not invent a baseline measurement from outer rectangles.
If the optical question cannot be resolved, report it unverified.

**Valid difference:** A compact control and a standard control have different
native heights and padding. Verify their intended variants before treating
their difference as a defect. Do not override native internals for symmetry.

Recheck relevant widths, expanded text and affected states after correction.
Zoom alone does not test whether `em`, `rem` and fixed pixels behave equivalently.
Where units are at risk, vary element/root font conditions independently.

## Consistency audit coverage

An ordinary request to check page X for consistency selects Audit with a
consistency focus. Keep the named page or region as scope. It is not permission
to redesign, edit, audit unrelated screens or perform a full accessibility audit.

1. Start from source with an inventory of regions, component families, distinct
   variants and known exceptions. Include headings, body/label/help/status text,
   actions, controls, icons, containers, toolbars, data and footer/pagination
   where present. Use stable locators or identifiable labels and owner-backed
   equivalence groups.
2. After source findings, reconcile with final rendered DOM. Include content
   below the first viewport, nested scroll areas and relevant same-page tabs,
   disclosures, menus and overlays. Add newly revealed elements to the inventory.
   Use read-only interactions. Do not save, submit, delete or cause external
   effects just to obtain coverage. Name inaccessible states as unverified.
3. Map every entry to its owner/reference and applicable source, measurement
   and sight evidence. Use `pass`, `defect`, `unverified` or justified
   `not-applicable` for each stage. Compare between as well as within groups.
4. Reconcile all discovered entries before concluding. An unmapped entry is a
   coverage gap. Report coverage and named gaps separately from prioritized
   findings. Required unverified entries prevent a complete consistency pass.

Repeated/virtualized data may use justified representative samples, but state
the uninspected population and variants. A partial sample supports only a
coverage-limited result, never an unqualified complete-page or every-row pass.
Distinct in-scope variants and known exceptions remain inventory requirements.
Do not enumerate every virtual row merely to simulate completeness.

When Skills compose, reuse one compatible inventory and evidence set. Retain
the platform owner's comparisons and valid exceptions. A DOM count, screenshot
or claimed percentage alone proves neither coverage nor correctness.

## WordPress runtime evidence

Check actually loaded styles, their order and token availability where consumed.
Registration and a file on disk do not establish page loading. Read the final
DOM after Core Notice relocation. Compare `.notice`, `.updated` and `.error`
using their actual classes and parent, including narrow-width specificity.
For Classic audit targets use [classic-patterns.md](classic-patterns.md).

Select widths and content/state variations able to change the scoped result.
Follow [responsive.md](responsive.md) for Core boundaries and reflow, and retain
the language-scoped RTL rule. Source-only audits need no browser session.
Report source, measured, viewed and unverified evidence separately. Existing
interaction, focus and accessibility duties still apply where affected.
