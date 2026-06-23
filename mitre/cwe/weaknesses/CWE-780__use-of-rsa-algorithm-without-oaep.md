---
cwe_id: CWE-780
name: Use of RSA Algorithm without OAEP
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/780.html
tags: [mitre-cwe, weakness, CWE-780]
---

# CWE-780 - Use of RSA Algorithm without OAEP

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-780](https://cwe.mitre.org/data/definitions/780.html)

## Description
The product uses the RSA algorithm but does not incorporate Optimal Asymmetric Encryption Padding (OAEP), which might weaken the encryption.

## Extended description
Padding schemes are often used with cryptographic algorithms to make the plaintext less predictable and complicate attack efforts. The OAEP scheme is often used with RSA to nullify the impact of predictable common text.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related weaknesses
- CWE-327 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/780.html
