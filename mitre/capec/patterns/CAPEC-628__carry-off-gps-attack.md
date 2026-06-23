---
capec_id: CAPEC-628
name: Carry-Off GPS Attack
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/628.html
tags: [mitre-capec, attack-pattern, CAPEC-628]
---

# CAPEC-628 - Carry-Off GPS Attack

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-628](https://capec.mitre.org/data/definitions/628.html)

## Description
A common form of a GPS spoofing attack, commonly termed a carry-off attack begins with an adversary broadcasting signals synchronized with the genuine signals observed by the target receiver. The power of the counterfeit signals is then gradually increased and drawn away from the genuine signals. Over time, the adversary can carry the target away from their intended destination and toward a location chosen by the adversary.

## Prerequisites
- The target must be relying on valid GPS signal to perform critical operations.

## Skills required
- **High**: This attack requires advanced knoweldge in GPS technology.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/628.html
