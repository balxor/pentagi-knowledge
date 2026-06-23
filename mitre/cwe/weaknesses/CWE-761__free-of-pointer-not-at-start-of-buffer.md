---
cwe_id: CWE-761
name: Free of Pointer not at Start of Buffer
type: weakness
abstraction: Variant
status: Incomplete
languages: [Memory-Unsafe, C]
related_capec: []
url: https://cwe.mitre.org/data/definitions/761.html
tags: [mitre-cwe, weakness, CWE-761]
---

# CWE-761 - Free of Pointer not at Start of Buffer

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-761](https://cwe.mitre.org/data/definitions/761.html)

## Description
The product calls free() on a pointer to a memory resource that was allocated on the heap, but the pointer is not at the start of the buffer.

## Extended description
This can cause the product to crash, or in some cases, modify critical program variables or execute code. This weakness often occurs when the memory is allocated explicitly on the heap with one of the malloc() family functions and free() is called, but pointer arithmetic has caused the pointer to be in the interior or end of the buffer.

## Applicable platforms / languages
Memory-Unsafe, C

## Common consequences
- **Integrity, Availability, Confidentiality**: Modify Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: When utilizing pointer arithmetic to traverse a buffer, use a separate variable to track progress through memory and preserve the originally allocated address for later freeing.
- **Implementation**: When programming in C++, consider using smart pointers provided by the boost library to help correctly and consistently manage memory.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, glibc in Linux provides protection against free of invalid pointers.
- **Architecture and Design**: Use a language that provides abstractions for memory allocation and deallocation.

## Related weaknesses
- CWE-763 (ChildOf)
- CWE-404 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-11930**: function "internally calls 'calloc' and returns a pointer at an index... inside the allocated buffer. This led to freeing invalid memory."

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/761.html
