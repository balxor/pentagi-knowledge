---
cwe_id: CWE-588
name: Attempt to Access Child of a Non-structure Pointer
type: weakness
abstraction: Variant
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/588.html
tags: [mitre-cwe, weakness, CWE-588]
---

# CWE-588 - Attempt to Access Child of a Non-structure Pointer

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-588](https://cwe.mitre.org/data/definitions/588.html)

## Description
Casting a non-structure type to a structure type and accessing a field can lead to memory access errors or data corruption.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity**: Modify Memory
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Requirements**: The choice could be made to use a language that is not susceptible to these issues.
- **Implementation**: Review of type casting operations can identify locations where incompatible types are cast.

## Related weaknesses
- CWE-704 (ChildOf)
- CWE-758 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-3510**: JSON decoder accesses a C union using an invalid offset to an object

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/588.html
