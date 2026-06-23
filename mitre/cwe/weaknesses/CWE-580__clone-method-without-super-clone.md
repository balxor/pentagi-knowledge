---
cwe_id: CWE-580
name: clone() Method Without super.clone()
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/580.html
tags: [mitre-cwe, weakness, CWE-580]
---

# CWE-580 - clone() Method Without super.clone()

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-580](https://cwe.mitre.org/data/definitions/580.html)

## Description
The product contains a clone() method that does not call super.clone() to obtain the new object.

## Extended description
All implementations of clone() should obtain the new object by calling super.clone(). If a class does not follow this convention, a subclass's clone() method will return an object of the wrong type.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity, Other**: Unexpected State, Quality Degradation

## Potential mitigations
- **Implementation**: Call super.clone() within your clone() method, when obtaining a new object.
- **Implementation**: In some cases, you can eliminate the clone method altogether and use copy constructors.

## Related weaknesses
- CWE-664 (ChildOf)
- CWE-573 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/580.html
