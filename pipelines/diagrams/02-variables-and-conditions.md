# Variables and conditions

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart TD
    A[Pipeline starts] --> B[Load variables]
    B --> C[Evaluate runtime isMain]
    C --> D[Run tests]
    D --> E{Succeeded and main branch}
    E -->|Yes| F[Run main-only step]
    E -->|No| G[Skip main-only step]
```

Related YAML: [`../examples/02-variables-and-conditions.yml`](../examples/02-variables-and-conditions.yml)
