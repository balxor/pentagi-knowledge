---
capec_id: CAPEC-474
name: Signature Spoofing by Key Theft
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-522]
related_attack: [T1552.004]
url: https://capec.mitre.org/data/definitions/474.html
tags: [mitre-capec, attack-pattern, CAPEC-474]
---

# CAPEC-474 - Signature Spoofing by Key Theft

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-474](https://capec.mitre.org/data/definitions/474.html)

## Description
An attacker obtains an authoritative or reputable signer's private signature key by theft and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Prerequisites
- An authoritative or reputable signer is storing their private signature key with insufficient protection.

## Skills required
- **High**: Ability to compromise systems containing sensitive data
- **Low**: Knowledge of common location methods and access methods to sensitive data

## Mitigations
- Restrict access to private keys from non-supervisory accounts
- Restrict access to administrative personnel and processes only
- Ensure all remote methods are secured
- Ensure all services are patched and up to date

## Related weaknesses (CWE)
- [CWE-522](https://cwe.mitre.org/data/definitions/522.html)

## Related ATT&CK techniques
- T1552.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/474.html
