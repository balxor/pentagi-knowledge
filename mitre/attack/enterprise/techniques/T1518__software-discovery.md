---
attack_id: T1518
name: Software Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [ESXi, IaaS, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1518
tags: [mitre-attack, technique, T1518]
---

# T1518 - Software Discovery

**Tactic(s):** Discovery  -  **Platforms:** ESXi, IaaS, Linux, macOS, Windows  -  **ATT&CK:** [T1518](https://attack.mitre.org/techniques/T1518)

## Summary
Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1518) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Such software may be deployed widely across the environment for configuration management or security reasons, such as [Software Deployment Tools](https://attack.mitre.org/techniques/T1072), and may allow adversaries broad access to infect devices or move laterally.

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, IaaS, Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1518
