# How Scoville Suite developed

Scoville Suite grew out of a practical problem: an agent could follow a long set of rules and still lose the goal between planning, implementation and review. The first versions gave each Skill its own answers. That worked in isolation, but shared behavior was repeated, the UI guidance split across two Skills, and the Codex Workflow added more machinery than the work itself needed.

The cleanup brought the common sources together. Scoville UI absorbed the WordPress guidance, with its backend rules applied only to plugin-owned `wp-admin` pages. Plan, Code, Handoff and UI remained shared between the general and Codex suites. Workflow and Ask stayed in the Codex suite, where their native task tools are available. This made the packages easier to build from one source, though it also meant checking what each edition actually contained rather than assuming the same files belonged everywhere.

A review then found a lot of issues. Some were ordinary defects: Plan writing failed on an older Python version, helpers stumbled over paths and Unicode, Ask for Claude lacked a default timeout, and its web tools were enabled by default. Other suggestions would have added more process without solving an observed problem. We fixed the defects and simplified the instructions, including the evidence format and repeated handoff records. We did not adopt every proposed limit or rewrite the whole Workflow just because a review suggested it.

Real use was less forgiving than the review. In a real project, much of the coordinator's input went into helper, JSON and encoding layers, followed by a polling loop. The Skills were doing work around Codex's native tools instead of using them directly. We removed those layers where the host already had the right operation, stopped polling, and gave workers only the context their assignment needed. In one controlled comparison, token use fell to roughly half. That was one comparison under fixed conditions, not a general saving rate.

The simpler route exposed its own limits. A worker ran past the old context threshold and reached auto-compaction, so rollover starts earlier. An Ask adviser could not reliably send an active result message because the host rejected it. The chat-based version then collected advisers' normal replies in the calling chat and asked whether their sessions were still needed after a review. Silence did not close them.

The first consolidated suites shipped, and later releases carried the corrected helpers and Workflow behavior. Package contents and published assets were checked against the built sources. Tests and controlled runs supported the specific changes, but they did not make every future agent run predictable. The Claude Code edition is still planned separately: its main session cannot hand itself over like a Codex coordinator, so it needs a different Workflow route rather than a copy of the Codex one.

The current Codex build uses native agents for Ask advisers and Workflow roles.
Ask keeps adviser handles for follow-ups. Workflow has a visible runner and
manager agents that exchange work directly, after finishing their current
assignment and required checks. These agents need no separate sidebar chats
or archival. Real consultations and a multi-manager run informed the revision.
Later dispatch and status corrections passed focused tests and independent
review, while their targeted live verification remains open.

Project Context Cleanup also joins both editions. It handles requested edits
to project rules and index text, preserving their scope, meaning and record
ownership. Its targeted tests distinguish observed behavior from package
checks.

The detailed Plans and Decisions remain in their own directories. They record choices and work that mattered at the time. Some of their old evidence links lead to reports removed from the current tree. Those reports remain in Git history. This page gives the development story without making a reader follow every audit, test log and release inventory.
