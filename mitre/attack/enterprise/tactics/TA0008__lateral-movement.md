---
attack_id: TA0008
name: Lateral Movement
type: tactic
shortname: lateral-movement
killchain_order: 11
url: https://attack.mitre.org/tactics/TA0008
tags: [mitre-attack, tactic, lateral-movement]
---

# TA0008 - Lateral Movement (Tactic)

> The adversary is trying to move through your environment.

## Goal
The adversary is trying to move through your environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Following through on their primary objective often requires exploring the network to find their target, then pivoting through multiple systems and accounts to gain access to it. Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier.

## Position in the attack flow
Phase 11 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (9)
- [T1021](https://attack.mitre.org/techniques/T1021) Remote Services
- [T1072](https://attack.mitre.org/techniques/T1072) Software Deployment Tools
- [T1080](https://attack.mitre.org/techniques/T1080) Taint Shared Content
- [T1091](https://attack.mitre.org/techniques/T1091) Replication Through Removable Media
- [T1210](https://attack.mitre.org/techniques/T1210) Exploitation of Remote Services
- [T1534](https://attack.mitre.org/techniques/T1534) Internal Spearphishing
- [T1550](https://attack.mitre.org/techniques/T1550) Use Alternate Authentication Material
- [T1563](https://attack.mitre.org/techniques/T1563) Remote Service Session Hijacking
- [T1570](https://attack.mitre.org/techniques/T1570) Lateral Tool Transfer

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0008
