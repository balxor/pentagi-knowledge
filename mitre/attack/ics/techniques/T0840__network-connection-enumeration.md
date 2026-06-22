---
attack_id: T0840
name: Network Connection Enumeration
type: technique
parent: null
tactics: [Discovery]
platforms: [None]
url: https://attack.mitre.org/techniques/T0840
tags: [mitre-attack, technique, T0840]
---

# T0840 - Network Connection Enumeration

**Tactic(s):** Discovery  -  **Platforms:** None  -  **ATT&CK:** [T0840](https://attack.mitre.org/techniques/T0840)

## Summary
Adversaries may perform network connection enumeration to discover information about device communication patterns. If an adversary can inspect the state of a network connection with tools, such as Netstat(Citation: Netstat), in conjunction with [System Firmware](https://attack.mitre.org/techniques/T0857), then they can determine the role of certain devices on the network  (Citation: MITRE). The adversary can also use [Network Sniffing](https://attack.mitre.org/techniques/T0842) to watch network traffic for details about the source, destination, protocol, and content.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0816 Mitigation Limited or Not Effective** - This type of attack technique cannot be easily mitigated with preventative controls since it is based on the abuse of system features.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0840
