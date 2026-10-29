## Native tool capture

Apply [machine-data.md](machine-data.md) before native machine-data delivery.
Use this template only for eligible output selected under that rule. Forward
rendered checker output unchanged as text, without JSON-encoding it again or
adding unchecked status lines. Structured helper results and native tool
arguments retain their own interfaces.

Retain every `exec_command` chunk, `session_id` and final exit status until the
child ends. Outer script completion does not establish child completion; do
not restart a running command. Use one capture per outer call.

The template selects 20000; use the same smallest applicable limit in the
generated command, both tools and outer directive. Replace `<command_json>`
with one JSON string literal encoding the complete generated command, including
quotes and backslashes. Replace the whole value, never paste into existing
quotes or a JavaScript template literal; JSON keeps backticks and `${` as data.

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

Command success and output completeness are separate: the child's `exit=`
determines success and a nonzero exit can supply valid failure evidence.
Process complete-file metadata as specified above. Capture failure, missing
output without that route, or empty output where required content was expected
stops dependent work. Preserve both failure streams.
