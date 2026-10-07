# Multi-stage artifact flow

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart LR
    A[Build stage] --> B[Build Python package]
    B --> C[Publish python-package artifact]
    C --> D[Validate stage]
    D --> E[Download artifact]
    E --> F[Install wheel]
    F --> G[Smoke test installed package]
```

Related YAML: [`../examples/03-multi-stage-artifact.yml`](../examples/03-multi-stage-artifact.yml)
