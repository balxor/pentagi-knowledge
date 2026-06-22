---
attack_id: TA0037
name: Command and Control
type: tactic
shortname: command-and-control
killchain_order: 10
url: https://attack.mitre.org/tactics/TA0037
tags: [mitre-attack, tactic, command-and-control]
---

# TA0037 - Command and Control (Tactic)

> The adversary is trying to communicate with compromised devices to control them.

## Goal
The adversary is trying to communicate with compromised devices to control them.

The command and control tactic represents how adversaries communicate with systems under their control within a target network. There are many ways an adversary can establish command and control with various levels of covertness, depending on system configuration and network topology. Due to the wide degree of variation available to the adversary at the network level, only the most common factors were used to describe the differences in command and control. There are still a great many specific techniques within the documented methods, largely due to how easy it is to define new protocols and use existing, legitimate protocols and network services for communication. 

The resulting breakdown should help convey the concept that detecting intrusion through command and control protocols without prior knowledge is a difficult proposition over the long term. Adversaries' main constraints in network-level defense avoidance are testing and deployment of tools to rapidly change their protocols, awareness of existing defensive technologies, and access to legitimate Web services that, when used appropriately, make their tools difficult to distinguish from benign traffic.

Additionally, in the mobile environment, mobile devices are frequently connected to networks outside enterprise control such as cellular networks or public Wi-Fi networks. Adversaries could attempt to evade detection by communicating on these networks, and potentially even by using non-Internet Protocol mechanisms such as Short Message Service (SMS). However, cellular networks often have data caps and/or extra data charges that could increase the potential for adversarial communication to be detected.

## Position in the attack flow
Phase 10 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (9)
- [T1437](https://attack.mitre.org/techniques/T1437) Application Layer Protocol
- [T1481](https://attack.mitre.org/techniques/T1481) Web Service
- [T1509](https://attack.mitre.org/techniques/T1509) Non-Standard Port
- [T1521](https://attack.mitre.org/techniques/T1521) Encrypted Channel
- [T1544](https://attack.mitre.org/techniques/T1544) Ingress Tool Transfer
- [T1616](https://attack.mitre.org/techniques/T1616) Call Control
- [T1637](https://attack.mitre.org/techniques/T1637) Dynamic Resolution
- [T1644](https://attack.mitre.org/techniques/T1644) Out of Band Data
- [T1663](https://attack.mitre.org/techniques/T1663) Remote Access Software

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0037
