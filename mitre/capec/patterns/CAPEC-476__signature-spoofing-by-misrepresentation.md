---
capec_id: CAPEC-476
name: Signature Spoofing by Misrepresentation
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-290]
related_attack: []
url: https://capec.mitre.org/data/definitions/476.html
tags: [mitre-capec, attack-pattern, CAPEC-476]
---

# CAPEC-476 - Signature Spoofing by Misrepresentation

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-476](https://capec.mitre.org/data/definitions/476.html)

## Description
An attacker exploits a weakness in the parsing or display code of the recipient software to generate a data blob containing a supposedly valid signature, but the signer's identity is falsely represented, which can lead to the attacker manipulating the recipient software or its victim user to perform compromising actions.

## Prerequisites
- Recipient is using signature verification software that does not clearly indicate potential homographs in the signer identity.Recipient is using signature verification software that contains a parsing vulnerability, or allows control characters in the signer identity field, such that a signature is mistakenly displayed as valid and from a known or authoritative signer.

## Skills required
- **High**: Attacker may be required to create malformed data blobs and know how to insert them in a location that the recipient will visit.

## Mitigations
- Ensure the application is using parsing and data display techniques that will accurately display control characters, international symbols and markings, and ultimately recognize potential homograph attacks.

## Related weaknesses (CWE)
- [CWE-290](https://cwe.mitre.org/data/definitions/290.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/476.html
