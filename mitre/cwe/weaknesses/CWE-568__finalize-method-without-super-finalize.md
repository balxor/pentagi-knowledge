---
cwe_id: CWE-568
name: finalize() Method Without super.finalize()
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/568.html
tags: [mitre-cwe, weakness, CWE-568]
---

# CWE-568 - finalize() Method Without super.finalize()

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-568](https://cwe.mitre.org/data/definitions/568.html)

## Description
The product contains a finalize() method that does not call super.finalize().

## Extended description
The Java Language Specification states that it is a good practice for a finalize() method to call super.finalize().

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Call the super.finalize() method.

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-459 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/568.html
