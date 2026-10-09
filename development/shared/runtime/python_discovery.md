Reuse an already verified interpreter meeting this Skill's Python 3.11+
requirement. Otherwise check `py -3`
on Windows or `python3` elsewhere; try `python` if needed. Choose it locally,
without asking the user. Verify its version before the first helper operation.
Use that executable wherever examples say `python` or `<verified-python>`,
including Python commands after `--run --`.
Report a missing runtime only when no suitable installed interpreter is found.

For direct helper calls in PowerShell, quote the interpreter path and prefix it
with `&`. Run generated commands unchanged in the current tool shell; do not
replace their process or argument handling with a direct call.
