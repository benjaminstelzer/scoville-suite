## How to use

Ask naturally, for example:

```text
Use scoville-ask-for-codex to ask SOL for an independent review of this patch.
```

```text
Ask Fable and Claude independently how they would approach this problem, then compare their answers.
```

### Configure defaults

`config.default.json` beside the installed `SKILL.md` owns the shipped defaults.
Save project choices under `ask` in `.scoville/config.json` at the project root.
Missing values use the shipped defaults. Reading settings creates no file.
Explicit requests override these values for that call without saving them.

The `astra`, `sol`, `claude` and `fable` presets resolve named requests. The
shipped `advisers` list applies when you do not name an adviser. Every preset's
model, effort and route is configurable. Current defaults:

```json
{{ include: member.defaults }}
```

For example, this `.scoville/config.json` selects SOL and Fable by default and
changes only SOL's effort:

```json
{
  "ask": {
    "advisers": ["sol", "fable"],
    "presets": {"sol": {"effort": "medium"}}
  }
}
```

Objects merge by field. The adviser list replaces earlier selections. Higher-layer preset fields also override inherited inline adviser fields; inline adviser fields win over presets within the same layer. An
explicit per-call model or effort wins without changing the saved defaults.
Follow-ups retain their original settings unless explicitly changed. For a
custom adviser, supply an ID, route, exact model and effort in `advisers`.
See the installed configuration reference for helper inputs and migration.

### How to Ask with Claude Code

1. Install [Claude Code](https://code.claude.com/docs/en/setup) if needed. Open a new terminal or PowerShell window; the folder does not matter.
2. Run `claude --version`. Opus 5.5 needs **2.1.280 or newer**. For an older version, run `claude update`, then check again. Keep running Claude sessions open.
3. Run `claude auth login` and complete sign-in in your browser. Run `claude auth status` to check that you are signed in.
4. In Codex with this Skill installed, ask: **“Ask Claude to review this change.”** The imported defaults above determine the model and effort. Change the `ask` settings in `.scoville/config.json` or name another model or effort in the request.

If ASK reports an expired OAuth session, repeat step 3 and retry. An old CLI can reject the correct model ID; repeat step 2 instead of substituting a model.
