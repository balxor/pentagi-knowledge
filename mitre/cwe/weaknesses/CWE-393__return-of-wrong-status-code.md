---
cwe_id: CWE-393
name: Return of Wrong Status Code
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/393.html
tags: [mitre-cwe, weakness, CWE-393]
---

# CWE-393 - Return of Wrong Status Code

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-393](https://cwe.mitre.org/data/definitions/393.html)

## Description
A function or operation returns an incorrect return value or status code that does not indicate the true result of execution, causing the product to modify its behavior based on the incorrect result.

## Extended description
This can lead to unpredictable behavior. If the function is used to make security-critical decisions or provide security-critical information, then the wrong status code can cause the product to assume that an action is safe or correct, even when it is not.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Unexpected State, Alter Execution Logic

## Related weaknesses
- CWE-684 (ChildOf)
- CWE-703 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-1132**: DNS server returns wrong response code for non-existent AAAA record, which effectively says that the domain is inaccessible.
- **CVE-2001-1509**: Hardware-specific implementation of system call causes incorrect results from geteuid.
- **CVE-2001-1559**: Chain: System call returns wrong value (CWE-393), leading to a resultant NULL dereference (CWE-476).
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/393.html
