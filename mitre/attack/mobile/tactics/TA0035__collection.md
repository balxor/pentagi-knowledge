---
attack_id: TA0035
name: Collection
type: tactic
shortname: collection
killchain_order: 9
url: https://attack.mitre.org/tactics/TA0035
tags: [mitre-attack, tactic, collection]
---

# TA0035 - Collection (Tactic)

> The adversary is trying to gather data of interest to their goal.

## Goal
The adversary is trying to gather data of interest to their goal.

Collection consists of techniques used to identify and gather information, such as sensitive files, from a target network prior to exfiltration. This category also covers locations on a system or network where the adversary may look for information to exfiltrate.

## Position in the attack flow
Phase 9 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (15)
- [T1409](https://attack.mitre.org/techniques/T1409) Stored Application Data
- [T1414](https://attack.mitre.org/techniques/T1414) Clipboard Data
- [T1417](https://attack.mitre.org/techniques/T1417) Input Capture
- [T1429](https://attack.mitre.org/techniques/T1429) Audio Capture
- [T1430](https://attack.mitre.org/techniques/T1430) Location Tracking
- [T1453](https://attack.mitre.org/techniques/T1453) Abuse Accessibility Features
- [T1512](https://attack.mitre.org/techniques/T1512) Video Capture
- [T1513](https://attack.mitre.org/techniques/T1513) Screen Capture
- [T1517](https://attack.mitre.org/techniques/T1517) Access Notifications
- [T1532](https://attack.mitre.org/techniques/T1532) Archive Collected Data
- [T1533](https://attack.mitre.org/techniques/T1533) Data from Local System
- [T1616](https://attack.mitre.org/techniques/T1616) Call Control
- [T1636](https://attack.mitre.org/techniques/T1636) Protected User Data
- [T1638](https://attack.mitre.org/techniques/T1638) Adversary-in-the-Middle
- [T1676](https://attack.mitre.org/techniques/T1676) Linked Devices

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0035
