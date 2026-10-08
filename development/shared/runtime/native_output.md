For native Codex calls, forward rendered checker output unchanged as text.
Do not JSON-encode it again or add unchecked status lines. Structured helper
results and native tool arguments keep their own interfaces.

Use one checked read or capture per outer call. This template selects 20000;
use the same smallest applicable limit in the generated command, both tools and
outer directive. Before execution, replace `<command_json>` with one JSON string
literal encoding the complete generated command, including quotes and backslashes.
Replace the whole value; never paste a command inside existing quotes or a
JavaScript template literal. JSON encoding preserves backticks and `${` as data.

```javascript
// @exec: {"max_output_tokens": 20000}
let r = await tools.exec_command({
  cmd: <command_json>,
  max_output_tokens: 20000
});
let output = r.output;
while (r.session_id !== undefined) {
  r = await tools.write_stdin({
    session_id: r.session_id, chars: "", yield_time_ms: 10000,
    max_output_tokens: 20000
  });
  output += r.output;
}
text(output);
```

Check completeness separately from command success:

| Result | Completion condition |
| --- | --- |
| Running `session_id` | Retain its ID and every chunk until completion; never restart the command. |
| `part=` from `--part` | Read all unchanged parts through `last`. |
| `exit=` from `--run` | Both streams are captured; the child exit status determines command success. A nonzero exit can supply valid failure evidence. |
| Complete-file metadata | Read the entire supplied file. |
| Empty output, capture or reader failure, `output_complete=false` | Required input remains unread; stop dependent work. |

Never discard a failure's stdout or stderr.
