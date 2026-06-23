---
cwe_id: CWE-126
name: Buffer Over-read
type: weakness
abstraction: Variant
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/126.html
tags: [mitre-cwe, weakness, CWE-126]
---

# CWE-126 - Buffer Over-read

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-126](https://cwe.mitre.org/data/definitions/126.html)

## Description
The product reads from a buffer using buffer access mechanisms such as indexes or pointers that reference memory locations after the targeted buffer.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality**: Read Memory
- **Confidentiality**: Bypass Protection Mechanism
- **Availability, Integrity**: DoS: Crash, Exit, or Restart

## Related weaknesses
- CWE-125 (ChildOf)
- CWE-788 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-1733**: Text editor has out-of-bounds read past end of line while indenting C code
- **CVE-2014-0160**: Chain: "Heartbleed" bug receives an inconsistent length parameter (CWE-130) enabling an out-of-bounds read (CWE-126), returning memory that could include private cryptographic keys and other sensitive data.
- **CVE-2009-2523**: Chain: product does not handle when an input string is not NULL terminated, leading to buffer over-read or heap-based buffer overflow.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/126.html
