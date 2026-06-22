---
attack_id: T1567
name: Exfiltration Over Web Service
type: technique
parent: null
tactics: [Exfiltration]
platforms: [ESXi, Linux, macOS, Office Suite, SaaS, Windows]
url: https://attack.mitre.org/techniques/T1567
tags: [mitre-attack, technique, T1567]
---

# T1567 - Exfiltration Over Web Service

**Tactic(s):** Exfiltration  -  **Platforms:** ESXi, Linux, macOS, Office Suite, SaaS, Windows  -  **ATT&CK:** [T1567](https://attack.mitre.org/techniques/T1567)

## Summary
Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Role in the attack flow
Used to achieve the **Exfiltration** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Office Suite, SaaS, Windows.

## Mitigations
- **M1021 Restrict Web-Based Content** - Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures:
- **M1057 Data Loss Prevention** - Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. (Citation: PurpleSec Data Loss Prevention) This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1567
