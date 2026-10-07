# Triggers and PR validation

## Objective

Diagnose the failure from evidence rather than asking Copilot to guess.

## Prerequisites

- A disposable feature branch and pipeline
- Permission to queue runs and view logs
- A known-good run to use as a baseline

## Fault-injection exercise

Create a pipeline pointing to `pipelines/examples/08-pr-validation.yml`. Open a pull request before adding a branch policy and observe that no validation run starts. Add the pipeline as a build-validation policy on `main`, update the source branch, and observe the new validation run.

Do not "fix" this by adding a YAML `pr:` block to an Azure Repos Git pipeline.

## Diagnostic procedure

1. Open the run summary and select the first failed task.
2. Read the raw log around the first error, not only the final exit code.
3. Record the stage, job, task, agent image, commit and build ID.
4. For more detail, queue one run with **Enable system diagnostics**, or temporarily set `system.debug: true`.
5. Redact diagnostic content before sharing it with Copilot.
6. Ask Copilot for two ranked hypotheses and a validation for each.
7. Change one cause at a time and rerun.

## Validation

- A PR without build validation does not queue the `trigger: none` pipeline.
- After the build-validation policy is added, a PR update queues it.
- The policy reports success or failure on the PR.
- The pipeline YAML still has `trigger: none` and no `pr:` block.

## Evidence

- Failed and successful run links or IDs
- The first relevant error line, redacted
- Hypothesis and test
- Minimal correction
- Proof that the intentional fault was removed

## Cleanup

Remove temporary policies/resources created only for the lab and delete fault-injection branches after merging or abandoning the exercise.
