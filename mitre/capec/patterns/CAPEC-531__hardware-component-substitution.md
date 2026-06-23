---
capec_id: CAPEC-531
name: Hardware Component Substitution
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.003]
url: https://capec.mitre.org/data/definitions/531.html
tags: [mitre-capec, attack-pattern, CAPEC-531]
---

# CAPEC-531 - Hardware Component Substitution

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-531](https://capec.mitre.org/data/definitions/531.html)

## Description
An attacker substitutes out a tested and approved hardware component for a maliciously-altered hardware component. This type of attack is carried out directly on the system, enabling the attacker to then cause disruption or additional compromise.

## Prerequisites
- Physical access to the system or the integration facility where hardware components are kept.

## Skills required
- **High**: Able to develop and manufacture malicious system components that perform the same functions and processes as their non-malicious counterparts.

## Related ATT&CK techniques
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/531.html
