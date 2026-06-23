---
cwe_id: CWE-14
name: Compiler Removal of Code to Clear Buffers
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Compiled]
related_capec: []
url: https://cwe.mitre.org/data/definitions/14.html
tags: [mitre-cwe, weakness, CWE-14]
---

# CWE-14 - Compiler Removal of Code to Clear Buffers

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-14](https://cwe.mitre.org/data/definitions/14.html)

## Description
Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka "dead store removal."

## Extended description
This compiler optimization error occurs when: Secret data are stored in memory. The secret data are scrubbed from memory by overwriting its contents. The source code is compiled using an optimizing compiler, which identifies and removes the function that overwrites the contents as a dead store because the memory is not used subsequently.

## Applicable platforms / languages
C, C++, Compiled

## Common consequences
- **Confidentiality, Access Control**: Read Memory, Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Store the sensitive data in a "volatile" memory location if available.
- **Build and Compilation**: If possible, configure your compiler so that it does not remove dead stores.
- **Architecture and Design**: Where possible, encrypt sensitive data that are used by a software system.

## Related weaknesses
- CWE-733 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/14.html
