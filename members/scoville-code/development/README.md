# Development

Code began with a familiar failure: the patch passed its tests but missed the
requested behavior. Adding more procedure could make the same mistake more
expensive. The useful change was to connect each edit and check to the actual
outcome, then stop when more checking would not change the decision.

The [source](../scoville-code/) and tests live in the suite. Install the built package.

The retained [research audit](audits/2026-10-02-overengineering.md) separates study findings from project conventions.
