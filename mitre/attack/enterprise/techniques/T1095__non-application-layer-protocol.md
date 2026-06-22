---
attack_id: T1095
name: Non-Application Layer Protocol
type: technique
parent: null
tactics: [Command and Control]
platforms: [ESXi, Linux, macOS, Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1095
tags: [mitre-attack, technique, T1095]
---

# T1095 - Non-Application Layer Protocol

**Tactic(s):** Command and Control  -  **Platforms:** ESXi, Linux, macOS, Network Devices, Windows  -  **ATT&CK:** [T1095](https://attack.mitre.org/techniques/T1095)

## Summary
Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among infected hosts within a network. The list of possible protocols is extensive.(Citation: Wikipedia OSI) Specific examples include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols, such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled protocols, such as Serial over LAN (SOL).

ICMP communication between hosts is one example.(Citation: Cisco Synful Knock Evolution) Because ICMP is part of the Internet Protocol Suite, it is required to be implemented by all IP-compatible hosts.(Citation: Microsoft ICMP) However, it is not as commonly monitored as other Internet Protocols such as TCP or UDP and may be used by adversaries to hide communications.

In ESXi environments, adversaries may leverage the Virtual Machine Communication Interface (VMCI) for communication between guest virtual machines and the ESXi host. This traffic is similar to client-server communications on traditional network sockets but is localized to the physical machine running the ESXi host, meaning it does not traverse external networks (routers, switches). This results in communications that are invisible to external monitoring and standard networking tools like tcpdump, netstat, nmap, and Wireshark. By adding a VMCI backdoor to a compromised ESXi host, adversaries may persistently regain access from any guest VM to the compromised ESXi host’s backdoor, regardless of network segmentation or firewall rules in place.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Network Devices, Windows.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.
- **M1037 Filter Network Traffic** - Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:
- **M1030 Network Segmentation** - Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1095
