---
cwe_id: CWE-496
name: Public Data Assigned to Private Array-Typed Field
type: weakness
abstraction: Variant
status: Incomplete
languages: [Object-Oriented, C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/496.html
tags: [mitre-cwe, weakness, CWE-496]
---

# CWE-496 - Public Data Assigned to Private Array-Typed Field

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-496](https://cwe.mitre.org/data/definitions/496.html)

## Description
Assigning public data to a private array is equivalent to giving public access to the array.

## Applicable platforms / languages
Object-Oriented, C, C++, Java, C#

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: Do not allow objects to modify private members of a class.

## Related weaknesses
- CWE-664 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/496.html
