---
cwe_id: CWE-414
name: Missing Lock Check
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/414.html
tags: [mitre-cwe, weakness, CWE-414]
---

# CWE-414 - Missing Lock Check

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-414](https://cwe.mitre.org/data/definitions/414.html)

## Description
A product does not check to see if a lock is present before performing sensitive operations on a resource.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Availability**: Modify Application Data, DoS: Instability, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design, Implementation**: Implement a reliable lock mechanism.

## Related weaknesses
- CWE-667 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-1056**: Product does not properly check if a lock is present, allowing other attackers to access functionality.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/414.html
