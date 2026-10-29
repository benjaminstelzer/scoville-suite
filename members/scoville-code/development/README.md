# Development

Code began with a familiar failure: the patch passed its tests but missed the
requested behavior. Adding more procedure could make the same mistake more
expensive. The useful change was to connect each edit and check to the actual
outcome, then stop when more checking would not change the decision.

The [source](../scoville-code/) and tests live in the suite. Install the built package.

The unchanged [evaluation catalog](tests/evaluation-cases.json) is historical
PLAN-0034 evidence. Its cases include superseded expectations, such as a fixed
two-correction threshold, and do not define current behavior.
