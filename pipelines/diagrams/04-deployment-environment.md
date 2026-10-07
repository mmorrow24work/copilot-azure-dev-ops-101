# Deployment environment

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart TD
    A[Pipeline run] --> B[Deployment job]
    B --> C[Target training-dev environment]
    C --> D[Copy approved artifact]
    D --> E[Calculate checksum]
    E --> F[Record deployment history]
```

Related YAML: [`../examples/04-deployment-environment.yml`](../examples/04-deployment-environment.yml)
