---
cwe_id: CWE-468
name: Incorrect Pointer Scaling
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/468.html
tags: [mitre-cwe, weakness, CWE-468]
---

# CWE-468 - Incorrect Pointer Scaling

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-468](https://cwe.mitre.org/data/definitions/468.html)

## Description
In C and C++, one may often accidentally refer to the wrong memory due to the semantics of when math operations are implicitly scaled.

## Applicable platforms / languages
C, C++

## Common consequences
- **Confidentiality, Integrity**: Read Memory, Modify Memory

## Potential mitigations
- **Architecture and Design**: Use a platform with high-level memory abstractions.
- **Implementation**: Always use array indexing instead of direct pointer manipulation.
- **Architecture and Design**: Use technologies for preventing buffer overflows.

## Related weaknesses
- CWE-682 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/468.html
