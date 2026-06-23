---
cwe_id: CWE-607
name: Public Static Final Field References Mutable Object
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/607.html
tags: [mitre-cwe, weakness, CWE-607]
---

# CWE-607 - Public Static Final Field References Mutable Object

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-607](https://cwe.mitre.org/data/definitions/607.html)

## Description
A public or protected static final field references a mutable object, which allows the object to be changed by malicious code, or accidentally from another package.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: Protect mutable objects by making them private. Restrict access to the getter and setter as well.

## Related weaknesses
- CWE-471 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/607.html
