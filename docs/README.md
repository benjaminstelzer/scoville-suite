# How Scoville Suite developed

Scoville grew from a frustrating pattern: an agent could follow plenty of rules
and still lose the goal between planning, implementation and review. Separate
Skills helped individual tasks, but duplicated guidance and elaborate
coordination added work of their own. The solution was to give shared behavior
one owner and keep each Skill focused on a useful responsibility.

Real use exposed defects that tidy instructions had hidden. Helpers mishandled
paths and Unicode, older Python versions behaved differently, and adviser calls
needed clearer timeout and permission defaults. Those failures made one lesson
concrete: a helper's output has to work in the next operation. Producing valid
JSON is a rather modest definition of success.

Workflow initially spent too much effort moving context through extra layers.
Native agent operations and smaller assignments simplified that path. Context
exhaustion and rejected messages then showed where explicit ownership and
retained progress still mattered. Removing machinery helped. Pretending the
host could never fail would not.

The same tension shaped the writing. A shorter handoff can accidentally turn a
preference into a requirement. A shorter project rule can lose its exception.
The useful target is the smallest explanation that preserves the decision and
the facts needed to act on it. Word count is easy to measure. That is not quite
the same thing.

General and Codex editions now share the common Skills, while Workflow, Ask and
Setup use the Codex-specific route. Focused checks support particular changes,
not a promise that every future agent run will behave predictably. The Plans
and Decisions retain the detailed history for work that needs it.
