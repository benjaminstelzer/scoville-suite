## How it works

- Check that the request needs materially different mechanisms, then freeze the factual brief and constraints.
- Generate candidates separately from landscape research and criticism when the host supports independent agents.
- Without delegation, use one generation pass and one landscape pass, and state that independence was unavailable.
- Group surface variants by mechanism, challenge weak assumptions and compare against inspected approaches.
- Return up to three directions, or two in Compact mode, with benefits, risks and cheap falsifiers. Stop before selection or implementation.

```mermaid
flowchart TD
    B["Coordinator: fix the brief and constraints"]
    subgraph P["Parallel agents: no shared findings during generation"]
        G1["Idea agent 1: one approach"]
        G2["Idea agent 2: a different approach"]
        GN["More idea agents if capacity allows"]
        L["Research agent: inspect existing approaches"]
    end
    B --> G1 & G2 & GN & L
    G1 & G2 & GN & L --> C["Coordinator: merge variants and compare with evidence"]
    C --> K{"Capacity for an independent critic?"}
    K -->|Yes| R["Critic agent: challenge assumptions and weak directions"]
    K -->|No| F["Coordinator: apply the same checks"]
    R & F --> S["Coordinator: shortlist with risks and cheap tests"]
    S --> H["Human chooses the direction"]
```
