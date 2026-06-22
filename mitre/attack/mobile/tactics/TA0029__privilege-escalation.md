---
attack_id: TA0029
name: Privilege Escalation
type: tactic
shortname: privilege-escalation
killchain_order: 4
url: https://attack.mitre.org/tactics/TA0029
tags: [mitre-attack, tactic, privilege-escalation]
---

# TA0029 - Privilege Escalation (Tactic)

> The adversary is trying to gain higher-level permissions.

## Goal
The adversary is trying to gain higher-level permissions.

Privilege escalation includes techniques that allow an attacker to obtain a higher level of permissions on the mobile device. Attackers may enter the mobile device with very limited privileges and may be required to take advantage of a device weakness to obtain higher privileges necessary to successfully carry out their mission objectives.

## Position in the attack flow
Phase 4 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (3)
- [T1404](https://attack.mitre.org/techniques/T1404) Exploitation for Privilege Escalation
- [T1626](https://attack.mitre.org/techniques/T1626) Abuse Elevation Control Mechanism
- [T1631](https://attack.mitre.org/techniques/T1631) Process Injection

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0029
