---
cwe_id: CWE-785
name: Use of Path Manipulation Function without Maximum-sized Buffer
type: weakness
abstraction: Variant
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/785.html
tags: [mitre-cwe, weakness, CWE-785]
---

# CWE-785 - Use of Path Manipulation Function without Maximum-sized Buffer

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-785](https://cwe.mitre.org/data/definitions/785.html)

## Description
The product invokes a function for normalizing paths or file names, but it provides an output buffer that is smaller than the maximum possible size, such as PATH_MAX.

## Extended description
Passing an inadequately-sized output buffer to a path manipulation function can result in a buffer overflow. Such functions include realpath(), readlink(), PathAppend(), and others.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity, Confidentiality, Availability**: Modify Memory, Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Always specify output buffers large enough to handle the maximum-size possible result from path manipulation functions.

## Related weaknesses
- CWE-676 (ChildOf)
- CWE-120 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/785.html
