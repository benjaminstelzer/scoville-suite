# Text-reference transport v2

Supplement `gemini-execution.md`; cases, hidden keys and safety limits stay
unchanged. Freeze this file's hash before use. Preserve v1 runs.

The v1 code-07 pilot named the required references but did not request them.
Its conditional request wording did not exercise conversation continuation.
This revision makes reference delivery explicit without naming the right route.

After the exact core and case, use this wrapper:

> Determine the hypothetical case's mode, risk, required reference routes,
> next action and evidence limits. Do not execute the hypothetical work or use
> tools. Select routes from the supplied Skill, not from this test wrapper.
> If your selected routes require packaged references not yet supplied, first
> reply only with `READ references/<name>.md`, one requested file per line.
> We will supply those files as text. Otherwise give your concise final answer.

Deliver only requested manifest-allowlisted, hash-verified package files in the
same conversation. Include no expected answer or evaluation feedback. Stop on
identity mismatch, tools, permission events, unknown files, repeated requests,
incomplete output or no final answer within four turns. Inspect each full stream;
do not sum possibly cumulative usage across turns.

Qualification requires one Core-only case with no request and one reference
case with actual text delivery, unchanged conversation identity and a completed
answer. A correct reference name alone does not qualify continuation. Record
semantic grade and transport result separately; neither substitutes for the
other. Do not retry automatically.
