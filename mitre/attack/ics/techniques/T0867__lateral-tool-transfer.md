---
attack_id: T0867
name: Lateral Tool Transfer
type: technique
parent: null
tactics: [Lateral Movement]
platforms: [None]
url: https://attack.mitre.org/techniques/T0867
tags: [mitre-attack, technique, T0867]
---

# T0867 - Lateral Tool Transfer

**Tactic(s):** Lateral Movement  -  **Platforms:** None  -  **ATT&CK:** [T0867](https://attack.mitre.org/techniques/T0867)

## Summary
Adversaries may transfer tools or other files from one system to another to stage adversary tools or other files over the course of an operation. (Citation: Enterprise ATT&CK) Copying of files may also be performed laterally between internal victim systems to support Lateral Movement with remote Execution using inherent file sharing protocols such as file sharing over SMB to connected network shares. (Citation: Enterprise ATT&CK)

In control systems environments, malware may use SMB and other file sharing protocols to move laterally through industrial networks.

## Role in the attack flow
Used to achieve the **Lateral Movement** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0931 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.  In industrial control environments, network intrusion prevention should be configured so it will not disrupt protocols and communications responsible for real-time functions related to control or safety.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0867
