---
attack_id: T1544
name: Ingress Tool Transfer
type: technique
parent: null
tactics: [Command and Control]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1544
tags: [mitre-attack, technique, T1544]
---

# T1544 - Ingress Tool Transfer

**Tactic(s):** Command and Control  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1544](https://attack.mitre.org/techniques/T1544)

## Summary
Adversaries may transfer tools or other files from an external system onto a compromised device to facilitate follow-on actions. Files may be copied from an external adversary-controlled system through the command and control channel  or through alternate protocols with another tool such as FTP.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1544
