---
capec_id: CAPEC-627
name: Counterfeit GPS Signals
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/627.html
tags: [mitre-capec, attack-pattern, CAPEC-627]
---

# CAPEC-627 - Counterfeit GPS Signals

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-627](https://capec.mitre.org/data/definitions/627.html)

## Description
An adversary attempts to deceive a GPS receiver by broadcasting counterfeit GPS signals, structured to resemble a set of normal GPS signals. These spoofed signals may be structured in such a way as to cause the receiver to estimate its position to be somewhere other than where it actually is, or to be located where it is but at a different time, as determined by the adversary.

## Prerequisites
- The target must be relying on valid GPS signal to perform critical operations.

## Skills required
- **High**: The ability to spoof GPS signals is not trival.

## Resources required
- Ability to create spoofed GPS signals.

## Consequences
- **Integrity**: Modify Data

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/627.html
