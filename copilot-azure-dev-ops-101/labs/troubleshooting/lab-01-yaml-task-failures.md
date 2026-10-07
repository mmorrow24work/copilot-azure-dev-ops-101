# YAML and task failures

## Objective

Diagnose the failure from evidence rather than asking Copilot to guess.

## Prerequisites

- A disposable feature branch and pipeline
- Permission to queue runs and view logs
- A known-good run to use as a baseline

## Fault-injection exercise

Start from `pipelines/examples/01-python-ci.yml`. Create two separate failures:

1. Change `requirements-dev.txt` to a nonexistent filename.
2. After diagnosing that failure, restore the filename and change the pytest path to a nonexistent directory.

For each failure, queue the pipeline and identify whether parsing, dependency installation or test execution failed.

## Diagnostic procedure

1. Open the run summary and select the first failed task.
2. Read the raw log around the first error, not only the final exit code.
3. Record the stage, job, task, agent image, commit and build ID.
4. For more detail, queue one run with **Enable system diagnostics**, or temporarily set `system.debug: true`.
5. Redact diagnostic content before sharing it with Copilot.
6. Ask Copilot for two ranked hypotheses and a validation for each.
7. Change one cause at a time and rerun.

## Validation

- The run reaches the expected failing task.
- The raw log identifies the missing file or invalid test path.
- The corrected run publishes test results and succeeds.
- The final diff contains no intentional fault.

## Evidence

- Failed and successful run links or IDs
- The first relevant error line, redacted
- Hypothesis and test
- Minimal correction
- Proof that the intentional fault was removed

## Cleanup

Remove temporary policies/resources created only for the lab and delete fault-injection branches after merging or abandoning the exercise.
