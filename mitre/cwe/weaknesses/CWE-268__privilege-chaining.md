---
cwe_id: CWE-268
name: Privilege Chaining
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/268.html
tags: [mitre-cwe, weakness, CWE-268]
---

# CWE-268 - Privilege Chaining

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-268](https://cwe.mitre.org/data/definitions/268.html)

## Description
Two distinct privileges, roles, capabilities, or rights can be combined in a way that allows an entity to perform unsafe actions that would not be allowed without that combination.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

## Related weaknesses
- CWE-269 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1736**: Chaining of user rights.
- **CVE-2002-1772**: Gain certain rights via privilege chaining in alternate channel.
- **CVE-2005-1973**: Application is allowed to assign extra permissions to itself.
- **CVE-2003-0640**: "operator" user can overwrite usernames and passwords to gain admin privileges.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/268.html
