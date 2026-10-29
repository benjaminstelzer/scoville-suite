## Native tool capture

Apply [machine-data.md](machine-data.md) before native machine-data delivery.
Use this template only for eligible output selected under that rule. Forward
rendered checker output unchanged as text, without JSON-encoding it again or
adding unchecked status lines. Structured helper results and native tool
arguments retain their own interfaces.

Retain every `exec_command` chunk, `session_id` and final exit status until the
child ends. Outer script completion does not establish child completion; do
not restart a running command. Make one bounded native call per outer call.

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
text(r.output);
text(r.session_id !== undefined
  ? {state: "pending", session_id: r.session_id}
  : {state: "finished", exit_code: r.exit_code});
```

For `pending`, retain the handle and start a separate outer call containing
one `tools.write_stdin({session_id: <retained_id>, chars: "",
yield_time_ms: 10000, max_output_tokens: 20000})`. Forward its eligible output
and report pending or finished in the same way. Continue until the actual
exit status arrives, unless an authorized interruption applies. If the outer
tool itself yields a running cell, resume that cell first.

Command success and output completeness are separate: the child's `exit=`
determines success and a nonzero exit can supply valid failure evidence.
Process complete-file metadata as specified above. Capture failure, missing
output without that route, or empty output where required content was expected
stops dependent work. Preserve both failure streams.
