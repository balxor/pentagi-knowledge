---
attack_id: T1626
name: Abuse Elevation Control Mechanism
type: technique
parent: null
tactics: [Privilege Escalation]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1626
tags: [mitre-attack, technique, T1626]
---

# T1626 - Abuse Elevation Control Mechanism

**Tactic(s):** Privilege Escalation  -  **Platforms:** Android  -  **ATT&CK:** [T1626](https://attack.mitre.org/techniques/T1626)

## Summary
Adversaries may circumvent mechanisms designed to control elevated privileges to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can gain on a machine. Authorization has to be granted to specific users in order to perform tasks that are designated as higher risk. An adversary can use several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.

## Role in the attack flow
Used to achieve the **Privilege Escalation** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1013 Application Developer Guidance** - Application Developer Guidance focuses on providing developers with the knowledge, tools, and best practices needed to write secure code, reduce vulnerabilities, and implement secure design principles. By integrating security throughout the software development lifecycle (SDLC), this mitigation aims to prevent the introduction of exploitable weaknesses in applications, systems, and APIs. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1626
