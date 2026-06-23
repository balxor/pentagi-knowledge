---
capec_id: CAPEC-606
name: Weakening of Cellular Encryption
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-757]
related_attack: []
url: https://capec.mitre.org/data/definitions/606.html
tags: [mitre-capec, attack-pattern, CAPEC-606]
---

# CAPEC-606 - Weakening of Cellular Encryption

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-606](https://capec.mitre.org/data/definitions/606.html)

## Description
An attacker, with control of a Cellular Rogue Base Station or through cooperation with a Malicious Mobile Network Operator can force the mobile device (e.g., the retransmission device) to use no encryption (A5/0 mode) or to use easily breakable encryption (A5/1 or A5/2 mode).

## Prerequisites
- Cellular devices that allow negotiating security modes to facilitate backwards compatibility and roaming on legacy networks.

## Skills required
- **Medium**: Adversaries can purchase and implement rogue BTS stations at a cost effective rate, and can push a mobile device to downgrade to a non-secure cellular protocol like 2G over GSM or CDMA.

## Consequences
- **Confidentiality**: Other (Tracking, Network Reconnaissance)

## Mitigations
- Use of hardened baseband firmware on retransmission device to detect and prevent the use of weak cellular encryption.
- Monitor cellular RF interface to detect the usage of weaker-than-expected cellular encryption.

## Related weaknesses (CWE)
- [CWE-757](https://cwe.mitre.org/data/definitions/757.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/606.html
