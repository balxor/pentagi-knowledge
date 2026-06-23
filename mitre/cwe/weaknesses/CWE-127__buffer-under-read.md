---
cwe_id: CWE-127
name: Buffer Under-read
type: weakness
abstraction: Variant
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/127.html
tags: [mitre-cwe, weakness, CWE-127]
---

# CWE-127 - Buffer Under-read

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-127](https://cwe.mitre.org/data/definitions/127.html)

## Description
The product reads from a buffer using buffer access mechanisms such as indexes or pointers that reference memory locations prior to the targeted buffer.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality**: Read Memory
- **Confidentiality**: Bypass Protection Mechanism

## Related weaknesses
- CWE-125 (ChildOf)
- CWE-786 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-40985**: HTML conversion package has a buffer under-read, allowing a crash

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/127.html
