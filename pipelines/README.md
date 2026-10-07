# Detailed Azure Pipelines examples

These examples are ordered to match Days 17 to 30. Copy an example to the repository root or point a new pipeline at it. Azure Repos Git does **not** honour YAML `pr:` triggers; configure build validation on the target branch instead.

- `examples/01-python-ci.yml`: CI, pytest and JUnit publication
- `examples/02-variables-and-conditions.yml`: variables, runtime expressions and conditions
- `examples/03-multi-stage-artifact.yml`: Build and Validate stages with pipeline artifacts
- `examples/04-deployment-environment.yml`: deployment job and environment history
- `examples/05-manual-validation.yml`: agentless manual validation between stages
- `examples/06-container-build.yml`: Docker build, test and artifact metadata
- `examples/07-iac-validation.yml`: Terraform formatting and validation without apply
- `examples/08-pr-validation.yml`: PR-only body used by an Azure Repos branch policy
- `templates/python-test-steps.yml`: reusable typed steps template
- `examples/09-template-consumer.yml`: template consumer example

## Validate in Azure DevOps

Create the pipeline once, run it manually, then add it to `main` under **Repos > Branches > Branch policies > Build validation** where PR validation is required. Keep service connections scoped to selected pipelines.

## Diagrams

Each numbered example has a matching Markdown Mermaid diagram under [`diagrams/`](diagrams/). The files use standard fenced `mermaid` blocks and conservative `flowchart` syntax.

## Troubleshooting practice

Use the fault-injection [Azure Pipelines troubleshooting labs](../labs/troubleshooting/README.md) after the worked examples.
