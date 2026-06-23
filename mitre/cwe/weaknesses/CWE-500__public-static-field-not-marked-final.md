---
cwe_id: CWE-500
name: Public Static Field Not Marked Final
type: weakness
abstraction: Variant
status: Draft
languages: [C++, Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/500.html
tags: [mitre-cwe, weakness, CWE-500]
---

# CWE-500 - Public Static Field Not Marked Final

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-500](https://cwe.mitre.org/data/definitions/500.html)

## Description
An object contains a public static field that is not marked final, which might allow it to be modified in unexpected ways.

## Extended description
Public static variables can be read without an accessor and changed without a mutator by any classes in the application.

## Applicable platforms / languages
C++, Java

## Common consequences
- **Integrity**: Modify Application Data
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Clearly identify the scope for all critical data elements, including whether they should be regarded as static.
- **Implementation**: Make any static fields private and constant. A constant field is denoted by the keyword 'const' in C/C++ and ' final' in Java

## Related weaknesses
- CWE-493 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/500.html
