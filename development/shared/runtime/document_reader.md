Without an applicable limit, read complete UTF-8 directly; invent no budget.
With an applicable limit:

1. Use the smallest declared or explicitly selected limit of the command and
   every enclosing tool output. Read separately unless the complete combined output,
   including labels and metadata, is measured and fits; combined reads share
   that budget.
2. If the file may exceed that limit, use the verified Python interpreter and
   bundled reader:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<document>" --max-output-tokens <limit> --part 1`.
   It validates the complete UTF-8 file and budgets labels too.
   Python runs the full checker path `<skill-directory>/scripts/check_text_size.py`
   after `-X utf8`. The checker reads every document only through `--file`, including
   SKILL.md files and references of any Skill, assignments, and `.py` files read as
   text. Keep the verified launcher, checker path and quoting unchanged. Copy the
   last correct complete command: change only `--part` for the reported next part;
   for another document change only `--file` and reset `--part` to 1.
3. For multipart output, follow `part=N bytes=start:end/total next=M` with
   `--part M` through `last`,
   where end equals total. Read every unchanged part in order before dependent
   work. Use one limit for the whole sequence. If an applicable limit changes,
   restart at part 1 with the new smallest limit; never raise a binding limit
   to keep the old sequence.

Reader parts are already bounded. Execute the supplied reader command unchanged;
do not wrap it in `--run`, add `--publish-full`, or save its output.

A reader error leaves the read incomplete, even if its diagnostic cannot fit.
Correct a visible cause and restart at part 1. Do not repeat an unchanged failed
call or raise a binding limit. Otherwise report the unread document and stop
dependent work.
Do not alter or copy the input, truncate it or recover omitted text after an
oversized read.

To check a supplied expected SHA-256, use the same checker with
`--file "<artifact>" --sha256 --max-output-tokens <limit>` and compare its
`sha256` with the supplied value. A mismatch or error stops dependent work.
Then read the same unchanged file from `--part 1` through `last` with the same
limit. Hash verification is not reading; ordinary sources need no extra hash check.
