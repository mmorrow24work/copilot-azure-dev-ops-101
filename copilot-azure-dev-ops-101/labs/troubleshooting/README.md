# Azure Pipelines troubleshooting labs

These fault-injection labs complement Days 17 to 30. Work in a feature branch and a disposable pipeline. Each lab follows the same diagnostic loop:

1. reproduce the failure;
2. identify the first failed stage, job and task;
3. inspect the raw task log before changing YAML;
4. form one testable hypothesis;
5. make the smallest correction;
6. rerun and preserve evidence;
7. revert intentional faults.

## Labs

- [Lab 1: YAML and task failures](lab-01-yaml-task-failures.md)
- [Lab 2: Triggers and PR validation](lab-02-triggers-pr-validation.md)
- [Lab 3: Variables, expressions and conditions](lab-03-variables-conditions.md)
- [Lab 4: Permissions and protected resources](lab-04-permissions-resources.md)
- [Lab 5: Artifacts and stage dependencies](lab-05-artifacts-dependencies.md)
- [Lab 6: Agents, tools and environment differences](lab-06-agents-tools.md)

Do not paste complete logs into Copilot until they are checked for tokens, URLs, email addresses and other sensitive data.
