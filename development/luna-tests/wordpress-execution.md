# WordPress suite comprehension test

Run five distinct cases from `wordpress-cases.md`. The author freezes
`wordpress-expected.md` before execution. SOL Medium coordinates and grades,
LUNA Medium answers. The author independently verifies the results.
Cases 01-03 use the built core and requested references. Cases 04-05 test
discovery with built WordPress, UI and Design frontmatter only.

## Repeat

From the Scoville Suite root, use a fresh task directory under workspace
`temp/YYYY-MM-DD-wordpress-suite/`. Never overwrite a prior run.

1. Run `python -B -W error::ResourceWarning -m unittest discover -s
   development/tests -q`.
2. Build with `python -B development/build_suite.py --output NEW/build` and
   verify with `--check-packages --output NEW/build`.
3. Use the qualified CLI and catalog from `workflow-context-execution.md`.
   Run `python -B development/luna-tests/preflight_codex_cli.py --model
   gpt-5.6-luna --codex CLI --catalog CATALOG --output NEW/preflight`.
   Require `valid:true`, no tools or authorization header, and a stopped tree.
4. Freeze prompts, keys and commands with `python -B
   development/luna-tests/prepare_wordpress.py --build NEW/build --output
   NEW/tests --codex CLI --catalog CATALOG`. Inspect all five prompts and
   confirm hidden keys are absent. The helper rejects changed pinned inputs.
5. SOL executes each `cases[].command` array in `NEW/tests/frozen.json`
   through `subprocess.run(command, check=True)`. Use the stored arguments,
   not a rebuilt shell string. Execute each once, in order. The runner permits
   four turns, 90 seconds per turn, and serves only receipt-matched text.
6. For each run, inspect all events, stderr, delivered files and native
   contexts. Require protocol PASS and exact `gpt-5.6-luna` / `medium` in
   every native context. Stop on transport failure or model mismatch.
7. SOL grades meaning against the frozen key. The author checks evidence and
   grades independently. Keep protocol, SOL judgment and author acceptance
   separate. Preserve failures. Corrections require a new build and identified
   reruns of affected cases, not changed keys or silent retries.

Full isolation, READ handling and cleanup rules remain in
`codex-cli-execution.md`. These instructions do not replace them.

Keep raw prompts, answers and native traces in task-temp. Retain only concise
results here. Tests demonstrate comprehension, not live WordPress behavior,
publication or installation. A later package must match the tested bytes.
