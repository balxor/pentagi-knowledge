---
attack_id: T0874
name: Hooking
type: technique
parent: null
tactics: [Execution, Privilege Escalation]
platforms: [None]
url: https://attack.mitre.org/techniques/T0874
tags: [mitre-attack, technique, T0874]
---

# T0874 - Hooking

**Tactic(s):** Execution, Privilege Escalation  -  **Platforms:** None  -  **ATT&CK:** [T0874](https://attack.mitre.org/techniques/T0874)

## Summary
Adversaries may hook into application programming interface (API) functions used by processes to redirect calls for execution and privilege escalation means. Windows processes often leverage these API functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. (Citation: Enterprise ATT&CK)

One type of hooking seen in ICS involves redirecting calls to these functions via import address table (IAT) hooking. IAT hooking uses modifications to a process IAT, where pointers to imported API functions are stored. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

## Role in the attack flow
Used to achieve the **Execution, Privilege Escalation** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0944 Restrict Library Loading** - Prevent abuse of library loading mechanisms in the operating system and software to load untrusted code by configuring appropriate library loading mechanisms and investigating potential vulnerable software.
- **M0947 Audit** - Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. Perform periodic integrity checks of the device to validate the correctness of the firmware, software, programs, and configurations. Integrity checks, which typically include cryptographic hashes or digital signatures, should be compared to those obtained at known valid states, especially after events like device reboots, program downloads, or program restarts.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0874
