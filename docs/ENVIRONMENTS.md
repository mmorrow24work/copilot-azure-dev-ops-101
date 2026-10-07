# Environment setup

Use a personal or authorised sandbox, not a production/customer organisation.

## Required

- Azure DevOps Services organisation with permission to create a private project
- Git 2.x
- PowerShell 7
- Python 3.11 or later
- Azure CLI plus the `azure-devops` extension
- GitHub Copilot subscription and a supported client or Copilot CLI

## PowerShell environment variables

```powershell
$env:ADO_ORG = "https://dev.azure.com/<organisation>"
$env:ADO_PROJECT = "copilot-ado-101"
```

Do not store tokens in repository files. Prefer `az login`; use a short-lived PAT only where required and clear it after the task.

## Install and verify

```powershell
az --version
az extension add --name azure-devops
az extension show --name azure-devops -o table
git --version
python --version
```
