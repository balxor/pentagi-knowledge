---
cwe_id: CWE-476
name: NULL Pointer Dereference
type: weakness
abstraction: Base
status: Stable
languages: [C, C++, Java, C#, Go]
related_capec: []
url: https://cwe.mitre.org/data/definitions/476.html
tags: [mitre-cwe, weakness, CWE-476]
---

# CWE-476 - NULL Pointer Dereference

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-476](https://cwe.mitre.org/data/definitions/476.html)

## Description
The product dereferences a pointer that it expects to be valid but is NULL.

## Applicable platforms / languages
C, C++, Java, C#, Go

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality**: Execute Unauthorized Code or Commands, Read Memory, Modify Memory

## Potential mitigations
- **Implementation**: For any pointers that could have been modified or provided from a function that can return NULL, check the pointer for NULL before use. When working with a multithreaded or otherwise asynchronous environment, ensure that proper locking APIs are used to lock before the check, and unlock when it has finished [REF-1484].
- **Requirements**: Select a programming language that is not susceptible to these issues.
- **Implementation**: Check the results of all functions that return a value and verify that the value is non-null before acting upon it.
- **Architecture and Design**: Identify all variables and data stores that receive information from external sources, and apply input validation to make sure that they are only initialized to expected values.
- **Implementation**: Explicitly initialize all variables and other data stores, either during declaration or just before the first usage.

## Related weaknesses
- CWE-710 (ChildOf)
- CWE-754 (ChildOf)
- CWE-754 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-41130**: C++ library for LLM inference has NULL pointer dereference if a read operation fails
- **CVE-2005-3274**: race condition causes a table to be corrupted if a timer activates while it is being modified, leading to resultant NULL dereference; also involves locking.
- **CVE-2002-1912**: large number of packets leads to NULL dereference
- **CVE-2005-0772**: packet with invalid error status value triggers NULL dereference
- **CVE-2009-4895**: Chain: race condition for an argument value, possibly resulting in NULL dereference
- **CVE-2020-29652**: ssh component for Go allows clients to cause a denial of service (nil pointer dereference) against SSH servers.
- **CVE-2009-2692**: Chain: Use of an unimplemented network socket operation pointing to an uninitialized handler function (CWE-456) causes a crash because of a null pointer dereference (CWE-476).
- **CVE-2009-3547**: Chain: race condition (CWE-362) might allow resource to be released before operating on it, leading to NULL dereference (CWE-476)
- **CVE-2009-3620**: Chain: some unprivileged ioctls do not verify that a structure has been initialized before invocation, leading to NULL dereference
- **CVE-2009-2698**: Chain: IP and UDP layers each track the same value with different mechanisms that can get out of sync, possibly resulting in a NULL dereference
- **CVE-2009-2692**: Chain: Use of an unimplemented network socket operation pointing to an uninitialized handler function (CWE-456) causes a crash because of a null pointer dereference (CWE-476)
- **CVE-2009-0949**: Chain: improper initialization of memory can lead to NULL dereference
- **CVE-2008-3597**: Chain: game server can access player data structures before initialization has happened leading to NULL dereference
- **CVE-2020-6078**: Chain: The return value of a function returning a pointer is not checked for success (CWE-252) resulting in the later use of an uninitialized variable (CWE-456) and a null pointer dereference (CWE-476)
- **CVE-2008-0062**: Chain: a message having an unknown message type may cause a reference to uninitialized memory resulting in a null pointer dereference (CWE-476) or dangling pointer (CWE-825), possibly crashing the system or causing heap corruption.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/476.html
