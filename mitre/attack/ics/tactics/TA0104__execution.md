---
attack_id: TA0104
name: Execution
type: tactic
shortname: execution
killchain_order: 2
url: https://attack.mitre.org/tactics/TA0104
tags: [mitre-attack, tactic, execution]
---

# TA0104 - Execution (Tactic)

> The adversary is trying to run code or manipulate system functions, parameters, and data in an unauthorized way.

## Goal
The adversary is trying to run code or manipulate system functions, parameters, and data in an unauthorized way.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system, device, or other asset. This execution may also rely on unknowing end users or the manipulation of device operating modes to run. Adversaries may infect remote targets with programmed executables or malicious project files that operate according to specified behavior and may alter expected device behavior in subtle ways. Commands for execution may also be issued from command-line interfaces, APIs, GUIs, or other available interfaces. Techniques that run malicious code may also be paired with techniques from other tactics, particularly to aid network [Discovery](https://attack.mitre.org/tactics/TA0102) and [Collection](https://attack.mitre.org/tactics/TA0100), impact operations, and inhibit response functions.

## Position in the attack flow
Phase 2 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (10)
- [T0807](https://attack.mitre.org/techniques/T0807) Command-Line Interface
- [T0821](https://attack.mitre.org/techniques/T0821) Modify Controller Tasking
- [T0823](https://attack.mitre.org/techniques/T0823) Graphical User Interface
- [T0834](https://attack.mitre.org/techniques/T0834) Native API
- [T0853](https://attack.mitre.org/techniques/T0853) Scripting
- [T0858](https://attack.mitre.org/techniques/T0858) Change Operating Mode
- [T0863](https://attack.mitre.org/techniques/T0863) User Execution
- [T0871](https://attack.mitre.org/techniques/T0871) Execution through API
- [T0874](https://attack.mitre.org/techniques/T0874) Hooking
- [T0895](https://attack.mitre.org/techniques/T0895) Autorun Image

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0104
