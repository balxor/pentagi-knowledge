---
cwe_id: CWE-543
name: Use of Singleton Pattern Without Synchronization in a Multithreaded Context
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/543.html
tags: [mitre-cwe, weakness, CWE-543]
---

# CWE-543 - Use of Singleton Pattern Without Synchronization in a Multithreaded Context

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-543](https://cwe.mitre.org/data/definitions/543.html)

## Description
The product uses the singleton pattern when creating a resource within a multithreaded environment.

## Extended description
The use of a singleton pattern may not be thread-safe.

## Applicable platforms / languages
Java, C++

## Common consequences
- **Other, Integrity**: Other, Modify Application Data

## Potential mitigations
- **Architecture and Design**: Use the Thread-Specific Storage Pattern. See References.
- **Implementation**: Do not use member fields to store information in the Servlet. In multithreading environments, storing user data in Servlet member fields introduces a data access race condition.
- **Implementation**: Avoid using the double-checked locking pattern in language versions that cannot guarantee thread safety. This pattern may be used to avoid the overhead of a synchronized call, but in certain versions of Java (for example), this has been shown to be unsafe because it still introduces a race condition (CWE-209).

## Related weaknesses
- CWE-820 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/543.html
