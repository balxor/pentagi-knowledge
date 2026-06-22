---
attack_id: T1639
name: Exfiltration Over Alternative Protocol
type: technique
parent: null
tactics: [Exfiltration]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1639
tags: [mitre-attack, technique, T1639]
---

# T1639 - Exfiltration Over Alternative Protocol

**Tactic(s):** Exfiltration  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1639](https://attack.mitre.org/techniques/T1639)

## Summary
Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Different protocol channels could also include Web services such as cloud storage. Adversaries may opt to also encrypt and/or obfuscate these alternate channels.

## Role in the attack flow
Used to achieve the **Exfiltration** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1639
