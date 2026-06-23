---
cwe_id: CWE-467
name: Use of sizeof() on a Pointer Type
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/467.html
tags: [mitre-cwe, weakness, CWE-467]
---

# CWE-467 - Use of sizeof() on a Pointer Type

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-467](https://cwe.mitre.org/data/definitions/467.html)

## Description
The code calls sizeof() on a pointer type, which can be an incorrect calculation if the programmer intended to determine the size of the data that is being pointed to.

## Extended description
The use of sizeof() on a pointer can sometimes generate useful information. An obvious case is to find out the wordsize on a platform. More often than not, the appearance of sizeof(pointer) indicates a bug.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity, Confidentiality**: Modify Memory, Read Memory

## Potential mitigations
- **Implementation**: Use expressions such as "sizeof(*pointer)" instead of "sizeof(pointer)", unless you intend to run sizeof() on a pointer type to gain some platform independence or if you are allocating a variable on the stack.

## Related weaknesses
- CWE-131 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/467.html
