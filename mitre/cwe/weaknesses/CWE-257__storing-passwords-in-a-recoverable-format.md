---
cwe_id: CWE-257
name: Storing Passwords in a Recoverable Format
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-49]
url: https://cwe.mitre.org/data/definitions/257.html
tags: [mitre-cwe, weakness, CWE-257]
---

# CWE-257 - Storing Passwords in a Recoverable Format

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-257](https://cwe.mitre.org/data/definitions/257.html)

## Description
The storage of passwords in a recoverable format makes them subject to password reuse attacks by malicious users. In fact, it should be noted that recoverable encrypted passwords provide no significant benefit over plaintext passwords since they are subject not only to reuse by malicious attackers but also by malicious insiders. If a system administrator can recover a password directly, or use a brute force search on the available information, the administrator can use the password on other accounts.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Access Control**: Gain Privileges or Assume Identity
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Use strong, non-reversible encryption to protect stored passwords.

## Related attack patterns (CAPEC)
- [CAPEC-49](https://capec.mitre.org/data/definitions/49.html)

## Related weaknesses
- CWE-522 (ChildOf)
- CWE-259 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-30018**: A messaging platform serializes all elements of User/Group objects, making private information available to adversaries

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/257.html
