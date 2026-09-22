# Luna CLI execution

## Scope and qualification

W-023 adds an explicitly authorized Terra-Medium context-fix test path only;
see [workflow-context-execution.md](workflow-context-execution.md). Current
runner SHA256 is `4cb9ea0f660c3bfee33f3d555a7549998e78c89a1e8ec2ddad85038488725519`;
16 offline checks pass. Luna remains the general release-gate tester. The
starter hash and 15-test pilot below describe the retained earlier Luna baseline.

This is a theoretical Skill-comprehension test, not proof that project actions
were executed. Test the built packages, never member templates or installed
live Skills. A repeat reproduces inputs and procedure, not identical model text.

On 2026-09-21, Code pilots 01-06 completed in one turn; 07 requested two
references and completed in the same conversation. SOL accepted 07 manually:
the pilot's literal-phrase grader incorrectly rejected “Do not edit production
or test code.” Preserve that original output; do not retry or alter the key.

CLI qualification is version-specific. Observed executable: Windows Codex
`0.155.0-alpha.9.2`, SHA256
`bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226`.
Pinned bundled catalog SHA256:
`0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0`.
See `codex-cli-preflight.md` for the localhost request-catalog check and its
limits. A changed executable, catalog or isolation option requires renewed
qualification before accepting tests.

## 1. Freeze inputs

Current package/case baseline: `codex-cli-inputs-r13.json`. Its predecessor is
recorded only for input provenance; historical Gemini results are not reused.
Code routing, Handoff status/read gate, Brainstorm comparison evidence and
Design partner-gate clarifications supersede earlier cores. R12 clarifies
Research's Deep completion; R13 clarifies mixed evidence-domain routing.
Use current hashes in `codex-cli-results.md`. The example uses R13;
CLI/helper hashes are unchanged.

The two paired Ask cores are superseded by
`codex-cli-inputs-r14-ask-paired.json`, which binds the new receipt and paired25
prompt. Other R13 packages/cases remain unchanged. Preserve historical receipts;
The later user-requested Astra high defaults use the `ask-astra-high` receipt
below, with no new model tests requested. R14/R15 retain their actual receipts.

1. Complete W-006 and build public packages under
   `E:/Dropbox/AI Projects/skills/public`. Keep Workflow in its separate private
   suite build; do not publish it.
2. Verify package files against both suites' build receipts using
   `../shared/build/verify_package_set.py` from the suite root.
   Record the exact command, receipts and SHA256 values in the batch manifest.
3. Freeze each selected `*-cases.md`, hidden `*-expected.md`, transport text,
   package receipt, every package file, runner and lifetime-helper hash.
   Do not modify keys to fit answers. A changed package starts a new revision.
4. Use the existing CLI login. Do not inspect, copy or log credentials. Do not
   change global Codex settings. Pin the catalog file produced by the qualified
   `codex debug models --bundled` invocation.
5. Create a new output directory under workspace `temp/YYYY-MM-DD-task-name/`.
   Each case gets a fresh empty workspace and conversation. Refuse an existing
   output directory; never overwrite a prior attempt.

Current public-package verification (PowerShell, from the suite root):

```powershell
python -B ../shared/build/verify_package_set.py `
  --root 'E:/Dropbox/AI Projects/skills/public' `
  --receipt 'E:/Dropbox/AI Projects/skills/public/build-receipt.json' `
  --receipt 'E:/Dropbox/AI Projects/temp/2026-09-21-suite-migration/ask-astra-high/build-receipt.json'
```

For a later build, replace both receipt paths with that build's receipts and
freeze their new hashes. Do not carry these historical paths into a new batch
without checking that they still describe its actual packages.

## 2. Construct one tester prompt

SOL Medium coordinates the run and grades against the author's fixed keys.
The tester is exactly `gpt-5.6-luna`, reasoning `medium`.

- Follow the selected case file's discovery range and response question.
  Discovery receives only the built frontmatter, exact case and discovery
  question. Other cases receive the built `SKILL.md`, exact case and that
  Skill's question. Do not apply Code's mode/risk question to every Skill.
- Append the neutral packaged-text instruction in `gemini-transport-v3.md`.
  Its filename is historical; no Gemini process is used. For Code, retain
  `codex-transport-v4.md`'s distinction between the hypothetical operation and
  answering, with reference-read requirements owned by the Skill. Historical
  v2-wrapper results retain their provenance and stated limitations.
- Brainstorm application cases use `codex-brainstorm-transport-v5.md` to
  distinguish scenario rules from dispatch of the evaluation question.
- From the Design04 repair onward, discovery-only cases replace the generic
  application/READ suffix with `codex-discovery-transport-v6.md`. Do not use
  this suffix for application cases.
- Never include keys, grader comments, earlier answers or unrelated Skills.
  Save the exact UTF-8 prompt bytes and their SHA256 before execution.
- For Ask single25, R15 supplies the manifested root `config.default.json`
  and verified absence of personal `config.json` as upfront fixture data.
  The READ runner remains limited to references/assets/scripts. Never read a
  user's personal configuration to satisfy a theoretical case.

## 3. Invoke the pinned CLI

Reusable starter: `run_codex_cli_case.py`. All 15 offline tests pass, including
real local process-boundary tests. Case 08 passed its real two-turn pilot with
SOL grading and independent author confirmation. Before first use after
a change, run its offline tests and qualify one bounded real pilot; do not infer live
qualification from unit tests. Do not reuse the historical pilot scripts:
they import a helper from Z: and contain a superseded substring grader.

Qualified starter SHA256:
`ac268d8304ea1d5106bae05f0d44ee01cff56f5dbd70a05a9ddc6d1cafc2de97`.
Owned `process_lifetime.py` SHA256:
`be98b0e5590389a96ace79a4dd5572cb36c4c19214371a78628adbe87cca7d32`.
Pilot evidence: workspace
`temp/2026-09-21-suite-luna-evaluation/code-r2-08-reusable-cli/`.

Offline checks (suite root; no model calls):

```powershell
python -B -W error::ResourceWarning -m unittest discover -s development/tests -p test_codex_cli_case.py -v
```

PowerShell invocation from the suite root (replace angle-bracket values with
the frozen batch manifest's values, not hashes recomputed to accept drift):

```powershell
python -B development/luna-tests/run_codex_cli_case.py `
  --case-id '<case-and-revision>' `
  --prompt '<absolute-reviewed-prompt.md>' `
  --package-root 'E:/Dropbox/AI Projects/skills/public/scoville-code-anti-ai-slop/scoville-code-anti-ai-slop' `
  --receipt 'E:/Dropbox/AI Projects/skills/public/build-receipt.json' `
  --receipt-member 'scoville-code-anti-ai-slop' `
  --catalog '<absolute-pinned-catalog.json>' `
  --codex 'C:/Users/benja/AppData/Local/OpenAI/Codex/bin/247581e40ee272fb/codex.exe' `
  --output '<absolute-new-temp-case-directory>' `
  --model gpt-5.6-luna --effort medium `
  --expected-prompt-sha256 '<reviewed-prompt-sha256>' `
  --expected-receipt-sha256 '1b9da874dad9fa63d3adb89bf61c628360e8f124c09068c934c95613f53e7c61' `
  --expected-catalog-sha256 '0a2bca132452338774a9c243e195095ad0b6400b17b2586306a69e8dcfade5f0' `
  --expected-codex-sha256 'bc45017e8239dc150258f69309ced9df6bbcdf5b8e4f346decf780ac0999e226' `
  --timeout-seconds 90 --max-turns 4
```

For another Skill, change its package root, member and corresponding receipt.
`--package-root` is the inner folder containing `SKILL.md`, not the receipt's
outer distribution `package_path`. For private Workflow, use
`E:/Dropbox/AI Projects/temp/2026-09-21-suite-migration/workflow-luna-final/scoville-suite/packages/scoville-workflow-for-codex/scoville-workflow-for-codex`
and the private receipt in the baseline manifest. Both nested names are required.
The prompt is prepared using section 2 and reviewed against the frozen case;
the starter transports it without receiving the hidden key. Record its exit
code and inspect its summary. Exit zero is transport success, not acceptance.

The starter must construct an argument array, not concatenate a shell command.
Use these global arguments before `exec`:

```text
--ask-for-approval never --sandbox read-only --model gpt-5.6-luna
-c model_reasoning_effort="medium"
-c model_catalog_json="<absolute-pinned-catalog-path>"
-c mcp_servers={}
-c web_search="disabled"
```

Append `--disable <name>` for each of these exact features:

```text
shell_tool apps hooks plugins remote_plugin plugin_sharing
browser_use browser_use_external browser_use_full_cdp_access computer_use
multi_agent multi_agent_v2 collaboration_modes code_mode_host
workspace_dependencies image_generation in_app_browser tool_suggest
skill_search skill_mcp_dependency_install enable_mcp_apps
codex_apps_mcp_2026_07_28 mcp_2026_07_28 auth_elicitation
tool_call_mcp_elicitation
```

Initial suffix; send the prompt through stdin:

```text
exec --ignore-user-config --ignore-rules --strict-config
--skip-git-repo-check --json -C <fresh-empty-workspace> -
```

Resume suffix, with the same globals and workspace as process cwd:

```text
exec resume --ignore-user-config --ignore-rules --strict-config
--skip-git-repo-check --json <exact-thread.started-id> -
```

Do not use `--ephemeral`: native identity/model evidence is required. Do not
substitute `latest`, another model or another reasoning level. Do not add
`node_repl.enabled`, `tools.view_image` or `tools.web_search`; this qualified
build rejects them. Disabling `unified_exec` is not a tool-isolation gate.

The process owner must stop the complete owned process tree on every exit,
including timeout and parser failure. The qualified pilot uses a Windows Job
Object and a gated child; its helper consumes a leading NUL byte before passing
the prompt to Codex. That byte is helper-specific, not part of the CLI prompt.

## 4. Serve requested text

Allow at most four turns, with a 90-second deadline per turn and no automatic
retry. Only a response consisting entirely of `READ <relative-path>` lines
requests files. Validate every path using `gemini-transport-v3.md`, verify the
original bytes against the frozen receipt, and deliver only requested UTF-8
text. Never run a requested script. Normalize CRLF only in delivered text.

Save each supplied path and hash. Append the transport's exact continuation
instruction, then resume the exact original thread. A new conversation is not
a valid continuation. Stop if turn four still has no final answer.

## 5. Validate transport before grading

Read the complete stdout event stream through EOF, including anything after
`turn.completed`; retain stderr separately. Require exit zero, one matching
thread identity, one started/completed turn and one nonempty agent answer per
invocation. Reject malformed JSON, unexpected ordering, extra answers, trailing
actions, tools, permissions, unknown events, stderr or process-cleanup failure.

Only this exact pre-turn diagnostic is permitted, at most once per invocation:

```text
Code Mode is unavailable because code-mode host is disabled. Code mode will fail closed; enable `features.code_mode_host` and install `codex-code-mode-host`.
```

Do not follow that message's suggestion. All other errors stop the batch.
Verify native `session_meta.id` equals the returned thread ID and every current
`turn_context` has model `gpt-5.6-luna`, effort `medium`. Require the expected
turn count. This is native configuration evidence, not backend attestation.

## 6. Grade and retain evidence

SOL compares the final answer with the frozen key for routing, assessment,
required artifact, authority limits and unsupported claims. Grade meaning,
not exact phrasing. The author independently checks the prompt, delivered
files, complete events, native identity and semantic judgment. Keep protocol
grade, SOL semantic grade and author acceptance separate; a runner cannot
award semantic PASS from substring matches.

For each case retain temporarily: manifest and commands, exact prompts,
delivered-file hashes, full events, stderr, answers, per-turn usage, thread ID,
native model/effort evidence, exit/cleanup result and grading reason. Record
only a concise accepted-result summary in `codex-cli-results.md`.

Preserve usage fields separately. Cached input is not extra input. Do not add
reasoning tokens to output or sum resumed usage without establishing whether
the respective fields overlap or are cumulative. Report uncertainty instead
of a fabricated cost total.

On a transport defect, stop and repair the runner before a new explicitly
identified attempt. On a Skill defect, fix the canonical source, rebuild and
rerun affected cases plus relevant regressions. Preserve failed attempts and
revision links. Never count an infrastructure failure as a comprehension fail.

ADR-0008 requires only the 64 IDs in `selected-cases.json`: Code20,
other non-Design sets5, each Ask base1, Design2 each for Generate/Critique/Repair.
Retain the source corpus; excluded
cases are not required passes. All selected cases must match the final packages. Passing
does not authorize publication. Keep raw evidence temporary unless a published
release links to it, following workspace retention rules.
