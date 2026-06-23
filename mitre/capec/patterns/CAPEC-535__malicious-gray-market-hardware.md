---
capec_id: CAPEC-535
name: Malicious Gray Market Hardware
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/535.html
tags: [mitre-capec, attack-pattern, CAPEC-535]
---

# CAPEC-535 - Malicious Gray Market Hardware

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-535](https://capec.mitre.org/data/definitions/535.html)

## Description
An attacker maliciously alters hardware components that will be sold on the gray market, allowing for victim disruption and compromise when the victim needs replacement hardware components for systems where the parts are no longer in regular supply from original suppliers, or where the hardware components from the attacker seems to be a great benefit from a cost perspective.

## Prerequisites
- Physical access to a gray market reseller's hardware components supply, or the ability to appear as a gray market reseller to the victim's buyer.

## Skills required
- **High**: Able to develop and manufacture malicious hardware components that perform the same functions and processes as their non-malicious counterparts.

## Mitigations
- Purchase only from authorized resellers.
- Validate serial numbers from multiple sources

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/535.html
