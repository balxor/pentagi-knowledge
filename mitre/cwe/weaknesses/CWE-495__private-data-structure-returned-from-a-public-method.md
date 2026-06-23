---
cwe_id: CWE-495
name: Private Data Structure Returned From A Public Method
type: weakness
abstraction: Variant
status: Draft
languages: [Object-Oriented, C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/495.html
tags: [mitre-cwe, weakness, CWE-495]
---

# CWE-495 - Private Data Structure Returned From A Public Method

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-495](https://cwe.mitre.org/data/definitions/495.html)

## Description
The product has a method that is declared public, but returns a reference to a private data structure, which could then be modified in unexpected ways.

## Applicable platforms / languages
Object-Oriented, C, C++, Java, C#

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: Declare the method private.
- **Implementation**: Clone the member data and keep an unmodified version of the data private to the object.
- **Implementation**: Use public setter methods that govern how a private member can be modified.

## Related weaknesses
- CWE-664 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/495.html
