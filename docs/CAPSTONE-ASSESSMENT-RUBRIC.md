# Capstone assessment rubric

## Assessment brief

Deliver one small feature through a governed Azure DevOps lifecycle: work item, branch, tested change, pull request, policy-gated validation, versioned artifact, deployment to `training-dev`, rollback notes, operational evidence and a 3-5 minute teach-back.

## Scoring

Total: **100 points**. A submission must also pass every mandatory gate.

### 1. Planning and traceability: 10 points

- **9-10**: Clear acceptance criteria; correctly typed work items; parent/child relationships; branch, commits and PR link back to the requirement.
- **7-8**: Traceability is complete but one link or criterion is weak.
- **4-6**: Work exists but links or outcomes are incomplete.
- **0-3**: Little usable planning evidence.

### 2. Source control and pull request discipline: 10 points

- **9-10**: Short-lived branch, meaningful commits, focused PR, review evidence and no direct push to protected `main`.
- **7-8**: Sound workflow with minor hygiene issues.
- **4-6**: PR exists but commit/review quality is weak.
- **0-3**: Changes bypass the expected review flow.

### 3. Application quality and automated tests: 15 points

- **13-15**: Behaviour is correct, tests cover success and relevant edge cases, and results are deterministic.
- **10-12**: Correct implementation with adequate tests.
- **6-9**: Partial tests or fragile behaviour.
- **0-5**: Important behaviour is untested or failing.

### 4. Azure Pipelines design: 20 points

- **17-20**: Valid YAML; explicit triggers; clear stages/jobs; reusable logic; pinned task majors; test publication; useful artifacts; correct conditions and failure behaviour.
- **13-16**: Reliable pipeline with small design gaps.
- **8-12**: Pipeline works but lacks evidence, reuse or clear boundaries.
- **0-7**: Pipeline is unreliable, unsafe or cannot complete.

### 5. Deployment, environment and rollback: 15 points

- **13-15**: Deployment job records environment history, artifact provenance is preserved, validation is objective and rollback is rehearsed.
- **10-12**: Successful deployment and documented rollback with minor gaps.
- **6-9**: Deployment works but provenance or rollback evidence is weak.
- **0-5**: No repeatable deployment or recovery path.

### 6. Security and governance: 15 points

- **13-15**: Least privilege, scoped resources, no exposed secrets, protected branch, safe evidence, appropriate identity method and documented risk decisions.
- **10-12**: Controls are mostly correct with minor weaknesses.
- **6-9**: Some controls exist but permissions or secret handling need work.
- **0-5**: Credential exposure, unjustified broad access or missing controls.

### 7. Troubleshooting and operational evidence: 10 points

- **9-10**: Reproduces and diagnoses a failure systematically, identifies the first relevant error, applies a minimal fix and proves recovery.
- **7-8**: Correct diagnosis and recovery with incomplete evidence.
- **4-6**: Fix works but root cause analysis is weak.
- **0-3**: Trial-and-error changes without evidence.

### 8. Documentation and teach-back: 5 points

- **5**: Concise, accurate runbook and clear demonstration covering outcome, validation, risk and lessons learned.
- **4**: Clear documentation with a minor omission.
- **2-3**: Understandable but incomplete.
- **0-1**: Cannot be repeated or explained.

## Mandatory gates

A submission cannot pass if any of these apply:

- a committed or exposed credential;
- unresolved failing required tests;
- no evidence connecting the requirement to the PR;
- deployment from unreviewed source when branch policy is required;
- no objective deployment validation;
- destructive or production activity outside the agreed sandbox;
- fabricated command output or validation evidence.

## Grade bands

- **85-100**: Distinction
- **70-84**: Merit
- **60-69**: Pass
- **Below 60**: Not yet competent

## Assessor evidence checklist

- Work item hierarchy and acceptance criteria
- Branch and commit history
- PR discussion and policy results
- Pipeline run and published tests
- Versioned artifact and checksum/version evidence
- Environment deployment history
- Security/governance review
- Failure diagnosis and successful rerun
- Rollback evidence
- Teach-back recording or live demonstration notes
