## How to use

```text
Use Scoville Plan to create an implementation plan for migrating the billing schema, including dependencies and acceptance criteria.
```

```text
Create a detailed repository-owned implementation plan for the billing migration so workers can execute each point without this conversation.
```

State the result you want and the constraints that matter. Plan records the
work, dependencies and acceptance criteria. It does not dispatch agents.

### Progress and decisions

New Plan points use ordered Steps with explicit progress:

```text
1. [status: done] Write the draft.
2. [status: in_progress] Review it against the brief.
3. [status: todo] Deliver the reviewed text.
```

The agent records observed progress, keeps open decisions visible and asks
before dependent work. Older unmarked Steps remain valid, with unknown progress.
Completed Steps still need the Plan point's acceptance checks.

To correct an existing record, ask: "Review and correct PLAN-0001." The agent
checks the evidence and actual result before changing progress. Inspection
without a correction request stays read-only.

### Companion app

[Plan Viewer downloads](https://github.com/benjaminstelzer/scoville-plan/releases/latest)
include a portable EXE and installers for Windows x64, DMGs and zipped apps for
macOS Apple Silicon and Intel, and a portable binary, AppImage, DEB and RPM for
Linux x64.

Open a project containing `PROJECT_INDEX.md`, `docs/plans` and `docs/decisions`.
The read-only Viewer shows current work, Step progress and decisions, refreshing
automatically while active. Removing a project from its list leaves the
repository untouched.

Portable copies keep the project list in `scoville-plan-viewer.xml` beside the
application. An installed copy in a read-only folder uses the platform's user
configuration directory. Keep the Skill and Viewer updated together: older
readers do not understand all current progress fields.

The [record guide](scoville-plan/references/edit.md) covers Step annotations,
field formats and helper commands. Plan uses `format_version: 1`.
