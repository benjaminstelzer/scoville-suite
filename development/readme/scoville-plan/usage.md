## How to use

```text
Use Scoville Plan to create an implementation plan for migrating the billing schema, including dependencies and acceptance criteria.
```

```text
Create a detailed repository-owned implementation plan for the billing migration so workers can execute each point without this conversation.
```

State the outcome, acceptance criteria and next action directly in the Plan.

### Set reasoning for a Step

Plan does not choose a model or reasoning level on its own. When using Scoville
Workflow for Codex from the Codex suite, you can retain an explicit model or
reasoning choice on a Step. Plan itself does not dispatch work. Without an
explicit choice, Workflow assesses the Step and uses the configured pair for
its route. Scoville Setup displays or saves those project settings.

You can request a reasoning level for one Step:

```text
1. [execute: reasoning=high] Check the migration and its rollback behavior.
```

To specify the model as well, put it first:

```text
1. [execute: model=gpt-6-astra; reasoning=high] Check the migration and its rollback behavior.
```

The regular levels are `low`, `medium`, `high` and `xhigh`. Setup offers and
saves these four. The format also supports `none`, `minimal`, `max` and `ultra`
for explicit annotations or manual entries in `.scoville/config.json`. Setup
preserves those manual entries when you change other settings. Every selected
pair must be supported by the actual model. An unsupported pair stops with an
explanation, without silently choosing another level.

Route classes such as `ultra_low` describe task complexity. They are separate
from reasoning levels: an `ultra_low` task can use reasoning `low`.

### Companion app

The optional Scoville Plan Viewer turns the repository records into a compact,
read-only desktop overview. Point it at a project containing
`PROJECT_INDEX.md`, `docs/plans`, and `docs/decisions` to see the active Plan
point, completed and upcoming work, paused, blocked, or cancelled steps, and
the current and historical Decisions. It rereads visible projects every four
seconds while the window is active, so edits made by an agent or editor appear
without a second tracking system.

[Download the current release](https://github.com/benjaminstelzer/scoville-plan/releases/latest)
for Windows x64, macOS Apple Silicon or Intel, and Linux x64. Windows offers a
portable EXE and installers. macOS offers DMGs and zipped apps. Linux offers a
portable binary, AppImage, DEB, and RPM packages.

The saved project list is one `scoville-plan-viewer.xml` file beside a portable
application. Installed copies in read-only system folders use the platform user
configuration directory for the same XML file. Removing a project from the
Viewer never changes its repository.

### Record compatibility

Plan uses `format_version: 1`. Evidence accepts plain text such as
`Evidence: Tests A, B passed.` and bracketed lists. Files support LF or
consistent CRLF line endings. Use matching current Skill and Viewer versions;
older readers require bracketed Evidence lists and LF.
