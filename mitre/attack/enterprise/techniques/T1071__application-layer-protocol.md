---
attack_id: T1071
name: Application Layer Protocol
type: technique
parent: null
tactics: [Command and Control]
platforms: [Linux, macOS, Windows, Network Devices, ESXi]
url: https://attack.mitre.org/techniques/T1071
tags: [mitre-attack, technique, T1071]
---

# T1071 - Application Layer Protocol

**Tactic(s):** Command and Control  -  **Platforms:** Linux, macOS, Windows, Network Devices, ESXi  -  **ATT&CK:** [T1071](https://attack.mitre.org/techniques/T1071)

## Summary
Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP.(Citation: Mandiant APT29 Eye Spy Email Nov 22)

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows, Network Devices, ESXi.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.
- **M1037 Filter Network Traffic** - Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1071
