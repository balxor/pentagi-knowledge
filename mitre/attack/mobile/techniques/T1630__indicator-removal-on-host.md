---
attack_id: T1630
name: Indicator Removal on Host
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [iOS, Android]
url: https://attack.mitre.org/techniques/T1630
tags: [mitre-attack, technique, T1630]
---

# T1630 - Indicator Removal on Host

**Tactic(s):** Defense Evasion  -  **Platforms:** iOS, Android  -  **ATT&CK:** [T1630](https://attack.mitre.org/techniques/T1630)

## Summary
Adversaries may delete, alter, or hide generated artifacts on a device, including files, jailbreak status, or the malicious application itself. These actions may interfere with event collection, reporting, or other notifications used to detect intrusion activity. This may compromise the integrity of mobile security solutions by causing notable events or information to go unreported.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: iOS, Android.

## Mitigations
- **M1001 Security Updates** - Install security updates in response to discovered vulnerabilities.
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.
- **M1002 Attestation** - Enable remote attestation capabilities when available (such as Android SafetyNet or Samsung Knox TIMA Attestation) and prohibit devices that fail the attestation from accessing enterprise resources.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1630
