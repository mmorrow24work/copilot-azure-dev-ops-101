# Safe Copilot workflow

Use Copilot in a controlled loop:

1. **Inspect**: ask it to read the issue, relevant files and repository instructions.
2. **Plan**: request assumptions, steps, risks and validation before edits.
3. **Implement**: make one reviewable change.
4. **Validate**: execute tests and Azure DevOps queries yourself.
5. **Review**: inspect the diff and logs for secrets and unsupported claims.
6. **Record**: capture evidence and limitations.

## Standard prompt

```text
Read .github/copilot-instructions.md and the current lesson. Do not change files yet.
Explain the intended Azure DevOps outcome, identify prerequisites and risks, and propose
an implementation plan with deterministic validation. Never invent command output and
never request or expose credentials.
```
