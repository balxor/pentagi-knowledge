---
attack_id: TA0010
name: Exfiltration
type: tactic
shortname: exfiltration
killchain_order: 14
url: https://attack.mitre.org/tactics/TA0010
tags: [mitre-attack, tactic, exfiltration]
---

# TA0010 - Exfiltration (Tactic)

> The adversary is trying to steal data.

## Goal
The adversary is trying to steal data.

Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.

## Position in the attack flow
Phase 14 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (9)
- [T1011](https://attack.mitre.org/techniques/T1011) Exfiltration Over Other Network Medium
- [T1020](https://attack.mitre.org/techniques/T1020) Automated Exfiltration
- [T1029](https://attack.mitre.org/techniques/T1029) Scheduled Transfer
- [T1030](https://attack.mitre.org/techniques/T1030) Data Transfer Size Limits
- [T1041](https://attack.mitre.org/techniques/T1041) Exfiltration Over C2 Channel
- [T1048](https://attack.mitre.org/techniques/T1048) Exfiltration Over Alternative Protocol
- [T1052](https://attack.mitre.org/techniques/T1052) Exfiltration Over Physical Medium
- [T1537](https://attack.mitre.org/techniques/T1537) Transfer Data to Cloud Account
- [T1567](https://attack.mitre.org/techniques/T1567) Exfiltration Over Web Service

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0010
