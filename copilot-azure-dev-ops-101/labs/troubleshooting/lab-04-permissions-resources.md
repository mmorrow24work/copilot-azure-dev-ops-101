# Permissions and protected resources

## Objective

Diagnose the failure from evidence rather than asking Copilot to guess.

## Prerequisites

- A disposable feature branch and pipeline
- Permission to queue runs and view logs
- A known-good run to use as a baseline

## Fault-injection exercise

Use a pipeline that references a variable group or environment not yet authorised for it. Queue the run and inspect the resource-authorisation message. Grant access only to the named pipeline, then rerun.

If your account automatically has access, ask a project administrator to demonstrate the resource permission page rather than weakening organisation-wide controls.

## Diagnostic procedure

1. Open the run summary and select the first failed task.
2. Read the raw log around the first error, not only the final exit code.
3. Record the stage, job, task, agent image, commit and build ID.
4. For more detail, queue one run with **Enable system diagnostics**, or temporarily set `system.debug: true`.
5. Redact diagnostic content before sharing it with Copilot.
6. Ask Copilot for two ranked hypotheses and a validation for each.
7. Change one cause at a time and rerun.

## Validation

- The original run records the precise protected resource that blocked execution.
- Access is granted to the selected pipeline only.
- `Grant access permission to all pipelines` remains disabled unless justified.
- The rerun proceeds beyond resource authorisation.

## Evidence

- Failed and successful run links or IDs
- The first relevant error line, redacted
- Hypothesis and test
- Minimal correction
- Proof that the intentional fault was removed

## Cleanup

Remove temporary policies/resources created only for the lab and delete fault-injection branches after merging or abandoning the exercise.
