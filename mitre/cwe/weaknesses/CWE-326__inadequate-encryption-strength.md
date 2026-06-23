---
cwe_id: CWE-326
name: Inadequate Encryption Strength
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-112, CAPEC-192, CAPEC-20]
url: https://cwe.mitre.org/data/definitions/326.html
tags: [mitre-cwe, weakness, CWE-326]
---

# CWE-326 - Inadequate Encryption Strength

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-326](https://cwe.mitre.org/data/definitions/326.html)

## Description
The product stores or transmits sensitive data using an encryption scheme that is theoretically sound, but is not strong enough for the level of protection required.

## Extended description
A weak encryption scheme can be subjected to brute force attacks that have a reasonable chance of succeeding using current attack methods and resources.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Confidentiality**: Bypass Protection Mechanism, Read Application Data

## Potential mitigations
- **Architecture and Design**: Use an encryption scheme that is currently considered to be strong by experts in the field.

## Related attack patterns (CAPEC)
- [CAPEC-112](https://capec.mitre.org/data/definitions/112.html)
- [CAPEC-192](https://capec.mitre.org/data/definitions/192.html)
- [CAPEC-20](https://capec.mitre.org/data/definitions/20.html)

## Related weaknesses
- CWE-693 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-1546**: Weak encryption
- **CVE-2004-2172**: Weak encryption (chosen plaintext attack)
- **CVE-2002-1682**: Weak encryption
- **CVE-2002-1697**: Weak encryption produces same ciphertext from the same plaintext blocks.
- **CVE-2002-1739**: Weak encryption
- **CVE-2005-2281**: Weak encryption scheme
- **CVE-2002-1872**: Weak encryption (XOR)
- **CVE-2002-1910**: Weak encryption (reversible algorithm).
- **CVE-2002-1946**: Weak encryption (one-to-one mapping).
- **CVE-2002-1975**: Encryption error uses fixed salt, simplifying brute force / dictionary attacks (overlaps randomness).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/326.html
