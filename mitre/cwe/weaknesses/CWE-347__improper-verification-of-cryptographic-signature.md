---
cwe_id: CWE-347
name: Improper Verification of Cryptographic Signature
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-463, CAPEC-475]
url: https://cwe.mitre.org/data/definitions/347.html
tags: [mitre-cwe, weakness, CWE-347]
---

# CWE-347 - Improper Verification of Cryptographic Signature

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-347](https://cwe.mitre.org/data/definitions/347.html)

## Description
The product does not verify, or incorrectly verifies, the cryptographic signature for data.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Integrity, Confidentiality**: Gain Privileges or Assume Identity, Modify Application Data, Execute Unauthorized Code or Commands

## Related attack patterns (CAPEC)
- [CAPEC-463](https://capec.mitre.org/data/definitions/463.html)
- [CAPEC-475](https://capec.mitre.org/data/definitions/475.html)

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-345 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1796**: Does not properly verify signatures for "trusted" entities.
- **CVE-2005-2181**: Insufficient verification allows spoofing.
- **CVE-2005-2182**: Insufficient verification allows spoofing.
- **CVE-2002-1706**: Accepts a configuration file without a Message Integrity Check (MIC) signature.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/347.html
