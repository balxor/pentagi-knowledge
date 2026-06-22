---
attack_id: TA0003
name: Persistence
type: tactic
shortname: persistence
killchain_order: 5
url: https://attack.mitre.org/tactics/TA0003
tags: [mitre-attack, tactic, persistence]
---

# TA0003 - Persistence (Tactic)

> The adversary is trying to maintain their foothold.

## Goal
The adversary is trying to maintain their foothold.

Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code.

## Position in the attack flow
Phase 5 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (22)
- [T1037](https://attack.mitre.org/techniques/T1037) Boot or Logon Initialization Scripts
- [T1053](https://attack.mitre.org/techniques/T1053) Scheduled Task/Job
- [T1078](https://attack.mitre.org/techniques/T1078) Valid Accounts
- [T1098](https://attack.mitre.org/techniques/T1098) Account Manipulation
- [T1112](https://attack.mitre.org/techniques/T1112) Modify Registry
- [T1133](https://attack.mitre.org/techniques/T1133) External Remote Services
- [T1136](https://attack.mitre.org/techniques/T1136) Create Account
- [T1137](https://attack.mitre.org/techniques/T1137) Office Application Startup
- [T1176](https://attack.mitre.org/techniques/T1176) Software Extensions
- [T1197](https://attack.mitre.org/techniques/T1197) BITS Jobs
- [T1205](https://attack.mitre.org/techniques/T1205) Traffic Signaling
- [T1505](https://attack.mitre.org/techniques/T1505) Server Software Component
- [T1525](https://attack.mitre.org/techniques/T1525) Implant Internal Image
- [T1542](https://attack.mitre.org/techniques/T1542) Pre-OS Boot
- [T1543](https://attack.mitre.org/techniques/T1543) Create or Modify System Process
- [T1546](https://attack.mitre.org/techniques/T1546) Event Triggered Execution
- [T1547](https://attack.mitre.org/techniques/T1547) Boot or Logon Autostart Execution
- [T1554](https://attack.mitre.org/techniques/T1554) Compromise Host Software Binary
- [T1556](https://attack.mitre.org/techniques/T1556) Modify Authentication Process
- [T1653](https://attack.mitre.org/techniques/T1653) Power Settings
- [T1668](https://attack.mitre.org/techniques/T1668) Exclusive Control
- [T1671](https://attack.mitre.org/techniques/T1671) Cloud Application Integration

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0003
