---
cwe_id: CWE-484
name: Omitted Break Statement in Switch
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, Java, C#, PHP, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/484.html
tags: [mitre-cwe, weakness, CWE-484]
---

# CWE-484 - Omitted Break Statement in Switch

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-484](https://cwe.mitre.org/data/definitions/484.html)

## Description
The product omits a break statement within a switch or similar construct, causing code associated with multiple conditions to execute. This can cause problems when the programmer only intended to execute code associated with one condition.

## Extended description
This can lead to critical code executing in situations where it should not.

## Applicable platforms / languages
C, C++, Java, C#, PHP, Not Language-Specific

## Common consequences
- **Other**: Alter Execution Logic

## Potential mitigations
- **Implementation**: Omitting a break statement so that one may fall through is often indistinguishable from an error, and therefore should be avoided. If you need to use fall-through capabilities, make sure that you have clearly documented this within the switch statement, and ensure that you have examined all the logical possibilities.
- **Implementation**: The functionality of omitting a break statement could be clarified with an if statement. This method is much safer.

## Related weaknesses
- CWE-710 (ChildOf)
- CWE-670 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/484.html
