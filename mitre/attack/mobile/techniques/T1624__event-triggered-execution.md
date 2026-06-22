---
attack_id: T1624
name: Event Triggered Execution
type: technique
parent: null
tactics: [Persistence]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1624
tags: [mitre-attack, technique, T1624]
---

# T1624 - Event Triggered Execution

**Tactic(s):** Persistence  -  **Platforms:** Android  -  **ATT&CK:** [T1624](https://attack.mitre.org/techniques/T1624)

## Summary
Adversaries may establish persistence using system mechanisms that trigger execution based on specific events. Mobile operating systems have means to subscribe to events such as receiving an SMS message, device boot completion, or other device activities. 

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via automatically and repeatedly executing malicious code. After gaining access to a victim’s system, adversaries may create or modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.

## Role in the attack flow
Used to achieve the **Persistence** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1624
