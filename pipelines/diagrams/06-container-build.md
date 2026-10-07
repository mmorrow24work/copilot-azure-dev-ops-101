# Container build

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart TD
    A[Checkout source] --> B[Docker build]
    B --> C[Tag with Build ID]
    C --> D[Inspect image]
    D --> E[Write metadata JSON]
    E --> F[Publish metadata artifact]
```

Related YAML: [`../examples/06-container-build.yml`](../examples/06-container-build.yml)
