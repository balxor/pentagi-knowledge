---
capec_id: CAPEC-473
name: Signature Spoof
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-20, CWE-327, CWE-290]
related_attack: [T1036.001, T1553.002]
url: https://capec.mitre.org/data/definitions/473.html
tags: [mitre-capec, attack-pattern, CAPEC-473]
---

# CAPEC-473 - Signature Spoof

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-473](https://capec.mitre.org/data/definitions/473.html)

## Description
An attacker generates a message or datablock that causes the recipient to believe that the message or datablock was generated and cryptographically signed by an authoritative or reputable source, misleading a victim or victim operating system into performing malicious actions.

## Prerequisites
- The victim or victim system is dependent upon a cryptographic signature-based verification system for validation of one or more security events or actions.
- The validation can be bypassed via an attacker-provided signature that makes it appear that the legitimate authoritative or reputable source provided the signature.

## Skills required
- **High**: Technical understanding of how signature verification algorithms work with data and applications

## Consequences
- **Access_Control**: Gain Privileges
- **Authentication**: Gain Privileges

## Related weaknesses (CWE)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-327](https://cwe.mitre.org/data/definitions/327.html)
- [CWE-290](https://cwe.mitre.org/data/definitions/290.html)

## Related ATT&CK techniques
- T1036.001
- T1553.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/473.html
