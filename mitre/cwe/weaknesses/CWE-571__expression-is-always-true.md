---
cwe_id: CWE-571
name: Expression is Always True
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/571.html
tags: [mitre-cwe, weakness, CWE-571]
---

# CWE-571 - Expression is Always True

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-571](https://cwe.mitre.org/data/definitions/571.html)

## Description
The product contains an expression that will always evaluate to true.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Potential mitigations
- **Implementation**: Consider refactoring the code, or determine if the code is not including a condition that could cause the expression to become false.

## Related weaknesses
- CWE-710 (ChildOf)
- CWE-561 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/571.html
