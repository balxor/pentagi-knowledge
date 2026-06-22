---
attack_id: T1670
name: Virtualization Solution
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1670
tags: [mitre-attack, technique, T1670]
---

# T1670 - Virtualization Solution

**Tactic(s):** Defense Evasion  -  **Platforms:** Android  -  **ATT&CK:** [T1670](https://attack.mitre.org/techniques/T1670)

## Summary
Adversaries may carry out malicious operations using virtualization solutions to escape from Android sandboxes and to avoid detection. Android uses sandboxes to separate resources and code execution between applications and the operating system.(Citation: Android Application Sandbox) There are a few virtualization solutions available on Android, such as the Android Virtualization Framework (AVF).(Citation: Android AVF Overview)  

 

Through virtualization solutions, adversaries may execute malicious operations without user knowledge. For example, adversaries may mimic a legitimate banking application’s functionalities in a virtual environment, thanks to the virtualization solution, while malicious code captures credentials.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1670
