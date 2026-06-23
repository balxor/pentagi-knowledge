---
cwe_id: CWE-270
name: Privilege Context Switching Error
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-17, CAPEC-30, CAPEC-35]
url: https://cwe.mitre.org/data/definitions/270.html
tags: [mitre-cwe, weakness, CWE-270]
---

# CWE-270 - Privilege Context Switching Error

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-270](https://cwe.mitre.org/data/definitions/270.html)

## Description
The product does not properly manage privileges while it is switching between different contexts that have different privileges or spheres of control.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **Architecture and Design**: Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

## Related attack patterns (CAPEC)
- [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
- [CAPEC-30](https://capec.mitre.org/data/definitions/30.html)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)

## Related weaknesses
- CWE-269 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1688**: Web browser cross domain problem when user hits "back" button.
- **CVE-2003-1026**: Web browser cross domain problem when user hits "back" button.
- **CVE-2002-1770**: Cross-domain issue - third party product passes code to web browser, which executes it in unsafe zone.
- **CVE-2005-2263**: Run callback in different security context after it has been changed from untrusted to trusted. * note that "context switch before actions are completed" is one type of problem that happens frequently, espec. in browsers.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/270.html
