# Geometry and sight validation

## Measure relationships, not declarations

For each selected relationship:

1. Before measurement, identify reference elements and edges, expected relationship,
   source and justified tolerance. Use an unchanged owner contract, suitable
   reference or, for greenfield work, requirements and direction chosen from the
   brief before implementation. Candidate CSS alone is not an independent target.
2. Settle required fonts, content and transitions. Inspect loaded styles and final
   DOM where relevant. Compare peers with the same role, variant, state, typography
   and layout conditions; explain deliberate differences.
3. Measure against that target. Report expected relationship and source, measured
   result and conclusion; evaluate optical alignment separately under Sight.

Never choose tolerance after seeing the result. An unresolved target stays
unresolved; there is no universal pixel tolerance. Equally wrong peer overrides
do not establish a correct target.

For each selected relation, report the expected value or relationship and source,
measured result and conclusion. Identify its target and applicable tolerance;
revision, state and viewport may be recorded once for a measurement group.
Use an existing report or task result, without a prescribed table or new file.

Keep the authored unit or expression, computed value and measured distance separate.
Preserve `em`, `rem`, `px`, percentages, unitless line-height, token references,
calculations and logical properties. Equal current pixels do not authorize
substitution. Record the relevant element or root font or container basis.

For vertically ordered non-overlapping boxes, `B.top - A.bottom` measures their
border-box separation. It does not measure glyph whitespace or a baseline.
Account for margins and collapsing, padding, borders, line boxes, wrapping,
intervening elements and fractional rounding. Do not sum declarations and call
the result observed geometry. A minimum height is not a fixed height.

## Inspect with a comparison and a hypothesis

View the scoped region in context first, then details at a consistent scale.
Keep an unaltered context image or crop when guides help comparison. For each
applicable concern, record a located deviation or scoped pass. Explain relevant
exclusions without producing boilerplate for unrelated lenses.

| Look for | Compare |
| --- | --- |
| Grouping and rhythm | Equivalent relationships within and across sections |
| Content edges and text alignment | Intended shared edge, top, baseline or center, not an assumed universal alignment |
| Apparent whitespace | Line boxes and glyph position alongside measured box gaps |
| Components, including status text, controls and icons | Intended internal text and icon placement as well as outer alignment; check unintended parent stretching and wrapped neighbors |
| Content and state changes | Wrap, clipping, overlap, hidden-content holes and reading order |

**Worked diagnosis:** Two same-variant controls have equal outer heights, but
the text in B sits visibly lower than in reference A. Mark their shared top
edge or use a side-by-side crop at the same scale. State that observation first.
Then inspect font and line-height, internal padding and alignment props. If an icon
is displaced, inspect its viewBox or font metrics too. Confirm the cause before
correcting its owner. Do not invent a baseline measurement from outer rectangles.
If the optical question cannot be resolved, report it unverified.

**Valid difference:** A compact control and a standard control have different
native heights and padding. Verify their intended variants before treating
their difference as a defect. Do not override native internals for symmetry.

Recheck relevant widths, expanded text and affected states after the correction
batch is complete.
Zoom alone does not test whether `em`, `rem` and fixed pixels behave equivalently.
Where units are at risk, vary element or root font conditions independently.
