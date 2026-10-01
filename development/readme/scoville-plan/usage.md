## How to use

```text
Use Scoville Plan to create an implementation plan for migrating the billing schema, including dependencies and acceptance criteria.
```

```text
Create a detailed repository-owned implementation plan for the billing migration so workers can execute each point without this conversation.
```

State the outcome, acceptance criteria and ordered Steps directly in the Plan.

### Step progress and repair

Every new Plan point has at least one Step, even for one action. Record progress
with a first annotation:

```text
1. [status: done] Write the draft.
2. [status: in_progress] Review the draft against the brief.
3. [status: todo] Deliver the reviewed text.
```

The values are `todo`, `in_progress`, `done` and `cancelled`. Put
status before any `route` or `execute` annotation. Old and mixed lists remain
valid: an unmarked Step has unknown progress. Completing Steps doesn't replace
the Plan point's acceptance checks. Pause and blockers belong to the Plan point.
New entries omit Next action. Legacy Steps/status and Next action remain supported.
Keep additional conditions in the new one-line Instructions field, or write
`Instructions: []` when there are none. Evidence holds observed results.

The context helper can return a named Plan's recorded position:

```text
python "<skill-directory>/scripts/select_context.py" --root "<project-root>" --plan PLAN-0001 --position --format json
```

It returns the current Plan point and explicitly started Steps, grouping only
adjacent active numbers. With none active, it identifies the first written todo
only when no earlier unknown Step prevents selection. It also supplies Instructions,
paused-item context and linked open Decisions. The agent judges free instructions;
the helper doesn't infer a return or acceptance from them. Unknown progress carries
an instruction to inspect
Evidence and actual results or changes against the requirements. The helper
doesn't guess or change records.
When Python is unavailable, load the helper's separate manual route.

```text
Review and correct PLAN-0001.
```

This request loads the separate repair instructions. The agent checks Evidence,
original reports and, where needed, the actual result, including code, tests or
written text. It corrects proven Work Item and Step progress, preserves unknown
states and validates the records. An inspection without a correction request
remains read-only. An explicit migration can transfer proven legacy instructions
and progress without losing history. Ordinary Plan maintenance doesn't load this route.

### Companion app

The optional Scoville Plan Viewer shows the repository records as a compact,
read-only desktop overview. Point it at a project with `PROJECT_INDEX.md`,
`docs/plans` and `docs/decisions`, and you'll see the active Plan point,
finished and upcoming work, paused, blocked or cancelled Plan points, and current
and past Decisions. While the window is active, it rereads visible projects
every four seconds, so changes from an agent or an editor show up on their
own. Marked Steps have an icon and a status label. Unmarked Steps keep an empty
icon slot and the same text alignment. Their progress remains unknown. Written
active Steps also appear in the overview. Next step replaces Next action and shows
only recorded active or safely selected todo Steps. Without Step status this field
stays hidden. Instructions and linked open Decisions appear separately. Completed Steps
show a check, and cancelled Steps show an X and crossed-out text.

Downloads include a portable EXE and installers for Windows x64, DMGs and
zipped apps for macOS Apple Silicon or Intel, and a portable binary, an
AppImage and DEB and RPM packages for Linux x64.

The portable version saves its project list in a `scoville-plan-viewer.xml`
next to the application. Installed copies in read-only system folders keep
the same XML file in the platform's user configuration directory. Removing a
project from the Viewer never touches its repository.

### Record compatibility

Plan uses `format_version: 1`. Evidence can be plain text such as
`Evidence: Tests A, B passed.` or a bracketed list. Files can use LF or
consistent CRLF line endings. Keep the Skill and the Viewer on matching
updated versions: older readers may require bracketed Evidence lists, LF and
Next action, and don't understand the new Step status and Instructions fields.

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
