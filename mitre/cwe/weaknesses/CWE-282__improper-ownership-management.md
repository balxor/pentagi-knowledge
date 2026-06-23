---
cwe_id: CWE-282
name: Improper Ownership Management
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-17, CAPEC-35]
url: https://cwe.mitre.org/data/definitions/282.html
tags: [mitre-cwe, weakness, CWE-282]
---

# CWE-282 - Improper Ownership Management

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-282](https://cwe.mitre.org/data/definitions/282.html)

## Description
The product assigns the wrong ownership, or does not properly verify the ownership, of an object or resource.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.

## Related attack patterns (CAPEC)
- [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-1125**: Program runs setuid root but relies on a configuration file owned by a non-root user.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/282.html
