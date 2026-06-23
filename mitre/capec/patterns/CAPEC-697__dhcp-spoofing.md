---
capec_id: CAPEC-697
name: DHCP Spoofing
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: [CWE-923]
related_attack: [T1557.003]
url: https://capec.mitre.org/data/definitions/697.html
tags: [mitre-capec, attack-pattern, CAPEC-697]
---

# CAPEC-697 - DHCP Spoofing

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-697](https://capec.mitre.org/data/definitions/697.html)

## Description
<xhtml:p>An adversary masquerades as a legitimate Dynamic Host Configuration Protocol (DHCP) server by spoofing DHCP traffic, with the goal of redirecting network traffic or denying service to DHCP.</xhtml:p>

## Extended description
DHCP is broadcast to the entire Local Area Network (LAN) and does not have any form of authentication by default. Therefore, it is susceptible to spoofing. An adversary with access to the target LAN can receive DHCP messages; obtaining the topology information required to potentially manipulate other hosts' network configurations. To improve the likelihood of the DHCP request being serviced by the Rogue server, an adversary can first starve the DHCP pool.

## Prerequisites
- The adversary must have access to a machine within the target LAN which can send DHCP offers to the target.

## Skills required
- **Medium**: The adversary must identify potential targets for DHCP Spoofing and craft network configurations to obtain the desired results.

## Resources required
- The adversary requires access to a machine within the target LAN on a network which does not secure its DHCP traffic through MAC-Forced Forwarding, port security, etc.

## Consequences
- **Access_Control**: Modify Data, Execute Unauthorized Commands
- **Availability**: Resource Consumption
- **Confidentiality**: Read Data
- **Integrity**: Modify Data, Execute Unauthorized Commands

## Execution flow
Execution Flow Explore Determine Exsisting DHCP lease: An adversary observes network traffic and waits for an existing DHCP lease to expire on a target machine in the LAN. Techniques Adversary observes LAN traffic for DHCP solicitations Experiment Capture the DHCP DISCOVER message: The adversary captures "DISCOVER" messages and crafts "OFFER" responses for the identified target MAC address. The success of this attack centers on the capturing of and responding to these "DISCOVER" messages. Techniques Adversary captures and responds to DHCP "DISCOVER" messages tailored to the target subnet. Exploit Compromise Network Access and Collect Network Activity: An adversary successfully acts as a rogue DHCP server by redirecting legitimate DHCP requests to itself. Techniques Adversary sends repeated DHCP "REQUEST" messages to quickly lease all the addresses within network's DHCP pool and forcing new DHCP requests to be handled by the rogue DHCP server.

## Mitigations
- Design: MAC-Forced Forwarding
- Implementation: Port Security and DHCP snooping
- Implementation: Network-based Intrusion Detection Systems

## Related weaknesses (CWE)
- [CWE-923](https://cwe.mitre.org/data/definitions/923.html)

## Related ATT&CK techniques
- T1557.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/697.html
