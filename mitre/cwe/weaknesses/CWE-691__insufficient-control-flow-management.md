---
cwe_id: CWE-691
name: Insufficient Control Flow Management
type: weakness
abstraction: Pillar
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-29]
url: https://cwe.mitre.org/data/definitions/691.html
tags: [mitre-cwe, weakness, CWE-691]
---

# CWE-691 - Insufficient Control Flow Management

**Abstraction:** Pillar  -  **Status:** Draft  -  **CWE:** [CWE-691](https://cwe.mitre.org/data/definitions/691.html)

## Description
The code does not sufficiently manage its control flow during execution, creating conditions in which the control flow can be modified in unexpected ways.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Other**: Alter Execution Logic

## Related attack patterns (CAPEC)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Observed examples (CVE)
- **CVE-2024-50653**: e-commerce product does not restrict the number of requests for coupons
- **CVE-2019-9805**: Chain: Creation of the packet client occurs before initialization is complete (CWE-696) resulting in a read from uninitialized memory (CWE-908), causing memory corruption.
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.
- **CVE-2011-1027**: Chain: off-by-one error (CWE-193) leads to infinite loop (CWE-835) using invalid hex-encoded characters.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/691.html
