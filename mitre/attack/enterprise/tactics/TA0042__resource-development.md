---
attack_id: TA0042
name: Resource Development
type: tactic
shortname: resource-development
killchain_order: 2
url: https://attack.mitre.org/tactics/TA0042
tags: [mitre-attack, tactic, resource-development]
---

# TA0042 - Resource Development (Tactic)

> The adversary is trying to establish resources they can use to support operations.

## Goal
The adversary is trying to establish resources they can use to support operations.

Resource Development consists of techniques that involve adversaries creating, purchasing, or compromising/stealing resources that can be used to support targeting. Such resources include infrastructure, accounts, or capabilities. These resources can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using purchased domains to support Command and Control, email accounts for phishing as a part of Initial Access, or stealing code signing certificates to help with Defense Evasion.

## Position in the attack flow
Phase 2 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (9)
- [T1583](https://attack.mitre.org/techniques/T1583) Acquire Infrastructure
- [T1584](https://attack.mitre.org/techniques/T1584) Compromise Infrastructure
- [T1585](https://attack.mitre.org/techniques/T1585) Establish Accounts
- [T1586](https://attack.mitre.org/techniques/T1586) Compromise Accounts
- [T1587](https://attack.mitre.org/techniques/T1587) Develop Capabilities
- [T1588](https://attack.mitre.org/techniques/T1588) Obtain Capabilities
- [T1608](https://attack.mitre.org/techniques/T1608) Stage Capabilities
- [T1650](https://attack.mitre.org/techniques/T1650) Acquire Access
- [T1683](https://attack.mitre.org/techniques/T1683) Generate Content

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0042
