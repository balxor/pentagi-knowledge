---
attack_id: T0823
name: Graphical User Interface
type: technique
parent: null
tactics: [Execution]
platforms: [None]
url: https://attack.mitre.org/techniques/T0823
tags: [mitre-attack, technique, T0823]
---

# T0823 - Graphical User Interface

**Tactic(s):** Execution  -  **Platforms:** None  -  **ATT&CK:** [T0823](https://attack.mitre.org/techniques/T0823)

## Summary
Adversaries may attempt to gain access to a machine via a Graphical User Interface (GUI) to enhance execution capabilities. Access to a GUI allows a user to interact with a computer in a more visual manner than a CLI. A GUI allows users to move a cursor and click on interface objects, with a mouse and keyboard as the main input devices, as opposed to just using the keyboard.

If physical access is not an option, then access might be possible via protocols such as VNC on Linux-based and Unix-based operating systems, and RDP on Windows operating systems. An adversary can use this access to execute programs and applications on the target machine.

## Role in the attack flow
Used to achieve the **Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0816 Mitigation Limited or Not Effective** - This type of attack technique cannot be easily mitigated with preventative controls since it is based on the abuse of system features.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0823
