---
attack_id: T1655
name: Masquerading
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1655
tags: [mitre-attack, technique, T1655]
---

# T1655 - Masquerading

**Tactic(s):** Defense Evasion  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1655](https://attack.mitre.org/techniques/T1655)

## Summary
Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name, location, or appearance of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1655)

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1655
