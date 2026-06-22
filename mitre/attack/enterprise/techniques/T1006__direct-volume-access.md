---
attack_id: T1006
name: Direct Volume Access
type: technique
parent: null
tactics: [Stealth]
platforms: [Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1006
tags: [mitre-attack, technique, T1006]
---

# T1006 - Direct Volume Access

**Tactic(s):** Stealth  -  **Platforms:** Network Devices, Windows  -  **ATT&CK:** [T1006](https://attack.mitre.org/techniques/T1006)

## Summary
Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools.(Citation: Hakobyan 2009)

Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell.(Citation: Github PowerSploit Ninjacopy) Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and [esentutl](https://attack.mitre.org/software/S0404)) to create shadow copies or backups of data from system volumes.(Citation: LOLBAS Esentutl)

## Role in the attack flow
Used to achieve the **Stealth** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Network Devices, Windows.

## Mitigations
- **M1040 Behavior Prevention on Endpoint** - Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:
- **M1018 User Account Management** - User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1006
