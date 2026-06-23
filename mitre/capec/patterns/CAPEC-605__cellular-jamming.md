---
capec_id: CAPEC-605
name: Cellular Jamming
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/605.html
tags: [mitre-capec, attack-pattern, CAPEC-605]
---

# CAPEC-605 - Cellular Jamming

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-605](https://capec.mitre.org/data/definitions/605.html)

## Description
In this attack scenario, the attacker actively transmits signals to overpower and disrupt the communication between a cellular user device and a cell tower. Several existing techniques are known in the open literature for this attack for 2G, 3G, and 4G LTE cellular technology. For example, some attacks target cell towers by overwhelming them with false status messages, while others introduce high levels of noise on signaling channels.

## Prerequisites
- Lack of anti-jam features in cellular technology (2G, 3G, 4G, LTE)

## Skills required
- **Low**: This attack can be performed by low capability attackers with commercially available tools.

## Consequences
- **Availability**: Resource Consumption (The attacker's goal is to prevent users from accessing the cellular network. Denying connectivity to the cellular network prevents the user from being able to transmit or receive any data, which also prevents VOIP calls, however this attack poses no threat to data confidentiality.)

## Mitigations
- Mitigating this attack requires countermeasures employed on both the retransmission device as well as on the cell tower. Therefore, any system that relies on existing commercial cell towards will likely be vulnerable to this attack. By using a private cellular LTE network (i.e., a custom cell tower), jamming countermeasures could be developed and employed.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/605.html
