---
attack_id: TA0106
name: Impair Process Control
type: tactic
shortname: impair-process-control
killchain_order: 11
url: https://attack.mitre.org/tactics/TA0106
tags: [mitre-attack, tactic, impair-process-control]
---

# TA0106 - Impair Process Control (Tactic)

> The adversary is trying to manipulate, disable, or damage physical control processes.

## Goal
The adversary is trying to manipulate, disable, or damage physical control processes.

Impair Process Control consists of techniques that adversaries use to disrupt control logic and cause determinantal effects to processes being controlled in the target environment. Targets of interest may include active procedures or parameters that manipulate the physical environment. These techniques can also include prevention or manipulation of reporting elements and control logic. If an adversary has modified process functionality, then they may also obfuscate the results, which are often self-revealing in their impact on the outcome of a product or the environment. The direct physical control these techniques exert may also threaten the safety of operators and downstream users, which can prompt response mechanisms. Adversaries may follow up with or use [Inhibit Response Function](https://attack.mitre.org/tactics/TA0107) techniques in tandem, to assist with the successful abuse of control processes to result in [Impact](https://attack.mitre.org/tactics/TA0105).

## Position in the attack flow
Phase 11 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (4)
- [T0806](https://attack.mitre.org/techniques/T0806) Brute Force I/O
- [T0836](https://attack.mitre.org/techniques/T0836) Modify Parameter
- [T1692](https://attack.mitre.org/techniques/T1692) Unauthorized Message
- [T1693](https://attack.mitre.org/techniques/T1693) Modify Firmware

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0106
