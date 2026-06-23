---
cwe_id: CWE-466
name: Return of Pointer Value Outside of Expected Range
type: weakness
abstraction: Base
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/466.html
tags: [mitre-cwe, weakness, CWE-466]
---

# CWE-466 - Return of Pointer Value Outside of Expected Range

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-466](https://cwe.mitre.org/data/definitions/466.html)

## Description
A function can return a pointer to memory that is outside of the buffer that the pointer is expected to reference.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality, Integrity**: Read Memory, Modify Memory

## Related weaknesses
- CWE-119 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/466.html
