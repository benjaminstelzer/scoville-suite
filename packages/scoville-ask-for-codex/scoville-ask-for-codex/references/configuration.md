# Settings and helper inputs

All helpers use Python 3.11+. Run them from this installed package with its
absolute path; never import a sibling Skill or use a development checkout.
`ask.py` reads one JSON object from stdin and returns JSON. `ok:false` or a
nonzero exit stops the affected operation. Native payload helpers make no host
calls. `list_models.py` starts the configured Codex executable's read-only
app-server session for `initialize` and paginated `model/list`, then closes it.
It starts no adviser task. Its `--command` option accepts an explicit executable
and arguments when the host's Codex binary is not on PATH. Use the executable
for the current host/account; never assume a different CLI catalog proves
desktop availability.

The selected project root owns `.scoville/config.json`. Its `ask` section
overrides this Skill's defaults. Missing files or fields use those defaults.
Reads never create a file and never search parent directories.
Objects merge by field;
`advisers` replaces the entire list so an explicit selection never adds unwanted
advisers. Select named advisers with strings such as `["sol", "fable"]`, or use
objects with `id` and per-call overrides. A matching ID inherits its configured
preset. Custom IDs need `route` (`native` or `claude-cli`), exact `model` and
`effort`; `name` is optional. One, two and more advisers use the same structure.
Explicit named requests select only those presets. Read the actual config for
current defaults rather than inferring model or effort from a Skill name.

Shipped settings, generated from their canonical file:

```json
{
  "schema_version": 1,
  "advisers": ["astra"],
  "presets": {
    "astra": {"route": "native", "model": "gpt-6-astra", "effort": "high"},
    "sol": {"route": "native", "model": "gpt-6-sol", "effort": "high"},
    "claude": {"route": "claude-cli", "model": "claude-opus-5-5", "effort": "high"},
    "fable": {"route": "claude-cli", "model": "claude-fable-5-1", "effort": "medium"}
  },
  "claude": {
    "max_budget_usd": 10,
    "session_persistence": true,
    "customizations": false,
    "timeout_seconds": 3600,
    "web_tools": false
  }
}
```

Save only changed values, for example:
`{"ask":{"advisers":["sol","fable"],"presets":{"sol":{"effort":"medium"}}}}`.
Request overrides use the fields inside `ask`. Retained follow-up
settings take precedence over new defaults unless explicitly changed.

`resolve` accepts `project_root` and optional unsaved `overrides`. Pass the
selected project's absolute root. When omitted, `cwd` supplies the root, or
the process working directory if neither was supplied. `project_config` is
rejected with migration guidance. Keep settings unchanged during a run.
For native
advisers it queries `model/list`, or accepts the unchanged freshly observed
`catalog` from `list_models.py`; do not synthesize or edit a catalog to permit a
model. Display the returned model/effort choices when configuration is requested.

`prepare` additionally requires `mode:review|consultation`, `question`, `scope`,
and a unique `reference`. Native entries need verified `caller_id`, exact
`caller_title`, `projectId`, `creation_authorized:true`, `prior_state:not_started`
and the observed `prior_task_ids`. CLI entries need an existing absolute `cwd`.
These authorization fields record existing authority; they do not grant it.

`followup` takes `handle`, `archived:false`, `delivery_state:not_sent`, a new
`reference`, `question`, `scope`, optional adviser `overrides` and fresh `catalog`.

## Migrate existing settings

Keep original personal configuration files. Compare their values with the
imported defaults and show differences before saving requested choices under
`ask` in the project's `.scoville/config.json`. Do not copy them automatically.
Map each old `astra` or `sol` object to an adviser with that ID, route `native`,
and its unchanged model/effort. Map `claude` to route `claude-cli` and retain its
budget, session persistence and customization flags in the `ask.claude`
object. A Claude-only flat configuration uses the same mapping. Build a single
explicit adviser list; do not merge five old defaults into an unsolicited round.
The old optional `command:claude` maps to the adapter's PATH lookup. A custom
command or conflicting settings across old variants need a user choice; do not
silently discard them. Validate with `resolve` before using the new file.
Retain old task/session IDs separately for follow-ups; missing identity or
settings cannot be inferred from an old display title.
