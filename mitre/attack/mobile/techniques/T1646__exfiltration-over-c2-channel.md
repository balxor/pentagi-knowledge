---
attack_id: T1646
name: Exfiltration Over C2 Channel
type: technique
parent: null
tactics: [Exfiltration]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1646
tags: [mitre-attack, technique, T1646]
---

# T1646 - Exfiltration Over C2 Channel

**Tactic(s):** Exfiltration  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1646](https://attack.mitre.org/techniques/T1646)

## Summary
Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Role in the attack flow
Used to achieve the **Exfiltration** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1646
