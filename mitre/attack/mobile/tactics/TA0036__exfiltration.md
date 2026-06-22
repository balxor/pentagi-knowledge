---
attack_id: TA0036
name: Exfiltration
type: tactic
shortname: exfiltration
killchain_order: 11
url: https://attack.mitre.org/tactics/TA0036
tags: [mitre-attack, tactic, exfiltration]
---

# TA0036 - Exfiltration (Tactic)

> The adversary is trying to steal data.

## Goal
The adversary is trying to steal data.

Exfiltration refers to techniques and attributes that result or aid in the adversary removing files and information from the targeted mobile device.

In the mobile environment, mobile devices are frequently connected to networks outside enterprise control such as cellular networks or public Wi-Fi networks. Adversaries could attempt to evade detection by communicating on these networks, and potentially even by using non-Internet Protocol mechanisms such as Short Message Service (SMS). However, cellular networks often have data caps and/or extra data charges that could increase the potential for adversarial communication to be detected.

## Position in the attack flow
Phase 11 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (2)
- [T1639](https://attack.mitre.org/techniques/T1639) Exfiltration Over Alternative Protocol
- [T1646](https://attack.mitre.org/techniques/T1646) Exfiltration Over C2 Channel

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0036
