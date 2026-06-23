---
cwe_id: CWE-567
name: Unsynchronized Access to Shared Data in a Multithreaded Context
type: weakness
abstraction: Base
status: Draft
languages: [Java]
related_capec: [CAPEC-25]
url: https://cwe.mitre.org/data/definitions/567.html
tags: [mitre-cwe, weakness, CWE-567]
---

# CWE-567 - Unsynchronized Access to Shared Data in a Multithreaded Context

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-567](https://cwe.mitre.org/data/definitions/567.html)

## Description
The product does not properly synchronize shared data, such as static variables across threads, which can lead to undefined behavior and unpredictable data changes.

## Extended description
Within servlets, shared static variables are not protected from concurrent access, but servlets are multithreaded. This is a typical programming mistake in J2EE applications, since the multithreading is handled by the framework. When a shared variable can be influenced by an attacker, one thread could wind up modifying the variable to contain data that is not valid for a different thread that is also using the data within the variable. Note that this weakness is not unique to servlets.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality, Integrity, Availability**: Read Application Data, Modify Application Data, DoS: Instability, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Remove the use of static variables used between servlets. If this cannot be avoided, use synchronized access for these variables.

## Related attack patterns (CAPEC)
- [CAPEC-25](https://capec.mitre.org/data/definitions/25.html)

## Related weaknesses
- CWE-820 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)
- CWE-488 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/567.html
