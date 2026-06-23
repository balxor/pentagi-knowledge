---
cwe_id: CWE-226
name: Sensitive Information in Resource Not Removed Before Reuse
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-37]
url: https://cwe.mitre.org/data/definitions/226.html
tags: [mitre-cwe, weakness, CWE-226]
---

# CWE-226 - Sensitive Information in Resource Not Removed Before Reuse

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-226](https://cwe.mitre.org/data/definitions/226.html)

## Description
The product releases a resource such as memory or a file so that it can be made available for reuse, but it does not clear or "zeroize" the information contained in the resource before the product performs a critical state transition or makes the resource available for reuse by other entities.

## Extended description
When resources are released, they can be made available for reuse. For example, after memory is de-allocated, an operating system may make the memory available to another process, or disk space may be reallocated when a file is deleted. As removing information requires time and additional resources, operating systems do not usually clear the previously written information. Even when the resource is reused by the same process, this weakness can arise when new data is not as large as the old data, which leaves portions of the old data still available. Equivalent errors can occur in other situations where the length of data is variable but the associated data structure is not. If memory is not cleared after use, the information may be read by less trustworthy parties when the memory is reallocated. This weakness can apply in hardware, such as when a device or system switches between power, sleep, or debug states during normal operation, or when execution changes to different users or privilege levels.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design, Implementation**: During critical state transitions, information not needed in the next state should be removed or overwritten with fixed patterns (such as all 0's) or random data, before the transition to the next state.
- **Architecture and Design, Implementation**: When releasing, de-allocating, or deleting a resource, overwrite its data and relevant metadata with fixed patterns or random data. Be cautious about complex resource types whose underlying representation might be non-contiguous or change at a low level, such as how a file might be split into different chunks on a file system, even though "logical" file positions are contiguous at the application layer. Such resource types might require invocation of special modes or APIs to tell the underlying operating system to perform the necessary clearing, such as SDelete (Secure Delete) on Windows, although the appropriate functionality might not be available at the application layer.

## Related attack patterns (CAPEC)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)

## Related weaknesses
- CWE-459 (ChildOf)
- CWE-212 (ChildOf)
- CWE-201 (CanPrecede)

## Observed examples (CVE)
- **CVE-2019-3733**: Cryptography library does not clear heap memory before release
- **CVE-2003-0001**: Ethernet NIC drivers do not pad frames with null bytes, leading to infoleak from malformed packets.
- **CVE-2003-0291**: router does not clear information from DHCP packets that have been previously used
- **CVE-2005-1406**: Products do not fully clear memory buffers when less data is stored into the buffer than previous.
- **CVE-2005-1858**: Products do not fully clear memory buffers when less data is stored into the buffer than previous.
- **CVE-2005-3180**: Products do not fully clear memory buffers when less data is stored into the buffer than previous.
- **CVE-2005-3276**: Product does not clear a data structure before writing to part of it, yielding information leak of previously used memory.
- **CVE-2002-2077**: Memory not properly cleared before reuse.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/226.html
