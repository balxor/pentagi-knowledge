---
cwe_id: CWE-318
name: Cleartext Storage of Sensitive Information in Executable
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-37, CAPEC-65]
url: https://cwe.mitre.org/data/definitions/318.html
tags: [mitre-cwe, weakness, CWE-318]
---

# CWE-318 - Cleartext Storage of Sensitive Information in Executable

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-318](https://cwe.mitre.org/data/definitions/318.html)

## Description
The product stores sensitive information in cleartext in an executable.

## Extended description
Attackers can reverse engineer binary code to obtain secret data. This is especially easy when the cleartext is plain ASCII. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related attack patterns (CAPEC)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-65](https://capec.mitre.org/data/definitions/65.html)

## Related weaknesses
- CWE-312 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1794**: Product stores RSA private key in a DLL and uses it to sign a certificate, allowing spoofing of servers and Adversary-in-the-Middle (AITM) attacks.
- **CVE-2001-1527**: administration passwords in cleartext in executable

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/318.html
