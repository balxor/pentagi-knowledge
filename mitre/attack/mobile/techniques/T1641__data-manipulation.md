---
attack_id: T1641
name: Data Manipulation
type: technique
parent: null
tactics: [Impact]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1641
tags: [mitre-attack, technique, T1641]
---

# T1641 - Data Manipulation

**Tactic(s):** Impact  -  **Platforms:** Android  -  **ATT&CK:** [T1641](https://attack.mitre.org/techniques/T1641)

## Summary
Adversaries may insert, delete, or alter data in order to manipulate external outcomes or hide activity. By manipulating data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

The type of modification and the impact it will have depends on the target application, process, and the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system, typically gained through a prolonged information gathering campaign, in order to have the desired impact.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1641
