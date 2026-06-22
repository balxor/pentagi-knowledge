---
attack_id: T1020
name: Automated Exfiltration
type: technique
parent: null
tactics: [Exfiltration]
platforms: [Linux, macOS, Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1020
tags: [mitre-attack, technique, T1020]
---

# T1020 - Automated Exfiltration

**Tactic(s):** Exfiltration  ·  **Platforms:** Linux, macOS, Network Devices, Windows  ·  **ATT&CK:** [T1020](https://attack.mitre.org/techniques/T1020)

## Summary
Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after being gathered during Collection.(Citation: ESET Gamaredon June 2020) 

When automated exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) and [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048).

## Role in the attack flow
Used to achieve the **Exfiltration** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Network Devices, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1020
