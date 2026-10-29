## How it was developed

Real transfers exposed lost blockers, decisions and ownership of unfinished
changes. Those cases shaped a compact template that preserves what the next
session needs to continue.

In current Codex tests with `gpt-6.1-sol / low`, an actual producer preserved
the original template, receiver instructions and outer fence, transferred the
task's authority and original capture evidence, and redacted the test secret.
A fresh receiver used that unchanged prompt and ran the remaining verifier
exactly once. The original effect was preserved. An incorrect assumption about
the original output's format was corrected before the verifier ran.

The receiver also used installed host rules. These cases demonstrate the
task, authority and evidence transfer, not isolated loading of candidate Code
rules. They do not establish no-progress recovery, tight-limit file delivery,
installed discovery or current behavior in Claude Code or other hosts.
