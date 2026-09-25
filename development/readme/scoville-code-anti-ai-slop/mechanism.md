## How it works

- Establish the observable outcome, responsible code, introduced risks and cheapest decisive check before substantial editing.
- Read the owner and relevant callers, contracts and tests. Expand only when the evidence points elsewhere.
- Fix the cause in the existing implementation. Avoid parallel paths, speculative abstractions and unrelated cleanup.
- Test the changed behavior. A successful build or mocked integration proves only what it exercised.
- Investigate failed checks without weakening required guarantees. Change obsolete assertions only when an explicitly authorized contract change requires it. After two unsuccessful corrections of the same cause, reassess the approach.
- Inspect the complete change and report observed results and remaining gaps. Stop checking when further evidence would not change the decision.
