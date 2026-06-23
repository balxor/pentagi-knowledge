---
cwe_id: CWE-561
name: Dead Code
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/561.html
tags: [mitre-cwe, weakness, CWE-561]
---

# CWE-561 - Dead Code

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-561](https://cwe.mitre.org/data/definitions/561.html)

## Description
The product contains dead code, which can never be executed.

## Extended description
Dead code is code that can never be executed in a running program. The surrounding code makes it impossible for a section of code to ever be executed.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation
- **Other**: Reduce Maintainability

## Potential mitigations
- **Implementation**: Remove dead code before deploying the application.

## Related weaknesses
- CWE-1164 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/561.html
