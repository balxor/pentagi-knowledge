---
attack_id: T1046
name: Network Service Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Containers, IaaS, Linux, macOS, Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1046
tags: [mitre-attack, technique, T1046]
---

# T1046 - Network Service Discovery

**Tactic(s):** Discovery  -  **Platforms:** Containers, IaaS, Linux, macOS, Network Devices, Windows  -  **ATT&CK:** [T1046](https://attack.mitre.org/techniques/T1046)

## Summary
Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A FIVEHANDS May 2021)   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as <code>dns-sd -B _ssh._tcp .</code>) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation: macOS APT Activity Bradley)

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Containers, IaaS, Linux, macOS, Network Devices, Windows.

## Mitigations
- **M1042 Disable or Remove Feature or Program** - Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: 
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.
- **M1030 Network Segmentation** - Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1046
