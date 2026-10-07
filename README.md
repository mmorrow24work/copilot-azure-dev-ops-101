# Copilot Azure DevOps 101

A 45-day, hands-on introduction to **Azure DevOps Services**, delivered with **GitHub Copilot** as a pair engineer. Azure DevOps is the subject; Copilot helps learners plan, explain, generate, review and troubleshoot, but every result must be validated.

## Learning model

Each weekday takes approximately 45 to 90 minutes and includes:

1. focused learning objectives;
2. Microsoft documentation;
3. a Copilot planning or review prompt;
4. an Azure DevOps lab;
5. deterministic validation and evidence;
6. a four-question self-check;
7. a short teach-back.

## Start here

1. Read [environment setup](docs/ENVIRONMENTS.md).
2. Read [safe Copilot workflow](docs/COPILOT-WORKFLOWS.md).
3. Start at [the curriculum index](curriculum/README.md).
4. Work only in a disposable/private sandbox organisation and project.

## Sample application

```powershell
python -m pip install -r requirements-dev.txt
pytest -q
```

## Important safety boundary

Never commit PATs, service-principal secrets, SSH private keys, cloud credential files or customer information. Prefer Microsoft Entra authentication, workload identity federation and narrowly scoped permissions.

## Detailed pipeline examples

See [pipelines/README.md](pipelines/README.md) and the [technical accuracy review](docs/TECHNICAL-ACCURACY-REVIEW.md).

## Assessment and diagnostics

- [Azure Pipelines troubleshooting labs](labs/troubleshooting/README.md)
- [Capstone assessment rubric](docs/CAPSTONE-ASSESSMENT-RUBRIC.md)
- [Pipeline Mermaid diagrams](pipelines/diagrams/01-python-ci.md)
