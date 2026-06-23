---
cwe_id: CWE-135
name: Incorrect Calculation of Multi-Byte String Length
type: weakness
abstraction: Base
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/135.html
tags: [mitre-cwe, weakness, CWE-135]
---

# CWE-135 - Incorrect Calculation of Multi-Byte String Length

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-135](https://cwe.mitre.org/data/definitions/135.html)

## Description
The product does not correctly calculate the length of strings that can contain wide or multi-byte characters.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Availability, Confidentiality**: Read Memory, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Confidentiality**: Read Memory

## Potential mitigations
- **Implementation**: Always verify the length of the string unit character.
- **Implementation**: Use length computing functions (e.g. strlen, wcslen, etc.) appropriately with their equivalent type (e.g.: byte, wchar_t, etc.)

## Related weaknesses
- CWE-682 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/135.html
