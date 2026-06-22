---
attack_id: T1029
name: Scheduled Transfer
type: technique
parent: null
tactics: [Exfiltration]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1029
tags: [mitre-attack, technique, T1029]
---

# T1029 - Scheduled Transfer

**Tactic(s):** Exfiltration  ·  **Platforms:** Linux, macOS, Windows  ·  **ATT&CK:** [T1029](https://attack.mitre.org/techniques/T1029)

## Summary
Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) or [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048).

## Role in the attack flow
Used to achieve the **Exfiltration** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1029
