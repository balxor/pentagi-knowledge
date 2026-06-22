---
attack_id: T1633
name: Virtualization/Sandbox Evasion
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1633
tags: [mitre-attack, technique, T1633]
---

# T1633 - Virtualization/Sandbox Evasion

**Tactic(s):** Defense Evasion  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1633](https://attack.mitre.org/techniques/T1633)

## Summary
Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors after checking for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware’s behavior to disengage from the victim or conceal the core functions of the payload. They may also search for VME artifacts before dropping further payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1633) during automated discovery to shape follow-on behaviors. 

Adversaries may use several methods to accomplish [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1633) such as checking for system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1633
