# Artifacts and stage dependencies

## Objective

Diagnose the failure from evidence rather than asking Copilot to guess.

## Prerequisites

- A disposable feature branch and pipeline
- Permission to queue runs and view logs
- A known-good run to use as a baseline

## Fault-injection exercise

Start from `03-multi-stage-artifact.yml`. Introduce these faults one at a time:

1. Download an artifact using the wrong name.
2. Remove `dependsOn: Build` from Validate.
3. Publish from an empty or incorrect directory.

Inspect the timeline and downloaded workspace to isolate naming, ordering and path errors.

## Diagnostic procedure

1. Open the run summary and select the first failed task.
2. Read the raw log around the first error, not only the final exit code.
3. Record the stage, job, task, agent image, commit and build ID.
4. For more detail, queue one run with **Enable system diagnostics**, or temporarily set `system.debug: true`.
5. Redact diagnostic content before sharing it with Copilot.
6. Ask Copilot for two ranked hypotheses and a validation for each.
7. Change one cause at a time and rerun.

## Validation

- The artifact name is identical at publish and download points.
- Validate cannot run before a successful Build.
- The artifact contains the expected package files.
- The installed artifact passes its smoke test.

## Evidence

- Failed and successful run links or IDs
- The first relevant error line, redacted
- Hypothesis and test
- Minimal correction
- Proof that the intentional fault was removed

## Cleanup

Remove temporary policies/resources created only for the lab and delete fault-injection branches after merging or abandoning the exercise.
