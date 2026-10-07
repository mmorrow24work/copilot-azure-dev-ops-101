# Variables, expressions and conditions

## Objective

Diagnose the failure from evidence rather than asking Copilot to guess.

## Prerequisites

- A disposable feature branch and pipeline
- Permission to queue runs and view logs
- A known-good run to use as a baseline

## Fault-injection exercise

Start from `02-variables-and-conditions.yml`. Introduce each fault separately:

1. Misspell `Build.SourceBranch`.
2. Compare it with `main` instead of `refs/heads/main`.
3. Reference `$(pythonVerison)` instead of `$(pythonVersion)`.

Use logs to distinguish an empty/mis-evaluated condition from an unresolved macro value.

## Diagnostic procedure

1. Open the run summary and select the first failed task.
2. Read the raw log around the first error, not only the final exit code.
3. Record the stage, job, task, agent image, commit and build ID.
4. For more detail, queue one run with **Enable system diagnostics**, or temporarily set `system.debug: true`.
5. Redact diagnostic content before sharing it with Copilot.
6. Ask Copilot for two ranked hypotheses and a validation for each.
7. Change one cause at a time and rerun.

## Validation

- The learner explains compile-time, macro and runtime evaluation boundaries.
- The main-only step runs on `refs/heads/main` and skips elsewhere.
- No secret variable is printed.
- The repaired pipeline finishes successfully.

## Evidence

- Failed and successful run links or IDs
- The first relevant error line, redacted
- Hypothesis and test
- Minimal correction
- Proof that the intentional fault was removed

## Cleanup

Remove temporary policies/resources created only for the lab and delete fault-injection branches after merging or abandoning the exercise.
