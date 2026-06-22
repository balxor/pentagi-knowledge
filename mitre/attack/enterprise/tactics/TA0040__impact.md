---
attack_id: TA0040
name: Impact
type: tactic
shortname: impact
killchain_order: 15
url: https://attack.mitre.org/tactics/TA0040
tags: [mitre-attack, tactic, impact]
---

# TA0040 - Impact (Tactic)

> The adversary is trying to manipulate, interrupt, or destroy your systems and data.

## Goal
The adversary is trying to manipulate, interrupt, or destroy your systems and data.
 
Impact consists of techniques that adversaries use to disrupt availability or compromise integrity by manipulating business and operational processes. Techniques used for impact can include destroying or tampering with data. In some cases, business processes can look fine, but may have been altered to benefit the adversaries’ goals. These techniques might be used by adversaries to follow through on their end goal or to provide cover for a confidentiality breach.

## Position in the attack flow
Phase 15 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (15)
- [T1485](https://attack.mitre.org/techniques/T1485) Data Destruction
- [T1486](https://attack.mitre.org/techniques/T1486) Data Encrypted for Impact
- [T1489](https://attack.mitre.org/techniques/T1489) Service Stop
- [T1490](https://attack.mitre.org/techniques/T1490) Inhibit System Recovery
- [T1491](https://attack.mitre.org/techniques/T1491) Defacement
- [T1495](https://attack.mitre.org/techniques/T1495) Firmware Corruption
- [T1496](https://attack.mitre.org/techniques/T1496) Resource Hijacking
- [T1498](https://attack.mitre.org/techniques/T1498) Network Denial of Service
- [T1499](https://attack.mitre.org/techniques/T1499) Endpoint Denial of Service
- [T1529](https://attack.mitre.org/techniques/T1529) System Shutdown/Reboot
- [T1531](https://attack.mitre.org/techniques/T1531) Account Access Removal
- [T1561](https://attack.mitre.org/techniques/T1561) Disk Wipe
- [T1565](https://attack.mitre.org/techniques/T1565) Data Manipulation
- [T1657](https://attack.mitre.org/techniques/T1657) Financial Theft
- [T1667](https://attack.mitre.org/techniques/T1667) Email Bombing

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0040
