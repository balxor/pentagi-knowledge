---
attack_id: TA0111
name: Privilege Escalation
type: tactic
shortname: privilege-escalation
killchain_order: 4
url: https://attack.mitre.org/tactics/TA0111
tags: [mitre-attack, tactic, privilege-escalation]
---

# TA0111 - Privilege Escalation (Tactic)

> The adversary is trying to gain higher-level permissions.

## Goal
The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities.

## Position in the attack flow
Phase 4 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (2)
- [T0874](https://attack.mitre.org/techniques/T0874) Hooking
- [T0890](https://attack.mitre.org/techniques/T0890) Exploitation for Privilege Escalation

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0111
