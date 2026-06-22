---
attack_id: T1533
name: Data from Local System
type: technique
parent: null
tactics: [Collection]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1533
tags: [mitre-attack, technique, T1533]
---

# T1533 - Data from Local System

**Tactic(s):** Collection  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1533](https://attack.mitre.org/techniques/T1533)

## Summary
Adversaries may search local system sources, such as file systems or local databases, to find files of interest and sensitive data prior to exfiltration.  

 

Access to local system data, which includes information stored by the operating system, often requires escalated privileges. Examples of local system data include authentication tokens, the device keyboard cache, Wi-Fi passwords, and photos. On Android, adversaries may also attempt to access files from external storage which may require additional storage-related permissions.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1533
