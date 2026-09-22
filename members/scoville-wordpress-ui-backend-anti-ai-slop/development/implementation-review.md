# Why native spacing needs an owner

The change followed reported spacing errors and unnecessary custom CSS in
WordPress admin work. Existing Core margins, component padding and plugin layout
rules cannot be treated as one interchangeable spacing scale. A new rule may
compensate for the screenshot while duplicating spacing already supplied by
WordPress.

The revised instructions require the agent to locate that owner before making
a correction, then measure and inspect the result. They also preserve valid
native differences. A consistency audit should not make every control equal
merely because the values differ.

The [decision](docs/decisions/0001-check-source-before-rendered-validation.md)
explains the choice. The reported failures were not reproduced during this
source review. Tests against a running WordPress interface remain deferred in
[the plan](docs/plans/0001-source-first-ui-validation.md).
