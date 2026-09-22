## How to use

Name Scoville Plan when the work needs durable repository state:

```text
Use Scoville Plan to create a repository-owned implementation Plan for migrating the billing schema, updating consumers, and rolling out safely. Preserve any existing planning owner and do not implement the work.
```

```text
Use Scoville Plan to resume the active Plan. Reconcile the current Work Item with observed repository state, update evidence and the next action, then continue only the authorized work.
```

```text
Use Scoville Plan to audit the existing Plan and Decision records for lifecycle, dependency, blocker, and completion-evidence defects. Do not change files.
```

Explicit `$scoville-plan` invocation also works on hosts that support named
Skill invocation.

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
