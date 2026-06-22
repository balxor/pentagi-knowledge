---
attack_id: T0853
name: Scripting
type: technique
parent: null
tactics: [Execution]
platforms: [None]
url: https://attack.mitre.org/techniques/T0853
tags: [mitre-attack, technique, T0853]
---

# T0853 - Scripting

**Tactic(s):** Execution  -  **Platforms:** None  -  **ATT&CK:** [T0853](https://attack.mitre.org/techniques/T0853)

## Summary
Adversaries may use scripting languages to execute arbitrary code in the form of a pre-written script or in the form of user-supplied code to an interpreter. Scripting languages are programming languages that differ from compiled languages, in that scripting languages use an interpreter, instead of a compiler. These interpreters read and compile part of the source code just before it is executed, as opposed to compilers, which compile each and every line of code to an executable file. Scripting allows software developers to run their code on any system where the interpreter exists. This way, they can distribute one package, instead of precompiling executables for many different systems. Scripting languages, such as Python, have their interpreters shipped as a default with many Linux distributions. 

In addition to being a useful tool for developers and administrators, scripting language interpreters may be abused by the adversary to execute code in the target environment. Due to the nature of scripting languages, this allows for weaponized code to be deployed to a target easily, and leaves open the possibility of on-the-fly scripting to perform a task.

## Role in the attack flow
Used to achieve the **Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0938 Execution Prevention** - Block execution of code on a system through application control, and/or script blocking.
- **M0948 Application Isolation and Sandboxing** - Restrict the execution of code to a virtual environment on or in-transit to an endpoint system.
- **M0942 Disable or Remove Feature or Program** - Remove or deny access to unnecessary and potentially vulnerable software to prevent abuse by adversaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0853
