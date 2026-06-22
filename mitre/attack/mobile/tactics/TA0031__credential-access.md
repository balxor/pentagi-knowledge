---
attack_id: TA0031
name: Credential Access
type: tactic
shortname: credential-access
killchain_order: 6
url: https://attack.mitre.org/tactics/TA0031
tags: [mitre-attack, tactic, credential-access]
---

# TA0031 - Credential Access (Tactic)

> The adversary is trying to steal account names, passwords, or other secrets that enable access to resources.

## Goal
The adversary is trying to steal account names, passwords, or other secrets that enable access to resources.

Credential access represents techniques that can be used by adversaries to obtain access to or control over passwords, tokens, cryptographic keys, or other values that could be used by an adversary to gain unauthorized access to resources. Credential access allows the adversary to assume the identity of an account, with all of that account's permissions on the system and network, and makes it harder for defenders to detect the adversary. With sufficient access within a network, an adversary can create accounts for later use within the environment.

## Position in the attack flow
Phase 6 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (6)
- [T1414](https://attack.mitre.org/techniques/T1414) Clipboard Data
- [T1417](https://attack.mitre.org/techniques/T1417) Input Capture
- [T1453](https://attack.mitre.org/techniques/T1453) Abuse Accessibility Features
- [T1517](https://attack.mitre.org/techniques/T1517) Access Notifications
- [T1634](https://attack.mitre.org/techniques/T1634) Credentials from Password Store
- [T1635](https://attack.mitre.org/techniques/T1635) Steal Application Access Token

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0031
