# Infrastructure as Code validation

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart TD
    A[Checkout IaC] --> B[Terraform format check]
    B --> C[Init without backend]
    C --> D[Terraform validate]
    D --> E{Valid}
    E -->|Yes| F[Validation succeeds]
    E -->|No| G[Correct IaC and rerun]
    F --> H[No apply performed]
```

Related YAML: [`../examples/07-iac-validation.yml`](../examples/07-iac-validation.yml)
