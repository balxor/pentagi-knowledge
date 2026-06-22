---
attack_id: T1135
name: Network Share Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1135
tags: [mitre-attack, technique, T1135]
---

# T1135 - Network Share Discovery

**Tactic(s):** Discovery  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1135](https://attack.mitre.org/techniques/T1135)

## Summary
Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation: TechNet Shared Folder) [Net](https://attack.mitre.org/software/S0039) can be used to query a remote system for available shared drives using the <code>net view \\\\remotesystem</code> command. It can also be used to query shared drives on the local system using <code>net share</code>. For macOS, the <code>sharing -l</code> command lists all shared points used for smb services.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1028 Operating System Configuration** - Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: 

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1135
