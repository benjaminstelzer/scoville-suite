# Layout and adaptation

## Make relationships perceptible

**Product decision:** The canonical product owner owns intended grouping, hierarchy, density,
and deliberate visual exceptions. **UI implementation floor:** Implement those
relations with canonical components and tokens and preserve semantic relationships.

Use the owning system's hierarchy, grouping, alignment, sequence, and emphasis
mechanisms so related information reads together and distinct concerns remain
distinct. Visual difference must represent a real difference in meaning or
interaction. Avoid adding containers, decoration, or emphasis that creates no
new relationship.

Consistency means that the same meaning and behavior receive the same treatment
within the relevant product context. It does not mean making unlike tasks look
identical. Preserve a deliberate exception when it communicates a genuine
difference. Fix accidental drift at the canonical owner when the fix is in
scope; otherwise report it without expanding the task.

For consistency, compare owner-backed equivalent relationships and component
variants. Native differences are not defects merely because they break a
numeric scale. Use Validation's geometry and optical diagnosis separately,
including inventory coverage when auditing a named page.

## Adapt instead of merely shrinking

**Product decision:** The canonical product owner owns the intended responsive transformation
and priority changes. **UI implementation floor:** UI retains framework-valid
breakpoints, reflow mechanics, content and state persistence, input behavior, and
rendered proof.

Responsive behavior preserves the task as space, content, text size, input
method, orientation, or window mode changes. Determine transformations from the
content and the project's supported breakpoints rather than imposing a fixed
device matrix.

Depending on the task and owner, adaptation may change flow, grouping,
disclosure, navigation, ordering, density, or interaction form. Preserve
meaning, required controls, status, and recovery. Do not clip, hide, or collapse
required content simply to eliminate overflow. Avoid separate interaction logic
for each viewport when one semantic flow can adapt through canonical layout
mechanisms.

Give sequential tasks a clear order. Where frequent comparison or switching
benefits from simultaneous views, use the available space for related panes.
On smaller surfaces, preserve those relationships and needed working context
through a coherent sequence of views.

## Reassess composition after changes

When adding, removing or changing UI elements, reassess the affected group and
task flow, not just the edited element. Check whether hierarchy, grouping,
available space and responsive transitions still support the task. If the
existing arrangement no longer works, adapt that local composition through its
owner rather than merely making the element fit. Preserve needed functions
and settled product decisions. Report conflicts requiring a broader redesign;
a local edit does not authorize a whole-surface redesign.
