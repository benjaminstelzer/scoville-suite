Without an applicable limit, read complete UTF-8 directly; invent no budget.
With an applicable limit:

1. Use the smallest declared or explicitly selected limit for the read and
   enclosing output. Read separately unless the complete combined output,
   including labels and metadata, is measured and fits; combined reads share
   that budget.
2. If the file may exceed that limit, use the verified Python interpreter and
   bundled reader:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<document>" --max-output-tokens <limit> --part 1`.
   It validates the complete UTF-8 file and budgets labels too.
3. For multipart output, follow `part=N bytes=start:end/total next=M` with
   `--part M` through `last`,
   where end equals total. Read every unchanged part in order before dependent
   work. Keep the budget unchanged; otherwise restart at part 1.

A reader error leaves the read incomplete, even if its diagnostic cannot fit.
Do not alter or copy the input, truncate it or recover omitted text after an
oversized read.

The reader program is `scripts/check_text_size.py`; pass its document only as
`--file`. Only named `.py` files may be Python program files. SKILL.md, references
and assignments are documents, never programs.
