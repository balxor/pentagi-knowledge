---
attack_id: T1532
name: Archive Collected Data
type: technique
parent: null
tactics: [Collection]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1532
tags: [mitre-attack, technique, T1532]
---

# T1532 - Archive Collected Data

**Tactic(s):** Collection  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1532](https://attack.mitre.org/techniques/T1532)

## Summary
Adversaries may compress and/or encrypt data that is collected prior to exfiltration. Compressing data can help to obfuscate its contents and minimize use of network resources. Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender. 

 

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, programming library, or custom algorithm.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1532
