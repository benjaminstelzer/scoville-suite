## Native tool capture

Use this template to run a generated capture command through Codex's native
tools. Forward the checker's rendered output unchanged as text. Do not
JSON-encode it again or add status lines of your own. Structured helper results
and native tool arguments keep their own interfaces.

The template uses 20000. Use the same smallest applicable limit in the
generated command, both tool calls and the `@exec` directive. Replace
`<command_json>` with one JSON string literal that encodes the complete
generated command, including quotes and backslashes. Replace the whole value
rather than pasting into existing quotes or a JavaScript template literal,
where backticks and `${` would be interpreted; JSON keeps them as data.

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

A finished outer script does not mean the child finished. For `pending`:

1. Keep the `session_id` and every chunk.
2. Continue the same session in a separate outer call with one
   `tools.write_stdin({session_id: <retained_id>, chars: "",
   yield_time_ms: 10000, max_output_tokens: 20000})`. Starting the command
   again would repeat its effects.
3. Forward that output and report pending or finished the same way until the
   actual exit status arrives or an authorized interruption applies.

Make one bounded native call per outer call. If the outer tool itself yields a
running cell, resume that cell first.

Command success and output completeness are separate. The child's `exit=`
decides success; a nonzero exit can be valid failure evidence with both
streams kept. A capture failure, missing output, or empty output where content
was required leaves that content unread. Resolve it before work that depends
on it.
