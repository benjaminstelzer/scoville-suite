## How to use

```text
Use Scoville Plan to create an implementation plan for migrating the billing schema, including dependencies and acceptance criteria.
```

```text
Create a detailed repository-owned implementation plan for the billing migration so workers can execute each point without this conversation.
```

Configure writing depth in this Skill's `assets/prompting.toml`. `profile` accepts
`auto`, `low`, `medium` or `high`. Explicit instructions take precedence within
their stated scope. Auto uses the target model, or the existing task class when
no model is known. Unknown models and missing selection inputs use medium.
Edit exact model assignments locally; Workflow has independent settings.
The resolver needs Python 3.11+. {{ profile: general }}Only missing Python enables the manual route.{{ /profile }}{{ profile: codex }}Python and the bundled helper are required; errors block the affected operation.{{ /profile }}

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
portable EXE and installers; macOS offers DMGs and zipped apps; Linux offers a
portable binary, AppImage, DEB, and RPM packages.

The saved project list is one `scoville-plan-viewer.xml` file beside a portable
application. Installed copies in read-only system folders use the platform user
configuration directory for the same XML file. Removing a project from the
Viewer never changes its repository.
