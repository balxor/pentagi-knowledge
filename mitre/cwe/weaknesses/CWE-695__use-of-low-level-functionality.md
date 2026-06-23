---
cwe_id: CWE-695
name: Use of Low-Level Functionality
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-36]
url: https://cwe.mitre.org/data/definitions/695.html
tags: [mitre-cwe, weakness, CWE-695]
---

# CWE-695 - Use of Low-Level Functionality

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-695](https://cwe.mitre.org/data/definitions/695.html)

## Description
The product uses low-level functionality that is explicitly prohibited by the framework or specification under which the product is supposed to operate.

## Extended description
The use of low-level functionality can violate the specification in unexpected ways that effectively disable built-in protection mechanisms, introduce exploitable inconsistencies, or otherwise expose the functionality to attack.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other

## Related attack patterns (CAPEC)
- [CAPEC-36](https://capec.mitre.org/data/definitions/36.html)

## Related weaknesses
- CWE-573 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/695.html
