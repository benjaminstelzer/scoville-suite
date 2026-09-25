# Workflow context-fix test procedure

Scope: W-021–W-023 only. Tester: `gpt-5.6-terra`, `medium`. This does not
replace the Luna publication gate. No installed/live Skill changes.

## Inputs and isolation

Use the existing CLI login; inspect no credentials and change no global config.
The runner disables tools/features, ignores user config/rules, uses read-only
sandboxing and an empty per-case workspace, checks native session model/effort,
and serves only hash-matched built files. Unknown tool/events or stderr stop it.
Official CLI option reference: https://developers.openai.com/codex/cli/reference
(accessed 2026-09-21). Local executable evidence qualifies this exact version.

Pinned inputs:
- CLI: `<user-home>/AppData/Local/OpenAI/Codex/bin/247581e40ee272fb/codex.exe`;
  SHA256 `bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226`.
- Catalog: `<workspace-root>/temp/2026-09-21-codex-loopback-tool-catalog/bundled-model-catalog.json`;
  SHA256 `0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0`.
- Runner: `run_codex_cli_case.py`;
  SHA256 `4cb9ea0f660c3bfee33f3d555a7549998e78c89a1e8ec2ddad85038488725519`.
- Lifetime helper unchanged:
  `be98b0e5590389a96ace79a4dd5572cb36c4c19214371a78628adbe87cca7d32`.
- Cases: `workflow-context-cases.md`; hidden key:
  `workflow-context-expected.md`. Freeze both before model execution.
- The supplemental question/key are in `workflow-context-supplement.md`.
  Its key never enters a prompt.

Missing catalog: regenerate with the pinned CLI's `debug models --bundled`,
capture stdout as an artifact and require the exact hash above. Changed
binary/catalog/isolation inputs require renewed qualification; never simply
replace a hash to accept drift. A replay reproduces inputs, not model wording.

## Repeat

Run from `<workspace-root>/skills/private/scoville-suite`.
Replace NEW below with a fresh task-owned temp directory; never reuse output.

1. Run `python -B -m unittest discover -s
   members/scoville-workflow-for-codex/development/tests -q` and
   `python -B -W error::ResourceWarning -m unittest discover -s
   development/tests -p test_codex_cli_case.py -q`.
2. Build: `python -B development/build_suite.py --output NEW/build
   --member scoville-workflow-for-codex`. Then
   `python -B development/build_suite.py --check-packages --output NEW/build`.
3. Qualify without a backend:
   `python -B development/luna-tests/preflight_codex_cli.py
   --model gpt-5.6-terra --codex CLI --catalog CATALOG --output NEW/preflight`.
   Require valid:true, one exact Terra/medium request, no Authorization header,
   no tools and stopped process tree. The tools field may be absent or []; an
   explicit null or nonempty value fails. The local HTTP400 is intentional.
4. Freeze:
   `python -B development/luna-tests/prepare_workflow_context.py
   --build NEW/build --output NEW/tests --codex CLI --catalog CATALOG`.
   It verifies package receipt/binary/catalog and emits three exact prompts plus
   frozen.json with hashes and complete argv arrays. Review the prompt/key
   separation before any call.
5. Execute one frozen case with Python:
   `m=json.loads(Path("NEW/tests/frozen.json").read_text());
   subprocess.run(m["cases"][0]["command"], check=True)`.
   Use index 1 or 2 for the other cases. Each starts a fresh conversation; READ
   requests resume only that conversation, at most four turns and 90 seconds
   per turn. No retries or substitute model after a protocol failure.
6. Require protocol PASS and every native turn_context equal to Terra/medium.
   Inspect final answers against the hidden key independently. Preserve
   omissions/failures; do not rewrite keys or overwrite attempts.
7. A targeted supplemental test may clarify an omitted required behavior.
   Freeze its new question/key before execution, record why it was added, and
   keep the first results. Supply exact built SKILL/core/activation plus only
   the Prompt section of workflow-context-supplement.md. Reuse the frozen
   command with a new case ID, prompt hash and output directory. Never include
   the Hidden author key or previous answers.
8. Retain concise findings and exact IDs/hashes in the owning report. Keep raw
   prompts, native traces and responses under task temp, not release packages.

## What this proves

Deterministic tests use real builder/lifecycle code with a mock native sender.
A separate Codex execution-memory smoke check preserved the actual built
payload across calls without printing it, passed it through the built Python
lifecycle helper and rejected a repeated send. Its guard/sender were fixtures.

Terra tests only rule comprehension. No live DIVI5 dispatch, archival,
installation, publication, production token reduction or Luna result follows.
Compare measured characters separately from native token counters; do not sum
resume counters without establishing whether they overlap.
