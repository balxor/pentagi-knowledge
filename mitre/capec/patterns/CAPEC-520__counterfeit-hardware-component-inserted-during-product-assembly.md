---
capec_id: CAPEC-520
name: Counterfeit Hardware Component Inserted During Product Assembly
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.003]
url: https://capec.mitre.org/data/definitions/520.html
tags: [mitre-capec, attack-pattern, CAPEC-520]
---

# CAPEC-520 - Counterfeit Hardware Component Inserted During Product Assembly

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-520](https://capec.mitre.org/data/definitions/520.html)

## Description
An adversary with either direct access to the product assembly process or to the supply of subcomponents used in the product assembly process introduces counterfeit hardware components into product assembly. The assembly containing the counterfeit components results in a system specifically designed for malicious purposes.

## Prerequisites
- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills required
- **High**: Resources to physically infiltrate manufacturer or manufacturer's supplier.

## Mitigations
- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.

## Related ATT&CK techniques
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/520.html
