---
attack_id: T1120
name: Peripheral Device Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1120
tags: [mitre-attack, technique, T1120]
---

# T1120 - Peripheral Device Discovery

**Tactic(s):** Discovery  ·  **Platforms:** Linux, macOS, Windows  ·  **ATT&CK:** [T1120](https://attack.mitre.org/techniques/T1120)

## Summary
Adversaries may attempt to gather information about attached peripheral devices and components connected to a computer system.(Citation: Peripheral Discovery Linux)(Citation: Peripheral Discovery macOS) Peripheral devices could include auxiliary resources that support a variety of functionalities such as keyboards, printers, cameras, smart card readers, or removable storage. The information may be used to enhance their awareness of the system and network environment or may be used for further actions.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1120
