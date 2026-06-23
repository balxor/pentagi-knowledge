---
cwe_id: CWE-266
name: Incorrect Privilege Assignment
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/266.html
tags: [mitre-cwe, weakness, CWE-266]
---

# CWE-266 - Incorrect Privilege Assignment

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-266](https://cwe.mitre.org/data/definitions/266.html)

## Description
A product incorrectly assigns a privilege to a particular actor, creating an unintended sphere of control for that actor.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

## Related weaknesses
- CWE-269 (ChildOf)
- CWE-286 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-1999-1193**: untrusted user placed in unix "wheel" group
- **CVE-2005-2741**: Product allows users to grant themselves certain rights that can be used to escalate privileges.
- **CVE-2005-2496**: Product uses group ID of a user instead of the group, causing it to run with different privileges. This is resultant from some other unknown issue.
- **CVE-2004-0274**: Product mistakenly assigns a particular status to an entity, leading to increased privileges.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/266.html
