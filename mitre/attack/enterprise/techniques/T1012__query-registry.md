---
attack_id: T1012
name: Query Registry
type: technique
parent: null
tactics: [Discovery]
platforms: [Windows]
url: https://attack.mitre.org/techniques/T1012
tags: [mitre-attack, technique, T1012]
---

# T1012 - Query Registry

**Tactic(s):** Discovery  -  **Platforms:** Windows  -  **ATT&CK:** [T1012](https://attack.mitre.org/techniques/T1012)

## Summary
Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation: Wikipedia Windows Registry) Information can easily be queried using the [Reg](https://attack.mitre.org/software/S0075) utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [Query Registry](https://attack.mitre.org/techniques/T1012) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1012
