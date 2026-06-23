---
cwe_id: CWE-464
name: Addition of Data Structure Sentinel
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/464.html
tags: [mitre-cwe, weakness, CWE-464]
---

# CWE-464 - Addition of Data Structure Sentinel

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-464](https://cwe.mitre.org/data/definitions/464.html)

## Description
The accidental addition of a data-structure sentinel can cause serious programming logic problems.

## Extended description
Data-structure sentinels are often used to mark the structure of data. A common example of this is the null character at the end of strings or a special sentinel to mark the end of a linked list. It is dangerous to allow this type of control data to be easily accessible. Therefore, it is important to protect from the addition or modification of sentinels.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation, Architecture and Design**: Encapsulate the user from interacting with data sentinels. Validate user input to verify that sentinels are not present.
- **Implementation**: Proper error checking can reduce the risk of inadvertently introducing sentinel values into data. For example, if a parsing function fails or encounters an error, it might return a value that is the same as the sentinel.
- **Architecture and Design**: Use an abstraction library to abstract away risky APIs. This is not a complete solution.
- **Operation**: Use OS-level preventative functionality. This is not a complete solution.

## Related weaknesses
- CWE-138 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/464.html
