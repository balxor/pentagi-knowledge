---
cwe_id: CWE-244
name: Improper Clearing of Heap Memory Before Release ('Heap Inspection')
type: weakness
abstraction: Variant
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/244.html
tags: [mitre-cwe, weakness, CWE-244]
---

# CWE-244 - Improper Clearing of Heap Memory Before Release ('Heap Inspection')

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-244](https://cwe.mitre.org/data/definitions/244.html)

## Description
Using realloc() to resize buffers that store sensitive information can leave the sensitive information exposed to attack, because it is not removed from memory.

## Extended description
When sensitive data such as a password or an encryption key is not removed from memory, it could be exposed to an attacker using a "heap inspection" attack that reads the sensitive data using memory dumps or other methods. The realloc() function is commonly used to increase the size of a block of allocated memory. This operation often requires copying the contents of the old memory block into a new and larger block. This operation leaves the contents of the original block intact but inaccessible to the program, preventing the program from being able to scrub sensitive data from memory. If an attacker can later examine the contents of a memory dump, the sensitive data could be exposed.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality, Other**: Read Memory, Other

## Related weaknesses
- CWE-226 (ChildOf)
- CWE-669 (CanPrecede)

## Observed examples (CVE)
- **CVE-2019-3733**: Cryptography library does not clear heap memory before release

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/244.html
