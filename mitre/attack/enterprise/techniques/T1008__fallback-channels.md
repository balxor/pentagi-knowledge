---
attack_id: T1008
name: Fallback Channels
type: technique
parent: null
tactics: [Command and Control]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1008
tags: [mitre-attack, technique, T1008]
---

# T1008 - Fallback Channels

**Tactic(s):** Command and Control  -  **Platforms:** ESXi, Linux, macOS, Windows  -  **ATT&CK:** [T1008](https://attack.mitre.org/techniques/T1008)

## Summary
Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1008
