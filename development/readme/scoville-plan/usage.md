## How to use

```text
Use Scoville Plan to create an implementation plan for migrating the billing schema, including dependencies and acceptance criteria.
```

```text
Create a detailed repository-owned implementation plan for the billing migration so workers can execute each point without this conversation.
```

State the outcome, acceptance criteria and next action directly in the Plan.

### Set reasoning for a Step

Plan doesn't pick a model or reasoning level by itself, and it doesn't
dispatch work either. If you use Scoville Workflow for Codex from the Codex
suite, you can attach an explicit model or reasoning choice to a Step.
Without one, Workflow assesses the Step and uses the pair configured for its
route. Scoville Setup shows or saves those project settings.

You can request a reasoning level for one Step:

```text
1. [execute: reasoning=high] Check the migration and its rollback behavior.
```

To specify the model as well, put it first:

```text
1. [execute: model=gpt-6-astra; reasoning=high] Check the migration and its rollback behavior.
```

The regular levels are `low`, `medium`, `high` and `xhigh`, and those are the
four Setup offers and saves. The format also accepts `none`, `minimal`, `max`
and `ultra`, either as explicit annotations or as manual entries in
`.scoville/config.json`. Setup leaves such manual entries alone when you
change other settings. Whatever pair you choose, the model has to support it.
If it doesn't, the run stops and explains why instead of quietly picking
another level.

Route classes such as `ultra_low` describe how complex a task is. They're
separate from reasoning levels: an `ultra_low` task can use reasoning `low`.

### Companion app

The optional Scoville Plan Viewer shows the repository records as a compact,
read-only desktop overview. Point it at a project with `PROJECT_INDEX.md`,
`docs/plans` and `docs/decisions`, and you'll see the active Plan point,
finished and upcoming work, paused, blocked or cancelled steps, and current
and past Decisions. While the window is active, it rereads visible projects
every four seconds, so changes from an agent or an editor show up on their
own.

[Download the current release](https://github.com/benjaminstelzer/scoville-plan/releases/latest)
for Windows x64, macOS Apple Silicon or Intel, and Linux x64. For Windows
there's a portable EXE and installers, for macOS DMGs and zipped apps, and for
Linux a portable binary, an AppImage and DEB and RPM packages.

The portable version saves its project list in a `scoville-plan-viewer.xml`
next to the application. Installed copies in read-only system folders keep
the same XML file in the platform's user configuration directory. Removing a
project from the Viewer never touches its repository.

### Record compatibility

Plan uses `format_version: 1`. Evidence can be plain text such as
`Evidence: Tests A, B passed.` or a bracketed list. Files can use LF or
consistent CRLF line endings. Keep the Skill and the Viewer on matching
current versions, because older readers need bracketed Evidence lists and LF.
