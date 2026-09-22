# Gemini CLI preflight

User-selected replacement: ADR-0002. No Gemini evaluation case is accepted yet.

The existing Antigravity CLI lists `gemini-3.8-flash-medium`. A disposable
sentinel probe used that model, `--effort medium`, `--mode plan`, `--sandbox`,
stream-json and no permission bypass. No existing project was attached.

Observed in conversation `69950c92-0d28-4af7-af45-0f12fa3ca486`:

- Native init model: `gemini-3.8-flash-medium`.
- Native permission mode: `request-review`.
- `write_to_file` returned a permission-denied error for the disposable sentinel.
- Sentinel absent; the owned Windows process job was terminated and empty.
- No separate effort field in init. Model slug identifies the Medium variant;
  argv records requested medium effort. Neither is backend attestation.

Raw evidence and supervisor:
workspace `temp/2026-09-21-suite-gemini-evaluation/permission-probe-01/` and
`temp/2026-09-21-suite-gemini-evaluation/probe_transport.py`.

This proves denial of the tested file write, not isolation of every advertised
tool. The supervisor aborts on tool events, but post-emission termination is not
itself a pre-execution security boundary. No claim of universal isolation.
Next: SOL independently reviews the evidence and runs one supplied-text,
no-tool discovery case under the same restrictions. Author review gates a batch.

## Rebuilt Code package

The public Code SKILL.md now includes the source reference-selection correction.
SHA-256: `5257f391368e795bcfdc837b0a82e7916f545042eef25cca902adfde9d418f58`.
All other public package files are unchanged. Public inventory verification
passed for 13 packages/188 files, and the Scoville current-source check passed.
The old Code tree and receipt remain in workspace
`temp/2026-09-21-suite-gemini-evaluation/luna-code-baseline/`.
Original evaluation-manifest.json stays historical; its Code hash no longer
describes the public candidate. Freeze new Gemini hashes before a batch.
