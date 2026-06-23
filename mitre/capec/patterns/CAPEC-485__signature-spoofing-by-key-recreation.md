---
capec_id: CAPEC-485
name: Signature Spoofing by Key Recreation
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-330]
related_attack: [T1552.004]
url: https://capec.mitre.org/data/definitions/485.html
tags: [mitre-capec, attack-pattern, CAPEC-485]
---

# CAPEC-485 - Signature Spoofing by Key Recreation

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-485](https://capec.mitre.org/data/definitions/485.html)

## Description
An attacker obtains an authoritative or reputable signer's private signature key by exploiting a cryptographic weakness in the signature algorithm or pseudorandom number generation and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Prerequisites
- An authoritative signer is using a weak method of random number generation or weak signing software that causes key leakage or permits key inference.
- An authoritative signer is using a signature algorithm with a direct weakness or with poorly chosen parameters that enable the key to be recovered using signatures from that signer.

## Skills required
- **High**: Ability to create malformed data blobs and know how to present them directly or indirectly to a victim.

## Mitigations
- Ensure cryptographic elements have been sufficiently tested for weaknesses.

## Related weaknesses (CWE)
- [CWE-330](https://cwe.mitre.org/data/definitions/330.html)

## Related ATT&CK techniques
- T1552.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/485.html
