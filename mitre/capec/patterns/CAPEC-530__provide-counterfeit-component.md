---
capec_id: CAPEC-530
name: Provide Counterfeit Component
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/530.html
tags: [mitre-capec, attack-pattern, CAPEC-530]
---

# CAPEC-530 - Provide Counterfeit Component

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-530](https://capec.mitre.org/data/definitions/530.html)

## Description
An attacker provides a counterfeit component during the procurement process of a lower-tier component supplier to a sub-system developer or integrator, which is then built into the system being upgraded or repaired by the victim, allowing the attacker to cause disruption or additional compromise.

## Prerequisites
- Advanced knowledge about the target system and sub-components.

## Skills required
- **High**: Able to develop and manufacture malicious system components that resemble legitimate name-brand components.

## Mitigations
- There are various methods to detect if the component is a counterfeit. See section II of [REF-703] for many techniques.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/530.html
