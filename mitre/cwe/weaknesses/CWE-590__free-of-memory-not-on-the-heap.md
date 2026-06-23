---
cwe_id: CWE-590
name: Free of Memory not on the Heap
type: weakness
abstraction: Variant
status: Incomplete
languages: [Memory-Unsafe, C]
related_capec: []
url: https://cwe.mitre.org/data/definitions/590.html
tags: [mitre-cwe, weakness, CWE-590]
---

# CWE-590 - Free of Memory not on the Heap

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-590](https://cwe.mitre.org/data/definitions/590.html)

## Description
The product calls free() on a pointer to memory that was not allocated using associated heap allocation functions such as malloc(), calloc(), or realloc().

## Extended description
When free() is called on an invalid pointer, the program's memory management data structures may become corrupted. This corruption can cause the program to crash or, in some circumstances, an attacker may be able to cause free() to operate on controllable memory locations to modify critical program variables or execute code.

## Applicable platforms / languages
Memory-Unsafe, C

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands, Modify Memory

## Potential mitigations
- **Implementation**: Only free pointers that you have called malloc on previously. This is the recommended solution. Keep track of which pointers point at the beginning of valid chunks and free them only once.
- **Implementation**: Before freeing a pointer, the programmer should make sure that the pointer was previously allocated on the heap and that the memory belongs to the programmer. Freeing an unallocated pointer will cause undefined behavior in the program.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, glibc in Linux provides protection against free of invalid pointers.
- **Architecture and Design**: Use a language that provides abstractions for memory allocation and deallocation.

## Related weaknesses
- CWE-762 (ChildOf)
- CWE-123 (CanPrecede)

## Observed examples (CVE)
- **CVE-2023-22291**: parser for a word processor attempts to free a stack pointer when intending to expand memory to hold a larger buffer

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/590.html
