## Compatibility

Requires a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0
or newer. This requirement is separate from the models actually tested.

{{ profile: general }}Any Agent Skills host with repository read/write access. Direct Markdown/YAML planning; no service or network required. The writing-profile helper needs Python 3.11+; selector, validator and Decision-batch helpers need Python 3. Manual alternatives load only without Python; helper errors remain errors. Developed for Codex and Claude Code; other hosts untested.{{ /profile }}{{ profile: codex }}Codex with repository read/write access and Python 3.11+. Direct Markdown/YAML planning; no service or network required. Bundled writing-profile, selector, validator and Decision-batch helpers are required for their operations. Missing dependencies or helper errors block the affected operation.{{ /profile }}
