---
capec_id: CAPEC-157
name: Sniffing Attacks
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-311]
related_attack: []
url: https://capec.mitre.org/data/definitions/157.html
tags: [mitre-capec, attack-pattern, CAPEC-157]
---

# CAPEC-157 - Sniffing Attacks

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-157](https://capec.mitre.org/data/definitions/157.html)

## Description
In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient. Sniffing Attacks are similar to Adversary-In-The-Middle attacks (CAPEC-94), but are entirely passive. AiTM attacks are predominantly active and often alter the content of the communications themselves.

## Prerequisites
- The target data stream must be transmitted on a medium to which the adversary has access.

## Resources required
- The adversary must be able to intercept the transmissions containing the data of interest. Depending on the medium of transmission and the path the data takes between the sender and recipient, the adversary may require special equipment and/or require that this equipment be placed in specific locations (e.g., a network sniffing tool)

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Determine Communication Mechanism: The adversary determines the nature and mechanism of communication between two components, looking for opportunities to exploit. Techniques Look for application documentation that might describe a communication mechanism used by a target. Experiment Position In Between Targets: The adversary positions themselves somewhere in the middle of the two components. If the communication is encrypted, the adversary will need to act as a proxy and route traffic between the components, exploiting a flaw in the encryption mechanism. Otherwise, the adversary can just observe the communication at either end. Techniques Use Wireshark or some other packet capturing tool to capture traffic on a network. Install spyware on a client that will intercept outgoing packets and route them to their destination as well as route incoming packets back to the client. Exploit a weakness in an encrypted communication mechanism to gain access to traffic. Look for outdated mechanisms such as SSL. Exploit Listen to Communication: The adversary observes communication, but does not alter or block it. The adversary gains access to sensitive information and can potentially utilize this information in a malicious way.

## Mitigations
- Encrypt sensitive information when transmitted on insecure mediums to prevent interception.

## Related weaknesses (CWE)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/157.html
