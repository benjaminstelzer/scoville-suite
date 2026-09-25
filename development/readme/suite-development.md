## Development and builds

Edit member sources under `members/`. Edit README fragments under
`development/readme/` and their ordered paths in `suite.json`. Member README
files are generated previews, not a second authoring source.

An isolated clone builds from the shared tools and templates bundled under
`development/shared/`. In the authoring workspace, the sibling `shared/`
directory owns those sources and supplies both suites. Installed Skills use
only the helpers inside their own package.

The shared Development block appears in this suite and its member previews.
Individual releases omit it. Maintain its source, test and note paths in each
member's `development` metadata in `suite.json`.

Regenerate previews with `python development/build_suite.py --write-readmes`.
Use `--check-readmes` to detect stale previews.

### Keep build caches out of synchronized source trees

When the checkout is inside Dropbox or another synchronized directory, keep
Python bytecode outside the checkout. Preserve an existing
`PYTHONPYCACHEPREFIX` that already points outside the synchronized tree.
Otherwise configure a user-level cache and open a new terminal or Codex session
afterward:

| Platform | User setting |
| --- | --- |
| Windows PowerShell | `[Environment]::SetEnvironmentVariable("PYTHONPYCACHEPREFIX", "$env:LOCALAPPDATA\pycache", "User")` |
| macOS zsh | Add `export PYTHONPYCACHEPREFIX="$HOME/Library/Caches/pycache"` to `~/.zprofile`. |
| Linux | Add `export PYTHONPYCACHEPREFIX="$HOME/.cache/pycache"` to `~/.profile`. |

Until a new session inherits the setting, invoke repository scripts with
`python -B`. Confirm the active location with
`python -c "import sys; print(sys.pycache_prefix)"`.

Before installing or building the Plan Viewer, create and exclude
`members/scoville-plan/development/viewer/node_modules` and
`members/scoville-plan/development/viewer/src-tauri/target` from synchronization.
On Windows, write the `com.dropbox.ignored` alternate data stream with
`Set-Content -LiteralPath <directory> -Stream com.dropbox.ignored -Value 1`.
On macOS use `xattr -w com.dropbox.ignored 1 <directory>`; on Linux use
`attr -s com.dropbox.ignored -V 1 <directory>`. Recheck the attribute after
`npm ci` and after a Cargo build because either tool may recreate its output
directory. Keep machine-specific Cargo target paths in local configuration,
never in versioned files.

Build this exported edition to a new directory outside the repository:

```text
python development/build_suite.py --output <new-output-directory> --public-only
```

The exported manifest fixes the edition and complete suite layout. All member
packages are bundled under the suite's `packages/` directory. An isolated build
needs no sibling source checkout or individual Skill repository.

The complete private authoring source also supports `--profile general|codex`
and `--layout standalone|suite`. Standalone projections retain family guidance;
suite projections require the full member set. Export always produces a complete
suite with its selected profile and layout. An exported single-profile source
does not offer the other profile.

The build receipt records the selected profile, layout, package inventory,
source revision and hashes. Uncommitted sources produce development builds.
Publication requires inspected committed sources and the release checks.
