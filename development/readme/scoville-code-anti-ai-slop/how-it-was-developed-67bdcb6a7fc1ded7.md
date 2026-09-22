## How it was developed

Code has grown through real engineering work. I read complete task histories
to find where an agent loses the requested outcome, works around the wrong
cause or keeps checking something it has already established. Repeated searches
and oversized tool output matter for the same reason: they consume context
without necessarily helping to fix the problem.

Those observations become instruction changes and regression cases. I also use
SkillOpt to explore shorter instructions. The
[development history](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/blob/b3509d8e6fc5f485e1b3274b600de7f717aea396/CHANGELOG.md)
includes an adopted compression and a later proposal I rejected because it
still missed a required concern. Shorter is useful when the required behavior
survives.

