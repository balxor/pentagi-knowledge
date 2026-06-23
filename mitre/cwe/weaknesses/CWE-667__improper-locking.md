---
cwe_id: CWE-667
name: Improper Locking
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-25, CAPEC-26, CAPEC-27]
url: https://cwe.mitre.org/data/definitions/667.html
tags: [mitre-cwe, weakness, CWE-667]
---

# CWE-667 - Improper Locking

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-667](https://cwe.mitre.org/data/definitions/667.html)

## Description
The product does not properly acquire or release a lock on a resource, leading to unexpected resource state changes and behaviors.

## Extended description
Locking is a type of synchronization behavior that ensures that multiple independently-operating processes or threads do not interfere with each other when accessing the same resource. All processes/threads are expected to follow the same steps for locking. If these steps are not followed precisely - or if no locking is done at all - then another process/thread could modify the shared resource in a way that is not visible or predictable to the original process. This can lead to data or memory corruption, denial of service, etc.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU)

## Potential mitigations
- **Implementation**: Use industry standard APIs to implement locking mechanism.

## Related attack patterns (CAPEC)
- [CAPEC-25](https://capec.mitre.org/data/definitions/25.html)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-27](https://capec.mitre.org/data/definitions/27.html)

## Related weaknesses
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-1782**: Chain: improper locking (CWE-667) leads to race condition (CWE-362), as exploited in the wild per CISA KEV.
- **CVE-2009-0935**: Attacker provides invalid address to a memory-reading function, causing a mutex to be unlocked twice
- **CVE-2010-4210**: function in OS kernel unlocks a mutex that was not previously locked, causing a panic or overwrite of arbitrary memory.
- **CVE-2008-4302**: Chain: OS kernel does not properly handle a failure of a function call (CWE-755), leading to an unlock of a resource that was not locked (CWE-832), with resultant crash.
- **CVE-2009-1243**: OS kernel performs an unlock in some incorrect circumstances, leading to panic.
- **CVE-2009-2857**: OS deadlock
- **CVE-2009-1961**: OS deadlock involving 3 separate functions
- **CVE-2009-2699**: deadlock in library
- **CVE-2009-4272**: deadlock triggered by packets that force collisions in a routing table
- **CVE-2002-1850**: read/write deadlock between web server and script
- **CVE-2004-0174**: web server deadlock involving multiple listening connections
- **CVE-2009-1388**: multiple simultaneous calls to the same function trigger deadlock.
- **CVE-2006-5158**: chain: other weakness leads to NULL pointer dereference (CWE-476) or deadlock (CWE-833).
- **CVE-2006-4342**: deadlock when an operation is performed on a resource while it is being removed.
- **CVE-2006-2374**: Deadlock in device driver triggered by using file handle of a related device.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/667.html
