## How it was developed

UI developed through interface work and comparisons of how agents use the
instructions. One recurring problem was checking the rendered page before
understanding which component or CSS rule owned it. Another was interrupting
related edits with repeated screenshots. The [changelog](CHANGELOG.md) follows
the changes to source inspection and validation after a completed batch.

I read task histories alongside the interface to see which checks help and
which merely repeat work. Earlier
[optimization runs](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/blob/3b054c35187437743e6994aad1a2d42bac228e53/CHANGELOG.md)
also explored selective loading and the boundary with Design. When SkillOpt
found no better candidate, I kept the existing instructions.

