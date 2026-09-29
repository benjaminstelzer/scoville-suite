# Compact Workflow continuations

The dispatch builder omits the complete Work Item on continuation and requires
supplemental facts. New assignments keep their existing context. Both executor
and reviewer continuations preserve task identity and role boundaries. The
coordinator selects applicable acceptance, permissions, constraints and evidence.

20 Workflow tests pass, including the real selector-to-CLI path, missing/empty
continuation inputs, retained facts, reviewer read-only behavior and unchanged
new-assignment context. All 32 suite tests pass on the isolated committed source.
The dirty development checkout initially failed one inventory test because an
unrelated Plan file was removed by concurrent Claude work. That work is excluded.

The five selected Workflow cases (02, 11, 12, 20, 21), title regression and two
continuation regressions pass semantic assessment with native GPT-6 Luna Medium
records. A real generated assignment was passed directly to the child-role
consumer. It retained completed checks, performed only the final inspection and
put predecessor takeover first, with no reference reads. These simulations do
not prove a live multichat run or a measured token saving.

Early generic Skill-harness attempts requested missing or forbidden references;
they remain recorded as failures. The final child test uses a role-consumer
harness rather than instructions to investigate a Skill. The first builder
variant also exposed avoidable Workflow reads, corrected by putting its existing
loading boundary first. No result was silently replaced or counted as a pass.

Six unchanged runtime packages retain the previous release's 40 selected cases
through byte comparison. New Workflow evidence completes the 45-case selection.
Raw prompts, expected behavior, package hashes, native identities and original
failures are retained in workspace temp/2026-09-28-workflow-compact-continuation.
The Skill Creator validator rejects the pre-existing compatibility field.
Publication validates supported YAML frontmatter and compatibility explicitly.
