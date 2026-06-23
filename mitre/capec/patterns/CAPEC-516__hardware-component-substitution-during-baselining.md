---
capec_id: CAPEC-516
name: Hardware Component Substitution During Baselining
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.003]
url: https://capec.mitre.org/data/definitions/516.html
tags: [mitre-capec, attack-pattern, CAPEC-516]
---

# CAPEC-516 - Hardware Component Substitution During Baselining

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-516](https://capec.mitre.org/data/definitions/516.html)

## Description
An adversary with access to system components during allocated baseline development can substitute a maliciously altered hardware component for a baseline component during the product development and research phases. This can lead to adjustments and calibrations being made in the product so that when the final product, now containing the modified component, is deployed it will not perform as designed and be advantageous to the adversary.

## Prerequisites
- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills required
- **High**: Resources to physically infiltrate supplier.
- **Medium**: Intelligence data on victim's purchasing habits.

## Mitigations
- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.

## Related ATT&CK techniques
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/516.html
