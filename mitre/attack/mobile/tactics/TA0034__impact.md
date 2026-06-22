---
attack_id: TA0034
name: Impact
type: tactic
shortname: impact
killchain_order: 12
url: https://attack.mitre.org/tactics/TA0034
tags: [mitre-attack, tactic, impact]
---

# TA0034 - Impact (Tactic)

> The adversary is trying to manipulate, interrupt, or destroy your devices and data.

## Goal
The adversary is trying to manipulate, interrupt, or destroy your devices and data.

The impact tactic consists of techniques used by the adversary to execute his or her mission objectives but that do not cleanly fit into another category such as Collection. Mission objectives vary based on each adversary's goals, but examples include toll fraud, destruction of device data, or locking the user out of his or her device until a ransom is paid.

## Position in the attack flow
Phase 12 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (10)
- [T1464](https://attack.mitre.org/techniques/T1464) Network Denial of Service
- [T1471](https://attack.mitre.org/techniques/T1471) Data Encrypted for Impact
- [T1516](https://attack.mitre.org/techniques/T1516) Input Injection
- [T1582](https://attack.mitre.org/techniques/T1582) SMS Control
- [T1616](https://attack.mitre.org/techniques/T1616) Call Control
- [T1640](https://attack.mitre.org/techniques/T1640) Account Access Removal
- [T1641](https://attack.mitre.org/techniques/T1641) Data Manipulation
- [T1642](https://attack.mitre.org/techniques/T1642) Endpoint Denial of Service
- [T1643](https://attack.mitre.org/techniques/T1643) Generate Traffic from Victim
- [T1662](https://attack.mitre.org/techniques/T1662) Data Destruction

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0034
