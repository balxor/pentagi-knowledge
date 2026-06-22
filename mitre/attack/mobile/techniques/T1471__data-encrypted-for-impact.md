---
attack_id: T1471
name: Data Encrypted for Impact
type: technique
parent: null
tactics: [Impact]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1471
tags: [mitre-attack, technique, T1471]
---

# T1471 - Data Encrypted for Impact

**Tactic(s):** Impact  -  **Platforms:** Android  -  **ATT&CK:** [T1471](https://attack.mitre.org/techniques/T1471)

## Summary
An adversary may encrypt files stored on a mobile device to prevent the user from accessing them. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1471
