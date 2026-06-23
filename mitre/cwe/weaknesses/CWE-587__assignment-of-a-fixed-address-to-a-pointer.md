---
cwe_id: CWE-587
name: Assignment of a Fixed Address to a Pointer
type: weakness
abstraction: Variant
status: Draft
languages: [Memory-Unsafe, C, C++, C#, Assembly]
related_capec: []
url: https://cwe.mitre.org/data/definitions/587.html
tags: [mitre-cwe, weakness, CWE-587]
---

# CWE-587 - Assignment of a Fixed Address to a Pointer

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-587](https://cwe.mitre.org/data/definitions/587.html)

## Description
The product sets a pointer to a specific address other than NULL or 0.

## Extended description
Using a fixed address is not portable, because that address will probably not be valid in all environments or platforms.

## Applicable platforms / languages
Memory-Unsafe, C, C++, C#, Assembly

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Availability**: DoS: Crash, Exit, or Restart, Reduce Maintainability, Reduce Reliability
- **Confidentiality, Integrity**: Read Memory, Modify Memory

## Potential mitigations
- **Implementation**: Never set a pointer to a fixed address.

## Related weaknesses
- CWE-344 (ChildOf)
- CWE-758 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/587.html
