---
cwe_id: CWE-662
name: Improper Synchronization
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-25, CAPEC-26, CAPEC-27, CAPEC-29]
url: https://cwe.mitre.org/data/definitions/662.html
tags: [mitre-cwe, weakness, CWE-662]
---

# CWE-662 - Improper Synchronization

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-662](https://cwe.mitre.org/data/definitions/662.html)

## Description
The product utilizes multiple threads, processes, components, or systems to allow temporary access to a shared resource that can only be exclusive to one process at a time, but it does not properly synchronize these actions, which might cause simultaneous accesses of this resource by multiple threads or processes.

## Extended description
Synchronization refers to a variety of behaviors and mechanisms that allow two or more independently-operating processes or threads to ensure that they operate on shared resources in predictable ways that do not interfere with each other. Some shared resource operations cannot be executed atomically; that is, multiple steps must be guaranteed to execute sequentially, without any interference by other processes. Synchronization mechanisms vary widely, but they may include locking, mutexes, and semaphores. When a multi-step operation on a shared resource cannot be guaranteed to execute independent of interference, then the resulting behavior can be unpredictable. Improper synchronization could lead to data or memory corruption, denial of service, etc.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality, Other**: Modify Application Data, Read Application Data, Alter Execution Logic

## Potential mitigations
- **Implementation**: Use industry standard APIs to synchronize your code.

## Related attack patterns (CAPEC)
- [CAPEC-25](https://capec.mitre.org/data/definitions/25.html)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-27](https://capec.mitre.org/data/definitions/27.html)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-664 (ChildOf)
- CWE-691 (ChildOf)
- CWE-362 (CanPrecede)

## Observed examples (CVE)
- **CVE-2021-1782**: Chain: improper locking (CWE-667) leads to race condition (CWE-362), as exploited in the wild per CISA KEV.
- **CVE-2009-0935**: Attacker provides invalid address to a memory-reading function, causing a mutex to be unlocked twice

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/662.html
