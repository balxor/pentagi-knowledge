---
cwe_id: CWE-493
name: Critical Public Variable Without Final Modifier
type: weakness
abstraction: Variant
status: Draft
languages: [Object-Oriented, Java, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/493.html
tags: [mitre-cwe, weakness, CWE-493]
---

# CWE-493 - Critical Public Variable Without Final Modifier

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-493](https://cwe.mitre.org/data/definitions/493.html)

## Description
The product has a critical public variable that is not final, which allows the variable to be modified to contain unexpected values.

## Extended description
If a field is non-final and public, it can be changed once the value is set by any function that has access to the class which contains the field. This could lead to a vulnerability if other parts of the program make assumptions about the contents of that field.

## Applicable platforms / languages
Object-Oriented, Java, C++

## Common consequences
- **Integrity**: Modify Application Data
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Declare all public fields as final when possible, especially if it is used to maintain internal state of an Applet or of classes used by an Applet. If a field must be public, then perform all appropriate sanity checks before accessing the field from your code.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/493.html
