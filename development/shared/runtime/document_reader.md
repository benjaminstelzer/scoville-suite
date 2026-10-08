Before a potentially large read, use the verified Python interpreter and the
bundled reader:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<document>" --max-output-tokens <limit> --part 1`.
The program is `scripts/check_text_size.py`; the document is only the `--file`
value. Start only named `.py` files as Python program files. SKILL.md, references
and assignments are documents, never programs.

Use the smallest declared or explicitly selected command and outer output limit.
The reader validates the complete UTF-8 file and budgets its labels too.
Follow `part=N bytes=start:end/total next=M` with `--part M` through `last`,
where end equals total. Read every unchanged part in order before dependent
work. Keep the same budget throughout; if it changes, restart at part 1.
Use separate outer calls unless their complete combined output, including
labels and metadata, has been measured and fits. Multiple reads or `text()`
calls in one outer call share its budget. A reader error leaves the read
incomplete, even if the budget cannot fit its diagnostic. Do not alter or copy
the input, truncate it or recover omitted text after an oversized read.
Without an applicable limit, read complete UTF-8 directly; invent no budget.
