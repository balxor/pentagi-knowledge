---
cwe_id: CWE-825
name: Expired Pointer Dereference
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/825.html
tags: [mitre-cwe, weakness, CWE-825]
---

# CWE-825 - Expired Pointer Dereference

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-825](https://cwe.mitre.org/data/definitions/825.html)

## Description
The product dereferences a pointer that contains a location for memory that was previously valid, but is no longer valid.

## Extended description
When a product releases memory, but it maintains a pointer to that memory, then the memory might be re-allocated at a later time. If the original pointer is accessed to read or write data, then this could cause the product to read or modify data that is in use by a different function or process. Depending on how the newly-allocated memory is used, this could lead to a denial of service, information exposure, or code execution.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality**: Read Memory
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Choose a language that provides automatic memory management.
- **Implementation**: When freeing pointers, be sure to set them to NULL once they are freed. However, the utilization of multiple or complex data structures may lower the usefulness of this strategy.

## Related weaknesses
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-672 (ChildOf)
- CWE-125 (CanPrecede)
- CWE-787 (CanPrecede)

## Observed examples (CVE)
- **CVE-2023-26463**: Chain: IPSec VPN product uses the same variable for multiple purposes in the same function (CWE-1109), leading to incorrect access control (CWE-284) and expired pointer dereference (CWE-825)
- **CVE-2008-5013**: access of expired memory address leads to arbitrary code execution
- **CVE-2010-3257**: stale pointer issue leads to denial of service and possibly other consequences
- **CVE-2008-0062**: Chain: a message having an unknown message type may cause a reference to uninitialized memory resulting in a null pointer dereference (CWE-476) or dangling pointer (CWE-825), possibly crashing the system or causing heap corruption.
- **CVE-2007-1211**: read of value at an offset into a structure after the offset is no longer valid

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/825.html
