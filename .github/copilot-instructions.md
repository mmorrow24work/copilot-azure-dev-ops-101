# Purpose

This repository teaches Azure DevOps Services through verified, hands-on labs. GitHub Copilot is the learning assistant, not the source of truth. Azure DevOps, not GitHub, is the primary subject.

# Audience and assumptions

- Write for engineers, architects and technical learners who may be new to Azure DevOps.
- Assume a private sandbox organisation and project, Windows PowerShell 7, Git, Python 3 and Azure CLI.
- Use Azure DevOps Services unless a lesson explicitly discusses Azure DevOps Server.
- Use British English and define acronyms on first use.

# Non-negotiable safety rules

- Never create, request, print or commit real secrets, PATs, private keys, credential files, customer data or internal URLs.
- Prefer Microsoft Entra tokens and workload identity federation over long-lived PATs or service-principal secrets.
- Use least privilege and scope service connections to selected pipelines.
- Do not grant global or organisation-wide permissions merely to make a lab work.
- Do not perform destructive operations unless the lesson explicitly includes a scoped cleanup step.
- Mark commands requiring placeholders and explain each placeholder.

# Daily lesson contract

Every daily lesson must contain:

1. Purpose and learning objectives
2. Prerequisites
3. Microsoft documentation reading
4. Copilot prompt with explicit constraints
5. Numbered hands-on Azure DevOps lab
6. Copy-pasteable PowerShell or YAML where appropriate
7. Deterministic validation commands and expected outcomes
8. Evidence to retain
9. Troubleshooting guidance
10. Cleanup
11. Four-question self-check with answers hidden below a details block
12. A 3-5 minute teach-back prompt

# Technical standards

- Validate Azure CLI commands against `az <group> --help` before presenting them as tested.
- Keep Azure DevOps CLI limitations visible; use portal or REST API steps where no CLI command exists.
- Use `api-version` on Azure DevOps REST calls.
- Pipelines must publish test results and preserve useful evidence.
- Use `python -m pip` instead of bare `pip`.
- Shell and PowerShell scripts must fail on errors and be safe to rerun where practical.
- YAML must use spaces, explicit task versions and descriptive display names.
- Do not claim a lab succeeded unless validation was run.

# Generated curriculum

Daily pages under `curriculum/week-*` are source-controlled learning assets. When changing them:

- preserve the standard section order;
- keep each day within a 45-90 minute scope;
- keep labs incremental and compatible with the running sample project;
- avoid duplicating secrets or live identifiers in evidence;
- update the week index if the topic or outcome changes.

# Completion report

After edits, report:

- files changed;
- checks executed;
- test and validation results;
- assumptions and anything not tested;
- security-relevant decisions.
