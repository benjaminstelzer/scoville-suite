# Consistency audit coverage

An ordinary request to check page X for consistency selects Audit with a
consistency focus. Keep the named page or region as scope. It is not permission
to redesign, edit, audit unrelated screens or perform a full accessibility audit.

1. Inventory the scoped regions, component families, distinct variants and known
   exceptions from source. Include text roles, actions, controls, icons,
   containers, toolbars, data, footers and pagination where present. Identify
   entries by stable locators or labels; group equivalents by their owner contract.
2. After source findings, reconcile with final rendered DOM. Include content
   below the first viewport, nested scroll areas and relevant same-page tabs,
   disclosures, menus and overlays. Add newly revealed elements to the inventory.
   Use read-only interactions. Do not save, submit, delete or cause external
   effects just to obtain coverage. Name inaccessible states as unverified.
3. Map every entry to its owner and applicable evidence under Validation's claim
   contract. Use `pass`, `defect`, `unverified` or justified `not-applicable` for
   each evidence kind that Validation's claim table requires. Compare between
   as well as within groups.
4. Reconcile all discovered entries before concluding. An unmapped entry is a
   coverage gap. Report coverage and named gaps separately from prioritized
   findings. Required unverified entries prevent a complete consistency pass.

Repeated or virtualized data may use justified representative samples, but state
the uninspected population and variants. A partial sample supports only a
coverage-limited result, never an unqualified complete-page or every-row pass.
Distinct in-scope variants and known exceptions remain inventory requirements.
Do not enumerate every virtual row merely to simulate completeness.

When Skills compose, reuse one compatible inventory and evidence set. Retain
the platform owner's comparisons and valid exceptions. A DOM count, screenshot
or claimed percentage alone proves neither coverage nor correctness.
