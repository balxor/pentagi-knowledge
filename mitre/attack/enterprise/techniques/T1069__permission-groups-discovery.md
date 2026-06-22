---
attack_id: T1069
name: Permission Groups Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Containers, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows]
url: https://attack.mitre.org/techniques/T1069
tags: [mitre-attack, technique, T1069]
---

# T1069 - Permission Groups Discovery

**Tactic(s):** Discovery  ·  **Platforms:** Containers, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows  ·  **ATT&CK:** [T1069](https://attack.mitre.org/techniques/T1069)

## Summary
Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike BloodHound April 2018)

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Containers, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1069
