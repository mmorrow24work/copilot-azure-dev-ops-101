# Day 39: CLI automation and idempotency

## Purpose

Write repeatable automation that detects existing state. This lesson uses Copilot to support reasoning and drafting while Azure DevOps remains the system being learned and validated.

## Learning objectives

By the end of this lesson, you can:

- write repeatable automation that detects existing state;
- complete a scoped Azure DevOps lab safely;
- prove the result with repeatable validation;
- explain where Copilot helped and where human review was required.

## Prerequisites

- Completed previous days or equivalent knowledge
- A private Azure DevOps sandbox and configured `$env:ADO_ORG` / `$env:ADO_PROJECT`
- Git, PowerShell 7, Python and Azure CLI with the Azure DevOps extension
- No production or customer credentials

## Read

- [Microsoft documentation](https://learn.microsoft.com/azure/devops/?view=azure-devops)
- Re-read [safe Copilot workflow](../../docs/COPILOT-WORKFLOWS.md)

## Ask Copilot

```text
Read .github/copilot-instructions.md and this Day 39 lesson. Act as an Azure DevOps
learning coach. First explain the intended outcome and list assumptions. Then propose the
smallest safe implementation plan and exact validation. Do not invent command output,
do not request secrets, and identify any step that must be completed in the portal.
```

Before using generated commands, compare them with `az --help`, `az devops --help`, or the linked Microsoft documentation.

## Azure DevOps lab

**Scenario:** Create `scripts/bootstrap-project.ps1` that checks before creating a project/repo.

1. Check your context:

```powershell
az devops configure --list
az devops project show --project $env:ADO_PROJECT --query "{name:name,state:state,visibility:visibility}" -o table
```

2. Ask Copilot to explain the change and its security boundary.
3. Carry out the day-specific task:

```powershell
# Use az devops project show and az repos show; handle not-found results, terminate on errors and never log credentials.
```

4. Review the portal, CLI output and local Git diff before continuing.
5. Save only redacted evidence. Never paste a PAT, bearer token or credential-bearing URL.

## Validation

**Pass condition:** Run the script twice. The second run must report existing resources and make no destructive change.

Also run the following local checks where applicable:

```powershell
git status --short
python -m pytest -q
```

If a command is not relevant to today's change, record `not applicable` rather than manufacturing a successful result.

## Evidence to retain

- Resource or work item IDs, with sensitive organisation information redacted if needed
- Command names and exit status
- Link to the pipeline run, PR, work item or environment where applicable
- A short statement of what was genuinely tested
- Any limitation, licence restriction or portal-only step

## Troubleshooting

1. Run the relevant command with `--help` and verify organisation/project defaults.
2. Check access level and permissions separately. A licence/access level does not automatically grant a permission.
3. For 401/403 responses, do not broaden permissions blindly. Identify the exact missing scope or role.
4. For pipelines, inspect the first failing task and its raw log before asking Copilot for a fix.
5. Re-run validation after every correction and record what changed.

## Cleanup

Remove only disposable resources created specifically for this lab. Keep shared project, repo, work items and pipeline history needed by later lessons. Clear temporary token environment variables and stop local containers or port-forwards.

## Self-check

1. What is the primary outcome of this day?
2. What must never be placed in repository evidence?
3. What makes the lab complete?
4. How should Copilot output be treated?

<details>
<summary>Answers</summary>

1. Write repeatable automation that detects existing state
2. Tokens, private keys, credential files, customer data or other sensitive identifiers.
3. A successful deterministic validation, not merely generated commands or plausible output.
4. As a draft to review and validate against documentation and the real Azure DevOps environment.

</details>

## Teach-back

In three to five minutes, explain **CLI automation and idempotency**, demonstrate the validation evidence, describe one failure mode, and state one way Copilot output could have been misleading without verification.
