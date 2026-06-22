---
attack_id: T1628
name: Hide Artifacts
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1628
tags: [mitre-attack, technique, T1628]
---

# T1628 - Hide Artifacts

**Tactic(s):** Defense Evasion  -  **Platforms:** Android  -  **ATT&CK:** [T1628](https://attack.mitre.org/techniques/T1628)

## Summary
Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Mobile operating systems have features and developer APIs to hide various artifacts, such as an application’s launcher icon. These APIs have legitimate usages, such as hiding an icon to avoid application drawer clutter when an application does not have a usable interface. Adversaries may abuse these features and APIs to hide artifacts from the user to evade detection.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1628
