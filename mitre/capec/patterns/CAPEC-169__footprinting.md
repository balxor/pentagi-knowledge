---
capec_id: CAPEC-169
name: Footprinting
type: attack-pattern
abstraction: Meta
likelihood: High
severity: Very Low
related_cwe: [CWE-200]
related_attack: [T1217, T1592, T1595]
url: https://capec.mitre.org/data/definitions/169.html
tags: [mitre-capec, attack-pattern, CAPEC-169]
---

# CAPEC-169 - Footprinting

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** Very Low  -  **CAPEC:** [CAPEC-169](https://capec.mitre.org/data/definitions/169.html)

## Description
An adversary engages in probing and exploration activities to identify constituents and properties of the target.

## Extended description
Footprinting is a general term to describe a variety of information gathering techniques, often used by attackers in preparation for some attack. It consists of using tools to learn as much as possible about the composition, configuration, and security mechanisms of the targeted application, system or network. Information that might be collected during a footprinting effort could include open ports, applications and their versions, network topology, and similar information. Although similar to fingerprinting, footprinting aims to get a more holistic view of a system or network, whereas fingerprinting is more targeted to a specific application or operating system. While footprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.

## Prerequisites
- An application must publicize identifiable information about the system or application through voluntary or involuntary means. Certain identification details of information systems are visible on communication networks (e.g., if an adversary uses a sniffer to inspect the traffic) due to their inherent structure and protocol standards. Any system or network that can be detected can be footprinted. However, some configuration choices may limit the useful information that can be collected during a footprinting attack.

## Skills required
- **Low**: The adversary knows how to send HTTP request, run the scan tool.

## Resources required
- The adversary requires a variety of tools to collect information about the target. These include port/network scanners and tools to analyze responses from applications to determine version and configuration information. Footprinting a system adequately may also take a few days if the attacker wishes the footprinting attempt to go undetected.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Request Footprinting: The attacker examines the website information and source code of the website and uses automated tools to get as much information as possible about the system and organization. Techniques Open Source Footprinting: Examine the website about the organization and skim through the webpage's HTML source to look for comments. Network Enumeration: Perform various queries (Registrar Query, Organizational Query, Domain Query, Network Query, POC Query) on the many whois databases found on the internet to identify domain names and associated networks. DNS Interrogation: Once basic information is gathered the attack could begin to query DNS. Other Techniques: Use ping sweep, TCP scan, UDP scan, OS Identification various techniques to gain more information about the system and network.

## Mitigations
- Keep patches up to date by installing weekly or daily if possible.
- Shut down unnecessary services/ports.
- Change default passwords by choosing strong passwords.
- Curtail unexpected input.
- Encrypt and password-protect sensitive data.
- Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1217
- T1592
- T1595

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/169.html
