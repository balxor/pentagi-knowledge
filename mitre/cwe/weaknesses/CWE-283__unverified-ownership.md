---
cwe_id: CWE-283
name: Unverified Ownership
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/283.html
tags: [mitre-cwe, weakness, CWE-283]
---

# CWE-283 - Unverified Ownership

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-283](https://cwe.mitre.org/data/definitions/283.html)

## Description
The product does not properly verify that a critical resource is owned by the proper entity.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design**: Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

## Related weaknesses
- CWE-282 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-0178**: Program does not verify the owner of a UNIX socket that is used for sending a password.
- **CVE-2004-2012**: Owner of special device not checked, allowing root.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/283.html
