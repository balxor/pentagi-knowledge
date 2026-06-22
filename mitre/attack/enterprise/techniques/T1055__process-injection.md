---
attack_id: T1055
name: Process Injection
type: technique
parent: null
tactics: [Stealth, Privilege Escalation]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1055
tags: [mitre-attack, technique, T1055]
---

# T1055 - Process Injection

**Tactic(s):** Stealth, Privilege Escalation  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1055](https://attack.mitre.org/techniques/T1055)

## Summary
Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. 

There are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. 

More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel.

## Role in the attack flow
Used to achieve the **Stealth, Privilege Escalation** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1026 Privileged Account Management** - Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:
- **M1040 Behavior Prevention on Endpoint** - Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1055
