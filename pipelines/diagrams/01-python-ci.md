# Python CI

This diagram uses the standard fenced `mermaid` block supported by GitHub Markdown and current Azure DevOps Markdown. It intentionally uses conservative flowchart syntax.

```mermaid
flowchart TD
    A[Push to main] --> B[Checkout source]
    B --> C[Select Python]
    C --> D[Install dependencies]
    D --> E[Run pytest]
    E --> F[Create JUnit XML]
    F --> G[Publish test results]
    G --> H{Tests passed}
    H -->|Yes| I[Run succeeds]
    H -->|No| J[Run fails with test evidence]
```

Related YAML: [`../examples/01-python-ci.yml`](../examples/01-python-ci.yml)
