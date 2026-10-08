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

Check completeness separately from command success. A running `session_id`
is unfinished; the loop retains its ID and every output chunk until completion.
Never restart a running command. A successful
`--part` result starts with `part=` and requires all parts through `last`.
A complete `--run` capture starts with `exit=` and includes both streams;
its child exit status still determines whether the command succeeded.
A nonzero child exit can provide valid failure evidence. Complete-file metadata
requires reading the entire supplied file. Empty output, capture or reader
failure, or `output_complete=false` leaves required input unread and stops
dependent work. Never discard a failure's stdout or stderr.
