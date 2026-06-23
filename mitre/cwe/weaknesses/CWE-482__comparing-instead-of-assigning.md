---
cwe_id: CWE-482
name: Comparing instead of Assigning
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/482.html
tags: [mitre-cwe, weakness, CWE-482]
---

# CWE-482 - Comparing instead of Assigning

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-482](https://cwe.mitre.org/data/definitions/482.html)

## Description
The code uses an operator for comparison when the intention was to perform an assignment.

## Extended description
In many languages, the compare statement is very close in appearance to the assignment statement; they are often confused.

## Applicable platforms / languages
C, C++

## Common consequences
- **Availability, Integrity**: Unexpected State

## Potential mitigations
- **Testing**: Many IDEs and static analysis products will detect this problem.

## Related weaknesses
- CWE-480 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/482.html
