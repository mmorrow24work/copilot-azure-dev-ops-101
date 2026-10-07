# Reusable test template

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart LR
    A[Consumer pipeline] --> B[Pass typed parameters]
    B --> C[Python test steps template]
    C --> D[Select Python]
    D --> E[Install requirements]
    E --> F[Run pytest]
    F --> G[Publish results]
```

Related YAML: [`../examples/09-template-consumer.yml`](../examples/09-template-consumer.yml)
