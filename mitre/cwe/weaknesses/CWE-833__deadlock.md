---
cwe_id: CWE-833
name: Deadlock
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-25]
url: https://cwe.mitre.org/data/definitions/833.html
tags: [mitre-cwe, weakness, CWE-833]
---

# CWE-833 - Deadlock

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-833](https://cwe.mitre.org/data/definitions/833.html)

## Description
The product contains multiple threads or executable segments that are waiting for each other to release a necessary lock, resulting in deadlock.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Other), DoS: Crash, Exit, or Restart

## Related attack patterns (CAPEC)
- [CAPEC-25](https://capec.mitre.org/data/definitions/25.html)

## Related weaknesses
- CWE-667 (ChildOf)
- CWE-662 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-1476**: A bug in some Intel Pentium processors allow DoS (hang) via an invalid "CMPXCHG8B" instruction, causing a deadlock
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
- **CVE-2006-2275**: Deadlock when large number of small messages cannot be processed quickly enough.
- **CVE-2005-3847**: OS kernel has deadlock triggered by a signal during a core dump.
- **CVE-2005-3106**: Race condition leads to deadlock.
- **CVE-2005-2456**: Chain: array index error (CWE-129) leads to deadlock (CWE-833)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/833.html
