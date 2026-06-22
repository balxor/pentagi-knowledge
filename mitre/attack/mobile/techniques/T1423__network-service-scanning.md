---
attack_id: T1423
name: Network Service Scanning
type: technique
parent: null
tactics: [Discovery]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1423
tags: [mitre-attack, technique, T1423]
---

# T1423 - Network Service Scanning

**Tactic(s):** Discovery  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1423](https://attack.mitre.org/techniques/T1423)

## Summary
Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information include port scans and vulnerability scans from the mobile device. This technique may take advantage of the mobile device's access to an internal enterprise network either through local connectivity or through a Virtual Private Network (VPN).

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1423
