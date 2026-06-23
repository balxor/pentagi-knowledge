---
cwe_id: CWE-491
name: Public cloneable() Method Without Final ('Object Hijack')
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/491.html
tags: [mitre-cwe, weakness, CWE-491]
---

# CWE-491 - Public cloneable() Method Without Final ('Object Hijack')

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-491](https://cwe.mitre.org/data/definitions/491.html)

## Description
A class has a cloneable() method that is not declared final, which allows an object to be created without calling the constructor. This can cause the object to be in an unexpected state.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity, Other**: Unexpected State, Varies by Context

## Potential mitigations
- **Implementation**: Make the cloneable() method final.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/491.html
