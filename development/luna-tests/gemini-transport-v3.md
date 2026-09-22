# Packaged-text transport v3

For subsequent Skill sets, retain `gemini-execution.md` safety rules and the
qualified v2 conversation protocol. Freeze this file and the supervisor before
each batch; preserve earlier runs. Cases and hidden keys are unchanged.

Discovery cases receive only exact built frontmatter and their test file's
discovery question. Other cases receive the exact built core, case and the
test file's response question, followed by:

> Apply the supplied Skill to this hypothetical case. Do not execute project
> actions or use tools. Source/read results in the case are fixtures. If the
> Skill requires a packaged text file not yet supplied, first reply only with
> `READ <relative-path>`, one file per line. We will supply it as text. Otherwise
> answer the case concisely, including any artifact the case requires. State
> unavailable facts as unknown; do not invent source content or completed work.

The path is relative to the built Skill directory. Serve only exact manifest
entries inside that directory, after hash verification. Permit UTF-8 text in
references, assets and scripts, not just `references/*.md`. Reject absolute
paths, backslashes, empty or dot segments, traversal, symlink escapes, unknown
files and duplicate requests. Never execute requested files. Normalize CRLF
to LF only for text delivery; hashes cover original package bytes.

Continue in the same conversation with the requested text and this instruction:

> Continue the same hypothetical case using only supplied text. Do not use
> tools or execute project actions. Request any other required packaged text
> with `READ <relative-path>` lines; otherwise provide the final case answer.

No grading feedback, keys or prior answers enter tester prompts. Keep v2's
four-turn limit and stop rules. Classify native system metadata separately
using only the already-qualified exact schema; tools and unknown events stop
the batch. Record semantic grades independently from transport success.

Before Handoff's full set, qualify an asset request with case 06. Verify actual
asset delivery, same conversation, clean completed output and fixed template
structure. Do not force the correct filename or supply the answer key.
