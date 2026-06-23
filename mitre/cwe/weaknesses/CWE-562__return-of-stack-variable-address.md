---
cwe_id: CWE-562
name: Return of Stack Variable Address
type: weakness
abstraction: Base
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/562.html
tags: [mitre-cwe, weakness, CWE-562]
---

# CWE-562 - Return of Stack Variable Address

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-562](https://cwe.mitre.org/data/definitions/562.html)

## Description
A function returns the address of a stack variable, which will cause unintended program behavior, typically in the form of a crash.

## Extended description
Because local variables are allocated on the stack, when a program returns a pointer to a local variable, it is returning a stack address. A subsequent function call is likely to re-use this same stack address, thereby overwriting the value of the pointer, which no longer corresponds to the same variable since a function's stack frame is invalidated when it returns. At best this will cause the value of the pointer to change unexpectedly. In many cases it causes the program to crash the next time the pointer is dereferenced.

## Applicable platforms / languages
C, C++

## Common consequences
- **Availability, Integrity, Confidentiality**: Read Memory, Modify Memory, Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Fix the code so that it does not return a stack address.

## Related weaknesses
- CWE-758 (ChildOf)
- CWE-672 (CanPrecede)
- CWE-825 (CanPrecede)

## Observed examples (CVE)
- **CVE-2024-33045**: product returns stack variable address, leading to memory corruption

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/562.html
