---
attack_id: T1637
name: Dynamic Resolution
type: technique
parent: null
tactics: [Command and Control]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1637
tags: [mitre-attack, technique, T1637]
---

# T1637 - Dynamic Resolution

**Tactic(s):** Command and Control  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1637](https://attack.mitre.org/techniques/T1637)

## Summary
Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. This algorithm can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1637
