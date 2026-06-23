---
cwe_id: CWE-228
name: Improper Handling of Syntactically Invalid Structure
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/228.html
tags: [mitre-cwe, weakness, CWE-228]
---

# CWE-228 - Improper Handling of Syntactically Invalid Structure

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-228](https://cwe.mitre.org/data/definitions/228.html)

## Description
The product does not handle or incorrectly handles input that is not syntactically well-formed with respect to the associated specification.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Availability**: Unexpected State, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU)

## Related weaknesses
- CWE-703 (ChildOf)
- CWE-707 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-0270**: Anti-virus product has assert error when line length is non-numeric.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/228.html
