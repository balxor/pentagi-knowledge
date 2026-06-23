---
cwe_id: CWE-1114
name: Inappropriate Whitespace Style
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1114.html
tags: [mitre-cwe, weakness, CWE-1114]
---

# CWE-1114 - Inappropriate Whitespace Style

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1114](https://cwe.mitre.org/data/definitions/1114.html)

## Description
The source code contains whitespace that is inconsistent across the code or does not follow expected standards for the product.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Increase Analytical Complexity
- **Other**: Reduce Maintainability

## Related weaknesses
- CWE-1078 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1114.html
