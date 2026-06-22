---
attack_id: T1679
name: Selective Exclusion
type: technique
parent: null
tactics: [Stealth]
platforms: [Windows]
url: https://attack.mitre.org/techniques/T1679
tags: [mitre-attack, technique, T1679]
---

# T1679 - Selective Exclusion

**Tactic(s):** Stealth  ·  **Platforms:** Windows  ·  **ATT&CK:** [T1679](https://attack.mitre.org/techniques/T1679)

## Summary
Adversaries may intentionally exclude certain files, folders, directories, file types, or system components from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries may avoid encrypting include `.dll`, `.exe`, and `.lnk`.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)  

Adversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts, or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. 

Exclusions may target files and components whose corruption would cause instability, break core services, or immediately expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators that could trigger alarms or otherwise inhibit achieving their goals.

## Role in the attack flow
Used to achieve the **Stealth** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1679
