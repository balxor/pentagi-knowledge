---
cwe_id: CWE-460
name: Improper Cleanup on Thrown Exception
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/460.html
tags: [mitre-cwe, weakness, CWE-460]
---

# CWE-460 - Improper Cleanup on Thrown Exception

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-460](https://cwe.mitre.org/data/definitions/460.html)

## Description
The product does not clean up its state or incorrectly cleans up its state when an exception is thrown, leading to unexpected state or control flow.

## Extended description
Often, when functions or loops become complicated, some level of resource cleanup is needed throughout execution. Exceptions can disturb the flow of the code and prevent the necessary cleanup from happening.

## Applicable platforms / languages
C, C++, Java, C#

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Implementation**: If one breaks from a loop or function by throwing an exception, make sure that cleanup happens or that you should exit the program. Use throwing exceptions sparsely.

## Related weaknesses
- CWE-459 (ChildOf)
- CWE-755 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/460.html
