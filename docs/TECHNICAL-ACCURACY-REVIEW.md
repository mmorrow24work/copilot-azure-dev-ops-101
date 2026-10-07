# Technical accuracy review

Review date: 7 October 2026.

## Corrections applied

1. Removed the YAML `pr:` trigger from the root pipeline. Azure Repos Git uses a build-validation branch policy for pull-request validation.
2. Added an explicit CI trigger for `main`; this avoids reliance on the organisation setting for implied YAML CI triggers.
3. Added a dedicated PR-validation YAML with `trigger: none`, intended to be queued by a branch policy.
4. Clarified that `ManualValidation@1` runs in an agentless `pool: server` job, separate from environment approvals/checks.
5. Distinguished pipeline artifacts from Azure Artifacts package feeds.
6. Added deployment-job examples that create environment deployment history and use `runOnce`.
7. Added typed template parameters and examples of compile-time `${{ }}`, macro `$( )`, and runtime `$[ ]` expressions.
8. Kept cloud deployment optional and prefers workload identity federation. No lab requires a committed cloud credential.
9. Marked Test Plans exercises as licence-dependent and avoids claiming that pytest publication alone updates manual Test Case work items.
10. Replaced or labelled portal-only/prose actions so they are not presented as executable PowerShell.

## Important caveats

- Microsoft-hosted parallel jobs might require a grant or paid parallelism for some private projects.
- Test Plans typically requires an appropriate access level/licence.
- Environment approvals/checks are configured on the protected resource in the web portal and are not defined inside pipeline YAML.
- Availability of Azure DevOps CLI subcommands varies; learners must check `az <group> --help` and use the portal or REST API where required.
- Azure DevOps YAML is evaluated by the service. A generic YAML parser can check structure but cannot fully validate task inputs, permissions, service connections or tenant-specific resources.
