---
attack_id: TA0011
name: Command and Control
type: tactic
shortname: command-and-control
killchain_order: 13
url: https://attack.mitre.org/tactics/TA0011
tags: [mitre-attack, tactic, command-and-control]
---

# TA0011 - Command and Control (Tactic)

> The adversary is trying to communicate with compromised systems to control them.

## Goal
The adversary is trying to communicate with compromised systems to control them.

Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal, expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses.

## Position in the attack flow
Phase 13 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (18)
- [T1001](https://attack.mitre.org/techniques/T1001) Data Obfuscation
- [T1008](https://attack.mitre.org/techniques/T1008) Fallback Channels
- [T1071](https://attack.mitre.org/techniques/T1071) Application Layer Protocol
- [T1090](https://attack.mitre.org/techniques/T1090) Proxy
- [T1092](https://attack.mitre.org/techniques/T1092) Communication Through Removable Media
- [T1095](https://attack.mitre.org/techniques/T1095) Non-Application Layer Protocol
- [T1102](https://attack.mitre.org/techniques/T1102) Web Service
- [T1104](https://attack.mitre.org/techniques/T1104) Multi-Stage Channels
- [T1105](https://attack.mitre.org/techniques/T1105) Ingress Tool Transfer
- [T1132](https://attack.mitre.org/techniques/T1132) Data Encoding
- [T1205](https://attack.mitre.org/techniques/T1205) Traffic Signaling
- [T1219](https://attack.mitre.org/techniques/T1219) Remote Access Tools
- [T1568](https://attack.mitre.org/techniques/T1568) Dynamic Resolution
- [T1571](https://attack.mitre.org/techniques/T1571) Non-Standard Port
- [T1572](https://attack.mitre.org/techniques/T1572) Protocol Tunneling
- [T1573](https://attack.mitre.org/techniques/T1573) Encrypted Channel
- [T1659](https://attack.mitre.org/techniques/T1659) Content Injection
- [T1665](https://attack.mitre.org/techniques/T1665) Hide Infrastructure

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0011
