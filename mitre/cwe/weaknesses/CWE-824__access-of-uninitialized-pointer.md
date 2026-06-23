---
cwe_id: CWE-824
name: Access of Uninitialized Pointer
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/824.html
tags: [mitre-cwe, weakness, CWE-824]
---

# CWE-824 - Access of Uninitialized Pointer

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-824](https://cwe.mitre.org/data/definitions/824.html)

## Description
The product accesses or uses a pointer that has not been initialized.

## Extended description
If the pointer contains an uninitialized value, then the value might not point to a valid memory location. This could cause the product to read from or write to unexpected memory locations, leading to a denial of service. If the uninitialized pointer is used as a function call, then arbitrary functions could be invoked. If an attacker can influence the portion of uninitialized memory that is contained in the pointer, this weakness could be leveraged to execute code or perform other attacks. Depending on memory layout, associated memory management behaviors, and product operation, the attacker might be able to influence the contents of the uninitialized pointer, thus gaining more fine-grained control of the memory location to be accessed.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality**: Read Memory
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands

## Related weaknesses
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-125 (CanPrecede)
- CWE-787 (CanPrecede)

## Observed examples (CVE)
- **CVE-2024-32878**: LLM product has a free of an uninitialized pointer
- **CVE-2019-3836**: Chain: secure communications library does not initialize a local variable for a data structure (CWE-456), leading to access of an uninitialized pointer (CWE-824).
- **CVE-2018-14641**: Chain: C union member is not initialized (CWE-456), leading to access of invalid pointer (CWE-824)
- **CVE-2010-0211**: chain: unchecked return value (CWE-252) leads to free of invalid, uninitialized pointer (CWE-824).
- **CVE-2009-2768**: Pointer in structure is not initialized, leading to NULL pointer dereference (CWE-476) and system crash.
- **CVE-2009-1721**: Free of an uninitialized pointer.
- **CVE-2009-1415**: Improper handling of invalid signatures leads to free of invalid pointer.
- **CVE-2009-0846**: Invalid encoding triggers free of uninitialized pointer.
- **CVE-2009-0040**: Crafted PNG image leads to free of uninitialized pointer.
- **CVE-2008-2934**: Crafted GIF image leads to free of uninitialized pointer.
- **CVE-2007-4682**: Access of uninitialized pointer might lead to code execution.
- **CVE-2007-4639**: Step-based manipulation: invocation of debugging function before the primary initialization function leads to access of an uninitialized pointer and code execution.
- **CVE-2007-4000**: Unchecked return values can lead to a write to an uninitialized pointer.
- **CVE-2007-2442**: zero-length input leads to free of uninitialized pointer.
- **CVE-2007-1213**: Crafted font leads to uninitialized function pointer.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/824.html
