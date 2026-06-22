---
attack_id: T1640
name: Account Access Removal
type: technique
parent: null
tactics: [Impact]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1640
tags: [mitre-attack, technique, T1640]
---

# T1640 - Account Access Removal

**Tactic(s):** Impact  -  **Platforms:** Android  -  **ATT&CK:** [T1640](https://attack.mitre.org/techniques/T1640)

## Summary
Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: credentials changed) to remove access to accounts.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1640
