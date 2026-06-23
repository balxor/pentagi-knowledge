---
cwe_id: CWE-286
name: Incorrect User Management
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/286.html
tags: [mitre-cwe, weakness, CWE-286]
---

# CWE-286 - Incorrect User Management

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-286](https://cwe.mitre.org/data/definitions/286.html)

## Description
The product does not properly manage a user within its environment.

## Extended description
Users can be assigned to the wrong group (class) of permissions resulting in unintended access rights to sensitive objects.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-36109**: Containerization product does not record a user's supplementary group ID, allowing bypass of group restrictions.
- **CVE-1999-1193**: Operating system assigns user to privileged wheel group, allowing the user to gain root privileges.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/286.html
