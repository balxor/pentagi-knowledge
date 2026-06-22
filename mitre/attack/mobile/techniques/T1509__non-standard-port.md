---
attack_id: T1509
name: Non-Standard Port
type: technique
parent: null
tactics: [Command and Control]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1509
tags: [mitre-attack, technique, T1509]
---

# T1509 - Non-Standard Port

**Tactic(s):** Command and Control  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1509](https://attack.mitre.org/techniques/T1509)

## Summary
Adversaries may generate network traffic using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088 or port 587 as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1509
