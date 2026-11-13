# Geometry and sight validation

## Measure relationships, not declarations

For each distance or alignment to check:

1. Before measuring, note the reference elements and their edges or centres,
   the expected relationship, its source and a justified tolerance: `Save
   bottom to card content bottom: 16px (card padding token), +/-0.5px
   rounding`. The source is independent of the change: an unchanged
   component, token, design-system or platform rule, a suitable reference,
   or for new UI the direction derived from the brief before implementation.
   The CSS under test and equally wrong peers supply no target.
2. In each selected condition, let required fonts, content and transitions
   settle; read the relevant loaded styles and final DOM. A substituted or
   blocked required font invalidates dependent measurements. Compare peers in
   equal role, variant, state, typography and layout; explain intended
   differences.
3. Read each measurement (rectangles, computed values) from the DOM or its
   platform equivalent and compare it with its target in code before
   display, as for any [machine data](machine-data.md). Report expected
   relationship and source, actual value, tolerance and result; revision,
   state and viewport may appear per group. Use an existing report or the
   task result; no prescribed table, no new file.

A value outside its tolerance is reported as a deviation; it is a defect
unless the difference is intended. Choose the tolerance before results; no
universal pixel tolerance applies. Without a target the relationship stays
unresolved.

Keep the authored unit or expression, the computed value and the measured
distance apart. Authored and reported values keep their `em`, `rem`, `px`,
percentage, unitless line-height, token reference, calculation or logical
property: equal current pixels do not turn `1rem` into `16px`. Record the
element or root font size or the container it is relative to.

For ordered non-overlapping boxes, `B.top - A.bottom` is the gap between
border boxes, not glyph whitespace or a baseline. Account for flow,
collapsing, padding and borders, line boxes, wrapping and rounding. Summed
declarations are not observed geometry; minimum height is not fixed height.

## Inspect with a comparison and a hypothesis

View the scoped region in context first, then details at a consistent scale.
Keep an unaltered context image or crop when guides help comparison. For each
row that applies, record a located deviation or a scoped pass. Explain a
relevant exclusion; write nothing for unrelated rows.

| Look for | Compare |
| --- | --- |
| Grouping and rhythm | Equivalent relationships within and across sections |
| Content edges and text alignment | Intended shared edge, top, baseline or center, not an assumed universal alignment |
| Apparent whitespace | Line boxes and glyph position alongside measured box gaps |
| Components, including status text, controls and icons | Intended internal text and icon placement as well as outer alignment; check unintended parent stretching and wrapped neighbors |
| Content and state changes | Wrap, clipping, overlap, hidden-content holes and reading order |

Equal outer boxes can hold displaced text or icons, such as two 24-high
controls whose labels sit 1px apart. View the difference, then inspect font
and line-height, padding, alignment and icon metrics. Where internal placement
is claimed, measure and view the inner content too; container overflow alone
proves no internal alignment.
Keep intended native variant differences. Report unresolved optical questions
as unverified.

When a change invalidates a check, repeat it under
[Validation](validation.md#select-and-refresh-evidence). Zoom alone does not
test whether `em`, `rem` and fixed pixels behave equivalently. Where units are
at risk, vary element or root font size independently.
