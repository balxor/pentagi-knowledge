---
attack_id: TA0109
name: Lateral Movement
type: tactic
shortname: lateral-movement
killchain_order: 7
url: https://attack.mitre.org/tactics/TA0109
tags: [mitre-attack, tactic, lateral-movement]
---

# TA0109 - Lateral Movement (Tactic)

> The adversary is trying to move through your ICS environment.

## Goal
The adversary is trying to move through your ICS environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. These techniques abuse default credentials, known accounts, and vulnerable services, and may also leverage dual-homed devices and systems that reside on both the IT and OT networks. The adversary uses these techniques to pivot to their next point in the environment, positioning themselves to where they want to be or think they should be. Following through on their primary objective often requires [Discovery](https://attack.mitre.org/tactics/TA0102) of the network and [Collection](https://attack.mitre.org/tactics/TA0100) to develop awareness of unique ICS devices and processes, in order to find their target and subsequently gain access to it. Reaching this objective often involves pivoting through multiple systems, devices, and accounts. Adversaries may install their own remote tools to accomplish Lateral Movement or leverage default tools, programs, and manufacturer set or other legitimate credentials native to the network, which may be stealthier.

## Position in the attack flow
Phase 7 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (6)
- [T0843](https://attack.mitre.org/techniques/T0843) Program Download
- [T0859](https://attack.mitre.org/techniques/T0859) Valid Accounts
- [T0866](https://attack.mitre.org/techniques/T0866) Exploitation of Remote Services
- [T0867](https://attack.mitre.org/techniques/T0867) Lateral Tool Transfer
- [T0886](https://attack.mitre.org/techniques/T0886) Remote Services
- [T1694](https://attack.mitre.org/techniques/T1694) Insecure Credentials

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0109
