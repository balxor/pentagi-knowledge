---
attack_id: T1491
name: Defacement
type: technique
parent: null
tactics: [Impact]
platforms: [Windows, IaaS, Linux, macOS, ESXi]
url: https://attack.mitre.org/techniques/T1491
tags: [mitre-attack, technique, T1491]
---

# T1491 - Defacement

**Tactic(s):** Impact  ·  **Platforms:** Windows, IaaS, Linux, macOS, ESXi  ·  **ATT&CK:** [T1491](https://attack.mitre.org/techniques/T1491)

## Summary
Adversaries may modify visual content available internally or externally to an enterprise network, thus affecting the integrity of the original content. Reasons for [Defacement](https://attack.mitre.org/techniques/T1491) include delivering messaging, intimidation, or claiming (possibly false) credit for an intrusion. Disturbing or offensive images may be used as a part of [Defacement](https://attack.mitre.org/techniques/T1491) in order to cause user discomfort, or to pressure compliance with accompanying messages.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows, IaaS, Linux, macOS, ESXi.

## Mitigations
- **M1053 Data Backup** - Data Backup involves taking and securely storing backups of data from end-user systems and critical servers. It ensures that data remains available in the event of system compromise, ransomware attacks, or other disruptions. Backup processes should include hardening backup systems, implementing secure storage solutions, and keeping backups isolated from the corporate network to prevent compromise during active incidents. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1491
