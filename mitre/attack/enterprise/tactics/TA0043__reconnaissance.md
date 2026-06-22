---
attack_id: TA0043
name: Reconnaissance
type: tactic
shortname: reconnaissance
killchain_order: 1
url: https://attack.mitre.org/tactics/TA0043
tags: [mitre-attack, tactic, reconnaissance]
---

# TA0043 - Reconnaissance (Tactic)

> The adversary is trying to gather information they can use to plan future operations.

## Goal
The adversary is trying to gather information they can use to plan future operations.

Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using gathered information to plan and execute Initial Access, to scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.

## Position in the attack flow
Phase 1 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (12)
- [T1589](https://attack.mitre.org/techniques/T1589) Gather Victim Identity Information
- [T1590](https://attack.mitre.org/techniques/T1590) Gather Victim Network Information
- [T1591](https://attack.mitre.org/techniques/T1591) Gather Victim Org Information
- [T1592](https://attack.mitre.org/techniques/T1592) Gather Victim Host Information
- [T1593](https://attack.mitre.org/techniques/T1593) Search Open Websites/Domains
- [T1594](https://attack.mitre.org/techniques/T1594) Search Victim-Owned Websites
- [T1595](https://attack.mitre.org/techniques/T1595) Active Scanning
- [T1596](https://attack.mitre.org/techniques/T1596) Search Open Technical Databases
- [T1597](https://attack.mitre.org/techniques/T1597) Search Closed Sources
- [T1598](https://attack.mitre.org/techniques/T1598) Phishing for Information
- [T1681](https://attack.mitre.org/techniques/T1681) Search Threat Vendor Data
- [T1682](https://attack.mitre.org/techniques/T1682) Query Public AI Services

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0043
