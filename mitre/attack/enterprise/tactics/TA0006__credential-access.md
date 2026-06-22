---
attack_id: TA0006
name: Credential Access
type: tactic
shortname: credential-access
killchain_order: 9
url: https://attack.mitre.org/tactics/TA0006
tags: [mitre-attack, tactic, credential-access]
---

# TA0006 - Credential Access (Tactic)

> The adversary is trying to steal account names and passwords.

## Goal
The adversary is trying to steal account names and passwords.

Credential Access consists of techniques for stealing credentials like account names and passwords. Techniques used to get credentials include keylogging or credential dumping. Using legitimate credentials can give adversaries access to systems, make them harder to detect, and provide the opportunity to create more accounts to help achieve their goals.

## Position in the attack flow
Phase 9 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (17)
- [T1003](https://attack.mitre.org/techniques/T1003) OS Credential Dumping
- [T1040](https://attack.mitre.org/techniques/T1040) Network Sniffing
- [T1056](https://attack.mitre.org/techniques/T1056) Input Capture
- [T1110](https://attack.mitre.org/techniques/T1110) Brute Force
- [T1111](https://attack.mitre.org/techniques/T1111) Multi-Factor Authentication Interception
- [T1187](https://attack.mitre.org/techniques/T1187) Forced Authentication
- [T1212](https://attack.mitre.org/techniques/T1212) Exploitation for Credential Access
- [T1528](https://attack.mitre.org/techniques/T1528) Steal Application Access Token
- [T1539](https://attack.mitre.org/techniques/T1539) Steal Web Session Cookie
- [T1552](https://attack.mitre.org/techniques/T1552) Unsecured Credentials
- [T1555](https://attack.mitre.org/techniques/T1555) Credentials from Password Stores
- [T1556](https://attack.mitre.org/techniques/T1556) Modify Authentication Process
- [T1557](https://attack.mitre.org/techniques/T1557) Adversary-in-the-Middle
- [T1558](https://attack.mitre.org/techniques/T1558) Steal or Forge Kerberos Tickets
- [T1606](https://attack.mitre.org/techniques/T1606) Forge Web Credentials
- [T1621](https://attack.mitre.org/techniques/T1621) Multi-Factor Authentication Request Generation
- [T1649](https://attack.mitre.org/techniques/T1649) Steal or Forge Authentication Certificates

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0006
