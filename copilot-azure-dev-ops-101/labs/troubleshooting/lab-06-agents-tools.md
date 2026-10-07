# Agents, tools and environment differences

## Objective

Diagnose the failure from evidence rather than asking Copilot to guess.

## Prerequisites

- A disposable feature branch and pipeline
- Permission to queue runs and view logs
- A known-good run to use as a baseline

## Fault-injection exercise

Use a Microsoft-hosted Ubuntu agent. Add a diagnostic step that reports the operating system, working directories and tool versions. Then request a deliberately unavailable tool version or use a Windows-only command in a Bash step. Diagnose the failure without changing agent permissions.

Restore a portable command or explicitly select the correct agent image.

## Diagnostic procedure

1. Open the run summary and select the first failed task.
2. Read the raw log around the first error, not only the final exit code.
3. Record the stage, job, task, agent image, commit and build ID.
4. For more detail, queue one run with **Enable system diagnostics**, or temporarily set `system.debug: true`.
5. Redact diagnostic content before sharing it with Copilot.
6. Ask Copilot for two ranked hypotheses and a validation for each.
7. Change one cause at a time and rerun.

## Validation

- Logs identify the agent OS and relevant tool version.
- The learner distinguishes a missing tool from a repository defect.
- The corrected pipeline uses an appropriate image or setup task.
- Diagnostic output contains no environment secrets.

## Evidence

- Failed and successful run links or IDs
- The first relevant error line, redacted
- Hypothesis and test
- Minimal correction
- Proof that the intentional fault was removed

## Cleanup

Remove temporary policies/resources created only for the lab and delete fault-injection branches after merging or abandoning the exercise.
