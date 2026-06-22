---
attack_id: T0834
name: Native API
type: technique
parent: null
tactics: [Execution]
platforms: [None]
url: https://attack.mitre.org/techniques/T0834
tags: [mitre-attack, technique, T0834]
---

# T0834 - Native API

**Tactic(s):** Execution  -  **Platforms:** None  -  **ATT&CK:** [T0834](https://attack.mitre.org/techniques/T0834)

## Summary
Adversaries may directly interact with the native OS application programming interface (API) to access system functions. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes. (Citation: The MITRE Corporation May 2017) These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations. 

Functionality provided by native APIs are often also exposed to user-mode applications via interfaces and libraries. For example, functions such as memcpy and direct operations on memory registers can be used to modify user and system memory space.

## Role in the attack flow
Used to achieve the **Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0938 Execution Prevention** - Block execution of code on a system through application control, and/or script blocking.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0834
