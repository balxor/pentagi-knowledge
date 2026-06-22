---
attack_id: T0809
name: Data Destruction
type: technique
parent: null
tactics: [Inhibit Response Function]
platforms: [None]
url: https://attack.mitre.org/techniques/T0809
tags: [mitre-attack, technique, T0809]
---

# T0809 - Data Destruction

**Tactic(s):** Inhibit Response Function  -  **Platforms:** None  -  **ATT&CK:** [T0809](https://attack.mitre.org/techniques/T0809)

## Summary
Adversaries may perform data destruction over the course of an operation. The adversary may drop or create malware, tools, or other non-native files on a target system to accomplish this, potentially leaving behind traces of malicious activities. Such non-native files and other data may be removed over the course of an intrusion to maintain a small footprint or as a standard part of the post-intrusion cleanup process. (Citation: Enterprise ATT&CK January 2018)

Data destruction may also be used to render operator interfaces unable to respond and to disrupt response functions from occurring as expected. An adversary may also destroy data backups that are vital to recovery after an incident.

Standard file deletion commands are available on most operating system and device interfaces to perform cleanup, but adversaries may use other tools as well. Two examples are Windows Sysinternals SDelete and Active@ Killdisk.

## Role in the attack flow
Used to achieve the **Inhibit Response Function** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0922 Restrict File and Directory Permissions** - Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.
- **M0953 Data Backup** - Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.
- **M0926 Privileged Account Management** - Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0809
