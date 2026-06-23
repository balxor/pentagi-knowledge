---
cwe_id: CWE-274
name: Improper Handling of Insufficient Privileges
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/274.html
tags: [mitre-cwe, weakness, CWE-274]
---

# CWE-274 - Improper Handling of Insufficient Privileges

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-274](https://cwe.mitre.org/data/definitions/274.html)

## Description
The product does not handle or incorrectly handles when it has insufficient privileges to perform an operation, leading to resultant weaknesses.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other, Alter Execution Logic

## Related weaknesses
- CWE-755 (ChildOf)
- CWE-269 (ChildOf)
- CWE-271 (PeerOf)
- CWE-280 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2001-1564**: System limits are not properly enforced after privileges are dropped.
- **CVE-2005-3286**: Firewall crashes when it can't read a critical memory block that was protected by a malicious process.
- **CVE-2005-1641**: Does not give admin sufficient privileges to overcome otherwise legitimate user actions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/274.html
