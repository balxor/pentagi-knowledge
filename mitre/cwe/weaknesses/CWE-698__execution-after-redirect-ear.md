---
cwe_id: CWE-698
name: Execution After Redirect (EAR)
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/698.html
tags: [mitre-cwe, weakness, CWE-698]
---

# CWE-698 - Execution After Redirect (EAR)

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-698](https://cwe.mitre.org/data/definitions/698.html)

## Description
The web application sends a redirect to another location, but instead of exiting, it executes additional code.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Other, Confidentiality, Integrity, Availability**: Alter Execution Logic, Execute Unauthorized Code or Commands

## Related weaknesses
- CWE-705 (ChildOf)
- CWE-670 (ChildOf)

## Observed examples (CVE)
- **CVE-2013-1402**: Execution-after-redirect allows access to application configuration details.
- **CVE-2009-1936**: chain: library file sends a redirect if it is directly requested but continues to execute, allowing remote file inclusion and path traversal.
- **CVE-2007-2713**: Remote attackers can obtain access to administrator functionality through EAR.
- **CVE-2007-4932**: Remote attackers can obtain access to administrator functionality through EAR.
- **CVE-2007-5578**: Bypass of authentication step through EAR.
- **CVE-2007-2713**: Chain: Execution after redirect triggers eval injection.
- **CVE-2007-6652**: chain: execution after redirect allows non-administrator to perform static code injection.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/698.html
