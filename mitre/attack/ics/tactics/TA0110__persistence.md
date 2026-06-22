---
attack_id: TA0110
name: Persistence
type: tactic
shortname: persistence
killchain_order: 3
url: https://attack.mitre.org/tactics/TA0110
tags: [mitre-attack, tactic, persistence]
---

# TA0110 - Persistence (Tactic)

> The adversary is trying to maintain their foothold in your ICS environment.

## Goal
The adversary is trying to maintain their foothold in your ICS environment.

Persistence consists of techniques that adversaries use to maintain access to ICS systems and devices across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that allow them to secure their ongoing activity and keep their foothold on systems. This may include replacing or hijacking legitimate code, firmware, and other project files, or adding startup code and downloading programs onto devices.

## Position in the attack flow
Phase 3 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (5)
- [T0859](https://attack.mitre.org/techniques/T0859) Valid Accounts
- [T0873](https://attack.mitre.org/techniques/T0873) Project File Infection
- [T0889](https://attack.mitre.org/techniques/T0889) Modify Program
- [T1693](https://attack.mitre.org/techniques/T1693) Modify Firmware
- [T1694](https://attack.mitre.org/techniques/T1694) Insecure Credentials

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0110
