---
attack_id: T1617
name: Hooking
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1617
tags: [mitre-attack, technique, T1617]
---

# T1617 - Hooking

**Tactic(s):** Defense Evasion  -  **Platforms:** Android  -  **ATT&CK:** [T1617](https://attack.mitre.org/techniques/T1617)

## Summary
Adversaries may utilize hooking to hide the presence of artifacts associated with their behaviors to evade detection. Hooking can be used to modify return values or data structures of system APIs and function calls. This process typically involves using 3rd party root frameworks, such as Xposed or Magisk, with either a system exploit or pre-existing root access. By including custom modules for root frameworks, adversaries can hook system APIs and alter the return value and/or system data structures to alter functionality/visibility of various aspects of the system.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1002 Attestation** - Enable remote attestation capabilities when available (such as Android SafetyNet or Samsung Knox TIMA Attestation) and prohibit devices that fail the attestation from accessing enterprise resources.
- **M1010 Deploy Compromised Device Detection Method** - A variety of methods exist that can be used to enable enterprises to identify compromised (e.g. rooted/jailbroken) devices, whether using security mechanisms built directly into the device, third-party mobile security applications, enterprise mobility management (EMM)/mobile device management (MDM) capabilities, or other methods. Some methods may be trivial to evade while others may be more sophisticated.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1617
