---
cwe_id: CWE-416
name: Use After Free
type: weakness
abstraction: Variant
status: Stable
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/416.html
tags: [mitre-cwe, weakness, CWE-416]
---

# CWE-416 - Use After Free

**Abstraction:** Variant  -  **Status:** Stable  -  **CWE:** [CWE-416](https://cwe.mitre.org/data/definitions/416.html)

## Description
The product reuses or references memory after it has been freed. At some point afterward, the memory may be allocated again and saved in another pointer, while the original pointer references a location somewhere within the new allocation. Any operations using the original pointer are no longer valid because the memory "belongs" to the code that operates on the new pointer.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Integrity**: Modify Memory
- **Availability**: DoS: Crash, Exit, or Restart
- **Confidentiality**: Read Memory
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Choose a language that provides automatic memory management.
- **Implementation**: When freeing pointers, be sure to set them to NULL once they are freed. However, the utilization of multiple or complex data structures may lower the usefulness of this strategy.

## Related weaknesses
- CWE-825 (ChildOf)
- CWE-672 (ChildOf)
- CWE-672 (ChildOf)
- CWE-672 (ChildOf)
- CWE-120 (CanPrecede)
- CWE-123 (CanPrecede)

## Observed examples (CVE)
- **CVE-2023-38160**: TCP/IP code for an OS has a use-after-free that can leak heap memory contents
- **CVE-2022-20141**: Chain: an operating system kernel has insufficent resource locking (CWE-413) leading to a use after free (CWE-416).
- **CVE-2022-2621**: Chain: two threads in a web browser use the same resource (CWE-366), but one of those threads can destroy the resource before the other has completed (CWE-416).
- **CVE-2021-0920**: Chain: mobile platform race condition (CWE-362) leading to use-after-free (CWE-416), as exploited in the wild per CISA KEV.
- **CVE-2020-6819**: Chain: race condition (CWE-362) leads to use-after-free (CWE-416), as exploited in the wild per CISA KEV.
- **CVE-2010-4168**: Use-after-free triggered by closing a connection while data is still being transmitted.
- **CVE-2010-2941**: Improper allocation for invalid data leads to use-after-free.
- **CVE-2010-2547**: certificate with a large number of Subject Alternate Names not properly handled in realloc, leading to use-after-free
- **CVE-2010-1772**: Timers are not disabled when a related object is deleted
- **CVE-2010-1437**: Access to a "dead" object that is being cleaned up
- **CVE-2010-1208**: object is deleted even with a non-zero reference count, and later accessed
- **CVE-2010-0629**: use-after-free involving request containing an invalid version number
- **CVE-2010-0378**: unload of an object that is currently being accessed by other functionality
- **CVE-2010-0302**: incorrectly tracking a reference count leads to use-after-free
- **CVE-2010-0249**: use-after-free related to use of uninitialized memory

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/416.html
