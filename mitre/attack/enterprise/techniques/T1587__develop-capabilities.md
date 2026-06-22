---
attack_id: T1587
name: Develop Capabilities
type: technique
parent: null
tactics: [Resource Development]
platforms: [PRE]
url: https://attack.mitre.org/techniques/T1587
tags: [mitre-attack, technique, T1587]
---

# T1587 - Develop Capabilities

**Tactic(s):** Resource Development  -  **Platforms:** PRE  -  **ATT&CK:** [T1587](https://attack.mitre.org/techniques/T1587)

## Summary
Adversaries may build capabilities that can be used during targeting. Rather than purchasing, freely downloading, or stealing capabilities, adversaries may develop their own capabilities in-house. This is the process of identifying development requirements and building solutions such as malware, exploits, and self-signed certificates. Adversaries may develop capabilities to support their operations throughout numerous phases of the adversary lifecycle.(Citation: Mandiant APT1)(Citation: Kaspersky Sofacy)(Citation: Bitdefender StrongPity June 2020)(Citation: Talos Promethium June 2020)

As with legitimate development efforts, different skill sets may be required for developing capabilities. The skills needed may be located in-house, or may need to be contracted out. Use of a contractor may be considered an extension of that adversary's development capabilities, provided the adversary plays a role in shaping requirements and maintains a degree of exclusivity to the capability.

## Role in the attack flow
Used to achieve the **Resource Development** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: PRE.

## Mitigations
- **M1056 Pre-compromise** - Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1587
