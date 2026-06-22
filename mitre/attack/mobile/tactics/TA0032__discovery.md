---
attack_id: TA0032
name: Discovery
type: tactic
shortname: discovery
killchain_order: 7
url: https://attack.mitre.org/tactics/TA0032
tags: [mitre-attack, tactic, discovery]
---

# TA0032 - Discovery (Tactic)

> The adversary is trying to figure out your environment.

## Goal
The adversary is trying to figure out your environment.

Discovery consists of techniques that allow the adversary to gain knowledge about the characteristics of the mobile device and potentially other networked systems. When adversaries gain access to a new system, they must orient themselves to what they now have control of and what benefits operating from that system give to their current objective or overall goals during the intrusion. The operating system may provide capabilities that aid in this post-compromise information-gathering phase.

## Position in the attack flow
Phase 7 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (8)
- [T1418](https://attack.mitre.org/techniques/T1418) Software Discovery
- [T1420](https://attack.mitre.org/techniques/T1420) File and Directory Discovery
- [T1421](https://attack.mitre.org/techniques/T1421) System Network Connections Discovery
- [T1422](https://attack.mitre.org/techniques/T1422) System Network Configuration Discovery
- [T1423](https://attack.mitre.org/techniques/T1423) Network Service Scanning
- [T1424](https://attack.mitre.org/techniques/T1424) Process Discovery
- [T1426](https://attack.mitre.org/techniques/T1426) System Information Discovery
- [T1430](https://attack.mitre.org/techniques/T1430) Location Tracking

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0032
