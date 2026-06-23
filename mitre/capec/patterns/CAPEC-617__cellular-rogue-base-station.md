---
capec_id: CAPEC-617
name: Cellular Rogue Base Station
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/617.html
tags: [mitre-capec, attack-pattern, CAPEC-617]
---

# CAPEC-617 - Cellular Rogue Base Station

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-617](https://capec.mitre.org/data/definitions/617.html)

## Description
In this attack scenario, the attacker imitates a cellular base station with their own "rogue" base station equipment. Since cellular devices connect to whatever station has the strongest signal, the attacker can easily convince a targeted cellular device (e.g. the retransmission device) to talk to the rogue base station.

## Prerequisites
- None

## Skills required
- **Low**: This technique has been demonstrated by amateur hackers and commercial tools and open source projects are available to automate the attack.

## Consequences
- **Confidentiality**: Read Data (Intercept and control cellular data communications to/from mobile device.)

## Mitigations
- Passively monitor cellular network connection for real-time threat detection and logging for manual review.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/617.html
