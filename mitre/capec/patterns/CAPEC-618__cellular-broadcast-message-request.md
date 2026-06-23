---
capec_id: CAPEC-618
name: Cellular Broadcast Message Request
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-201]
related_attack: []
url: https://capec.mitre.org/data/definitions/618.html
tags: [mitre-capec, attack-pattern, CAPEC-618]
---

# CAPEC-618 - Cellular Broadcast Message Request

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-618](https://capec.mitre.org/data/definitions/618.html)

## Description
In this attack scenario, the attacker uses knowledge of the target’s mobile phone number (i.e., the number associated with the SIM used in the retransmission device) to cause the cellular network to send broadcast messages to alert the mobile device. Since the network knows which cell tower the target’s mobile device is attached to, the broadcast messages are only sent in the Location Area Code (LAC) where the target is currently located. By triggering the cellular broadcast message and then listening for the presence or absence of that message, an attacker could verify that the target is in (or not in) a given location.

## Prerequisites
- The attacker must have knowledge of the target’s mobile phone number.

## Skills required
- **Low**: Open source and commercial tools are available for this attack.

## Consequences
- **Other**: Other (An attacker could verify that the target is in (or not in) a given location.)

## Mitigations
- Frequent changing of mobile number.

## Related weaknesses (CWE)
- [CWE-201](https://cwe.mitre.org/data/definitions/201.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/618.html
