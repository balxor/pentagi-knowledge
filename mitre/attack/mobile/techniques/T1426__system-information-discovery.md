---
attack_id: T1426
name: System Information Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1426
tags: [mitre-attack, technique, T1426]
---

# T1426 - System Information Discovery

**Tactic(s):** Discovery  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1426](https://attack.mitre.org/techniques/T1426)

## Summary
Adversaries may attempt to get detailed information about a device’s operating system and hardware, including versions, patches, and architecture. Adversaries may use the information from [System Information Discovery](https://attack.mitre.org/techniques/T1426) during automated discovery to shape follow-on behaviors, including whether or not to fully infects the target and/or attempts specific actions. 

 

On Android, much of this information is programmatically accessible to applications through the `android.os.Build` class. (Citation: Android-Build) iOS is much more restrictive with what information is visible to applications. Typically, applications will only be able to query the device model and which version of iOS it is running.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1426
