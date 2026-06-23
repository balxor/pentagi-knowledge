---
cwe_id: CWE-788
name: Access of Memory Location After End of Buffer
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/788.html
tags: [mitre-cwe, weakness, CWE-788]
---

# CWE-788 - Access of Memory Location After End of Buffer

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-788](https://cwe.mitre.org/data/definitions/788.html)

## Description
The product reads or writes to a buffer using an index or pointer that references a memory location after the end of the buffer.

## Extended description
This typically occurs when a pointer or its index is incremented to a position after the buffer; or when pointer arithmetic results in a position after the buffer.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality**: Read Memory
- **Integrity, Availability**: Modify Memory, DoS: Crash, Exit, or Restart
- **Integrity**: Modify Memory, Execute Unauthorized Code or Commands

## Related weaknesses
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)

## Observed examples (CVE)
- **CVE-2009-2550**: Classic stack-based buffer overflow in media player using a long entry in a playlist
- **CVE-2009-2403**: Heap-based buffer overflow in media player using a long entry in a playlist
- **CVE-2009-0689**: large precision value in a format string triggers overflow
- **CVE-2009-0558**: attacker-controlled array index leads to code execution
- **CVE-2008-4113**: OS kernel trusts userland-supplied length value, allowing reading of sensitive information
- **CVE-2007-4268**: Chain: integer signedness error (CWE-195) passes signed comparison, leading to heap overflow (CWE-122)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/788.html
