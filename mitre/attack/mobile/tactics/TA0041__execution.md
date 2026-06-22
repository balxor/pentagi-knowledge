---
attack_id: TA0041
name: Execution
type: tactic
shortname: execution
killchain_order: 2
url: https://attack.mitre.org/tactics/TA0041
tags: [mitre-attack, tactic, execution]
---

# TA0041 - Execution (Tactic)

> The adversary is trying to run malicious code.

## Goal
The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a mobile device. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data.

## Position in the attack flow
Phase 2 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (4)
- [T1575](https://attack.mitre.org/techniques/T1575) Native API
- [T1603](https://attack.mitre.org/techniques/T1603) Scheduled Task/Job
- [T1623](https://attack.mitre.org/techniques/T1623) Command and Scripting Interpreter
- [T1658](https://attack.mitre.org/techniques/T1658) Exploitation for Client Execution

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0041
