---
cwe_id: CWE-789
name: Memory Allocation with Excessive Size Value
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/789.html
tags: [mitre-cwe, weakness, CWE-789]
---

# CWE-789 - Memory Allocation with Excessive Size Value

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-789](https://cwe.mitre.org/data/definitions/789.html)

## Description
The product allocates memory based on an untrusted, large size value, but it does not ensure that the size is within expected limits, allowing arbitrary amounts of memory to be allocated.

## Applicable platforms / languages
C, C++, Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (Memory)

## Potential mitigations
- **Implementation, Architecture and Design**: Perform adequate input validation against any value that influences the amount of memory that is allocated. Define an appropriate strategy for handling requests that exceed the limit, and consider supporting a configuration option so that the administrator can extend the amount of memory to be used if necessary.
- **Operation**: Run your program using system-provided resource limits for memory. This might still cause the program to crash or exit, but the impact to the rest of the system will be minimized.

## Related weaknesses
- CWE-770 (ChildOf)
- CWE-476 (CanPrecede)

## Observed examples (CVE)
- **CVE-2023-2253**: Query capability for API endpoint allows a large value for number of records to return, leading to allocation of a large array
- **CVE-2019-19911**: Chain: Python library does not limit the resources used to process images that specify a very large number of bands (CWE-1284), leading to excessive memory consumption (CWE-789) or an integer overflow (CWE-190).
- **CVE-2010-3701**: program uses ::alloca() for encoding messages, but large messages trigger segfault
- **CVE-2008-1708**: memory consumption and daemon exit by specifying a large value in a length field
- **CVE-2008-0977**: large value in a length field leads to memory consumption and crash when no more memory is available
- **CVE-2006-3791**: large key size in game program triggers crash when a resizing function cannot allocate enough memory
- **CVE-2004-2589**: large Content-Length HTTP header value triggers application crash in instant messaging application due to failure in memory allocation

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/789.html
