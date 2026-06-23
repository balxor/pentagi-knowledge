---
cwe_id: CWE-374
name: Passing Mutable Objects to an Untrusted Method
type: weakness
abstraction: Base
status: Draft
languages: [Object-Oriented, C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/374.html
tags: [mitre-cwe, weakness, CWE-374]
---

# CWE-374 - Passing Mutable Objects to an Untrusted Method

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-374](https://cwe.mitre.org/data/definitions/374.html)

## Description
The product sends non-cloned mutable data as an argument to a method or function.

## Extended description
The function or method that has been called can alter or delete the mutable data. This could violate assumptions that the calling function has made about its state. In situations where unknown code is called with references to mutable data, this external code could make changes to the data sent. If this data was not previously cloned, the modified data might not be valid in the context of execution.

## Applicable platforms / languages
Object-Oriented, C, C++, Java, C#

## Common consequences
- **Integrity**: Modify Memory

## Potential mitigations
- **Implementation**: Pass in data which should not be altered as constant or immutable.
- **Implementation**: Clone all mutable data before passing it into an external function . This is the preferred mitigation. This way, regardless of what changes are made to the data, a valid copy is retained for use by the class.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/374.html
