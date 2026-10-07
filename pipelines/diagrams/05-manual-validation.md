# Manual validation

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart TD
    A[Build stage] --> B[Agentless approval stage]
    B --> C{ManualValidation decision}
    C -->|Approve| D[Deploy stage]
    C -->|Reject or timeout| E[Run stops]
    D --> F[Simulated deployment]
```

Related YAML: [`../examples/05-manual-validation.yml`](../examples/05-manual-validation.yml)
