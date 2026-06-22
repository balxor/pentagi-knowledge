---
attack_id: T1631
name: Process Injection
type: technique
parent: null
tactics: [Defense Evasion, Privilege Escalation]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1631
tags: [mitre-attack, technique, T1631]
---

# T1631 - Process Injection

**Tactic(s):** Defense Evasion, Privilege Escalation  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1631](https://attack.mitre.org/techniques/T1631)

## Summary
Adversaries may inject code into processes in order to evade process-based defenses or even elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. 

Both Android and iOS have no legitimate way to achieve process injection. The only way this is possible is by abusing existing root access or exploiting a vulnerability.

## Role in the attack flow
Used to achieve the **Defense Evasion, Privilege Escalation** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1631
