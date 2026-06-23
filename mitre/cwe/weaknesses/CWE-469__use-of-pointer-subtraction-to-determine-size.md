---
cwe_id: CWE-469
name: Use of Pointer Subtraction to Determine Size
type: weakness
abstraction: Base
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/469.html
tags: [mitre-cwe, weakness, CWE-469]
---

# CWE-469 - Use of Pointer Subtraction to Determine Size

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-469](https://cwe.mitre.org/data/definitions/469.html)

## Description
The product subtracts one pointer from another in order to determine size, but this calculation can be incorrect if the pointers do not exist in the same memory chunk.

## Applicable platforms / languages
C, C++

## Common consequences
- **Access Control, Integrity, Confidentiality, Availability**: Modify Memory, Read Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Save an index variable. This is the recommended solution. Rather than subtract pointers from one another, use an index variable of the same size as the pointers in question. Use this variable to "walk" from one pointer to the other and calculate the difference. Always validate this number.

## Related weaknesses
- CWE-682 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/469.html
