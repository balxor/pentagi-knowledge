---
attack_id: T1420
name: File and Directory Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1420
tags: [mitre-attack, technique, T1420]
---

# T1420 - File and Directory Discovery

**Tactic(s):** Discovery  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1420](https://attack.mitre.org/techniques/T1420)

## Summary
Adversaries may enumerate files and directories or search in specific device locations for desired information within a filesystem. Adversaries may use the information from [File and Directory Discovery](https://attack.mitre.org/techniques/T1420) during automated discovery to shape follow-on behaviors, including deciding if the adversary should fully infect the target and/or attempt specific actions. 

On Android, Linux file permissions and SELinux policies typically stringently restrict what can be accessed by apps without taking advantage of a privilege escalation exploit. The contents of the external storage directory are generally visible, which could present concerns if sensitive data is inappropriately stored there. iOS's security architecture generally restricts the ability to perform any type of [File and Directory Discovery](https://attack.mitre.org/techniques/T1420) without use of escalated privileges.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1420
