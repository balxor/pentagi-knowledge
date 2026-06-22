---
attack_id: T1056
name: Input Capture
type: technique
parent: null
tactics: [Collection, Credential Access]
platforms: [Linux, macOS, Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1056
tags: [mitre-attack, technique, T1056]
---

# T1056 - Input Capture

**Tactic(s):** Collection, Credential Access  -  **Platforms:** Linux, macOS, Network Devices, Windows  -  **ATT&CK:** [T1056](https://attack.mitre.org/techniques/T1056)

## Summary
Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004)) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [Web Portal Capture](https://attack.mitre.org/techniques/T1056/003)).

## Role in the attack flow
Used to achieve the **Collection, Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Network Devices, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1056
