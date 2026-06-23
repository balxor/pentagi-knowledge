---
cwe_id: CWE-670
name: Always-Incorrect Control Flow Implementation
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/670.html
tags: [mitre-cwe, weakness, CWE-670]
---

# CWE-670 - Always-Incorrect Control Flow Implementation

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-670](https://cwe.mitre.org/data/definitions/670.html)

## Description
The code contains a control flow path that does not reflect the algorithm that the path is intended to implement, leading to incorrect behavior any time this path is navigated.

## Extended description
This weakness captures cases in which a particular code segment is always incorrect with respect to the algorithm that it is implementing. For example, if a C programmer intends to include multiple statements in a single block but does not include the enclosing braces (CWE-483), then the logic is always incorrect. This issue is in contrast to most weaknesses in which the code usually behaves correctly, except when it is externally manipulated in malicious ways.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other, Alter Execution Logic

## Related weaknesses
- CWE-691 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-3011**: virtual interrupt controller in a virtualization product allows crash of host by writing a certain invalid value to a register, which triggers a fatal error instead of returning an error code

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/670.html
