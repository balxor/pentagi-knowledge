---
capec_id: CAPEC-612
name: WiFi MAC Address Tracking
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-201, CWE-300]
related_attack: []
url: https://capec.mitre.org/data/definitions/612.html
tags: [mitre-capec, attack-pattern, CAPEC-612]
---

# CAPEC-612 - WiFi MAC Address Tracking

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-612](https://capec.mitre.org/data/definitions/612.html)

## Description
In this attack scenario, the attacker passively listens for WiFi messages and logs the associated Media Access Control (MAC) addresses. These addresses are intended to be unique to each wireless device (although they can be configured and changed by software). Once the attacker is able to associate a MAC address with a particular user or set of users (for example, when attending a public event), the attacker can then scan for that MAC address to track that user in the future.

## Prerequisites
- None

## Skills required
- **Low**: Open source and commercial software tools are available and several commercial advertising companies routinely set up tools to collect and monitor MAC addresses.

## Mitigations
- Automatic randomization of WiFi MAC addresses
- Frequent changing of handset and retransmission device

## Related weaknesses (CWE)
- [CWE-201](https://cwe.mitre.org/data/definitions/201.html)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/612.html
