# Select writing depth without Python

Read this file only when Python is absent. An old Python version, missing
helper, invalid configuration or helper error requires a concrete diagnostic.

Read this Skill's `assets/prompting.toml`. Resolve each selected Step or whole
item without Steps in this order:

1. Use an explicit low, medium or high request within its stated scope.
2. Otherwise use a fixed low, medium or high configuration.
3. For auto with a target model, use its exact models entry; unknown IDs use
   medium. Do not then use the task class.
4. Only without a target model, reuse the existing task class: ultra_low/low
   gives low, medium gives medium, high/ultra_high gives high. No class gives medium.

Read `references/prompting/common.md` and only the selected profile file.
Do not change risk, model routing, permissions or dispatch boundaries.
