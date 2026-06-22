---
attack_id: TA0103
name: Evasion
type: tactic
shortname: evasion
killchain_order: 5
url: https://attack.mitre.org/tactics/TA0103
tags: [mitre-attack, tactic, evasion]
---

# TA0103 - Evasion (Tactic)

> The adversary is trying to avoid security defenses.

## Goal
The adversary is trying to avoid security defenses.

Evasion consists of techniques that adversaries use to avoid technical defenses throughout their campaign. Techniques used for evasion include removal of indicators of compromise, spoofing communications, and exploiting software vulnerabilities. Adversaries may also leverage and abuse trusted devices and processes to hide their activity, possibly by masquerading as master devices or native software. Methods of defense evasion for this purpose are often more passive in nature.

## Position in the attack flow
Phase 5 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (7)
- [T0820](https://attack.mitre.org/techniques/T0820) Exploitation for Evasion
- [T0849](https://attack.mitre.org/techniques/T0849) Masquerading
- [T0851](https://attack.mitre.org/techniques/T0851) Rootkit
- [T0858](https://attack.mitre.org/techniques/T0858) Change Operating Mode
- [T0872](https://attack.mitre.org/techniques/T0872) Indicator Removal on Host
- [T0894](https://attack.mitre.org/techniques/T0894) System Binary Proxy Execution
- [T1692](https://attack.mitre.org/techniques/T1692) Unauthorized Message

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0103
