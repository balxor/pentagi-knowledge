---
attack_id: T1627
name: Execution Guardrails
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1627
tags: [mitre-attack, technique, T1627]
---

# T1627 - Execution Guardrails

**Tactic(s):** Defense Evasion  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1627](https://attack.mitre.org/techniques/T1627)

## Summary
Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign. Values an adversary can provide about a target system or environment to use as guardrails may include environment information such as location.(Citation: SWB Exodus March 2019)

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [System Checks](https://attack.mitre.org/techniques/T1633/001). While use of [System Checks](https://attack.mitre.org/techniques/T1633/001) may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1627
