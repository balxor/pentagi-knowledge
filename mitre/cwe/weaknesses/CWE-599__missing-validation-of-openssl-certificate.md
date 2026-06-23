---
cwe_id: CWE-599
name: Missing Validation of OpenSSL Certificate
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/599.html
tags: [mitre-cwe, weakness, CWE-599]
---

# CWE-599 - Missing Validation of OpenSSL Certificate

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-599](https://cwe.mitre.org/data/definitions/599.html)

## Description
The product uses OpenSSL and trusts or uses a certificate without using the SSL_get_verify_result() function to ensure that the certificate satisfies all necessary security requirements.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Ensure that proper authentication is included in the system design.
- **Implementation**: Understand and properly implement all checks necessary to ensure the identity of entities involved in encrypted communications.

## Related weaknesses
- CWE-295 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/599.html
