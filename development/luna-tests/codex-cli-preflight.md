# Codex CLI restart preflight

ADR-0003 selects `gpt-5.6-luna` with `medium` through Codex CLI. SOL Medium
coordinates. No new model run is accepted by this preflight.

Observed CLI: `0.155.0-alpha.9.2`, executable SHA256
`bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226`.
The local help supports `exec --ignore-user-config`: config.toml is skipped,
authentication remains. Approval selection precedes `exec` in this build.
Use per-run overrides only; do not change global settings or copy credentials.

SOL's read-only feature check resolved shell, apps, hooks, plugins, browser,
computer-use and delegation overrides to false. Explicitly disable Node;
the bundled Luna catalog does not disable it by default. Feature flags are
not proof of the complete outgoing tool list. The previous MCP-empty override
did not establish removal of bootstrap servers. Filesystem read-only mode
does not prove clipboard isolation.

Next check: direct the CLI to a localhost-only mock Responses provider with
`requires_openai_auth=false`, no key or extra headers. Capture only model,
reasoning and tool names/types, never header values or prompt content. Return
an error without a model response or tool call. Bound its lifetime and stop
all owned processes. Do not forward requests or intercept real-provider TLS.
Record unknown-model warnings and provider differences; a mock request alone
does not prove an identical authenticated-provider catalog.

Official configuration documents custom-provider base_url, wire_api=responses
and requires_openai_auth (false by default):
https://developers.openai.com/codex/config-reference/
CLI options:
https://developers.openai.com/codex/cli/reference/

Actual native model/effort evidence and safe pilot execution remain pending.

First loopback attempt stopped before any HTTP request: strict-config rejects
`node_repl.enabled` as unknown in this CLI build. Request count was zero, exit
code 1, no timeout; the owned process tree stopped. The proposed Node override
therefore is not usable evidence. Retry only the local mock without this key,
retain code_mode_host=false and inspect whether Node tools remain exposed.
Historical attempt: workspace Z:/Projekts/AI/temp/2026-09-21-codex-loopback-tool-catalog/run-01.
Further artifacts belong under the canonical E: workspace temp directory.

Second loopback attempt under E:/Dropbox/AI Projects/temp/2026-09-21-codex-loopback-tool-catalog/run-02
also stopped before HTTP: strict-config rejects `tools.view_image`. SOL's
bundled-schema check also rejects `tools.web_search`; remove both invalid keys
together, retaining `web_search="disabled"`. Neither attempted run establishes
a tool catalog. The next local check must use only schema-validated overrides.

Run-03 reached localhost once: `model=gpt-5.6-luna`, reasoning `medium`,
`tools=[]`, no Authorization header, no timeout and stopped process tree.
CLI output states Code Mode fails closed while its host is disabled. The mock
returned its intentional error; no model or tool response was generated.
Model catalog refresh received local HTTP 501, so provider catalog parity
remains unproved. Check the documented `model_catalog_json` override with an
unchanged bundled-catalog snapshot before a real pilot. Do not interpret the
empty mock tool list as proof for an unpinned real-provider catalog.

Run-04 pins the unchanged bundled catalog through `model_catalog_json`.
Catalog SHA256: `0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0`.
The author verified the projection: Luna/medium, `tools=[]`, no Auth header.
Stderr is empty; no refresh or unknown-model warning. The intentional mock
error ended the turn and the process tree stopped. This proves the local
serialized catalog for these pinned inputs, not backend execution.

Exactly one real code-01 pilot is authorized with the same catalog and runtime
restrictions through existing CLI login. Remove only mock-provider routing and
mock proxies; capture exact-thread native model/effort and full events. Any
tool/permission event or unexpected error stops execution. Do not count the
known pre-turn Code Mode fail-closed diagnostic as a test result.
