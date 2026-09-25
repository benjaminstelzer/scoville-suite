## Compatibility

**Codex online.** Requires Codex desktop with native task controls for native advisers, a verified calling task and saved project, network access, and Python 3.11 or newer. Use a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0 or newer. Tests performed are recorded separately from this minimum.

The model catalog comes from the current Codex app-server through `model/list`. A listed model still needs to be accepted by the task host. Native third-party models require a suitable provider connection, such as EasyCLIProxy where configured. The Claude CLI route requires installed, authenticated Claude Code. Opus 5.5 requires version 2.1.280 or newer. See “How to Ask with Claude Code” for setup.

The Python helpers are required. A missing interpreter or helper failure has no manual replacement route. Tasks use the host’s normal sidebar sorting.

Ask is also available as a standalone Skill from
[scoville-ask-for-codex](https://github.com/benjaminstelzer/scoville-ask-for-codex).
Its standalone package works independently. Installing the complete suite uses
the suite packages and includes every member.
