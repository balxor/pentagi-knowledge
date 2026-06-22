---
attack_id: T1560
name: Archive Collected Data
type: technique
parent: null
tactics: [Collection]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1560
tags: [mitre-attack, technique, T1560]
---

# T1560 - Archive Collected Data

**Tactic(s):** Collection  ·  **Platforms:** Linux, macOS, Windows  ·  **ATT&CK:** [T1560](https://attack.mitre.org/techniques/T1560)

## Summary
An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1560
