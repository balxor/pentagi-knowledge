---
cwe_id: CWE-1041
name: Use of Redundant Code
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1041.html
tags: [mitre-cwe, weakness, CWE-1041]
---

# CWE-1041 - Use of Redundant Code

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1041](https://cwe.mitre.org/data/definitions/1041.html)

## Description
The product has multiple functions, methods, procedures, macros, etc. that contain the same code.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability

## Potential mitigations
- **Implementation**: Merge common functionality into a single function and then call that function from across the entire code base.

## Related weaknesses
- CWE-710 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1041.html
