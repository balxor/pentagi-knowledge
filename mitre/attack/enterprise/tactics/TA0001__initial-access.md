---
attack_id: TA0001
name: Initial Access
type: tactic
shortname: initial-access
killchain_order: 3
url: https://attack.mitre.org/tactics/TA0001
tags: [mitre-attack, tactic, initial-access]
---

# TA0001 - Initial Access (Tactic)

> The adversary is trying to get into your network.

## Goal
The adversary is trying to get into your network.

Initial Access consists of techniques that use various entry vectors to gain their initial foothold within a network. Techniques used to gain a foothold include targeted spearphishing and exploiting weaknesses on public-facing web servers. Footholds gained through initial access may allow for continued access, like valid accounts and use of external remote services, or may be limited-use due to changing passwords.

## Position in the attack flow
Phase 3 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (11)
- [T1078](https://attack.mitre.org/techniques/T1078) Valid Accounts
- [T1091](https://attack.mitre.org/techniques/T1091) Replication Through Removable Media
- [T1133](https://attack.mitre.org/techniques/T1133) External Remote Services
- [T1189](https://attack.mitre.org/techniques/T1189) Drive-by Compromise
- [T1190](https://attack.mitre.org/techniques/T1190) Exploit Public-Facing Application
- [T1195](https://attack.mitre.org/techniques/T1195) Supply Chain Compromise
- [T1199](https://attack.mitre.org/techniques/T1199) Trusted Relationship
- [T1200](https://attack.mitre.org/techniques/T1200) Hardware Additions
- [T1566](https://attack.mitre.org/techniques/T1566) Phishing
- [T1659](https://attack.mitre.org/techniques/T1659) Content Injection
- [T1669](https://attack.mitre.org/techniques/T1669) Wi-Fi Networks

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0001
