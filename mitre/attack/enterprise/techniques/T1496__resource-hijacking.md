---
attack_id: T1496
name: Resource Hijacking
type: technique
parent: null
tactics: [Impact]
platforms: [Windows, IaaS, Linux, macOS, Containers, SaaS]
url: https://attack.mitre.org/techniques/T1496
tags: [mitre-attack, technique, T1496]
---

# T1496 - Resource Hijacking

**Tactic(s):** Impact  -  **Platforms:** Windows, IaaS, Linux, macOS, Containers, SaaS  -  **ATT&CK:** [T1496](https://attack.mitre.org/techniques/T1496)

## Summary
Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. 

Resource hijacking may take a number of different forms. For example, adversaries may:

* Leverage compute resources in order to mine cryptocurrency
* Sell network bandwidth to proxy networks
* Generate SMS traffic for profit
* Abuse cloud-based messaging services to send large quantities of spam messages

In some cases, adversaries may leverage multiple types of Resource Hijacking at once.(Citation: Sysdig Cryptojacking Proxyjacking 2023)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows, IaaS, Linux, macOS, Containers, SaaS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1496
