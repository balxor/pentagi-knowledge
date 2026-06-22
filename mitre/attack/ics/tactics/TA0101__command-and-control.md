---
attack_id: TA0101
name: Command and Control
type: tactic
shortname: command-and-control
killchain_order: 9
url: https://attack.mitre.org/tactics/TA0101
tags: [mitre-attack, tactic, command-and-control]
---

# TA0101 - Command and Control (Tactic)

> The adversary is trying to communicate with and control compromised systems, controllers, and platforms with access to your ICS environment.

## Goal
The adversary is trying to communicate with and control compromised systems, controllers, and platforms with access to your ICS environment.

Command and Control consists of techniques that adversaries use to communicate with and send commands to compromised systems, devices, controllers, and platforms with specialized applications used in ICS environments. Examples of these specialized communication devices include human machine interfaces (HMIs), data historians, SCADA servers, and engineering workstations (EWS). Adversaries often seek to use commonly available resources and mimic expected network traffic to avoid detection and suspicion. For instance, commonly used ports and protocols in ICS environments, and even expected IT resources, depending on the target network. Command and Control may be established to varying degrees of stealth, often depending on the victim’s network structure and defenses.

## Position in the attack flow
Phase 9 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (3)
- [T0869](https://attack.mitre.org/techniques/T0869) Standard Application Layer Protocol
- [T0884](https://attack.mitre.org/techniques/T0884) Connection Proxy
- [T0885](https://attack.mitre.org/techniques/T0885) Commonly Used Port

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0101
