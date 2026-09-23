# Web and responsive design

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-WEB-RESPONSIVE`, `SRC-TYPE-DETAIL`, `SRC-TYPE-EMPIRICAL`, `SRC-FONT-TECH`, `SRC-FONT-LICENCE-PROOF`, `SRC-IMAGE-METADATA-ACCESS`, `SRC-DATA-ACCESS-LOCALE`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when web content or workflow must intentionally transform across available
space, content pressure, zoom, text expansion, language, orientation or input;
or when that transformation must be critiqued or repaired. Do not load for
fixed print/slides/social graphics, native-app flow without web adaptation,
framework breakpoint/query syntax, component semantics, browser testing,
performance or runtime proof alone, or isolated type/colour/image/access work.

## Responsive design record

Before widths or implementation, record only open relevant fields; otherwise use the Core minimal record:

`source condition | first pressure signature | preserved invariants | candidate
operators | selected transformation | allowed variation | disconfirming
condition | Design proof target | UI proof owner`.

The source condition includes actual container/window, short/long/dynamic/error
content, state, language and script direction, zoom/text scale, orientation,
input/capability, safe area, environment and incumbent system. The first
pressure signature is the earliest observable loss: broken measure or line
shape, weak hierarchy, ambiguous grouping/order, trapped space, collision,
crop damage, lost state/action/orientation, or task blockage.

Preserve required content, task, state, recovery, essential reading order, type
roles, semantic spatial relations, concept character and protected image
subject unless a deliberate revision is authorised. Candidate operators include
preserve, reflow, reorder, regroup, split, wrap, disclose, collapse, replace,
change density, change navigation, bounded scroll for genuinely
two-dimensional work, alternate representation, or alternate image source/crop.
Breakpoints follow the accepted transformation; they do not define it.

## Generate and decide from pressure

Inspect only applicable lanes:

- **Content/language:** real short, long, translated, unbreakable, missing and
  state copy. Preserve meaning and task; change wrapping, measure, grouping or
  disclosure only for a named consequence.
- **Type/reading:** roles, measure, line breaks, leading, paragraph rhythm and
  annotations. Preserve role and continuity; do not apply a generic fluid scale.
- **Space/density:** within-group, between-group, section, edge and sequence
  intervals. Preserve grouping and deliberate tension; do not shrink every gap
  or add uniform whitespace.
- **Hierarchy/order:** distinguish importance, narrative, task, visual, source,
  focus and announcement orders. A visual reorder may not silently reverse
  meaning or access.
- **Image/crop:** protect subject, gesture, label and context. Define a crop
  envelope or alternate source; resolution switching and `cover` are not art
  direction.
- **Navigation/action/state:** keep task, current location, primary action,
  status and recovery available; change pattern only after evaluating frequency,
  disclosure cost and incumbent support.
- **Dense/two-dimensional work:** preserve comparison, scale, topology and
  manipulation. Bounded horizontal interaction or an alternate view can be
  preferable to destructive stacking or hiding.
- **Capability/environment:** account for hover absence, keyboard, touch,
  orientation, safe area, reduced motion/data, slow delivery, zoom and text
  scaling by specifying intended consequences, not framework mechanics.

Choose the transformation that resolves the first pressure while preserving the
most important relationships. State what may vary - density, line breaks, crop,
disclosure, navigation, composition - and what would falsify the choice. Responsive
design may produce substantially different compositions; it need not resemble a
scaled desktop canvas.

## Match pressure to a transformation

Reduce the available width with real content until the first important relation
fails. Compare an operation that addresses that failure, then inspect widths
on both sides of the change and between the intended endpoints.

| First pressure | Operation to compare | Protected relation / countercase |
| --- | --- | --- |
| A label loses its value or action | Rewrap the field or regroup its row | Preserve label/value/action association; peer comparison may favour a bounded table |
| Reading lines or a control cannot fit | Change measure, track allocation or flow | Preserve readable type and full required copy; shrinking everything is not the default |
| A crop loses the subject's working relation | Change focal envelope, aspect or source | Keep meaning and truthful context; `cover` alone cannot decide the crop |
| Repeated navigation displaces the task | Compare supported disclosure or a different arrangement | Preserve location, access and recovery; do not hide essential content to make space |
| Two-dimensional comparison collapses when stacked | Compare bounded scrolling or a task-equivalent view | Preserve axes, row/column relations and reachable content |

Record the observed content pressure as the reason for the breakpoint, not a
device label. A settled single-column layout may need no transformation. This
map supplies design intent; the implementation owner supplies tested mechanics.

## Critique failure signatures and causes

- **Long narrow stack:** automatic stacking replaced hierarchy and task logic.
  Rebuild groups and compare regroup, reorder, disclosure or alternate patterns.
- **Broken headline/paragraph rhythm:** fluid size ignored role, real copy,
  measure or line breaks. Repair the typographic relationship and recompose its
  neighbours.
- **Uniformly compressed spacing:** a ramp replaced semantic intervals. Restore
  the specific group/section/edge relation that failed.
- **Decorative emptiness beside cramped content:** negative space has no
  separation, pacing, framing, direction or emphasis job. Reallocate it; do not
  fill or enlarge it by default.
- **Responsive image loses meaning:** technical source selection replaced crop
  intent. Protect the subject or choose an alternate source/composition.
- **Overflow in toolbar, labels, code or data:** parent sizing, wrapping or
  inherent two-dimensionality is unresolved. Repair the parent or define bounded
  access with preserved orientation.
- **Compact navigation loses state/action:** a familiar mobile pattern ignored
  recurrence, location and disclosure cost. Compare persistent, local, disclosed,
  search or task-specific alternatives.
- **Visual and programmatic order diverge:** placement changed without a stable
  semantic order. Restore source/task order and allow only meaning-preserving
  visual variation.
- **Endpoints pass, middle/localisation fails:** named devices replaced
  continuous pressure inspection. Find the first failing condition using real
  content and state.
- **Template page stack:** hero, logo bar, three features, testimonial, pricing
  and CTA repeat at identical heights because a section library preceded the
  audience's questions. Rebuild from argument order; let length follow content
  consequence. Keep any conventional section that answers a real question, and
  never invent a testimonial or counter-template to fill the page.

## Smallest repair and regression

Repair `pressure cause → affected relationship → smallest transformation` rather
than prescribing a new device layout. Preserve exact content, incumbent-system
constraints, working style character, task/state/recovery and unaffected domain
decisions. Compare before/after with identical content and state; regress
meaningful container ranges, intermediate conditions, long/short/localised and
error content, zoom/text expansion, relevant orientation/input, image crops and
state/action persistence. Record every unrun lane as `Not verified`.

## Exceptions

Horizontal interaction is legitimate for tables, maps, timelines, code,
editors or other two-dimensional relationships when bounded, oriented and
operable. A dense mode may serve expert recurrence; progressive disclosure may
serve unfamiliar or high-consequence work. Fixed-position or persistent actions,
alternate content, unusual crops and expressive responsive departures are
allowed when their function, access floor, system authority, disconfirming
condition and proof are explicit. Reflow requirements are scoped access floors,
not universal breakpoints, layouts or visual recipes.

## Proof and ownership

Design compares populated narrow, intermediate and wide renders at the same
content/state and judges hierarchy, reading continuity, grouping, rhythm,
negative-space function, crop meaning, task continuity and style preservation.
The implementation owner
implements queries, breakpoints, components, DOM/source order,
semantics, focus/input/announcements, browser behaviour and performance, then
supplies runtime evidence for relevant ranges, content fixtures and states. A
screenshot, overflow detector, DOM metric or named device does not alone prove
responsive behaviour, usability or access. An incumbent framework limitation is
recorded as a system gap; Design intent changes only through the canonical
decision record.

This leaf owns responsive priority and transformation intent. Base typography,
composition, imagery, colour and interaction intent remain with their craft
owners; implementation mechanics and runtime proof remain with UI/Code. Do not
claim responsive-complete, accessible, usable, performant, framework-compatible
or superior beyond the exact rendered and runtime conditions inspected.
