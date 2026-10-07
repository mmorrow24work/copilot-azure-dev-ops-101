# Azure Repos PR validation

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart TD
    A[Open or update pull request] --> B[Branch policy evaluates]
    B --> C[Queue validation pipeline]
    C --> D[Checkout proposed merge]
    D --> E[Install dependencies]
    E --> F[Run tests]
    F --> G[Publish results]
    G --> H{Policy successful}
    H -->|Yes| I[Merge can proceed]
    H -->|No| J[Merge blocked]
```

Related YAML: [`../examples/08-pr-validation.yml`](../examples/08-pr-validation.yml)
