---
attack_id: T1561
name: Disk Wipe
type: technique
parent: null
tactics: [Impact]
platforms: [Linux, macOS, Windows, Network Devices]
url: https://attack.mitre.org/techniques/T1561
tags: [mitre-attack, technique, T1561]
---

# T1561 - Disk Wipe

**Tactic(s):** Impact  -  **Platforms:** Linux, macOS, Windows, Network Devices  -  **ATT&CK:** [T1561](https://attack.mitre.org/techniques/T1561)

## Summary
Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot record (MBR). A complete wipe of all disk sectors may be attempted.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Novetta Blockbuster Destructive Malware)

On network devices, adversaries may wipe configuration files and other data from the device using [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `erase`.(Citation: erase_cmd_cisco)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows, Network Devices.

## Mitigations
- **M1053 Data Backup** - Data Backup involves taking and securely storing backups of data from end-user systems and critical servers. It ensures that data remains available in the event of system compromise, ransomware attacks, or other disruptions. Backup processes should include hardening backup systems, implementing secure storage solutions, and keeping backups isolated from the corporate network to prevent compromise during active incidents. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1561
