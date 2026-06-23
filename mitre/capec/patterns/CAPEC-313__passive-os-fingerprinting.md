---
capec_id: CAPEC-313
name: Passive OS Fingerprinting
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Low
related_cwe: [CWE-200]
related_attack: [T1082]
url: https://capec.mitre.org/data/definitions/313.html
tags: [mitre-capec, attack-pattern, CAPEC-313]
---

# CAPEC-313 - Passive OS Fingerprinting

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Low  -  **CAPEC:** [CAPEC-313](https://capec.mitre.org/data/definitions/313.html)

## Description
An adversary engages in activity to detect the version or type of OS software in a an environment by passively monitoring communication between devices, nodes, or applications. Passive techniques for operating system detection send no actual probes to a target, but monitor network or client-server communication between nodes in order to identify operating systems based on observed behavior as compared to a database of known signatures or values. While passive OS fingerprinting is not usually as reliable as active methods, it is generally better able to evade detection.

## Prerequisites
- The ability to monitor network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources required
- Any tool capable of monitoring network communications, like a packet sniffer (e.g., Wireshark)

## Consequences
- **Access_Control**: Hide Activities
- **Authorization**: Hide Activities
- **Confidentiality**: Read Data, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1082

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/313.html
