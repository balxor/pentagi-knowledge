---
cwe_id: CWE-563
name: Assignment to Variable without Use
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/563.html
tags: [mitre-cwe, weakness, CWE-563]
---

# CWE-563 - Assignment to Variable without Use

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-563](https://cwe.mitre.org/data/definitions/563.html)

## Description
The variable's value is assigned but never used, making it a dead store.

## Extended description
After the assignment, the variable is either assigned another value or goes out of scope. It is likely that the variable is simply vestigial, but it is also possible that the unused variable points out a bug.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Potential mitigations
- **Implementation**: Remove unused variables from the code.

## Related weaknesses
- CWE-1164 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/563.html
