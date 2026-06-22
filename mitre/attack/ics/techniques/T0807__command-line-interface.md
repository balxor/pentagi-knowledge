---
attack_id: T0807
name: Command-Line Interface
type: technique
parent: null
tactics: [Execution]
platforms: [None]
url: https://attack.mitre.org/techniques/T0807
tags: [mitre-attack, technique, T0807]
---

# T0807 - Command-Line Interface

**Tactic(s):** Execution  -  **Platforms:** None  -  **ATT&CK:** [T0807](https://attack.mitre.org/techniques/T0807)

## Summary
Adversaries may utilize command-line interfaces (CLIs) to interact with systems and execute commands. CLIs provide a means of interacting with computer systems and are a common feature across many types of platforms and devices within control systems environments. (Citation: Enterprise ATT&CK January 2018) Adversaries may also use CLIs to install and run new software, including malicious tools that may be installed over the course of an operation.

CLIs are typically accessed locally, but can also be exposed via services, such as SSH, Telnet, and RDP.  Commands that are executed in the CLI execute with the current permissions level of the process running the terminal emulator, unless the command specifies a change in permissions context. Many controllers have CLI interfaces for management purposes.

## Role in the attack flow
Used to achieve the **Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0938 Execution Prevention** - Block execution of code on a system through application control, and/or script blocking.
- **M0942 Disable or Remove Feature or Program** - Remove or deny access to unnecessary and potentially vulnerable software to prevent abuse by adversaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0807
