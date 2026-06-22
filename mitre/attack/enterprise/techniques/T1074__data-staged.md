---
attack_id: T1074
name: Data Staged
type: technique
parent: null
tactics: [Collection]
platforms: [ESXi, IaaS, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1074
tags: [mitre-attack, technique, T1074]
---

# T1074 - Data Staged

**Tactic(s):** Collection  ·  **Platforms:** ESXi, IaaS, Linux, macOS, Windows  ·  **ATT&CK:** [T1074](https://attack.mitre.org/techniques/T1074)

## Summary
Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560). Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and bash may be used to copy data into a staging location.(Citation: PWC Cloud Hopper April 2017)

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and stage data in that instance.(Citation: Mandiant M-Trends 2020)

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, IaaS, Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1074
