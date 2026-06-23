---
cwe_id: CWE-483
name: Incorrect Block Delimitation
type: weakness
abstraction: Base
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/483.html
tags: [mitre-cwe, weakness, CWE-483]
---

# CWE-483 - Incorrect Block Delimitation

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-483](https://cwe.mitre.org/data/definitions/483.html)

## Description
The code does not explicitly delimit a block that is intended to contain 2 or more statements, creating a logic error.

## Extended description
In some languages, braces (or other delimiters) are optional for blocks. When the delimiter is omitted, it is possible to insert a logic error in which a statement is thought to be in a block but is not. In some cases, the logic error can have security implications.

## Applicable platforms / languages
C, C++

## Common consequences
- **Confidentiality, Integrity, Availability**: Alter Execution Logic

## Potential mitigations
- **Implementation**: Always use explicit block delimitation and use static-analysis technologies to enforce this practice.

## Related weaknesses
- CWE-670 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/483.html
