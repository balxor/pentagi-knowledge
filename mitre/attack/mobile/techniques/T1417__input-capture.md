---
attack_id: T1417
name: Input Capture
type: technique
parent: null
tactics: [Collection, Credential Access]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1417
tags: [mitre-attack, technique, T1417]
---

# T1417 - Input Capture

**Tactic(s):** Collection, Credential Access  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1417](https://attack.mitre.org/techniques/T1417)

## Summary
Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal device usage, users often provide credentials to various locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [Keylogging](https://attack.mitre.org/techniques/T1417/001)) or rely on deceiving the user into providing input into what they believe to be a genuine application prompt (e.g. [GUI Input Capture](https://attack.mitre.org/techniques/T1417/002)).

## Role in the attack flow
Used to achieve the **Collection, Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1012 Enterprise Policy** - An enterprise mobility management (EMM), also known as mobile device management (MDM), system can be used to provision policies to mobile devices to control aspects of their allowed behavior.
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1417
