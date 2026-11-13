# Consistency audit coverage

A request to check page X for consistency selects Audit with a consistency
focus on the named page or region. Redesign, edits, other screens and a full
accessibility audit are separate requests.

1. From the source, build the inventory: the scope's regions, component
   families, distinct variants and known exceptions. Where present, include
   text roles, actions, controls, icons, containers, toolbars, data, footers
   and pagination. Give each entry a stable locator or label. Group entries
   that are the same kind of element and should follow the same component,
   variant or rule, however they are built.
2. After the source findings, compare the inventory with the final rendered
   DOM. Include content below the first viewport, nested scroll areas and
   relevant same-page tabs, disclosures, menus and overlays, and add what
   they reveal. Interact read-only: never save, submit, delete or cause an
   external effect for coverage. Name states you cannot reach as unverified.
3. For every entry, name what decides it (component, token, platform default,
   product requirement or local rule) and the checks Validation's claim table
   requires. Give each check `pass`, `defect`, `unverified` or a justified
   `not-applicable`. Compare within and between groups, such as buttons with
   the fields beside them.
4. Before concluding, confirm every entry has what decides it and its
   results; one without is a coverage gap. Report coverage and named gaps
   separately from prioritized findings. A required entry left unverified
   prevents a complete consistency pass.

Repeated or virtualized data may use a justified representative sample. State
the population and variants not inspected: `5 of 240 rows inspected, 235 not;
variant "archived" not seen`. Distinct in-scope variants and known exceptions
each stay in the inventory. Do not enumerate every virtual row merely to
simulate completeness.

When Skills compose, reuse one compatible inventory with its measurements,
images and results. Keep the platform Skill's or reference's comparisons and
valid exceptions. A DOM count, screenshot or claimed percentage alone proves
neither coverage nor correctness.
