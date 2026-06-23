---
capec_id: CAPEC-477
name: Signature Spoofing by Mixing Signed and Unsigned Content
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-693, CWE-311, CWE-319]
related_attack: []
url: https://capec.mitre.org/data/definitions/477.html
tags: [mitre-capec, attack-pattern, CAPEC-477]
---

# CAPEC-477 - Signature Spoofing by Mixing Signed and Unsigned Content

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-477](https://capec.mitre.org/data/definitions/477.html)

## Description
An attacker exploits the underlying complexity of a data structure that allows for both signed and unsigned content, to cause unsigned data to be processed as though it were signed data.

## Prerequisites
- Signer and recipient are using complex data storage structures that allow for a mix between signed and unsigned data
- Recipient is using signature verification software that does not maintain separation between signed and unsigned data once the signature has been verified.

## Skills required
- **High**: Attacker must be able to create malformed data blobs and know how to insert them in a location that the recipient will visit.

## Mitigations
- Ensure the application is fully patched and does not allow the processing of unsigned data as if it is signed data.

## Related weaknesses (CWE)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)
- [CWE-319](https://cwe.mitre.org/data/definitions/319.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/477.html
