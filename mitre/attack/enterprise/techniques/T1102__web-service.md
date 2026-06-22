---
attack_id: T1102
name: Web Service
type: technique
parent: null
tactics: [Command and Control]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1102
tags: [mitre-attack, technique, T1102]
---

# T1102 - Web Service

**Tactic(s):** Command and Control  -  **Platforms:** ESXi, Linux, macOS, Windows  -  **ATT&CK:** [T1102](https://attack.mitre.org/techniques/T1102)

## Summary
Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise.(Citation: Broadcom BirdyClient Microsoft Graph API 2024) Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.
- **M1021 Restrict Web-Based Content** - Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1102
