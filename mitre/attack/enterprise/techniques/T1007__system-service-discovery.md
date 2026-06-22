---
attack_id: T1007
name: System Service Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1007
tags: [mitre-attack, technique, T1007]
---

# T1007 - System Service Discovery

**Tactic(s):** Discovery  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1007](https://attack.mitre.org/techniques/T1007)

## Summary
Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as <code>sc query</code>, <code>tasklist /svc</code>, <code>systemctl --type=service</code>, and <code>net start</code>. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation: SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)

Adversaries may use the information from [System Service Discovery](https://attack.mitre.org/techniques/T1007) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1007
