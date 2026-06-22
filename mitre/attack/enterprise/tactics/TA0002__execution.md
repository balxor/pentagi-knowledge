---
attack_id: TA0002
name: Execution
type: tactic
shortname: execution
killchain_order: 4
url: https://attack.mitre.org/tactics/TA0002
tags: [mitre-attack, tactic, execution]
---

# TA0002 - Execution (Tactic)

> The adversary is trying to run malicious code.

## Goal
The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data. For example, an adversary might use a remote access tool to run a PowerShell script that does Remote System Discovery.

## Position in the attack flow
Phase 4 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (20)
- [T1047](https://attack.mitre.org/techniques/T1047) Windows Management Instrumentation
- [T1053](https://attack.mitre.org/techniques/T1053) Scheduled Task/Job
- [T1059](https://attack.mitre.org/techniques/T1059) Command and Scripting Interpreter
- [T1072](https://attack.mitre.org/techniques/T1072) Software Deployment Tools
- [T1106](https://attack.mitre.org/techniques/T1106) Native API
- [T1127](https://attack.mitre.org/techniques/T1127) Trusted Developer Utilities Proxy Execution
- [T1129](https://attack.mitre.org/techniques/T1129) Shared Modules
- [T1197](https://attack.mitre.org/techniques/T1197) BITS Jobs
- [T1203](https://attack.mitre.org/techniques/T1203) Exploitation for Client Execution
- [T1204](https://attack.mitre.org/techniques/T1204) User Execution
- [T1559](https://attack.mitre.org/techniques/T1559) Inter-Process Communication
- [T1569](https://attack.mitre.org/techniques/T1569) System Services
- [T1574](https://attack.mitre.org/techniques/T1574) Hijack Execution Flow
- [T1609](https://attack.mitre.org/techniques/T1609) Container Administration Command
- [T1610](https://attack.mitre.org/techniques/T1610) Deploy Container
- [T1648](https://attack.mitre.org/techniques/T1648) Serverless Execution
- [T1651](https://attack.mitre.org/techniques/T1651) Cloud Administration Command
- [T1674](https://attack.mitre.org/techniques/T1674) Input Injection
- [T1675](https://attack.mitre.org/techniques/T1675) ESXi Administration Command
- [T1677](https://attack.mitre.org/techniques/T1677) Poisoned Pipeline Execution

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0002
