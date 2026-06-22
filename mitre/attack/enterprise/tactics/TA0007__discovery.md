---
attack_id: TA0007
name: Discovery
type: tactic
shortname: discovery
killchain_order: 10
url: https://attack.mitre.org/tactics/TA0007
tags: [mitre-attack, tactic, discovery]
---

# TA0007 - Discovery (Tactic)

> The adversary is trying to figure out your environment.

## Goal
The adversary is trying to figure out your environment.

Discovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and orient themselves before deciding how to act. They also allow adversaries to explore what they can control and what’s around their entry point in order to discover how it could benefit their current objective. Native operating system tools are often used toward this post-compromise information-gathering objective.

## Position in the attack flow
Phase 10 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (34)
- [T1007](https://attack.mitre.org/techniques/T1007) System Service Discovery
- [T1010](https://attack.mitre.org/techniques/T1010) Application Window Discovery
- [T1012](https://attack.mitre.org/techniques/T1012) Query Registry
- [T1016](https://attack.mitre.org/techniques/T1016) System Network Configuration Discovery
- [T1018](https://attack.mitre.org/techniques/T1018) Remote System Discovery
- [T1033](https://attack.mitre.org/techniques/T1033) System Owner/User Discovery
- [T1040](https://attack.mitre.org/techniques/T1040) Network Sniffing
- [T1046](https://attack.mitre.org/techniques/T1046) Network Service Discovery
- [T1049](https://attack.mitre.org/techniques/T1049) System Network Connections Discovery
- [T1057](https://attack.mitre.org/techniques/T1057) Process Discovery
- [T1069](https://attack.mitre.org/techniques/T1069) Permission Groups Discovery
- [T1082](https://attack.mitre.org/techniques/T1082) System Information Discovery
- [T1083](https://attack.mitre.org/techniques/T1083) File and Directory Discovery
- [T1087](https://attack.mitre.org/techniques/T1087) Account Discovery
- [T1120](https://attack.mitre.org/techniques/T1120) Peripheral Device Discovery
- [T1124](https://attack.mitre.org/techniques/T1124) System Time Discovery
- [T1135](https://attack.mitre.org/techniques/T1135) Network Share Discovery
- [T1201](https://attack.mitre.org/techniques/T1201) Password Policy Discovery
- [T1217](https://attack.mitre.org/techniques/T1217) Browser Information Discovery
- [T1482](https://attack.mitre.org/techniques/T1482) Domain Trust Discovery
- [T1497](https://attack.mitre.org/techniques/T1497) Virtualization/Sandbox Evasion
- [T1518](https://attack.mitre.org/techniques/T1518) Software Discovery
- [T1526](https://attack.mitre.org/techniques/T1526) Cloud Service Discovery
- [T1538](https://attack.mitre.org/techniques/T1538) Cloud Service Dashboard
- [T1580](https://attack.mitre.org/techniques/T1580) Cloud Infrastructure Discovery
- [T1613](https://attack.mitre.org/techniques/T1613) Container and Resource Discovery
- [T1614](https://attack.mitre.org/techniques/T1614) System Location Discovery
- [T1615](https://attack.mitre.org/techniques/T1615) Group Policy Discovery
- [T1619](https://attack.mitre.org/techniques/T1619) Cloud Storage Object Discovery
- [T1622](https://attack.mitre.org/techniques/T1622) Debugger Evasion
- [T1652](https://attack.mitre.org/techniques/T1652) Device Driver Discovery
- [T1654](https://attack.mitre.org/techniques/T1654) Log Enumeration
- [T1673](https://attack.mitre.org/techniques/T1673) Virtual Machine Discovery
- [T1680](https://attack.mitre.org/techniques/T1680) Local Storage Discovery

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0007
