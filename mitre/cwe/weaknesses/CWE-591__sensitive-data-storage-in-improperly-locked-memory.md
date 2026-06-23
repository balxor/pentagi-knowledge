---
cwe_id: CWE-591
name: Sensitive Data Storage in Improperly Locked Memory
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/591.html
tags: [mitre-cwe, weakness, CWE-591]
---

# CWE-591 - Sensitive Data Storage in Improperly Locked Memory

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-591](https://cwe.mitre.org/data/definitions/591.html)

## Description
The product stores sensitive data in memory that is not locked, or that has been incorrectly locked, which might cause the memory to be written to swap files on disk by the virtual memory manager. This can make the data more accessible to external actors.

## Extended description
On Windows systems the VirtualLock function can lock a page of memory to ensure that it will remain present in memory and not be swapped to disk. However, on older versions of Windows, such as 95, 98, or Me, the VirtualLock() function is only a stub and provides no protection. On POSIX systems the mlock() call ensures that a page will stay resident in memory but does not guarantee that the page will not appear in the swap. Therefore, it is unsuitable for use as a protection mechanism for sensitive data. Some platforms, in particular Linux, do make the guarantee that the page will not be swapped, but this is non-standard and is not portable. Calls to mlock() also require supervisor privilege. Return values for both of these calls must be checked to ensure that the lock operation was actually successful.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data, Read Memory

## Potential mitigations
- **Architecture and Design**: Identify data that needs to be protected from swapping and choose platform-appropriate protection mechanisms.
- **Implementation**: Check return values to ensure locking operations are successful.

## Related weaknesses
- CWE-413 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-38106**: OS kernel stores sensitive data in improperly locked memory, allowing local users to gain privileges by winning a race condition

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/591.html
