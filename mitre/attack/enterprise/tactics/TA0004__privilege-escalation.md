---
attack_id: TA0004
name: Privilege Escalation
type: tactic
shortname: privilege-escalation
killchain_order: 6
url: https://attack.mitre.org/tactics/TA0004
tags: [mitre-attack, tactic, privilege-escalation]
---

# TA0004 - Privilege Escalation (Tactic)

> The adversary is trying to gain higher-level permissions.

## Goal
The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: 

* SYSTEM/root level
* local administrator
* user account with admin-like access 
* user accounts with access to specific system or perform specific function

These techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.

## Position in the attack flow
Phase 6 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (13)
- [T1037](https://attack.mitre.org/techniques/T1037) Boot or Logon Initialization Scripts
- [T1053](https://attack.mitre.org/techniques/T1053) Scheduled Task/Job
- [T1055](https://attack.mitre.org/techniques/T1055) Process Injection
- [T1068](https://attack.mitre.org/techniques/T1068) Exploitation for Privilege Escalation
- [T1078](https://attack.mitre.org/techniques/T1078) Valid Accounts
- [T1098](https://attack.mitre.org/techniques/T1098) Account Manipulation
- [T1134](https://attack.mitre.org/techniques/T1134) Access Token Manipulation
- [T1484](https://attack.mitre.org/techniques/T1484) Domain or Tenant Policy Modification
- [T1543](https://attack.mitre.org/techniques/T1543) Create or Modify System Process
- [T1546](https://attack.mitre.org/techniques/T1546) Event Triggered Execution
- [T1547](https://attack.mitre.org/techniques/T1547) Boot or Logon Autostart Execution
- [T1548](https://attack.mitre.org/techniques/T1548) Abuse Elevation Control Mechanism
- [T1611](https://attack.mitre.org/techniques/T1611) Escape to Host

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0004
