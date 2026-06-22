---
attack_id: T1645
name: Compromise Client Software Binary
type: technique
parent: null
tactics: [Persistence]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1645
tags: [mitre-attack, technique, T1645]
---

# T1645 - Compromise Client Software Binary

**Tactic(s):** Persistence  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1645](https://attack.mitre.org/techniques/T1645)

## Summary
Adversaries may modify system software binaries to establish persistent access to devices. System software binaries are used by the underlying operating system and users over adb or terminal emulators. 

Adversaries may make modifications to client software binaries to carry out malicious tasks when those binaries are executed. For example, malware may come with a pre-compiled malicious binary intended to overwrite the genuine one on the device. Since these binaries may be routinely executed by the system or user, the adversary can leverage this for persistent access to the device.

## Role in the attack flow
Used to achieve the **Persistence** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1003 Lock Bootloader** - On devices that provide the capability to unlock the bootloader (hence allowing any operating system code to be flashed onto the device), perform periodic checks to ensure that the bootloader is locked.
- **M1004 System Partition Integrity** - Ensure that Android devices being used include and enable the Verified Boot capability, which cryptographically ensures the integrity of the system partition.
- **M1001 Security Updates** - Install security updates in response to discovered vulnerabilities.
- **M1002 Attestation** - Enable remote attestation capabilities when available (such as Android SafetyNet or Samsung Knox TIMA Attestation) and prohibit devices that fail the attestation from accessing enterprise resources.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1645
