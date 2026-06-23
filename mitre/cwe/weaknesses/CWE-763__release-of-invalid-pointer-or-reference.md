---
cwe_id: CWE-763
name: Release of Invalid Pointer or Reference
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/763.html
tags: [mitre-cwe, weakness, CWE-763]
---

# CWE-763 - Release of Invalid Pointer or Reference

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-763](https://cwe.mitre.org/data/definitions/763.html)

## Description
The product attempts to return a memory resource to the system, but it calls the wrong release function or calls the appropriate release function incorrectly.

## Extended description
This weakness can take several forms, such as: The memory was allocated, explicitly or implicitly, via one memory management method and deallocated using a different, non-compatible function (CWE-762). The function calls or memory management routines chosen are appropriate, however they are used incorrectly, such as in CWE-761.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Integrity, Availability, Confidentiality**: Modify Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Only call matching memory management functions. Do not mix and match routines. For example, when you allocate a buffer with malloc(), dispose of the original pointer with free().
- **Implementation**: When programming in C++, consider using smart pointers provided by the boost library to help correctly and consistently manage memory.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, glibc in Linux provides protection against free of invalid pointers.
- **Architecture and Design**: Use a language that provides abstractions for memory allocation and deallocation.

## Related weaknesses
- CWE-404 (ChildOf)
- CWE-404 (ChildOf)
- CWE-404 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-11930**: function "internally calls 'calloc' and returns a pointer at an index... inside the allocated buffer. This led to freeing invalid memory."

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/763.html
