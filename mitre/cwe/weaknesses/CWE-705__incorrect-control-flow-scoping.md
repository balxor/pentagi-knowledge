---
cwe_id: CWE-705
name: Incorrect Control Flow Scoping
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/705.html
tags: [mitre-cwe, weakness, CWE-705]
---

# CWE-705 - Incorrect Control Flow Scoping

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-705](https://cwe.mitre.org/data/definitions/705.html)

## Description
The product does not properly return control flow to the proper location after it has completed a task or detected an unusual condition.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Alter Execution Logic, Other

## Related weaknesses
- CWE-691 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-21087**: Java code in a smartphone OS can encounter a "boot loop" due to an uncaught exception
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/705.html
