---
capec_id: CAPEC-158
name: Sniffing Network Traffic
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-311]
related_attack: [T1040, T1111]
url: https://capec.mitre.org/data/definitions/158.html
tags: [mitre-capec, attack-pattern, CAPEC-158]
---

# CAPEC-158 - Sniffing Network Traffic

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-158](https://capec.mitre.org/data/definitions/158.html)

## Description
In this attack pattern, the adversary monitors network traffic between nodes of a public or multicast network in an attempt to capture sensitive information at the protocol level. Network sniffing applications can reveal TCP/IP, DNS, Ethernet, and other low-level network communication information. The adversary takes a passive role in this attack pattern and simply observes and analyzes the traffic. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the target information.

## Prerequisites
- The target must be communicating on a network protocol visible by a network sniffing application.
- The adversary must obtain a logical position on the network from intercepting target network traffic is possible. Depending on the network topology, traffic sniffing may be simple or challenging. If both the target sender and target recipient are members of a single subnet, the adversary must also be on that subnet in order to see their traffic communication.

## Skills required
- **Low**: Adversaries can obtain and set up open-source network sniffing tools easily.

## Resources required
- A tool with the capability of presenting network communication traffic (e.g., Wireshark, tcpdump, Cain and Abel, etc.).

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Obfuscate network traffic through encryption to prevent its readability by network sniffers.
- Employ appropriate levels of segmentation to your network in accordance with best practices.

## Related weaknesses (CWE)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)

## Related ATT&CK techniques
- T1040
- T1111

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/158.html
