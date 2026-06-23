---
cwe_id: CWE-908
name: Use of Uninitialized Resource
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/908.html
tags: [mitre-cwe, weakness, CWE-908]
---

# CWE-908 - Use of Uninitialized Resource

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-908](https://cwe.mitre.org/data/definitions/908.html)

## Description
The product uses or accesses a resource that has not been initialized.

## Extended description
When a resource has not been properly initialized, the product may behave unexpectedly. This may lead to a crash or invalid memory access, but the consequences vary depending on the type of resource and how it is used within the product.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Explicitly initialize the resource before use. If this is performed through an API function or standard procedure, follow all required steps.
- **Implementation**: Pay close attention to complex conditionals that affect initialization, since some branches might not perform the initialization.
- **Implementation**: Avoid race conditions (CWE-362) during initialization routines.
- **Build and Compilation**: Run or compile the product with settings that generate warnings about uninitialized variables or data.

## Related weaknesses
- CWE-665 (ChildOf)
- CWE-665 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-9805**: Chain: Creation of the packet client occurs before initialization is complete (CWE-696) resulting in a read from uninitialized memory (CWE-908), causing memory corruption.
- **CVE-2008-4197**: Use of uninitialized memory may allow code execution.
- **CVE-2008-2934**: Free of an uninitialized pointer leads to crash and possible code execution.
- **CVE-2008-0063**: Product does not clear memory contents when generating an error message, leading to information leak.
- **CVE-2008-0062**: Lack of initialization triggers NULL pointer dereference or double-free.
- **CVE-2008-0081**: Uninitialized variable leads to code execution in popular desktop application.
- **CVE-2008-3688**: Chain: Uninitialized variable leads to infinite loop.
- **CVE-2008-3475**: Chain: Improper initialization leads to memory corruption.
- **CVE-2005-1036**: Chain: Bypass of access restrictions due to improper authorization (CWE-862) of a user results from an improperly initialized (CWE-909) I/O permission bitmap
- **CVE-2008-3597**: Chain: game server can access player data structures before initialization has happened leading to NULL dereference
- **CVE-2009-2692**: Chain: Use of an unimplemented network socket operation pointing to an uninitialized handler function (CWE-456) causes a crash because of a null pointer dereference (CWE-476)
- **CVE-2009-0949**: Chain: improper initialization of memory can lead to NULL dereference
- **CVE-2009-3620**: Chain: some unprivileged ioctls do not verify that a structure has been initialized before invocation, leading to NULL dereference

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/908.html
