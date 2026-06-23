---
capec_id: CAPEC-615
name: Evil Twin Wi-Fi Attack
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-300]
related_attack: []
url: https://capec.mitre.org/data/definitions/615.html
tags: [mitre-capec, attack-pattern, CAPEC-615]
---

# CAPEC-615 - Evil Twin Wi-Fi Attack

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-615](https://capec.mitre.org/data/definitions/615.html)

## Description
Adversaries install Wi-Fi equipment that acts as a legitimate Wi-Fi network access point. When a device connects to this access point, Wi-Fi data traffic is intercepted, captured, and analyzed. This also allows the adversary to use "adversary-in-the-middle" (CAPEC-94) for all communications.

## Prerequisites
- None

## Consequences
- **Confidentiality**: Read Data (Intercept and control Wi-Fi data communications to/from mobile device.)

## Mitigations
- Commercial defensive technology that monitors for rogue Wi-Fi access points, adversary-in-the-middle attacks, and anomalous activity with the mobile device baseband radios.

## Related weaknesses (CWE)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/615.html
