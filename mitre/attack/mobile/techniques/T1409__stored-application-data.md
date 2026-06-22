---
attack_id: T1409
name: Stored Application Data
type: technique
parent: null
tactics: [Collection]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1409
tags: [mitre-attack, technique, T1409]
---

# T1409 - Stored Application Data

**Tactic(s):** Collection  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1409](https://attack.mitre.org/techniques/T1409)

## Summary
Adversaries may try to access and collect application data resident on the device. Adversaries often target popular applications, such as Facebook, WeChat, and Gmail.(Citation: SWB Exodus March 2019) 

 

Due to mobile OS sandboxing, this technique is only possible in three scenarios: 

 

* An application stores files in unprotected external storage 
* An application stores files in its internal storage directory with insecure permissions (e.g. 777) 
* The adversary gains root permissions on the device

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1409
