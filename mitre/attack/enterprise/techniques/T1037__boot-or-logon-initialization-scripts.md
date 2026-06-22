---
attack_id: T1037
name: Boot or Logon Initialization Scripts
type: technique
parent: null
tactics: [Persistence, Privilege Escalation]
platforms: [ESXi, Linux, macOS, Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1037
tags: [mitre-attack, technique, T1037]
---

# T1037 - Boot or Logon Initialization Scripts

**Tactic(s):** Persistence, Privilege Escalation  -  **Platforms:** ESXi, Linux, macOS, Network Devices, Windows  -  **ATT&CK:** [T1037](https://attack.mitre.org/techniques/T1037)

## Summary
Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation: Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

## Role in the attack flow
Used to achieve the **Persistence, Privilege Escalation** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Network Devices, Windows.

## Mitigations
- **M1024 Restrict Registry Permissions** - Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures:
- **M1022 Restrict File and Directory Permissions** - Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1037
