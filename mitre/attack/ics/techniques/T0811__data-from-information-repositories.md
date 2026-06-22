---
attack_id: T0811
name: Data from Information Repositories
type: technique
parent: null
tactics: [Collection]
platforms: [None]
url: https://attack.mitre.org/techniques/T0811
tags: [mitre-attack, technique, T0811]
---

# T0811 - Data from Information Repositories

**Tactic(s):** Collection  -  **Platforms:** None  -  **ATT&CK:** [T0811](https://attack.mitre.org/techniques/T0811)

## Summary
Adversaries may target and collect data from information repositories. This can include sensitive data such as specifications, schematics, or diagrams of control system layouts, devices, and processes. Examples of information repositories include reference databases in the process environment, as well as databases in the corporate network that might contain information about the ICS.(Citation: Cybersecurity & Infrastructure Security Agency March 2018)

Information collected from these systems may provide the adversary with a better understanding of the operational environment, vendors used, processes, or procedures of the ICS.

In a campaign between 2011 and 2013 against ONG organizations, Chinese state-sponsored actors searched document repositories for specific information such as, system manuals, remote terminal unit (RTU) sites, personnel lists, documents that included the string SCAD*, user credentials, and remote dial-up access information. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0947 Audit** - Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. Perform periodic integrity checks of the device to validate the correctness of the firmware, software, programs, and configurations. Integrity checks, which typically include cryptographic hashes or digital signatures, should be compared to those obtained at known valid states, especially after events like device reboots, program downloads, or program restarts.
- **M0941 Encrypt Sensitive Information** - Protect sensitive data-at-rest with strong encryption.
- **M0922 Restrict File and Directory Permissions** - Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.
- **M0918 User Account Management** - Manage the creation, modification, use, and permissions associated to user accounts.
- **M0926 Privileged Account Management** - Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root.
- **M0917 User Training** - Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful spearphishing, social engineering, and other techniques that involve user interaction.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0811
