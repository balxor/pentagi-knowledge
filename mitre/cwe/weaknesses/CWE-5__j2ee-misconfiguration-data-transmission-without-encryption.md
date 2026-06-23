---
cwe_id: CWE-5
name: J2EE Misconfiguration: Data Transmission Without Encryption
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/5.html
tags: [mitre-cwe, weakness, CWE-5]
---

# CWE-5 - J2EE Misconfiguration: Data Transmission Without Encryption

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-5](https://cwe.mitre.org/data/definitions/5.html)

## Description
Information sent over a network can be compromised while in transit. An attacker may be able to read or modify the contents if the data are sent in plaintext or are weakly encrypted.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Modify Application Data

## Potential mitigations
- **System Configuration**: The product configuration should ensure that SSL or an encryption mechanism of equivalent strength and vetted reputation is used for all access-controlled pages.

## Related weaknesses
- CWE-319 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/5.html
