---
cwe_id: CWE-375
name: Returning a Mutable Object to an Untrusted Caller
type: weakness
abstraction: Base
status: Draft
languages: [Object-Oriented, C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/375.html
tags: [mitre-cwe, weakness, CWE-375]
---

# CWE-375 - Returning a Mutable Object to an Untrusted Caller

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-375](https://cwe.mitre.org/data/definitions/375.html)

## Description
Sending non-cloned mutable data as a return value may result in that data being altered or deleted by the calling function.

## Extended description
In situations where functions return references to mutable data, it is possible that the external code which called the function may make changes to the data sent. If this data was not previously cloned, the class will then be using modified data which may violate assumptions about its internal state.

## Applicable platforms / languages
Object-Oriented, C, C++, Java, C#

## Common consequences
- **Access Control, Integrity**: Modify Memory

## Potential mitigations
- **Implementation**: Declare returned data which should not be altered as constant or immutable.
- **Implementation**: Clone all mutable data before returning references to it. This is the preferred mitigation. This way, regardless of what changes are made to the data, a valid copy is retained for use by the class.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/375.html
