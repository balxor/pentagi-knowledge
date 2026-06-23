---
cwe_id: CWE-1325
name: Improperly Controlled Sequential Memory Allocation
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++, Not Language-Specific]
related_capec: [CAPEC-130]
url: https://cwe.mitre.org/data/definitions/1325.html
tags: [mitre-cwe, weakness, CWE-1325]
---

# CWE-1325 - Improperly Controlled Sequential Memory Allocation

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1325](https://cwe.mitre.org/data/definitions/1325.html)

## Description
The product manages a group of objects or resources and performs a separate memory allocation for each object, but it does not properly limit the total amount of memory that is consumed by all of the combined objects.

## Extended description
While the product might limit the amount of memory that is allocated in a single operation for a single object (such as a malloc of an array), if an attacker can cause multiple objects to be allocated in separate operations, then this might cause higher total memory consumption than the developer intended, leading to a denial of service.

## Applicable platforms / languages
C, C++, Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Memory)

## Potential mitigations
- **Implementation**: Ensure multiple allocations of the same kind of object are properly tracked - possibly across multiple sessions, requests, or messages. Define an appropriate strategy for handling requests that exceed the limit, and consider supporting a configuration option so that the administrator can extend the amount of memory to be used if necessary.
- **Operation**: Run the program using system-provided resource limits for memory. This might still cause the program to crash or exit, but the impact to the rest of the system will be minimized.

## Related attack patterns (CAPEC)
- [CAPEC-130](https://capec.mitre.org/data/definitions/130.html)

## Related weaknesses
- CWE-770 (ChildOf)
- CWE-789 (PeerOf)
- CWE-476 (CanPrecede)

## Observed examples (CVE)
- **CVE-2020-36049**: JavaScript-based packet decoder uses concatenation of many small strings, causing out-of-memory (OOM) condition
- **CVE-2019-20176**: Product allocates a new buffer on the stack for each file in a directory, allowing stack exhaustion
- **CVE-2013-1591**: Chain: an integer overflow (CWE-190) in the image size calculation causes an infinite loop (CWE-835) which sequentially allocates buffers without limits (CWE-1325) until the stack is full.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1325.html
