---
attack_id: TA0102
name: Discovery
type: tactic
shortname: discovery
killchain_order: 6
url: https://attack.mitre.org/tactics/TA0102
tags: [mitre-attack, tactic, discovery]
---

# TA0102 - Discovery (Tactic)

> The adversary is locating information to assess and identify their targets in your environment.

## Goal
The adversary is locating information to assess and identify their targets in your environment.

Discovery consists of techniques that adversaries use to survey your ICS environment and gain knowledge about the internal network, control system devices, and how their processes interact. These techniques help adversaries observe the environment and determine next steps for target selection and Lateral Movement. They also allow adversaries to explore what they can control and gain insight on interactions between various control system processes. Discovery techniques are often an act of progression into the environment which enable the adversary to orient themselves before deciding how to act. Adversaries may use Discovery techniques that result in Collection, to help determine how available resources benefit their current objective. A combination of native device communications and functions, and custom tools are often used toward this post-compromise information-gathering objective.

## Position in the attack flow
Phase 6 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (5)
- [T0840](https://attack.mitre.org/techniques/T0840) Network Connection Enumeration
- [T0842](https://attack.mitre.org/techniques/T0842) Network Sniffing
- [T0846](https://attack.mitre.org/techniques/T0846) Remote System Discovery
- [T0887](https://attack.mitre.org/techniques/T0887) Wireless Sniffing
- [T0888](https://attack.mitre.org/techniques/T0888) Remote System Information Discovery

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0102
