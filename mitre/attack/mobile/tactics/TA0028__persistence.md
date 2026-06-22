---
attack_id: TA0028
name: Persistence
type: tactic
shortname: persistence
killchain_order: 3
url: https://attack.mitre.org/tactics/TA0028
tags: [mitre-attack, tactic, persistence]
---

# TA0028 - Persistence (Tactic)

> The adversary is trying to maintain their foothold.

## Goal
The adversary is trying to maintain their foothold.

Persistence is any access, action, or configuration change to a mobile device that gives an attacker a persistent presence on the device. Attackers often will need to maintain access to mobile devices through interruptions such as device reboots and potentially even factory data resets.

## Position in the attack flow
Phase 3 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (8)
- [T1398](https://attack.mitre.org/techniques/T1398) Boot or Logon Initialization Scripts
- [T1541](https://attack.mitre.org/techniques/T1541) Foreground Persistence
- [T1577](https://attack.mitre.org/techniques/T1577) Compromise Application Executable
- [T1603](https://attack.mitre.org/techniques/T1603) Scheduled Task/Job
- [T1624](https://attack.mitre.org/techniques/T1624) Event Triggered Execution
- [T1625](https://attack.mitre.org/techniques/T1625) Hijack Execution Flow
- [T1645](https://attack.mitre.org/techniques/T1645) Compromise Client Software Binary
- [T1676](https://attack.mitre.org/techniques/T1676) Linked Devices

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0028
