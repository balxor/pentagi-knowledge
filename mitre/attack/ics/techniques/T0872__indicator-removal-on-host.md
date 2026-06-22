---
attack_id: T0872
name: Indicator Removal on Host
type: technique
parent: null
tactics: [Evasion]
platforms: [None]
url: https://attack.mitre.org/techniques/T0872
tags: [mitre-attack, technique, T0872]
---

# T0872 - Indicator Removal on Host

**Tactic(s):** Evasion  -  **Platforms:** None  -  **ATT&CK:** [T0872](https://attack.mitre.org/techniques/T0872)

## Summary
Adversaries may attempt to remove indicators of their presence on a system in an effort to cover their tracks. In cases where an adversary may feel detection is imminent, they may try to overwrite, delete, or cover up changes they have made to the device.

## Role in the attack flow
Used to achieve the **Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0922 Restrict File and Directory Permissions** - Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0872
