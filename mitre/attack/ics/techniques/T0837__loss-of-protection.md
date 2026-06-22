---
attack_id: T0837
name: Loss of Protection
type: technique
parent: null
tactics: [Impact]
platforms: [None]
url: https://attack.mitre.org/techniques/T0837
tags: [mitre-attack, technique, T0837]
---

# T0837 - Loss of Protection

**Tactic(s):** Impact  -  **Platforms:** None  -  **ATT&CK:** [T0837](https://attack.mitre.org/techniques/T0837)

## Summary
Adversaries may compromise protective system functions designed to prevent the effects of faults and abnormal conditions. This can result in equipment damage, prolonged process disruptions and hazards to personnel. 

Many faults and abnormal conditions in process control happen too quickly for a human operator to react to. Speed is critical in correcting these conditions to limit serious impacts such as Loss of Control and Property Damage. 

Adversaries may target and disable protective system functions as a prerequisite to subsequent attack execution or to allow for future faults and abnormal conditions to go unchecked. Detection of a Loss of Protection by operators can result in the shutdown of a process due to strict policies regarding protection systems. This can cause a Loss of Productivity and Revenue and may meet the technical goals of adversaries seeking to cause process disruptions.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0837
