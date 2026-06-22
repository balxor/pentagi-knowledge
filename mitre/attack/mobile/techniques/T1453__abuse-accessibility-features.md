---
attack_id: T1453
name: Abuse Accessibility Features
type: technique
parent: null
tactics: [Collection, Credential Access]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1453
tags: [mitre-attack, technique, T1453]
---

# T1453 - Abuse Accessibility Features

**Tactic(s):** Collection, Credential Access  -  **Platforms:** Android  -  **ATT&CK:** [T1453](https://attack.mitre.org/techniques/T1453)

## Summary
Adversaries may abuse accessibility features in Android devices to steal sensitive data and to spread malware to other devices. Accessibility features in Android are designed to assist users with disabilities, performing a variety of tasks, such as using Action Blocks to control lightbulbs, and changing the device’s user interface, such as changing the font size and adjusting contract or colors.(Citation: Google_AndroidAcsOverview) 

One example of how adversaries abuse accessibility features is overlaying an HTML object mimicking a legitimate login screen. The user types their credentials in the overlay HTML object, which is then sent to the adversaries.(Citation: SahinSRLabs_FluBot_Dec2021)  

Another example is a malicious accessibility feature acting as a keylogger. The keylogger monitors changes on the EditText fields and sends it to the adversaries.(Citation: SahinSRLabs_FluBot_Dec2021) This method of attack is also described in [Keylogging](https://attack.mitre.org/techniques/T1417/001); whereas [Abuse Accessibility Features](https://attack.mitre.org/techniques/T1453) captures the overall abuse of accessibility features.

## Role in the attack flow
Used to achieve the **Collection, Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1453
