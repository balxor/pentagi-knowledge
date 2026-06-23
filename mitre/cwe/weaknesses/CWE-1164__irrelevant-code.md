---
cwe_id: CWE-1164
name: Irrelevant Code
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1164.html
tags: [mitre-cwe, weakness, CWE-1164]
---

# CWE-1164 - Irrelevant Code

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1164](https://cwe.mitre.org/data/definitions/1164.html)

## Description
The product contains code that is not essential for execution, i.e. makes no state changes and has no side effects that alter data or control flow, such that removal of the code would have no impact to functionality or correctness.

## Extended description
Irrelevant code could include dead code, initialization that is not used, empty blocks, code that could be entirely removed due to optimization, etc.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability
- **Other**: Reduce Performance

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1164.html
