---
attack_id: T1418
name: Software Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1418
tags: [mitre-attack, technique, T1418]
---

# T1418 - Software Discovery

**Tactic(s):** Discovery  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1418](https://attack.mitre.org/techniques/T1418)

## Summary
Adversaries may attempt to get a listing of applications that are installed on a device. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1418) during automated discovery to shape follow-on behaviors, including whether or not to fully infect the target and/or attempts specific actions. 

 

Adversaries may attempt to enumerate applications for a variety of reasons, such as figuring out what security measures are present or to identify the presence of target applications.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1418
