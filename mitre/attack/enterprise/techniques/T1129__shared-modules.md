---
attack_id: T1129
name: Shared Modules
type: technique
parent: null
tactics: [Execution]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1129
tags: [mitre-attack, technique, T1129]
---

# T1129 - Shared Modules

**Tactic(s):** Execution  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1129](https://attack.mitre.org/techniques/T1129)

## Summary
Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions (i.e., [Native API](https://attack.mitre.org/techniques/T1106)).

Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network communications or execution of specific actions on objective.

The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides in `dlfcn.h` in functions such as `dlopen` and `dlsym`. Although macOS can execute `.so` files, common practice uses `.dylib` files.(Citation: Apple Dev Dynamic Libraries)(Citation: Linux Shared Libraries)(Citation: RotaJakiro 2021 netlab360 analysis)(Citation: Unit42 OceanLotus 2017)

The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in `NTDLL.dll` and is part of the Windows [Native API](https://attack.mitre.org/techniques/T1106) which is called from functions like `LoadLibrary` at run time.(Citation: Microsoft DLL)

## Role in the attack flow
Used to achieve the **Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1038 Execution Prevention** - Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1129
