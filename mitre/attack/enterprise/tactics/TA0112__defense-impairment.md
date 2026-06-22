---
attack_id: TA0112
name: Defense Impairment
type: tactic
shortname: defense-impairment
killchain_order: 8
url: https://attack.mitre.org/tactics/TA0112
tags: [mitre-attack, tactic, defense-impairment]
---

# TA0112 - Defense Impairment (Tactic)

> The adversary is trying to break security mechanisms, pipelines, and tooling so defenders can’t see or trust what’s happening.

## Goal
The adversary is trying to break security mechanisms, pipelines, and tooling so defenders can’t see or trust what’s happening.

Defense Impairment consists of techniques that degrade, disable, or undermine the effectiveness and trustworthiness of security controls and monitoring mechanisms. These techniques are characterized by direct interference with defensive systems. The goal is to reduce defenders’ ability to detect, interpret, or respond to adversary activity.

## Position in the attack flow
Phase 8 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (18)
- [T1112](https://attack.mitre.org/techniques/T1112) Modify Registry
- [T1207](https://attack.mitre.org/techniques/T1207) Rogue Domain Controller
- [T1222](https://attack.mitre.org/techniques/T1222) File and Directory Permissions Modification
- [T1484](https://attack.mitre.org/techniques/T1484) Domain or Tenant Policy Modification
- [T1553](https://attack.mitre.org/techniques/T1553) Subvert Trust Controls
- [T1556](https://attack.mitre.org/techniques/T1556) Modify Authentication Process
- [T1578](https://attack.mitre.org/techniques/T1578) Modify Cloud Compute Infrastructure
- [T1599](https://attack.mitre.org/techniques/T1599) Network Boundary Bridging
- [T1600](https://attack.mitre.org/techniques/T1600) Weaken Encryption
- [T1601](https://attack.mitre.org/techniques/T1601) Modify System Image
- [T1647](https://attack.mitre.org/techniques/T1647) Plist File Modification
- [T1666](https://attack.mitre.org/techniques/T1666) Modify Cloud Resource Hierarchy
- [T1685](https://attack.mitre.org/techniques/T1685) Disable or Modify Tools
- [T1686](https://attack.mitre.org/techniques/T1686) Disable or Modify System Firewall
- [T1687](https://attack.mitre.org/techniques/T1687) Exploitation for Defense Impairment
- [T1688](https://attack.mitre.org/techniques/T1688) Safe Mode Boot
- [T1689](https://attack.mitre.org/techniques/T1689) Downgrade Attack
- [T1690](https://attack.mitre.org/techniques/T1690) Prevent Command History Logging

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0112
