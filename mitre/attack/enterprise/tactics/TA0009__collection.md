---
attack_id: TA0009
name: Collection
type: tactic
shortname: collection
killchain_order: 12
url: https://attack.mitre.org/tactics/TA0009
tags: [mitre-attack, tactic, collection]
---

# TA0009 - Collection (Tactic)

> The adversary is trying to gather data of interest to their goal.

## Goal
The adversary is trying to gather data of interest to their goal.

Collection consists of techniques adversaries may use to gather information and the sources information is collected from that are relevant to following through on the adversary's objectives. Frequently, the next goal after collecting data is to either steal (exfiltrate) the data or to use the data to gain more information about the target environment. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input.

## Position in the attack flow
Phase 12 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (17)
- [T1005](https://attack.mitre.org/techniques/T1005) Data from Local System
- [T1025](https://attack.mitre.org/techniques/T1025) Data from Removable Media
- [T1039](https://attack.mitre.org/techniques/T1039) Data from Network Shared Drive
- [T1056](https://attack.mitre.org/techniques/T1056) Input Capture
- [T1074](https://attack.mitre.org/techniques/T1074) Data Staged
- [T1113](https://attack.mitre.org/techniques/T1113) Screen Capture
- [T1114](https://attack.mitre.org/techniques/T1114) Email Collection
- [T1115](https://attack.mitre.org/techniques/T1115) Clipboard Data
- [T1119](https://attack.mitre.org/techniques/T1119) Automated Collection
- [T1123](https://attack.mitre.org/techniques/T1123) Audio Capture
- [T1125](https://attack.mitre.org/techniques/T1125) Video Capture
- [T1185](https://attack.mitre.org/techniques/T1185) Browser Session Hijacking
- [T1213](https://attack.mitre.org/techniques/T1213) Data from Information Repositories
- [T1530](https://attack.mitre.org/techniques/T1530) Data from Cloud Storage
- [T1557](https://attack.mitre.org/techniques/T1557) Adversary-in-the-Middle
- [T1560](https://attack.mitre.org/techniques/T1560) Archive Collected Data
- [T1602](https://attack.mitre.org/techniques/T1602) Data from Configuration Repository

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0009
