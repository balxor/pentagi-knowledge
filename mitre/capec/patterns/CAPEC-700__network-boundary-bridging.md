---
capec_id: CAPEC-700
name: Network Boundary Bridging
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: []
related_attack: [T1599]
url: https://capec.mitre.org/data/definitions/700.html
tags: [mitre-capec, attack-pattern, CAPEC-700]
---

# CAPEC-700 - Network Boundary Bridging

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-700](https://capec.mitre.org/data/definitions/700.html)

## Description
An adversary which has gained elevated access to network boundary devices may use these devices to create a channel to bridge trusted and untrusted networks. Boundary devices do not necessarily have to be on the network’s edge, but rather must serve to segment portions of the target network the adversary wishes to cross into.

## Extended description
Network boundary devices are network devices such as routers and firewalls which segment networks by restricting certain types of traffic from flowing through the device. Network boundary devices are often directly accessible through a portal page for management purposes. An adversary’s goal when conducting network boundary bridging is to connect networks which are being segmented by the device. To do so, the adversary must first compromise the network boundary device.

## Prerequisites
- The adversary must have control of a network boundary device.

## Skills required
- **Medium**: The adversary must understand how to manage the target network device to create or edit policies which will bridge networks.

## Resources required
- The adversary requires either high privileges or full control of a boundary device on a target network.

## Consequences
- **Access_Control**: Read Data, Bypass Protection Mechanism
- **Authorization**: Alter Execution Logic, Hide Activities
- **Confidentiality**: Read Data, Bypass Protection Mechanism
- **Integrity**: Alter Execution Logic, Hide Activities

## Execution flow
Execution Flow Explore Identify potential targets: An adversary identifies network boundary devices that can be compromised. Techniques The adversary traces network traffic to identify which devices the traffic flows through. Additionally, the adversary can identify devices using fingerprinting methods or locating the management page to determine identifying information about the device. Experiment Compromise targets: The adversary must compromise the identified targets in the previous step. Techniques Once the device is identified, the adversary can attempt to input known default credentials for the device to gain access to the management console. Adversaries with sufficient identifying knowledge about the target device can exploit known vulnerabilities in network devices to obtain administrative access. Exploit Bridge Networks: The adversary changes the configuration of the compromised network device to connect the networks the device was segmenting. Depending on the type of network boundary device and its capabilities, bridging can be implemented using various methods. Techniques The adversary can abuse Network Address Translation (NAT) in firewalls and routers to manipulate traffic flow to their own design. With control of the network device, the adversary can manipulate NAT by either using existing configurations or creating their own to allow two previously unconnected networks to communicate. Some network devices can be configured to become a proxy server. Adversaries can set up or exploit an existing proxy server on compromised network devices to create a bridge between separate networks.

## Mitigations
- Design: Ensure network devices are storing credentials in encrypted stores
- Design: Follow the principle of least privilege and restrict administrative duties to as few accounts as possible. Ensure these privileged accounts are secured with strong credentials which do not overlap with other network devices.
- Configuration: When possible, configure network boundary devices to use MFA.
- Configuration: Change the default configuration for network devices to harden their security profiles. Default configurations are often enabled with insecure features to allow ease of installation and management. However, these configurations can be easily discovered and exploited by adversaries.
- Implementation: Perform integrity checks on audit logs for network device management and review them to identify abnormalities in configurations.
- Implementation: Prevent network boundary devices from being physically accessed by unauthorized personnel to prevent tampering.

## Related ATT&CK techniques
- T1599

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/700.html
