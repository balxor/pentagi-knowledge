---
cwe_id: CWE-582
name: Array Declared Public, Final, and Static
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/582.html
tags: [mitre-cwe, weakness, CWE-582]
---

# CWE-582 - Array Declared Public, Final, and Static

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-582](https://cwe.mitre.org/data/definitions/582.html)

## Description
The product declares an array public, final, and static, which is not sufficient to prevent the array's contents from being modified.

## Extended description
Because arrays are mutable objects, the final constraint requires that the array object itself be assigned only once, but makes no guarantees about the values of the array elements. Since the array is public, a malicious program can change the values stored in the array. As such, in most cases an array declared public, final and static is a bug.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: In most situations the array should be made private.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/582.html
