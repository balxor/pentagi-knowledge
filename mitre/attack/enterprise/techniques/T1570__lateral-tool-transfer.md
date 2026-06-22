---
attack_id: T1570
name: Lateral Tool Transfer
type: technique
parent: null
tactics: [Lateral Movement]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1570
tags: [mitre-attack, technique, T1570]
---

# T1570 - Lateral Tool Transfer

**Tactic(s):** Lateral Movement  -  **Platforms:** ESXi, Linux, macOS, Windows  -  **ATT&CK:** [T1570](https://attack.mitre.org/techniques/T1570)

## Summary
Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) to connected network shares or with authenticated connections via [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001).(Citation: Unit42 LockerGoga 2019)

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [ftp](https://attack.mitre.org/software/S0095). In some cases, adversaries may be able to leverage [Web Service](https://attack.mitre.org/techniques/T1102)s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.(Citation: Dropbox Malware Sync)

## Role in the attack flow
Used to achieve the **Lateral Movement** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

## Mitigations
- **M1037 Filter Network Traffic** - Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1570
