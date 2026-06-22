---
attack_id: T1398
name: Boot or Logon Initialization Scripts
type: technique
parent: null
tactics: [Persistence]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1398
tags: [mitre-attack, technique, T1398]
---

# T1398 - Boot or Logon Initialization Scripts

**Tactic(s):** Persistence  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1398](https://attack.mitre.org/techniques/T1398)

## Summary
Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence. Initialization scripts are part of the underlying operating system and are not accessible to the user unless the device has been rooted or jailbroken.

## Role in the attack flow
Used to achieve the **Persistence** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1001 Security Updates** - Install security updates in response to discovered vulnerabilities.
- **M1004 System Partition Integrity** - Ensure that Android devices being used include and enable the Verified Boot capability, which cryptographically ensures the integrity of the system partition.
- **M1002 Attestation** - Enable remote attestation capabilities when available (such as Android SafetyNet or Samsung Knox TIMA Attestation) and prohibit devices that fail the attestation from accessing enterprise resources.
- **M1003 Lock Bootloader** - On devices that provide the capability to unlock the bootloader (hence allowing any operating system code to be flashed onto the device), perform periodic checks to ensure that the bootloader is locked.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1398
