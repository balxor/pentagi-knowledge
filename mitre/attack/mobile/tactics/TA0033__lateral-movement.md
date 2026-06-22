---
attack_id: TA0033
name: Lateral Movement
type: tactic
shortname: lateral-movement
killchain_order: 8
url: https://attack.mitre.org/tactics/TA0033
tags: [mitre-attack, tactic, lateral-movement]
---

# TA0033 - Lateral Movement (Tactic)

> The adversary is trying to move through your environment.

## Goal
The adversary is trying to move through your environment.

Lateral movement consists of techniques that enable an adversary to access and control remote systems on a network and could, but does not necessarily, include execution of tools on remote systems. The lateral movement techniques could allow an adversary to gather information from a system without needing additional tools, such as a remote access tool.

## Position in the attack flow
Phase 8 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (2)
- [T1428](https://attack.mitre.org/techniques/T1428) Exploitation of Remote Services
- [T1458](https://attack.mitre.org/techniques/T1458) Replication Through Removable Media

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0033
